## 2024-05-23 - CLI Loading States
**Learning:** The `upstream-apm` CLI relied on manual `console.log` for progress updates, which made long-running operations like downloads feel unresponsive or cluttered.
**Action:** Implemented a lightweight `Spinner` class (using `process.stdout` and `chalk`) to provide visual feedback. This pattern should be used for all future async CLI operations to improve perceived performance and polish.
