import argparse
import json
import sys
from pathlib import Path
from typing import Callable, Type, cast

try:
    from jsonschema import ValidationError, validate
except ModuleNotFoundError:  # pragma: no cover - exercised via subprocess test
    ValidationError = Exception
    validate = None


def require_jsonschema() -> tuple[Callable[..., None], Type[BaseException]]:
    """Return the jsonschema.validate function or exit with guidance."""

    if validate is None:
        print(
            "Error: The optional 'jsonschema' dependency is required to validate schemas.",
            file=sys.stderr,
        )
        print(
            "Install it with `pip install jsonschema` and re-run the command.",
            file=sys.stderr,
        )
        sys.exit(1)

    return cast(Callable[..., None], validate), cast(Type[BaseException], ValidationError)


SCHEMA_MAP = {
    "plan": "implementation_plan.schema.json",
    "log": "memory_log.schema.json",
    "task": "task_assignment.schema.json",
}

# Only the implementation plan schema is currently wired up for the CLI helper.
# The additional entries in ``SCHEMA_MAP`` are kept so that internal consumers –
# such as tests or future tooling – can still reference them without having to
# update imports once CLI support lands.  By limiting the public ``choices`` to
# the stable set we ensure that ``argparse`` fails with the standard
# ``invalid choice`` message that downstream tooling expects while we finish
# validating the remaining schemas.
SUPPORTED_ARTIFACT_TYPES = ("plan",)


def load_json_file(file_path):
    """Load and return JSON data from a file."""

    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}", file=sys.stderr)
        sys.exit(1)

    except UnicodeDecodeError as e:
        print(
            "Error: Could not decode file "
            f"'{file_path}' as UTF-8 - {e}",
            file=sys.stderr,
        )
        sys.exit(1)

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file '{file_path}' - {e}", file=sys.stderr)
        sys.exit(1)


def get_schema_path(artifact_type):
    """Return the full path to the schema file for the given artifact type."""

    schema_file = SCHEMA_MAP.get(artifact_type)

    if not schema_file:
        print(f"Error: Schema for artifact type '{artifact_type}' is not defined yet.", file=sys.stderr)
        print_usage_and_exit()

    return Path(__file__).parent / schema_file


def validate_json(instance, schema, file_path, artifact_type):
    """Validate the JSON instance against the schema."""

    validator, error_type = require_jsonschema()

    try:
        validator(instance=instance, schema=schema)
        print(f"Validation successful: '{file_path}' conforms to the '{artifact_type}' schema.")

    except error_type as e:  # type: ignore[misc]
        print(f"Validation failed for '{file_path}'!", file=sys.stderr)
        print("---Error Details---", file=sys.stderr)
        print(f"Message: {e.message}", file=sys.stderr)
        print(f"Path in JSON: {list(e.path)}", file=sys.stderr)
        print(f"Validator: {e.validator} = {e.validator_value}", file=sys.stderr)
        sys.exit(1)


def print_usage_and_exit():
    """Print usage information and exit."""
    print("Usage: python validate_schema.py <artifact_type> <file_path>", file=sys.stderr)
    print(f"  <artifact_type>: one of {list(SCHEMA_MAP.keys())}", file=sys.stderr)
    print("  <file_path>: path to the JSON file to validate", file=sys.stderr)
    sys.exit(2)


def parse_args():
    """Parse and return command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Validate a JSON file against a predefined APM schema.",
        add_help=False
    )

    parser.add_argument(
        "artifact_type",
        choices=SUPPORTED_ARTIFACT_TYPES,
        help=(
            "The type of artifact to validate. Choices: "
            f"{list(SUPPORTED_ARTIFACT_TYPES)}"
        ),
    )

    parser.add_argument(
        "file_path",
        help="The path to the JSON file to validate."
    )

    parser.add_argument(
        "-h", "--help", action="help", default=argparse.SUPPRESS,
        help="Show this help message and exit."
    )

    try:
        args = parser.parse_args()

    except Exception:
        print_usage_and_exit()

    return args


def main():
    args = parse_args()
    schema_path = get_schema_path(args.artifact_type)
    schema = load_json_file(schema_path)
    instance = load_json_file(args.file_path)
    validate_json(instance, schema, args.file_path, args.artifact_type)

if __name__ == "__main__":
    main()
