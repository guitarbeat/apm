"""Unit tests for legend upgrade detection in the Rigorous setup helper."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "phd-apm" / "02-setup_review.py"

spec = importlib.util.spec_from_file_location("setup_review", MODULE_PATH)
setup_review = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = setup_review  # type: ignore[arg-type]
spec.loader.exec_module(setup_review)  # type: ignore[assignment]


def test_requires_audience_metadata_missing_markers_triggers_upgrade() -> None:
    assert setup_review.requires_audience_metadata("no legend here") is True


def test_requires_audience_metadata_markdown_header_without_entries_triggers_upgrade() -> None:
    content = "## Audience Legend\n\n- placeholder"
    assert setup_review.requires_audience_metadata(content) is True


def test_requires_audience_metadata_markdown_with_expected_entries_is_recognized() -> None:
    legend_lines = "\n".join(setup_review.audience_legend_lines())
    content = f"## Audience Legend\n\n{legend_lines}"
    assert setup_review.requires_audience_metadata(content) is False


def test_requires_audience_metadata_json_with_expected_entries_is_recognized() -> None:
    system_state = setup_review.build_system_state("example")
    content = json.dumps(system_state)
    assert setup_review.requires_audience_metadata(content) is False


def test_requires_audience_metadata_json_missing_fields_triggers_upgrade() -> None:
    content = json.dumps({"metadata": {"audience_legend": [{"icon": "👤"}]}})
    assert setup_review.requires_audience_metadata(content) is True
