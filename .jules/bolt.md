## 2024-05-23 - Lazy Loading Heavy Dependencies
**Learning:** Node.js CLIs using static imports of heavy libraries (like `axios`, `adm-zip`) incur a significant startup penalty, even for commands that don't use them (like `--help`). Switching to dynamic `await import()` reduced startup time from ~505ms to ~174ms (~65% improvement).
**Action:** For CLI tools, always audit top-level imports and lazy-load heavy dependencies that are not needed for the critical initialization path.

## 2024-05-24 - Partial Lazy Loading Pitfall
**Learning:** Even when lazy loading is improved, it's easy to miss UI libraries like `@inquirer/prompts`. These can still add significant overhead (adding ~55ms in this case). Ensuring *all* non-critical dependencies are lazy-loaded is required for maximum CLI responsiveness.
**Action:** Audit imports recursively or use tools to visualize import cost when optimizing CLI startup time. Don't stop at the "obvious" heavy libraries.
