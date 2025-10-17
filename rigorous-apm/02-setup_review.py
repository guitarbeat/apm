#!/usr/bin/env python3
"""Utility for bootstrapping Rigorous APM review workspaces.

The original script only prompted for a single `.tex` file path and exited if
anything unexpected happened. The streamlined edition below keeps the workflow
interactive-friendly while also supporting non-interactive automation and a new
"lite" review mode that bundles early checkpoints together.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


class SetupError(RuntimeError):
    """Raised when the review workspace cannot be prepared."""


@dataclass
class ReviewWorkspace:
    manuscript_path: Path
    manuscript_name: str
    review_dir_path: Path
    mode: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create a Rigorous APM review workspace with optional streamlined "
            "(lite) scaffolding."
        )
    )
    parser.add_argument(
        "manuscript",
        nargs="?",
        help="Path to the manuscript .tex file or directory containing one.",
    )
    parser.add_argument(
        "--mode",
        choices=("standard", "lite"),
        default="standard",
        help="Select the review coordination mode declared in generated assets.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing *_review directory if it already exists.",
    )
    return parser.parse_args()


def prompt_for_path() -> str:
    return input("Enter the path to your LaTeX manuscript (.tex or folder): ").strip()


def normalise_path(raw_path: str | None) -> Path:
    if raw_path is None:
        raw_path = prompt_for_path()
    raw_path = raw_path.strip('"').strip("'")
    path = Path(raw_path).expanduser()
    return path


def select_manuscript(path: Path) -> Path:
    if not path.exists():
        raise SetupError(f"Manuscript path '{path}' does not exist.")
    if path.is_file():
        if path.suffix.lower() != ".tex":
            raise SetupError("The manuscript file must have a .tex extension.")
        return path

    tex_candidates = sorted(p for p in path.glob("*.tex") if p.is_file())
    if not tex_candidates:
        raise SetupError(
            "No .tex files were found in the provided directory. "
            "Please point to a LaTeX manuscript."
        )
    if len(tex_candidates) == 1:
        return tex_candidates[0]

    print("Multiple LaTeX files were discovered:")
    for idx, candidate in enumerate(tex_candidates, start=1):
        print(f"  {idx}. {candidate.name}")
    while True:
        choice = input("Select the file number to review: ").strip()
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue
        idx = int(choice)
        if 1 <= idx <= len(tex_candidates):
            return tex_candidates[idx - 1]
        print("Selection out of range. Try again.")


def prepare_workspace(manuscript: Path, mode: str, force: bool) -> ReviewWorkspace:
    manuscript_dir = manuscript.parent
    manuscript_name = manuscript.stem
    review_dir_path = manuscript_dir / f"{manuscript_name}_review"

    if review_dir_path.exists():
        if not force:
            raise SetupError(
                f"Review directory '{review_dir_path}' already exists. "
                "Use --force to overwrite."
            )
        shutil.rmtree(review_dir_path)
    review_dir_path.mkdir(parents=True, exist_ok=True)
    (review_dir_path / "agent_outputs").mkdir(exist_ok=True)
    return ReviewWorkspace(manuscript, manuscript_name, review_dir_path, mode)


def system_state_template(workspace: ReviewWorkspace) -> dict:
    if workspace.mode == "lite":
        pending_agents = [
            "section_bundle",
            "rigor_bundle",
            "writing_bundle",
            "qc",
            "es",
        ]
    else:
        pending_agents = [
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
        ]

    return {
        "manuscript_context": {
            "title": workspace.manuscript_name,
            "target_outlet": "To be filled by Setup Agent",
            "current_stage": "To be filled by Setup Agent",
        },
        "review_progress": {
            "current_phase": "Setup",
            "completed_agents": [],
            "pending_agents": pending_agents,
            "workflow_mode": workspace.mode,
        },
        "agent_outputs_summary": {},
        "last_action": "Initial setup complete.",
    }


def implementation_plan(workspace: ReviewWorkspace) -> str:
    header = dedent(
        f"""---
        review_mode: {workspace.mode}
        manuscript: {workspace.manuscript_name}
        generated_by: setup_review.py
        ---

        """
    )
    if workspace.mode == "lite":
        body = dedent(
            f"""# {workspace.manuscript_name} - Streamlined Implementation Plan

            **Review mode:** lite (combined checkpoints for rapid assessment)

            ## Phase 0: Intake Confirmation
            - Task 0.1: Snapshot manuscript context │ setup_lite_intake
              - Confirm manuscript metadata, timeline, and review priorities in a single exchange.

            ## Phase 1: Structural & Rigor Bundle
            - Task 1.1: Holistic structural and rigor scan │ bundle_section_rigor
              - Coordinate section (S1-S10) and rigor (R1-R7) specialists through combined Task Assignment Prompts.
              - Capture only blockers, red flags, and must-fix gaps instead of full narratives.

            ## Phase 2: Writing & Presentation Bundle
            - Task 2.1: Unified writing quality review │ bundle_writing
              - Engage writing agents (W1-W7) with a single consolidated prompt emphasising style, clarity, and readiness risks.

            ## Phase 3: Publication Readiness Synthesis
            - Task 3.1: Quality Control Synthesis │ qc
              - Request a triaged issue list sorted by impact and remediation effort.
            - Task 3.2: Executive Summary │ es
              - Deliver a concise executive brief (≤ 12 bullet points) aligned with lite-mode findings.

            **Next step:** Share this Implementation Plan and the generated `system_state.json` with the Rigorous Setup Agent or use the dedicated lite initiation prompt.
            """
        )
    else:
        body = dedent(
            f"""# {workspace.manuscript_name} - Implementation Plan

            **Review mode:** standard (full 26-agent orchestration)

            ## Phase 1: Section Analysis (s1-s10)
            - Task 1.1: Title & Keywords Analysis │ section_s1
            - Task 1.2: Abstract Analysis │ section_s2
            - Task 1.3: Introduction Analysis │ section_s3
            - Task 1.4: Literature Review Analysis │ section_s4
            - Task 1.5: Methodology Analysis │ section_s5
            - Task 1.6: Results Analysis │ section_s6
            - Task 1.7: Discussion Analysis │ section_s7
            - Task 1.8: Conclusion Analysis │ section_s8
            - Task 1.9: References Analysis │ section_s9
            - Task 1.10: Supplementary Materials Analysis │ section_s10

            ## Phase 2: Rigor Analysis (r1-r7)
            - Task 2.1: Originality & Contribution Assessment │ rigor_r1
            - Task 2.2: Impact & Significance Evaluation │ rigor_r2
            - Task 2.3: Ethics & Compliance Review │ rigor_r3
            - Task 2.4: Data & Code Availability Assessment │ rigor_r4
            - Task 2.5: Statistical Rigor Analysis │ rigor_r5
            - Task 2.6: Technical Accuracy Review │ rigor_r6
            - Task 2.7: Consistency Check │ rigor_r7

            ## Phase 3: Writing Analysis (w1-w7)
            - Task 3.1: Language & Style Analysis │ writing_w1
            - Task 3.2: Narrative Structure Assessment │ writing_w2
            - Task 3.3: Clarity & Conciseness Review │ writing_w3
            - Task 3.4: Terminology Consistency Check │ writing_w4
            - Task 3.5: Inclusive Language Assessment │ writing_w5
            - Task 3.6: Citation Formatting Review │ writing_w6
            - Task 3.7: Target Audience Alignment │ writing_w7

            ## Phase 4: Quality Control Synthesis (qc)
            - Task 4.1: Quality Control Synthesis │ qc

            ## Phase 5: Executive Summary (es)
            - Task 5.1: Executive Summary Generation │ es

            **Next step:** Share this Implementation Plan and the generated `system_state.json` with the Rigorous Setup Agent for enhancement.
            """
        )
    return header + body


def write_workspace_assets(workspace: ReviewWorkspace) -> None:
    state_path = workspace.review_dir_path / "system_state.json"
    with open(state_path, "w", encoding="utf-8") as fp:
        json.dump(system_state_template(workspace), fp, indent=2, ensure_ascii=False)

    plan_path = workspace.review_dir_path / "Implementation_Plan.md"
    with open(plan_path, "w", encoding="utf-8") as fp:
        fp.write(implementation_plan(workspace))


def main() -> None:
    args = parse_args()
    try:
        manuscript_input = normalise_path(args.manuscript)
        manuscript = select_manuscript(manuscript_input)
        workspace = prepare_workspace(manuscript, args.mode, args.force)
        write_workspace_assets(workspace)
    except SetupError as err:
        print(f"\033[91mError: {err}\033[0m")
        sys.exit(1)

    print(f"\033[92mCreated review directory: {workspace.review_dir_path}\033[0m")
    print(
        "\033[92mGenerated files: system_state.json, Implementation_Plan.md, agent_outputs/\033[0m"
    )
    if workspace.mode == "lite":
        print(
            "\033[93mLite mode selected. Share the plan with the lite Setup prompt for a condensed discovery round.\033[0m"
        )
    else:
        print(
            "\033[93mNext step: Provide 'Implementation_Plan.md' to the Rigorous Setup Agent for full-plan enhancement.\033[0m"
        )


if __name__ == "__main__":
    main()
