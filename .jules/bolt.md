## 2024-05-23 - Lazy Loading Heavy Dependencies
**Learning:** Node.js CLIs using static imports of heavy libraries (like `axios`, `adm-zip`) incur a significant startup penalty, even for commands that don't use them (like `--help`). Switching to dynamic `await import()` reduced startup time from ~505ms to ~174ms (~65% improvement).
**Action:** For CLI tools, always audit top-level imports and lazy-load heavy dependencies that are not needed for the critical initialization path.

## 2024-05-24 - Async I/O for Smooth Spinners
**Learning:** Synchronous file operations (like `adm-zip.extractAllTo`) block the Node.js event loop, causing CLI spinners (`setInterval`) to freeze. Using callback-based async methods (`extractAllToAsync`) prevents UI jank.
**Action:** Always prefer async/callback variants for heavy I/O in CLI tools to keep the UI responsive.
