## 2024-05-23 - CLI Loading States
**Learning:** Users perceive "hanging" or "frozen" CLIs when network operations (like downloads) take time without visual feedback. A simple spinner drastically improves confidence.
**Action:** Always implement a spinner or progress bar for any async operation expected to take > 1 second. Ensure it cleans up (clears line) properly to avoid "ghost text" artifacts.
