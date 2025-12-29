## 2024-05-22 - [CLI Progress Indicators]
**Learning:** Users lack visibility during long-running CLI operations (downloads, updates), making the process feel unresponsive.
**Action:** Implemented a lightweight `Spinner` class using `process.stdout` and `chalk` to provide visual feedback without adding new dependencies. This pattern should be used for any operation taking more than 500ms.
