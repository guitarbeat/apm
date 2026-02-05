## 2025-05-24 - Cursor Restoration on Process Exit
**Learning:** CLI applications that hide the cursor (using ANSI escape codes like `\x1B[?25l`) often leave the terminal in a "blind" state if the user interrupts the process (Ctrl+C). Node.js does not automatically restore the cursor on `SIGINT` or `SIGTERM`.
**Action:** Always attach `SIGINT` and `SIGTERM` listeners when initiating a UI state that alters terminal settings (like hiding the cursor). Ensure these listeners restore the cursor (`\x1B[?25h`) and then exit the process. Use a singleton pattern or a global flag to prevent attaching duplicate listeners if the UI component (like a Spinner) is instantiated multiple times.

## 2025-05-27 - CLI Success Message Readability
**Learning:** In dark mode terminals (which most devs use), `chalk.gray` is often too subtle for critical "Next Steps" instructions. Users tend to scan for success/fail colors and may miss important post-install actions if they blend into the background.
**Action:** For actionable "Next Steps" or important post-operation instructions, use high-contrast colors like `chalk.bold.cyan` for headers and `chalk.white` for list items, instead of `chalk.gray` which should be reserved for low-priority logs.

## 2025-05-30 - Standardized Error Reporting
**Learning:** Inconsistent error reporting (manual `console.error` vs structured utilities) leads to a disjointed user experience where failures feel like crashes rather than handled states.
**Action:** Implement and use a standardized `displayError` utility that mirrors success messages (`✔` vs `✖`) and separates operational logs (stdOut) from error details (stdErr) to maintain CLI stream best practices.
