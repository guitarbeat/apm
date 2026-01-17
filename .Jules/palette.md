## 2024-05-23 - CLI Loading States
**Learning:** The `upstream-apm` CLI relied on manual `console.log` for progress updates, which made long-running operations like downloads feel unresponsive or cluttered.
**Action:** Implemented a lightweight `Spinner` class (using `process.stdout` and `chalk`) to provide visual feedback. This pattern should be used for all future async CLI operations to improve perceived performance and polish.

## 2026-01-17 - Nested Spinner Logging
**Learning:** Console logs (like `console.log`) executed while a `Spinner` is active cause visual artifacts (ghost text, broken frames) because the spinner cleans the line expecting to be the only writer.
**Action:** Added `silent` options to utility functions (like `downloadAndExtract`) to suppress internal logging when called within a parent spinner context, ensuring a clean UI.
