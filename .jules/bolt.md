## 2024-05-23 - Lazy Loading Heavy Dependencies
**Learning:** Node.js CLIs using static imports of heavy libraries (like `axios`, `adm-zip`) incur a significant startup penalty, even for commands that don't use them (like `--help`). Switching to dynamic `await import()` reduced startup time from ~505ms to ~174ms (~65% improvement).
**Action:** For CLI tools, always audit top-level imports and lazy-load heavy dependencies that are not needed for the critical initialization path.

## 2024-05-23 - Lazy Loading @inquirer/prompts
**Learning:** Statically importing `@inquirer/prompts` added ~60-87ms to the CLI startup time. Since it's only needed for interactive commands (`init`, `update`), lazy-loading it reduced the `--help` command execution time by ~150ms (~50% improvement).
**Action:** Audit interactive CLI libraries and ensure they are only imported when interactivity is actually required.

## 2025-05-23 - Async I/O for Large Operations
**Learning:** Synchronous zip extraction using `adm-zip` blocks the event loop, freezing CLI spinners and preventing signal handling (SIGINT). Wrapping callback-based async methods (`extractAllToAsync`) in Promises resolves this.
**Action:** Always use asynchronous I/O methods for potentially large file operations in Node.js CLIs to maintain UI responsiveness.

## 2025-05-23 - Redundant Lazy Imports
**Learning:** Copy-pasting lazy import blocks (e.g., `const { x } = await import(...)`) within the same scope can lead to `SyntaxError: Identifier has already been declared`, causing the CLI to crash.
**Action:** Verify variable scope when using dynamic imports and avoid redundant declarations.
