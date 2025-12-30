## 2024-05-23 - Lazy Loading Dependencies
**Learning:** In Node.js CLIs, importing large dependencies (like `axios`, `adm-zip`) at the top level significantly impacts startup time. Using `await import()` inside the functions that actually need them defers this cost.
**Action:** Always check for heavy, conditionally used imports in CLI entry points and refactor them to lazy imports. Use `const { default: Module } = await import('module')` for CommonJS interop.
