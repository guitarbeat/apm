# Agent Guidelines

This repository hosts two complementary Agentic Project Management (APM) systems. Every change should improve one or both of these systems while keeping their goals aligned.

## Shared Expectations
- Follow the existing file organization; document any renames of the top-level `rigorous-apm/` or `upstream-apm/` directories so collaborators can update scripts accordingly.
- Keep instructions actionable for agent operators and contributors. When you add or edit guidance, mention the relevant file path so readers can navigate quickly.
- Prefer incremental updates that maintain compatibility with existing prompts, automation snippets, and scaffolding scripts.
- Run targeted checks (unit tests, schema validation, linting, or dry-run scripts) whenever you touch executable assets. Documentation-only updates do not require tests.

## Rigorous APM (`rigorous-apm/`)
- Preserve the onboarding flow described in `rigorous-apm/01-START_HERE.md`. Updates should clarify how to launch or coordinate the 26 specialist agents without introducing breaking workflow changes.
- When modifying `02-setup_review.py`, ensure the helper still bootstraps review workspaces from the command line. Provide example invocations that cover new flags or behaviors.
- Prompts inside `03-` through `05-` directories should remain interoperable with IDE drag-and-drop workflows. Keep JSON or `.apm` snippets free of trailing spaces and ready for copy/paste.
- Guides under `06-guides/` must cross-link to any newly added artifacts so the training loop stays comprehensive.

## Upstream APM (`upstream-apm/`)
- Align edits with the terminology used in `upstream-apm/docs/Workflow_Overview.md` and the root `README.md` to keep the upstream documentation internally consistent.
- When adjusting schema or validation utilities in `upstream-apm/prompts/schemas/`, verify that `python upstream-apm/prompts/schemas/validate_schema.py --help` succeeds and document any new arguments.
- Maintain backwards-compatible prompt structures under `upstream-apm/prompts/` so existing projects can ingest updates without retooling.
- Keep test coverage current: run `pytest` from the repository root after changing Python modules or prompt schemas within `upstream-apm/` tree.

## Commit & PR Guidance
- Reference affected files or directories in commit messages and PR descriptions.
- Summaries should call out whether the change benefits Rigorous APM, Upstream APM, or both.
