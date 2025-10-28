"""Regression tests for manuscript asset copy reporting in the Rigorous setup helper."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "rigorous-apm" / "02-setup_review.py"

spec = importlib.util.spec_from_file_location("setup_review", MODULE_PATH)
setup_review = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = setup_review  # type: ignore[arg-type]
spec.loader.exec_module(setup_review)  # type: ignore[assignment]


def test_phase_zero_checklist_mentions_skipped_copy_when_assets_missing(tmp_path: Path) -> None:
    plan = setup_review.build_implementation_plan(
        "Example Manuscript",
        tmp_path,
        assets_copied=False,
        detail_level="concise",
    )

    assert "Copy skipped" in plan


def test_summary_omits_manuscript_assets_when_copy_skipped(
    tmp_path: Path, capsys: CaptureFixture[str]
) -> None:
    setup_review.print_post_run_summary(
        tmp_path,
        assets_copied=False,
        system_state_filename="state.json",
    )

    output = capsys.readouterr().out
    assert "Manuscript assets" not in output
    assert "Workspace" in output
