#!/usr/bin/env python3
"""Utility helpers for creating a PhD APM review workspace."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, List, Sequence, Tuple

DEFAULT_COLLECTION_DIR_NAME = "rigorous_apm_reviews"
AGENT_LIBRARY_ROOT = Path(__file__).resolve().parent / "05-implementation-agents"
AUTOMATION_SNIPPETS = {
    "setup": Path(__file__).resolve().parent
    / "03-review-kickoff"
    / "share_plan_with_setup.apm",
    "manager": Path(__file__).resolve().parent
    / "03-review-kickoff"
    / "manager_load_plan.apm",
}

# Version tracking
UPSTREAM_APM_VERSION = "0.5.0"
RIGOROUS_APM_VERSION = "1.0.0"
COMBINED_VERSION = f"upstream-v{UPSTREAM_APM_VERSION}+rigorous-v{RIGOROUS_APM_VERSION}"


AUDIENCE_DEFINITIONS: OrderedDict[str, dict[str, str]] = OrderedDict(
    [
        (
            "human",
            {
                "icon": "👤",
                "label": "Human-only",
                "description": "Operators and reviewers execute this themselves.",
            },
        ),
        (
            "agent",
            {
                "icon": "🤖",
                "label": "Agent-ready",
                "description": "Paste directly into an AI agent or IDE without edits.",
            },
        ),
        (
            "shared",
            {
                "icon": "🔁",
                "label": "Shared",
                "description": "Humans trigger or configure it; agents consume or update it.",
            },
        ),
    ]
)


AGENT_METADATA = {
    "s1": {
        "label": "S1 Title & Keywords Agent",
        "specialization": "Analyzes title clarity, keyword relevance, and discoverability.",
    },
    "s2": {
        "label": "S2 Abstract Agent",
        "specialization": "Evaluates abstract structure, focus, and completeness.",
    },
    "s3": {
        "label": "S3 Introduction Agent",
        "specialization": "Reviews problem framing, motivation, and literature positioning.",
    },
    "s4": {
        "label": "S4 Literature Review Agent",
        "specialization": "Assesses literature coverage, synthesis quality, and gaps.",
    },
    "s5": {
        "label": "S5 Methodology Agent",
        "specialization": "Examines research design, reproducibility, and methodological rigor.",
    },
    "s6": {
        "label": "S6 Results Agent",
        "specialization": "Analyzes data presentation, interpretation, and evidence strength.",
    },
    "s7": {
        "label": "S7 Discussion Agent",
        "specialization": "Evaluates discussion depth, implications, and limitations coverage.",
    },
    "s8": {
        "label": "S8 Conclusion Agent",
        "specialization": "Checks conclusion strength, alignment with findings, and outlook.",
    },
    "s9": {
        "label": "S9 References Agent",
        "specialization": "Reviews citation accuracy, completeness, and formatting.",
    },
    "s10": {
        "label": "S10 Supplementary Materials Agent",
        "specialization": "Assesses supplementary content completeness and accessibility.",
    },
    "r1": {
        "label": "R1 Originality & Contribution Agent",
        "specialization": "Assesses research novelty, contribution clarity, and significance.",
    },
    "r2": {
        "label": "R2 Impact & Significance Agent",
        "specialization": "Evaluates potential impact, importance, and broader implications.",
    },
    "r3": {
        "label": "R3 Ethics & Compliance Agent",
        "specialization": "Reviews ethical considerations, compliance, and consent procedures.",
    },
    "r4": {
        "label": "R4 Data & Code Availability Agent",
        "specialization": "Checks data sharing, code availability, and reproducibility assets.",
    },
    "r5": {
        "label": "R5 Statistical Rigor Agent",
        "specialization": "Evaluates statistical methods, analyses, and power adequacy.",
    },
    "r6": {
        "label": "R6 Technical Accuracy Agent",
        "specialization": "Verifies technical correctness, methodology soundness, and calculations.",
    },
    "r7": {
        "label": "R7 Consistency Agent",
        "specialization": "Checks internal consistency, coherence, and logical flow.",
    },
    "w1": {
        "label": "W1 Language & Style Agent",
        "specialization": "Evaluates academic tone, clarity, and presentation quality.",
    },
    "w2": {
        "label": "W2 Narrative Structure Agent",
        "specialization": "Reviews narrative flow, transitions, and story coherence.",
    },
    "w3": {
        "label": "W3 Clarity & Conciseness Agent",
        "specialization": "Assesses clarity, brevity, and reader accessibility.",
    },
    "w4": {
        "label": "W4 Terminology Consistency Agent",
        "specialization": "Checks terminology usage, definitions, and field alignment.",
    },
    "w5": {
        "label": "W5 Inclusive Language Agent",
        "specialization": "Evaluates inclusive language, bias, and accessibility.",
    },
    "w6": {
        "label": "W6 Citation Formatting Agent",
        "specialization": "Reviews citation style compliance and formatting consistency.",
    },
    "w7": {
        "label": "W7 Target Audience Alignment Agent",
        "specialization": "Assesses alignment with the target audience's expectations.",
    },
    "qc": {
        "label": "QC Quality Control Agent",
        "specialization": "Synthesizes findings to surface gaps, blockers, and follow-ups.",
    },
    "es": {
        "label": "ES Executive Summary Agent",
        "specialization": "Builds the decision-ready executive summary package.",
    },
}


@dataclass(frozen=True)
class AgentTemplate:
    agent_id: str
    title: str


def audience_icon(audience: str) -> str:
    try:
        return AUDIENCE_DEFINITIONS[audience]["icon"]
    except KeyError as exc:
        raise ValueError(f"Unknown audience '{audience}'") from exc


def audience_legend_lines() -> List[str]:
    lines: List[str] = []
    for definition in AUDIENCE_DEFINITIONS.values():
        lines.append(
            f"- {definition['icon']} {definition['label']} – {definition['description']}"
        )
    return lines


def requires_audience_metadata(existing_content: str) -> bool:
    lowered = existing_content.casefold()
    expected_icons = {definition["icon"] for definition in AUDIENCE_DEFINITIONS.values()}
    expected_labels = {
        definition["label"].casefold() for definition in AUDIENCE_DEFINITIONS.values()
    }

    if "audience_legend" in lowered:
        try:
            parsed = json.loads(existing_content)
        except json.JSONDecodeError:
            parsed = None

        if isinstance(parsed, dict):
            legend_entries = parsed.get("metadata", {}).get("audience_legend")
            if isinstance(legend_entries, list):
                icons_in_json = set()
                labels_in_json = set()
                for entry in legend_entries:
                    if not isinstance(entry, dict):
                        continue
                    icon = entry.get("icon")
                    label = entry.get("label")
                    if isinstance(icon, str):
                        icons_in_json.add(icon)
                    if isinstance(label, str):
                        labels_in_json.add(label.casefold())

                if expected_icons.issubset(icons_in_json) and expected_labels.issubset(
                    labels_in_json
                ):
                    return False

    if "audience legend" in lowered:
        icons_present = all(icon in existing_content for icon in expected_icons)
        labels_present = all(label in lowered for label in expected_labels)
        if icons_present and labels_present:
            return False

    return True


def format_checklist_item(description: str, audience: str) -> str:
    icon = audience_icon(audience)
    return f"- [ ] {icon} {description}"


def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Bootstrap a manuscript review workspace with scaffolding for the PhD APM."
    )
    parser.add_argument(
        "-m",
        "--manuscript",
        help="Path to the LaTeX manuscript (.tex) you want to review. If omitted, an interactive prompt is used.",
    )
    parser.add_argument(
        "-o",
        "--output-root",
        help=(
            "Directory where review workspaces should be created. Defaults to a 'rigorous_apm_reviews' "
            "folder next to the manuscript."
        ),
    )
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="Fail instead of prompting when required information is missing.",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Overwrite existing scaffold files if the review workspace already exists.",
    )
    parser.add_argument(
        "--copy-manuscript",
        action="store_true",
        help=(
            "Copy the manuscript file and common supporting assets (bib/cls/sty/bst files and figures directory) "
            "into the generated workspace under 'manuscript_assets/'."
        ),
    )
    parser.add_argument(
        "--system-state-format",
        choices=["json", "markdown"],
        default="json",
        help="File format to use when saving the generated system state (default: json).",
    )
    parser.add_argument(
        "--plan-detail-level",
        choices=["concise", "descriptive"],
        default="concise",
        help=(
            "Choose how much context to include for each Implementation Agent checklist entry. "
            "Use 'descriptive' to append each agent's specialization from the cheat sheet."
        ),
    )
    parser.add_argument(
        "--manuscript-type",
        choices=["empirical", "theoretical", "review"],
        help="Type of manuscript being reviewed (empirical, theoretical, or review).",
    )
    parser.add_argument(
        "--target-outlet",
        help="Target journal or publication outlet for the manuscript.",
    )
    parser.add_argument(
        "--research-field",
        help="Research field or domain of the manuscript (e.g., neuroscience, psychology).",
    )
    return parser.parse_args(argv)


def normalize_path(raw: str) -> Path:
    return Path(raw.strip().strip("\"").strip("'"))


def request_manuscript_path(args: argparse.Namespace) -> Path:
    if args.manuscript:
        return normalize_path(args.manuscript)

    if args.non_interactive:
        print("\033[91mError: --manuscript is required when running in non-interactive mode.\033[0m")
        sys.exit(1)

    try:
        response = input("Enter the full path to your LaTeX manuscript (.tex file): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n\033[91mError: Manuscript path input cancelled.\033[0m")
        sys.exit(1)

    if not response:
        print("\033[91mError: Manuscript path cannot be empty.\033[0m")
        sys.exit(1)

    return normalize_path(response)


def choose_from_options(prompt: str, options: Sequence[Path]) -> Path:
    while True:
        print(prompt)
        for idx, option in enumerate(options, start=1):
            print(f"  [{idx}] {option}")
        try:
            selection = input("Select a manuscript file by number: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\033[91mError: Manuscript selection cancelled.\033[0m")
            sys.exit(1)

        if not selection.isdigit():
            print("\033[93mPlease enter one of the listed numbers.\033[0m")
            continue

        index = int(selection)
        if 1 <= index <= len(options):
            return options[index - 1]

        print("\033[93mSelection out of range. Try again.\033[0m")


def resolve_manuscript(manuscript_input: Path, args: argparse.Namespace) -> Tuple[Path, Path]:
    manuscript_input = manuscript_input.expanduser()

    if manuscript_input.is_file():
        if manuscript_input.suffix.lower() != ".tex":
            print(
                f"\033[91mError: Expected a .tex file. Received '{manuscript_input.name}'.\033[0m"
            )
            sys.exit(1)
        return manuscript_input, manuscript_input.parent

    if manuscript_input.is_dir():
        tex_files = sorted(manuscript_input.glob("*.tex"))
        if not tex_files:
            print(
                f"\033[91mError: No .tex files were found inside '{manuscript_input}'. Specify the manuscript file directly.\033[0m"
            )
            sys.exit(1)

        if len(tex_files) == 1:
            return tex_files[0], tex_files[0].parent

        if args.non_interactive:
            joined = ", ".join(file.name for file in tex_files)
            print(
                "\033[91mError: Multiple .tex files found ("
                + joined
                + "). Provide the manuscript file path explicitly.\033[0m"
            )
            sys.exit(1)

        selected = choose_from_options(
            "Multiple manuscripts detected. Choose the primary .tex file:", tex_files
        )
        return selected, selected.parent

    print(f"\033[91mError: Manuscript path not found: '{manuscript_input}'.\033[0m")
    sys.exit(1)


def summarize_supporting_assets(manuscript_file: Path) -> List[Path]:
    siblings: List[Path] = []
    seen: set[Path] = set()

    def record(path: Path) -> None:
        resolved = path.resolve()
        if resolved not in seen:
            siblings.append(path)
            seen.add(resolved)

    related_extensions = [".bib", ".bst", ".cls", ".sty"]
    for extension in related_extensions:
        candidate = manuscript_file.with_suffix(extension)
        if candidate.exists():
            record(candidate)

    allowed_directory_names = ["figures", "figure", "imgs", "images", "img", "tables"]
    directories_by_alias: dict[str, List[Path]] = {alias: [] for alias in allowed_directory_names}

    for entry in manuscript_file.parent.iterdir():
        if entry.is_dir():
            lowered = entry.name.lower()
            if lowered in directories_by_alias:
                directories_by_alias[lowered].append(entry)

    for alias in allowed_directory_names:
        for directory in sorted(directories_by_alias[alias], key=lambda path: path.name):
            record(directory)

    return siblings


def determine_review_directory(
    manuscript_dir: Path, manuscript_name: str, args: argparse.Namespace
) -> Path:
    output_root = (
        normalize_path(args.output_root).expanduser() if args.output_root else manuscript_dir / DEFAULT_COLLECTION_DIR_NAME
    )
    review_dir_path = output_root / f"{manuscript_name}_review"
    return review_dir_path


def ensure_workspace(review_dir_path: Path, force: bool) -> None:
    existed_before = review_dir_path.exists()
    review_dir_path.mkdir(parents=True, exist_ok=True)
    agent_output_dir = review_dir_path / "agent_outputs"
    agent_output_dir.mkdir(exist_ok=True)

    if existed_before and not force:
        print(
            "\033[93mNotice: Review directory already exists. Use --force to overwrite existing scaffold files as needed.\033[0m"
        )
    elif existed_before and force:
        print("\033[93mReusing existing review directory with --force.\033[0m")
    print(f"\033[92mWorkspace ready: {review_dir_path}\033[0m")


def copy_manuscript_assets(
    manuscript_file: Path, review_dir_path: Path, force: bool
) -> bool:
    destination = review_dir_path / "manuscript_assets"
    if destination.exists():
        if force:
            shutil.rmtree(destination)
        else:
            print(
                f"\033[93mSkipped copying manuscript assets (use --force to refresh): {destination}\033[0m"
            )
            return False

    destination.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copy2(manuscript_file, destination / manuscript_file.name)
    except OSError as exc:
        print(f"\033[91mError copying manuscript file '{manuscript_file}': {exc}\033[0m")
        return False

    copied_paths = [manuscript_file]
    for sibling in summarize_supporting_assets(manuscript_file):
        target = destination / sibling.name
        try:
            if sibling.is_dir():
                shutil.copytree(sibling, target)
            else:
                shutil.copy2(sibling, target)
        except OSError as exc:
            print(f"\033[91mError: Failed to copy '{sibling}' -> '{target}': {exc}\033[0m")
            return False
        copied_paths.append(sibling)

    copied_list = ", ".join(path.name for path in copied_paths)
    print(f"\033[92mCopied manuscript assets -> {destination} ({copied_list})\033[0m")
    return True


def write_file(
    path: Path,
    content: str,
    overwrite: bool,
    upgrade_detector: Callable[[str], bool] | None = None,
) -> str:
    if path.exists() and not overwrite:
        if upgrade_detector is not None:
            try:
                existing = path.read_text(encoding="utf-8")
            except OSError as exc:
                print(
                    f"\033[93mWarning: Could not read existing file to check for audience metadata: {path} ({exc})\033[0m"
                )
            else:
                if upgrade_detector(existing):
                    path.parent.mkdir(parents=True, exist_ok=True)
                    with open(path, "w", encoding="utf-8") as handle:
                        handle.write(content.rstrip() + "\n")
                    print(
                        "\033[92mUpgraded existing file with audience legend: "
                        f"{path}\033[0m"
                    )
                    return "upgraded"
        print(f"\033[93mSkipped existing file (use --force to overwrite): {path}\033[0m")
        return "skipped"

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content.rstrip() + "\n")
    print(f"\033[92mWrote: {path}\033[0m")
    return "written"


def check_version_compatibility() -> bool:
    """Check version compatibility and display version information."""
    print(f"\033[94mPhD APM Version: {RIGOROUS_APM_VERSION}\033[0m")
    print(f"\033[94mUpstream APM Version: {UPSTREAM_APM_VERSION}\033[0m")
    print(f"\033[94mCombined Version: {COMBINED_VERSION}\033[0m")
    
    # Check if upstream guides exist
    script_dir = Path(__file__).resolve().parent
    upstream_guides_dir = script_dir / "06-guides" / "upstream"
    
    if not upstream_guides_dir.exists():
        print("\033[93mWarning: Upstream guides directory not found at 06-guides/upstream/\033[0m")
        print("\033[93mSome guide references in generated artifacts may not resolve correctly.\033[0m")
        return False
    
    # Check for key upstream guides
    required_guides = [
        "Context_Synthesis_Guide.md",
        "Implementation_Plan_Guide.md",
        "Memory_Log_Guide.md",
        "Memory_System_Guide.md",
        "Task_Assignment_Guide.md"
    ]
    
    missing_guides = []
    for guide in required_guides:
        if not (upstream_guides_dir / guide).exists():
            missing_guides.append(guide)
    
    if missing_guides:
        print(f"\033[93mWarning: Missing upstream guides: {', '.join(missing_guides)}\033[0m")
        return False
    
    print("\033[92mVersion compatibility check passed.\033[0m")
    return True


def build_bootstrap_prompt(
    manuscript_name: str,
    review_dir_path: Path,
    manuscript_type: str = "",
    target_outlet: str = "",
    research_field: str = ""
) -> str:
    """Build Manager Agent Bootstrap Prompt in upstream YAML format."""
    workspace_root = str(review_dir_path.resolve())
    
    lines: List[str] = [
        "---",
        f"workspace_root: {workspace_root}",
        "---",
        "",
        "# Manager Agent Bootstrap Prompt",
        "",
        "You are the first Manager Agent of this APM session: Manager Agent 1.",
        "",
        "## User Intent and Requirements",
        "",
        f"This is a manuscript review project for **{manuscript_name}** using the PhD APM domain extension.",
        "",
        "**Manuscript Details:**",
        f"- **Name:** {manuscript_name}",
        f"- **Type:** {manuscript_type or 'To be determined during Context Synthesis'}",
        f"- **Target Outlet:** {target_outlet or 'To be determined during Context Synthesis'}",
        f"- **Research Field:** {research_field or 'To be determined during Context Synthesis'}",
        "",
        "**Review Objectives:**",
        "- Conduct comprehensive academic manuscript review",
        "- Evaluate section structure, scientific rigor, and writing quality",
        "- Generate actionable feedback for manuscript improvement",
        "- Produce decision-ready executive summary",
        "",
        "## Implementation Plan Overview",
        "",
        "The Implementation Plan follows a 5-phase manuscript review workflow with 26 specialized agents:",
        "",
        "### Phase 1: Section Analysis (S1-S10)",
        "Analyze each manuscript section independently:",
        "- S1: Title & Keywords",
        "- S2: Abstract",
        "- S3: Introduction",
        "- S4: Literature Review",
        "- S5: Methodology",
        "- S6: Results",
        "- S7: Discussion",
        "- S8: Conclusion",
        "- S9: References",
        "- S10: Supplementary Materials",
        "",
        "### Phase 2: Rigor Analysis (R1-R7)",
        "Evaluate scientific methodology and standards:",
        "- R1: Originality & Contribution",
        "- R2: Impact & Significance",
        "- R3: Ethics & Compliance",
        "- R4: Data & Code Availability",
        "- R5: Statistical Rigor",
        "- R6: Technical Accuracy",
        "- R7: Consistency",
        "",
        "### Phase 3: Writing Analysis (W1-W7)",
        "Assess language, style, and presentation:",
        "- W1: Language & Style",
        "- W2: Narrative Structure",
        "- W3: Clarity & Conciseness",
        "- W4: Terminology Consistency",
        "- W5: Inclusive Language",
        "- W6: Citation Formatting",
        "- W7: Target Audience Alignment",
        "",
        "### Phase 4: Quality Control (QC)",
        "Synthesize findings from all 24 agents to identify gaps, blockers, and follow-ups.",
        "",
        "### Phase 5: Executive Summary (ES)",
        "Generate decision-ready executive summary package.",
        "",
        "## 26-Agent Coordination Strategy",
        "",
        "**Parallel Execution Model:**",
        "1. Execute all Section agents (S1-S10) in parallel",
        "2. Execute Rigor (R1-R7) and Writing (W1-W7) agents in parallel after Section phase completes",
        "3. Execute QC agent after all analysis agents complete",
        "4. Execute ES agent after QC completes",
        "",
        "**Task Assignment Protocol:**",
        "- Create Task Assignment Prompts following {GUIDE_PATH:upstream/Task_Assignment_Guide.md}",
        "- Each agent receives manuscript context and specific analysis criteria",
        "- Agents create Memory Logs following {GUIDE_PATH:upstream/Memory_Log_Guide.md}",
        "- Review Memory Logs to track progress and coordinate next tasks",
        "",
        "**Memory System Organization:**",
        "- Phase-based directory structure: `Memory/Phase_01_Section_Analysis/`, etc.",
        "- Individual agent logs: `S1_Title_Keywords.md`, `R1_Originality.md`, etc.",
        "- Phase summaries after each phase completion",
        "",
        "## Next Steps for Manager Agent",
        "",
        "Follow this sequence exactly. Steps 1-10 in one response. Step 11 after explicit User confirmation:",
        "",
        "**Plan Responsibilities & Project Understanding**",
        "1. Read {GUIDE_PATH:upstream/Implementation_Plan_Guide.md}",
        "2. Read the entire `Implementation_Plan.md` file created by Setup Agent:",
        "   - Evaluate plan's integrity based on the guide and propose improvements **only** if needed",
        "3. Confirm your understanding of the project scope, phases, and task structure & your plan management responsibilities",
        "",
        "**Memory System Responsibilities**",
        "4. Read {GUIDE_PATH:upstream/Memory_System_Guide.md}",
        "5. Read {GUIDE_PATH:upstream/Memory_Log_Guide.md}",
        "6. Read the `Memory_Root.md` file to understand current memory system state",
        "7. Confirm your understanding of memory management responsibilities",
        "",
        "**Task Coordination Preparation**",
        "8. Read {GUIDE_PATH:upstream/Task_Assignment_Guide.md}",
        "9. Confirm your understanding of task assignment prompt creation and coordination duties",
        "",
        "**Execution Confirmation**",
        "10. Summarize your complete understanding and **AWAIT USER CONFIRMATION** - Do not proceed to phase execution until confirmed",
        "",
        "**Execution**",
        "11. When User confirms readiness, proceed as follows:",
        "    a. Read the first phase from the Implementation Plan.",
        "    b. Create `Memory/Phase_01_Section_Analysis/` directory.",
        "    c. For all tasks in Phase 1, create completely empty `.md` Memory Log files in the phase's directory.",
        "    d. Once all empty logs exist, issue the first Task Assignment Prompt.",
    ]
    
    return "\n".join(lines)


def build_metadata_json(manuscript_name: str, manuscript_type: str = "", target_outlet: str = "", research_field: str = "") -> dict:
    """Build metadata.json structure with APM version tracking and manuscript metadata."""
    from datetime import datetime
    
    return {
        "apm_version": COMBINED_VERSION,
        "domain": "manuscript-review",
        "manuscript": {
            "name": manuscript_name,
            "type": manuscript_type or "To be filled by Setup Agent",
            "target_outlet": target_outlet or "To be filled by Setup Agent",
            "field": research_field or "To be filled by Setup Agent"
        },
        "review_started": datetime.now().strftime("%Y-%m-%d"),
        "phases": {
            "section_analysis": "pending",
            "rigor_analysis": "pending",
            "writing_analysis": "pending",
            "quality_control": "pending",
            "executive_summary": "pending"
        }
    }


def build_system_state(manuscript_name: str) -> dict:
    return {
        "metadata": {
            "audience_legend": [
                {
                    "icon": entry["icon"],
                    "label": entry["label"],
                    "description": entry["description"],
                }
                for entry in AUDIENCE_DEFINITIONS.values()
            ]
        },
        "manuscript_context": {
            "title": manuscript_name,
            "target_outlet": "To be filled by Setup Agent",
            "current_stage": "To be filled by Setup Agent",
        },
        "review_progress": {
            "current_phase": "Setup",
            "completed_agents": [],
            "pending_agents": [
                "s1",
                "s2",
                "s3",
                "s4",
                "s5",
                "s6",
                "s7",
                "s8",
                "s9",
                "s10",
                "r1",
                "r2",
                "r3",
                "r4",
                "r5",
                "r6",
                "r7",
                "w1",
                "w2",
                "w3",
                "w4",
                "w5",
                "w6",
                "w7",
                "qc",
                "es",
            ],
        },
        "agent_outputs_summary": {},
        "last_action": "Initial setup complete.",
    }


def format_system_state(system_state: dict, output_format: str) -> tuple[str, str]:
    if output_format == "json":
        return "system_state.json", json.dumps(system_state, indent=2, ensure_ascii=False)

    if output_format == "markdown":
        lines: List[str] = [
            "# System State",
            "",
            "## Audience Legend",
        ]

        legend_entries = (
            system_state.get("metadata", {}).get("audience_legend") or []
        )
        if legend_entries:
            for entry in legend_entries:
                lines.append(
                    f"- {entry.get('icon', '')} {entry.get('label', '')} – {entry.get('description', '')}"
                )
        else:
            lines.extend(audience_legend_lines())

        lines.extend(
            [
                "",
                "## Manuscript Context",
            ]
        )
    
        manuscript_context = system_state.get("manuscript_context", {})
        lines.extend(
            [
                f"- **Title:** {manuscript_context.get('title', '')}",
                f"- **Target outlet:** {manuscript_context.get('target_outlet', '')}",
                f"- **Current stage:** {manuscript_context.get('current_stage', '')}",
                "",
            ]
        )

        review_progress = system_state.get("review_progress", {})
        lines.extend(
            [
                "## Review Progress",
                f"- **Current phase:** {review_progress.get('current_phase', '')}",
                "- **Completed agents:**",
            ]
        )

        completed_agents = review_progress.get("completed_agents", [])
        if completed_agents:
            lines.extend([f"  - {agent}" for agent in completed_agents])
        else:
            lines.append("  - _None yet_")

        lines.append("- **Pending agents:**")
        pending_agents = review_progress.get("pending_agents", [])
        if pending_agents:
            lines.extend([f"  - {agent}" for agent in pending_agents])
        else:
            lines.append("  - _None_")
        lines.append("")

        lines.append("## Agent Outputs Summary")
        agent_outputs_summary = system_state.get("agent_outputs_summary", {})
        if agent_outputs_summary:
            for agent, summary in agent_outputs_summary.items():
                lines.append(f"- **{agent}:** {summary}")
        else:
            lines.append("- _No agent outputs recorded yet._")
        lines.append("")

        lines.append("## Last Action")
        lines.append(system_state.get("last_action", ""))
        lines.append("")

        return "system_state.md", "\n".join(lines)

    raise ValueError(f"Unsupported system state format: {output_format}")


def extract_agent_title(path: Path) -> str:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            for line in handle:
                stripped = line.strip()
                if stripped.startswith("#"):
                    return stripped.lstrip("#").strip()
    except FileNotFoundError:
        pass
    return path.stem.replace("_", " ").title()


def agent_sort_key(agent_id: str) -> Tuple[str, int]:
    match = re.match(r"([a-z]+)(\d+)$", agent_id.lower())
    if match:
        prefix, number = match.groups()
        return prefix, int(number)
    return agent_id.lower(), 0


def collect_agent_templates() -> OrderedDict[str, List[AgentTemplate]]:
    groups: OrderedDict[str, List[AgentTemplate]] = OrderedDict()

    def collect_from_directory(directory: Path) -> List[AgentTemplate]:
        if not directory.exists():
            return []
        templates: List[AgentTemplate] = []
        for file_path in directory.glob("*.md"):
            agent_id = file_path.stem.split("_")[0]
            templates.append(AgentTemplate(agent_id=agent_id, title=extract_agent_title(file_path)))
        templates.sort(key=lambda template: agent_sort_key(template.agent_id))
        return templates

    section_templates = collect_from_directory(AGENT_LIBRARY_ROOT / "section")
    if section_templates:
        groups["Phase 1: Section Analysis (s1-s10)"] = section_templates

    rigor_templates = collect_from_directory(AGENT_LIBRARY_ROOT / "rigor")
    if rigor_templates:
        groups["Phase 2: Rigor Analysis (r1-r7)"] = rigor_templates

    writing_templates = collect_from_directory(AGENT_LIBRARY_ROOT / "writing")
    if writing_templates:
        groups["Phase 3: Writing Analysis (w1-w7)"] = writing_templates

    synthesis_templates: List[AgentTemplate] = []
    synthesis_map = {
        "quality_control_agent_prompt.md": "qc",
        "executive_summary_agent_prompt.md": "es",
    }
    for filename, agent_id in synthesis_map.items():
        file_path = AGENT_LIBRARY_ROOT / filename
        if file_path.exists():
            synthesis_templates.append(AgentTemplate(agent_id=agent_id, title=extract_agent_title(file_path)))
    if synthesis_templates:
        groups["Phase 4: Synthesis"] = synthesis_templates

    return groups


def describe_agent(agent_id: str, fallback_title: str, detail_level: str) -> str:
    metadata = AGENT_METADATA.get(agent_id.lower())
    if not metadata:
        return fallback_title

    label = metadata["label"]
    if detail_level == "descriptive":
        specialization = metadata.get("specialization")
        if specialization:
            return f"{label} — {specialization}"
    return label


def build_implementation_plan(
    manuscript_name: str,
    review_dir_path: Path,
    assets_copied: bool,
    detail_level: str,
) -> str:
    """Build Implementation Plan in upstream-compatible format with proper guide references."""
    lines: List[str] = [
        f"# {manuscript_name} - Implementation Plan",
        "",
        "**Generated automatically by `02-setup_review.py`. This plan follows upstream APM v0.5 patterns.**",
        "",
        "## Project Overview",
        "",
        f"This is a manuscript review project for **{manuscript_name}** using the PhD APM domain extension.",
        "The review follows a 5-phase workflow with 26 specialized Implementation Agents.",
        "",
        "**Key References:**",
        "- Context Synthesis: {{GUIDE_PATH:upstream/Context_Synthesis_Guide.md}}",
        "- Implementation Planning: {{GUIDE_PATH:upstream/Implementation_Plan_Guide.md}}",
        "- Memory System: {{GUIDE_PATH:upstream/Memory_System_Guide.md}}",
        "- Task Assignment: {{GUIDE_PATH:upstream/Task_Assignment_Guide.md}}",
        "",
        "## Audience Legend",
    ]

    lines.extend(audience_legend_lines())

    lines.extend(
        [
            "",
            "## Phase 0: Workspace Preparation",
            "",
            format_checklist_item(
                f"Verify project workspace at `{review_dir_path}`",
                "human",
            ),
        ]
    )

    if assets_copied:
        lines.append(
            format_checklist_item(
                "Confirm staged manuscript package inside `manuscript_assets/` (copied by the helper).",
                "shared",
            )
        )
    else:
        lines.append(
            format_checklist_item(
                "Copy skipped — stage manuscript files so they are ready to share with the Setup Agent.",
                "human",
            )
        )

    lines.extend(
        [
            "",
            format_checklist_item(
                "Review metadata.json for manuscript details and phase tracking",
                "shared",
            ),
            "",
        ]
    )

    for phase, templates in collect_agent_templates().items():
        lines.append(f"## {phase}")
        lines.append("")
        for template in templates:
            label = describe_agent(template.agent_id, template.title, detail_level)
            lines.append(
                format_checklist_item(
                    f"{label} │ `{template.agent_id}`",
                    "agent",
                )
            )
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## Manuscript-Specific Workflow",
            "",
            "This Implementation Plan preserves the phd-apm 5-phase review workflow:",
            "",
            "1. **Phase 1: Section Analysis (S1-S10)** - Analyze each manuscript section independently",
            "2. **Phase 2: Rigor Analysis (R1-R7)** - Evaluate scientific methodology and standards",
            "3. **Phase 3: Writing Analysis (W1-W7)** - Assess language, style, and presentation",
            "4. **Phase 4: Quality Control (QC)** - Synthesize findings from all 24 agents",
            "5. **Phase 5: Executive Summary (ES)** - Generate final comprehensive report",
            "",
            "**Coordination Strategy:**",
            "- Section agents (S1-S10) execute in parallel",
            "- Rigor (R1-R7) and Writing (W1-W7) agents execute in parallel after Section phase",
            "- QC agent synthesizes all findings",
            "- ES agent creates decision-ready summary",
            "",
            "**Memory Logging:**",
            "Each agent creates a Memory Log following {{GUIDE_PATH:upstream/Memory_Log_Guide.md}}",
            "",
            "---",
            "",
            "## Next Steps",
            "",
            "Once the Setup Agent finalizes this plan:",
            "1. Review the generated Bootstrap Prompt",
            "2. Initialize Manager Agent with the Bootstrap Prompt",
            "3. Manager Agent will coordinate the 26 Implementation Agents through the 5-phase workflow",
        ]
    )

    return "\n".join(lines)


def print_post_run_summary(
    review_dir_path: Path,
    assets_copied: bool,
    system_state_filename: str,
    legend_upgraded_targets: List[Path] | None = None,
) -> None:
    print("\033[92mReview workspace ready.\033[0m")

    summary_items = [
        ("Workspace", review_dir_path, "human"),
        (
            "Implementation plan",
            review_dir_path / "Implementation_Plan.md",
            "shared",
        ),
        (
            "Bootstrap prompt",
            review_dir_path / "Manager_Bootstrap_Prompt.md",
            "shared",
        ),
        ("Metadata", review_dir_path / "metadata.json", "shared"),
        ("System state", review_dir_path / system_state_filename, "shared"),
    ]

    if assets_copied:
        summary_items.append(
            ("Manuscript assets", review_dir_path / "manuscript_assets", "shared")
        )

    label_width = max(len(label) for label, _, _ in summary_items)
    for label, path, audience in summary_items:
        icon = audience_icon(audience)
        print(f"  {label:<{label_width}} : {icon} {path}")

    print("")
    print("Next steps:")
    next_steps = [
        (
            "Drag '03-review-kickoff/review_kickoff_prompt.md' into your agentic IDE.",
            "shared",
        ),
        (
            "Use the 'share_plan_with_setup.apm' automation snippet to give the plan to the Setup Agent.",
            "shared",
        ),
        (
            "After revisions, run 'manager_load_plan.apm' so the Manager imports the latest plan.",
            "shared",
        ),
    ]

    for index, (step, audience) in enumerate(next_steps, start=1):
        icon = audience_icon(audience)
        print(f"  {index}. {icon} {step}")

    if legend_upgraded_targets:
        print("")
        print("Legend upgraded automatically:")
        for target in legend_upgraded_targets:
            print(f"  - {target}")
        print("Existing files were refreshed to include the shared audience legend.")

    missing_snippets = [
        name for name, snippet in AUTOMATION_SNIPPETS.items() if not snippet.exists()
    ]
    if missing_snippets:
        missing_list = ", ".join(
            AUTOMATION_SNIPPETS[name].name for name in missing_snippets
        )
        print(
            f"\033[93mWarning: missing automation snippet(s): {missing_list}. Refresh the repository.\033[0m"
        )


def main(argv: List[str] | None = None) -> None:
    args = parse_args(argv)
    
    # Check version compatibility
    print("\n" + "="*60)
    print("PhD APM - Manuscript Review Workspace Setup")
    print("="*60 + "\n")
    check_version_compatibility()
    print("")
    
    manuscript_input = request_manuscript_path(args)
    manuscript_file, manuscript_dir = resolve_manuscript(manuscript_input, args)
    manuscript_name = manuscript_file.stem

    review_dir_path = determine_review_directory(manuscript_dir, manuscript_name, args)
    ensure_workspace(review_dir_path, force=args.force)

    # Generate metadata.json with APM version tracking
    metadata = build_metadata_json(
        manuscript_name,
        manuscript_type=args.manuscript_type or "",
        target_outlet=args.target_outlet or "",
        research_field=args.research_field or ""
    )
    
    system_state = build_system_state(manuscript_name)
    system_state_filename, system_state_content = format_system_state(
        system_state, args.system_state_format
    )
    assets_copied = False
    if args.copy_manuscript:
        assets_copied = copy_manuscript_assets(
            manuscript_file, review_dir_path, force=args.force
        )
        if not assets_copied:
            print("\033[91mExiting due to file copy failure.\033[0m")
            sys.exit(1)

    implementation_plan_content = build_implementation_plan(
        manuscript_name,
        review_dir_path,
        assets_copied=assets_copied,
        detail_level=args.plan_detail_level,
    )
    
    # Generate Bootstrap Prompt in upstream format
    bootstrap_prompt_content = build_bootstrap_prompt(
        manuscript_name,
        review_dir_path,
        manuscript_type=args.manuscript_type or "",
        target_outlet=args.target_outlet or "",
        research_field=args.research_field or ""
    )

    legend_upgraded_targets: List[Path] = []

    # Write metadata.json
    metadata_path = review_dir_path / "metadata.json"
    metadata_content = json.dumps(metadata, indent=2, ensure_ascii=False)
    write_file(metadata_path, metadata_content, overwrite=args.force)

    system_state_path = review_dir_path / system_state_filename
    system_state_status = write_file(
        system_state_path,
        system_state_content,
        overwrite=args.force,
        upgrade_detector=requires_audience_metadata,
    )
    if system_state_status == "upgraded":
        legend_upgraded_targets.append(system_state_path)

    implementation_plan_path = review_dir_path / "Implementation_Plan.md"
    implementation_plan_status = write_file(
        implementation_plan_path,
        implementation_plan_content,
        overwrite=args.force,
        upgrade_detector=requires_audience_metadata,
    )
    if implementation_plan_status == "upgraded":
        legend_upgraded_targets.append(implementation_plan_path)
    
    # Write Bootstrap Prompt
    bootstrap_prompt_path = review_dir_path / "Manager_Bootstrap_Prompt.md"
    write_file(bootstrap_prompt_path, bootstrap_prompt_content, overwrite=args.force)

    print_post_run_summary(
        review_dir_path,
        assets_copied=assets_copied,
        system_state_filename=system_state_filename,
        legend_upgraded_targets=legend_upgraded_targets,
    )


if __name__ == "__main__":
    main()
