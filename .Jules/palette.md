## 2025-05-27 - CLI Success Message Readability & Standardization
**Learning:** In dark mode terminals, `chalk.gray` is often too subtle for critical "Next Steps". Users tend to scan for success/fail colors and may miss important post-install actions if they blend into the background. CLI success messages often bury important "next steps" in low-contrast text.
**Action:**
1. Use a dedicated `displaySuccess` utility that provides a green checkmark (✔) for immediate visual confirmation.
2. Use high-contrast colors (White/Cyan) for "Next steps" instructions, distinct from the gray used for low-priority metadata.
3. Visually separate the success status from the action items.

## 2025-05-24 - Cursor Restoration on Process Exit
**Learning:** CLI applications that hide the cursor (using ANSI escape codes like `\x1B[?25l`) often leave the terminal in a "blind" state if the user interrupts the process (Ctrl+C). Node.js does not automatically restore the cursor on `SIGINT` or `SIGTERM`.
**Action:** Always attach `SIGINT` and `SIGTERM` listeners when initiating a UI state that alters terminal settings (like hiding the cursor). Ensure these listeners restore the cursor (`\x1B[?25h`) and then exit the process. Use a singleton pattern or a global flag to prevent attaching duplicate listeners if the UI component (like a Spinner) is instantiated multiple times.

## 2024-05-23 - CLI Loading States
**Learning:** The `upstream-apm` CLI relied on manual `console.log` for progress updates, which made long-running operations like downloads feel unresponsive or cluttered.
**Action:** Implemented a lightweight `Spinner` class (using `process.stdout` and `chalk`) to provide visual feedback. This pattern should be used for all future async CLI operations to improve perceived performance and polish.
