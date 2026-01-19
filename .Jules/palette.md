## 2024-05-23 - CLI Loading States
**Learning:** The `upstream-apm` CLI relied on manual `console.log` for progress updates, which made long-running operations like downloads feel unresponsive or cluttered.
**Action:** Implemented a lightweight `Spinner` class (using `process.stdout` and `chalk`) to provide visual feedback. This pattern should be used for all future async CLI operations to improve perceived performance and polish.

## 2025-05-24 - CLI Success Message Hierarchy
**Learning:** Using `chalk.gray` for "Next steps" instructions in CLI output caused them to blend into the background, reducing the likelihood of users seeing critical post-installation actions.
**Action:** Establish a pattern where success headers use `chalk.green.bold` with a checkmark, and next steps use `chalk.bold.cyan` for the header with `chalk.white` (or default) text for the list items to ensure high contrast and readability.
