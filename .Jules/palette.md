## 2024-05-23 - CLI Loading States
**Learning:** The `upstream-apm` CLI relied on manual `console.log` for progress updates, which made long-running operations like downloads feel unresponsive or cluttered.
**Action:** Implemented a lightweight `Spinner` class (using `process.stdout` and `chalk`) to provide visual feedback. This pattern should be used for all future async CLI operations to improve perceived performance and polish.

## 2024-05-24 - Default Assistant Selection
**Learning:** Users often re-initialize projects or update them. Forcing them to re-select the same assistant every time creates unnecessary friction.
**Action:** Implemented logic to detect the previously installed assistant from metadata and set it as the default choice in the interactive prompt. This respects user context and speeds up repetitive tasks.
