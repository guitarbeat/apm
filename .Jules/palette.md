# PALETTE'S JOURNAL

This journal documents CRITICAL UX and accessibility learnings.
It is NOT a log of routine work.

Format:
## YYYY-MM-DD - [Title]
**Learning:** [UX/a11y insight]
**Action:** [How to apply next time]

---

## 2025-12-23 - CLI Progress Feedback
**Learning:** Users lack confidence in long-running CLI operations (like file downloads) without visual feedback, often assuming the process has hung.
**Action:** Implement immediate feedback (spinners or progress bars) for any network or file system operation lasting >1 second. Implemented a dependency-free progress bar using `process.stdout` and stream monitoring.
