## 2024-05-23 - Lazy Loading CLI Dependencies
**Learning:** Static imports in Node.js CLIs incur a startup penalty even when the imported modules aren't used for the invoked command (e.g. `apm --help`). Heavy dependencies like `axios` and `adm-zip` significantly increase startup time.
**Action:** Use dynamic imports (`await import(...)`) for heavy dependencies inside the specific functions or commands that require them. For CommonJS modules in an ESM project, remember to destructure the default export: `const { default: Module } = await import('module')`.
