## 2024-05-23 - Lazy Load CLI Dependencies
**Learning:** Static imports in Node.js CLIs incur a startup penalty even for unused commands. Heavy libraries like `axios`, `adm-zip`, and `@inquirer/prompts` can add hundreds of milliseconds to boot time.
**Action:** Use dynamic `await import('module')` inside command actions or specific functions to lazy-load these heavy dependencies only when needed.
