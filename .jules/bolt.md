## 2024-05-23 - Lazy Loading Dependencies
**Learning:** Top-level static imports in CLI tools (like `axios`, `adm-zip`) significantly slow down startup time, even for commands that don't use them (like `--help`). The memory claimed these were lazy-loaded, but the code showed static imports.
**Action:** Always verify "optimization" claims in memory against actual code. Implement dynamic imports (`await import(...)`) for heavy dependencies in CLI entry points and command handlers.
