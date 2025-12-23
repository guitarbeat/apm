## 2024-05-23 - Lazy Loading Heavy Dependencies in CLI
**Learning:** CLI startup time is critical. Heavy dependencies like `axios`, `adm-zip`, and `@inquirer/prompts` can significantly slow down the CLI startup, even for simple commands like `--help` or `--version`.
**Action:** Use dynamic imports (`await import(...)`) to load these dependencies only when they are actually needed in specific commands (`init`, `update`), keeping the main entry point lightweight.
