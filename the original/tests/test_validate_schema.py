import sys
from pathlib import Path

import types

import pytest


if "jsonschema" not in sys.modules:
    jsonschema_stub = types.ModuleType("jsonschema")

    class ValidationError(Exception):
        pass

    def validate(*args, **kwargs):
        return None

    jsonschema_stub.ValidationError = ValidationError
    jsonschema_stub.validate = validate
    sys.modules["jsonschema"] = jsonschema_stub


ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from prompts.schemas import validate_schema


EXAMPLES_DIR = ROOT_DIR / "prompts" / "schemas" / "examples"


def test_plan_example_valid(monkeypatch, capsys):
    example_path = EXAMPLES_DIR / "json_plan_example.json"
    monkeypatch.setattr(sys, "argv", ["validate_schema.py", "plan", str(example_path)])

    validate_schema.main()

    captured = capsys.readouterr()
    assert "Validation successful" in captured.out
    assert captured.err == ""


def test_log_example_is_unsupported(monkeypatch, capsys):
    example_path = EXAMPLES_DIR / "json_memory_log_example.json"
    monkeypatch.setattr(sys, "argv", ["validate_schema.py", "log", str(example_path)])

    with pytest.raises(SystemExit) as excinfo:
        validate_schema.main()

    assert excinfo.value.code == 2
    captured = capsys.readouterr()
    assert "invalid choice: 'log'" in captured.err


def test_task_example_is_unsupported(monkeypatch, capsys):
    example_path = EXAMPLES_DIR / "json_task_assignment_example.json"
    monkeypatch.setattr(sys, "argv", ["validate_schema.py", "task", str(example_path)])

    with pytest.raises(SystemExit) as excinfo:
        validate_schema.main()

    assert excinfo.value.code == 2
    captured = capsys.readouterr()
    assert "invalid choice: 'task'" in captured.err


def test_plan_invalid_json(monkeypatch, tmp_path, capsys):
    invalid_json_path = tmp_path / "invalid_plan.json"
    invalid_json_path.write_text("{invalid: true}")
    monkeypatch.setattr(sys, "argv", ["validate_schema.py", "plan", str(invalid_json_path)])

    with pytest.raises(SystemExit) as excinfo:
        validate_schema.main()

    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert "Error: Invalid JSON" in captured.err
