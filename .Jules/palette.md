## 2025-05-24 - Cursor Restoration on Process Exit
**Learning:** CLI applications that hide the cursor (using ANSI escape codes like `\x1B[?25l`) often leave the terminal in a "blind" state if the user interrupts the process (Ctrl+C). Node.js does not automatically restore the cursor on `SIGINT` or `SIGTERM`.
**Action:** Always attach `SIGINT` and `SIGTERM` listeners when initiating a UI state that alters terminal settings (like hiding the cursor). Ensure these listeners restore the cursor (`\x1B[?25h`) and then exit the process. Use a singleton pattern or a global flag to prevent attaching duplicate listeners if the UI component (like a Spinner) is instantiated multiple times.

## 2025-05-24 - Visual Hierarchy in CLI Success Messages
**Learning:** Users often scan CLI output for "what happened" and "what to do next". Flat gray text for both status and instructions reduces scannability and actionable clarity.
**Action:** Use a consistent `displaySuccess` utility that visually separates the primary success status (green/bold), metadata (gray/white), and next steps (cyan header). Use numbering and high contrast for steps to guide user action immediately.
