## 2024-05-23 - Lazy Loading Heavy Dependencies
**Learning:** Node.js CLIs using static imports of heavy libraries (like `axios`, `adm-zip`) incur a significant startup penalty, even for commands that don't use them (like `--help`). Switching to dynamic `await import()` reduced startup time from ~505ms to ~174ms (~65% improvement).
**Action:** For CLI tools, always audit top-level imports and lazy-load heavy dependencies that are not needed for the critical initialization path.

## 2024-05-24 - Lazy Loading Internal Modules
**Learning:** Moving internal modules (like `utils.js`, `downloader.js`) and built-in modules (`fs`) to dynamic imports inside command actions reduced startup time from ~94ms to ~79ms (~15% improvement). `createRequire` is significantly faster (~1ms) than `fs.readFileSync` (requires ~15ms `fs` import) for reading JSON configuration at startup.
**Action:** For CLI entry points, avoid top-level imports of any module that is not strictly required for command parsing or help generation.
