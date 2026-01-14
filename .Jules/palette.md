## 2024-05-23 - CLI Loading States
**Learning:** The `upstream-apm` CLI relied on manual `console.log` for progress updates, which made long-running operations like downloads feel unresponsive or cluttered.
**Action:** Implemented a lightweight `Spinner` class (using `process.stdout` and `chalk`) to provide visual feedback. This pattern should be used for all future async CLI operations to improve perceived performance and polish.

## 2024-05-24 - CLI Readability & Color Contrast
**Learning:** CLI success messages that use extensive gray text (low contrast) on black backgrounds can be hard to read and lack actionable focus. Highlighting key paths and commands with distinct colors (cyan, yellow) significantly improves scannability and guides the user to the next step.
**Action:** When designing CLI output, use colors to establish a hierarchy of information. Reserve gray for meta-data (like versions) but use brighter colors for primary actions and file paths.
