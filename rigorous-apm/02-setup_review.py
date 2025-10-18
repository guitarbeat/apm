#!/usr/bin/env python3
"""Utility helpers for creating a Rigorous APM review workspace."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path
from typing import List, Sequence, Tuple

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


def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Bootstrap a manuscript review workspace with scaffolding for the Rigorous APM."
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
    siblings = []
    related_extensions = [".bib", ".bst", ".cls", ".sty"]
    for extension in related_extensions:
        candidate = manuscript_file.with_suffix(extension)
        if candidate.exists():
            siblings.append(candidate)

    sibling_directories = ["figures", "figure", "imgs", "images", "img", "tables"]
    for directory_name in sibling_directories:
        candidate_dir = manuscript_file.parent / directory_name
        if candidate_dir.exists() and candidate_dir.is_dir():
            siblings.append(candidate_dir)

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


def copy_manuscript_assets(manuscript_file: Path, review_dir_path: Path, force: bool) -> None:
    destination = review_dir_path / "manuscript_assets"
    if destination.exists():
        if force:
            shutil.rmtree(destination)
        else:
            print(
                f"\033[93mSkipped copying manuscript assets (use --force to refresh): {destination}\033[0m"
            )
            return

    destination.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copy2(manuscript_file, destination / manuscript_file.name)
    except OSError as exc:
        print(f"\033[91mError copying manuscript file '{manuscript_file}': {exc}\033[0m")
        return

    copied_paths = [manuscript_file]
    for sibling in summarize_supporting_assets(manuscript_file):
        target = destination / sibling.name
        try:
            if sibling.is_dir():
                shutil.copytree(sibling, target)
            else:
                shutil.copy2(sibling, target)
        except OSError as exc:
            print(f"\033[93mWarning: Failed to copy '{sibling}' -> '{target}': {exc}\033[0m")
            continue
        copied_paths.append(sibling)

    copied_list = ", ".join(path.name for path in copied_paths)
    print(f"\033[92mCopied manuscript assets -> {destination} ({copied_list})\033[0m")


def write_file(path: Path, content: str, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        print(f"\033[93mSkipped existing file (use --force to overwrite): {path}\033[0m")
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content.rstrip() + "\n")
    print(f"\033[92mWrote: {path}\033[0m")


def build_system_state(manuscript_name: str) -> dict:
    return {
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
            "## Manuscript Context",
        ]

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
    lines: List[str] = [
        f"# {manuscript_name} - Implementation Plan",
        "",
        "**Generated automatically by `02-setup_review.py`. Customize before handing to the Rigorous Setup Agent.**",
        "",
        "## Review Kickoff Checklist",
        "- [ ] Confirm manuscript scope and target outlet details with the Setup Agent",
        "- [ ] Provide manuscript files and supporting assets to the Setup Agent",
        "- [ ] Capture the refined Implementation Plan for Manager handoff",
        "",
        "## Phase 0: Workspace Preparation",
        f"- [ ] Verify project workspace at `{review_dir_path}`",
    ]

    if assets_copied:
        lines.append(
            "- [ ] Confirm staged manuscript package inside `manuscript_assets/` (copied by the helper)."
        )
    else:
        lines.append(
            "- [ ] Stage manuscript files so they are ready to share with the Setup Agent."
        )

    lines.append("")

    for phase, templates in collect_agent_templates().items():
        lines.append(f"## {phase}")
        lines.append("")
        for template in templates:
            label = describe_agent(template.agent_id, template.title, detail_level)
            lines.append(f"- [ ] {label} │ `{template.agent_id}`")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(
        "Once the Setup Agent finalizes this plan, run the Manager Agent using the Review Kickoff prompt (03-review-kickoff/)."
    )

    return "\n".join(lines)


def print_post_run_summary(
    review_dir_path: Path, assets_copied: bool, system_state_filename: str
) -> None:
    print("\033[92mReview workspace ready.\033[0m")

    summary_items = [
        ("Workspace", review_dir_path),
        ("Implementation plan", review_dir_path / "Implementation_Plan.md"),
        ("System state", review_dir_path / system_state_filename),
    ]

    if assets_copied:
        summary_items.append(("Manuscript assets", review_dir_path / "manuscript_assets"))

    label_width = max(len(label) for label, _ in summary_items)
    for label, path in summary_items:
        print(f"  {label:<{label_width}} : {path}")

    print("")
    print("Next steps:")
    next_steps = [
        "Drag '03-review-kickoff/review_kickoff_prompt.md' into your agentic IDE.",
        "Use the 'share_plan_with_setup.apm' automation snippet to give the plan to the Setup Agent.",
        "After revisions, run 'manager_load_plan.apm' so the Manager imports the latest plan.",
    ]

    for index, step in enumerate(next_steps, start=1):
        print(f"  {index}. {step}")

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
    manuscript_input = request_manuscript_path(args)
    manuscript_file, manuscript_dir = resolve_manuscript(manuscript_input, args)
    manuscript_name = manuscript_file.stem

    review_dir_path = determine_review_directory(manuscript_dir, manuscript_name, args)
    ensure_workspace(review_dir_path, force=args.force)

    system_state = build_system_state(manuscript_name)
    system_state_filename, system_state_content = format_system_state(
        system_state, args.system_state_format
    )
    implementation_plan_content = build_implementation_plan(
        manuscript_name,
        review_dir_path,
        assets_copied=args.copy_manuscript,
        detail_level=args.plan_detail_level,
    )

    write_file(
        review_dir_path / system_state_filename,
        system_state_content,
        overwrite=args.force,
    )
    write_file(review_dir_path / "Implementation_Plan.md", implementation_plan_content, overwrite=args.force)

    if args.copy_manuscript:
        copy_manuscript_assets(manuscript_file, review_dir_path, force=args.force)

    print_post_run_summary(
        review_dir_path,
        assets_copied=args.copy_manuscript,
        system_state_filename=system_state_filename,
    )


if __name__ == "__main__":
    main()
