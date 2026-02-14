import json
import os
import subprocess
import sys
import types
from pathlib import Path

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

from prompts.schemas import validate_schema  # noqa: E402

EXAMPLES_DIR = ROOT_DIR / "prompts" / "schemas" / "examples"


@pytest.fixture
def utf8_plan_file(tmp_path):
    example_path = EXAMPLES_DIR / "json_plan_example.json"
    plan_data = json.loads(example_path.read_text(encoding="utf-8"))
    plan_data["projectOverview"] = "Plan includes serving crème brûlée to celebrate."
    utf8_file = tmp_path / "utf8_plan.json"
    utf8_file.write_text(json.dumps(plan_data), encoding="utf-8")
    return utf8_file


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


def test_plan_utf8_file(monkeypatch, capsys, utf8_plan_file):
    monkeypatch.setattr(sys, "argv", ["validate_schema.py", "plan", str(utf8_plan_file)])

    validate_schema.main()

    captured = capsys.readouterr()
    assert "Validation successful" in captured.out
    assert captured.err == ""


def test_plan_missing_json_file(monkeypatch, tmp_path, capsys):
    missing_json_path = tmp_path / "missing_plan.json"
    monkeypatch.setattr(sys, "argv", ["validate_schema.py", "plan", str(missing_json_path)])

    with pytest.raises(SystemExit) as excinfo:
        validate_schema.main()

    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert f"Error: File not found - {missing_json_path}" in captured.err


def test_help_succeeds_without_jsonschema():
    script_path = ROOT_DIR / "prompts" / "schemas" / "validate_schema.py"

    result = subprocess.run(
        [sys.executable, str(script_path), "--help"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "Validate a JSON file against a predefined APM schema." in result.stdout


def test_validation_requires_jsonschema_dependency(tmp_path):
    script_path = ROOT_DIR / "prompts" / "schemas" / "validate_schema.py"
    example_path = ROOT_DIR / "prompts" / "schemas" / "examples" / "json_plan_example.json"

    fake_site = tmp_path / "fake_site"
    fake_site.mkdir()
    package_dir = fake_site / "jsonschema"
    package_dir.mkdir()
    (package_dir / "__init__.py").write_text(
        "raise ModuleNotFoundError('jsonschema intentionally unavailable')\n",
        encoding="utf-8",
    )

    env = os.environ.copy()
    env["PYTHONNOUSERSITE"] = "1"
    existing_path = env.get("PYTHONPATH")
    env["PYTHONPATH"] = str(fake_site)
    if existing_path:
        env["PYTHONPATH"] += os.pathsep + existing_path

    result = subprocess.run(
        [sys.executable, str(script_path), "plan", str(example_path)],
        capture_output=True,
        text=True,
        check=False,
        env=env,
    )

    assert result.returncode == 1
    assert "optional 'jsonschema'" in result.stderr
