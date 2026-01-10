## 2024-05-23 - CLI Loading Feedback
**Learning:** Users perceive CLI tools as "stuck" or "hanging" during network operations > 2 seconds without visual feedback. Static "Downloading..." text is insufficient for variable network speeds.
**Action:** Always implement a determinate or indeterminate spinner for any async network or file system operation that blocks the main thread or takes more than 500ms. Ensure the cursor is hidden during animation and restored on exit (SIGINT/completion) to prevent terminal artifacting.
