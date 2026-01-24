## 2025-05-24 - Cursor Restoration on Process Exit
**Learning:** CLI applications that hide the cursor (using ANSI escape codes like `\x1B[?25l`) often leave the terminal in a "blind" state if the user interrupts the process (Ctrl+C). Node.js does not automatically restore the cursor on `SIGINT` or `SIGTERM`.
**Action:** Always attach `SIGINT` and `SIGTERM` listeners when initiating a UI state that alters terminal settings (like hiding the cursor). Ensure these listeners restore the cursor (`\x1B[?25h`) and then exit the process. Use a singleton pattern or a global flag to prevent attaching duplicate listeners if the UI component (like a Spinner) is instantiated multiple times.
## 2025-05-24 - Standardized CLI Success States
**Learning:** Users often miss key information (like version numbers or next steps) when CLI output is unstructured or uniformly colored. Standardizing success messages with a visual hierarchy (Green Title > Key-Value Info > Numbered Next Steps) reduces cognitive load and ensures consistent post-action guidance.
**Action:** Use a reusable `displaySuccess` utility for all major CLI command completions instead of ad-hoc `console.log` statements.
