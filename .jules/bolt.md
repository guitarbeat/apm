## 2024-05-23 - Lazy Loading Heavy Dependencies
**Learning:** Node.js CLIs using static imports of heavy libraries (like `axios`, `adm-zip`) incur a significant startup penalty, even for commands that don't use them (like `--help`). Switching to dynamic `await import()` reduced startup time from ~505ms to ~174ms (~65% improvement).
**Action:** For CLI tools, always audit top-level imports and lazy-load heavy dependencies that are not needed for the critical initialization path.

## 2024-05-23 - Lazy Loading @inquirer/prompts
**Learning:** Statically importing `@inquirer/prompts` added ~60-87ms to the CLI startup time. Since it's only needed for interactive commands (`init`, `update`), lazy-loading it reduced the `--help` command execution time by ~150ms (~50% improvement).
**Action:** Audit interactive CLI libraries and ensure they are only imported when interactivity is actually required.

## 2024-05-23 - Lazy Loading Logic Extraction
**Learning:** Moving logic that depends on global constants (like `createOrUpdateMetadata` using `CURRENT_CLI_VERSION`) to a separate utility file requires updating the function signature to accept those values as arguments. This is essential for enabling lazy loading of the utility file without circular dependencies or missing data.
**Action:** When refactoring for lazy loading, explicitly pass necessary context (like versions or config) to utility functions instead of relying on closure scope from the main entry point.

## 2024-05-23 - Duplicate Variable Declarations in Dynamic Imports
**Learning:** Copy-pasting dynamic import blocks (e.g., `const { select } = await import('@inquirer/prompts')`) inside try/catch blocks or if/else branches can lead to "Identifier has already been declared" SyntaxErrors if the variable is also declared in the outer scope.
**Action:** Declare dynamic imports once at the top of the async action handler or verify scope carefully when using them in nested blocks.
