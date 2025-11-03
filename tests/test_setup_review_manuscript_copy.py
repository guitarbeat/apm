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


def test_case_insensitive_asset_directories_are_copied(tmp_path: Path) -> None:
    manuscript_dir = tmp_path / "source"
    manuscript_dir.mkdir()

    manuscript_file = manuscript_dir / "paper.tex"
    manuscript_file.write_text("\\documentclass{article}")

    (manuscript_dir / "Figures").mkdir()
    (manuscript_dir / "Tables").mkdir()

    review_dir = tmp_path / "review"
    copied = setup_review.copy_manuscript_assets(manuscript_file, review_dir, force=False)

    assert copied is True
    destination = review_dir / "manuscript_assets"
    assert (destination / "paper.tex").is_file()
    assert (destination / "Figures").is_dir()
    assert (destination / "Tables").is_dir()

    discovered = setup_review.summarize_supporting_assets(manuscript_file)
    discovered_names = [path.name for path in discovered]

    assert "Figures" in discovered_names
    assert "Tables" in discovered_names
    assert len(discovered_names) == len(set(discovered_names))
