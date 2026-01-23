## 2025-05-24 - Cursor Restoration on Process Exit
**Learning:** CLI applications that hide the cursor (using ANSI escape codes like `\x1B[?25l`) often leave the terminal in a "blind" state if the user interrupts the process (Ctrl+C). Node.js does not automatically restore the cursor on `SIGINT` or `SIGTERM`.
**Action:** Always attach `SIGINT` and `SIGTERM` listeners when initiating a UI state that alters terminal settings (like hiding the cursor). Ensure these listeners restore the cursor (`\x1B[?25h`) and then exit the process. Use a singleton pattern or a global flag to prevent attaching duplicate listeners if the UI component (like a Spinner) is instantiated multiple times.

## 2025-05-27 - Standardized Success Messages
**Learning:** CLI success messages often bury important "next steps" in low-contrast text. Users tend to miss what they should do next if it looks like just another log line.
**Action:** Use a dedicated `displaySuccess` utility that:
1. Uses a green checkmark (✔) for immediate visual confirmation.
2. Uses high-contrast colors (White/Cyan) for "Next steps" instructions, distinct from the gray used for low-priority metadata.
3. Visually separates the success status from the action items.
