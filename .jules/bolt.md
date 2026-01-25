## 2024-05-23 - Lazy Loading Heavy Dependencies
**Learning:** Node.js CLIs using static imports of heavy libraries (like `axios`, `adm-zip`) incur a significant startup penalty, even for commands that don't use them (like `--help`). Switching to dynamic `await import()` reduced startup time from ~505ms to ~174ms (~65% improvement).
**Action:** For CLI tools, always audit top-level imports and lazy-load heavy dependencies that are not needed for the critical initialization path.

## 2024-05-23 - Lazy Loading @inquirer/prompts
**Learning:** Statically importing `@inquirer/prompts` added ~60-87ms to the CLI startup time. Since it's only needed for interactive commands (`init`, `update`), lazy-loading it reduced the `--help` command execution time by ~150ms (~50% improvement).
**Action:** Audit interactive CLI libraries and ensure they are only imported when interactivity is actually required.

## 2024-05-24 - Lazy Loading Internal Modules
**Learning:** Lazy loading internal modules (`utils.js`, `downloader.js`) in `index.js` reduced startup time from ~110ms to ~85ms (~25% improvement). Even local ESM imports add up.
**Action:** For CLI tools, lazy load not just external heavy libs but also internal heavy modules that are not needed for the immediate command.
