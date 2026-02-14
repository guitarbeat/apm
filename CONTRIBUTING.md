# Contributing to Agentic Project Management

Thank you for your interest in contributing!

For detailed guidelines on patterns and architecture, please see [AGENTS.md](AGENTS.md).
For specific instructions on the `upstream-apm` CLI, see [upstream-apm/CONTRIBUTING.md](upstream-apm/CONTRIBUTING.md).

## Code Standards & CI/CD

This repository enforces code standards using automation.

### Node.js (upstream-apm)

- **Linting**: ESLint with Airbnb rules.
- **Formatting**: Prettier.
- **Tests**: Vitest.

Run checks locally:
```bash
cd upstream-apm
pnpm install
pnpm lint
pnpm run format:check
pnpm test
```

### Python (phd-apm & tests)

- **Linting**: Ruff.
- **Formatting**: Black.
- **Tests**: Pytest.

Run checks locally:
```bash
pip install ruff black pytest
ruff check .
black --check .
pytest upstream-apm/tests/
```

### Pre-commit Hooks

We use [pre-commit](https://pre-commit.com/) to automatically check and fix issues before commit.

Install pre-commit:
```bash
pip install pre-commit
pre-commit install
```
