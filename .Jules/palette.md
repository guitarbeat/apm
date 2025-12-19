## 2025-02-21 - CLI Information Hierarchy & List Visibility
**Learning:** In terminal UIs, users often miss "next steps" instructions when they are styled with low contrast (gray) similar to less important info. Additionally, default list limits (7 items) obscure options in medium-sized lists (10+ items), hiding choices like "Roo Code" by default.
**Action:** Use high-contrast colors (Cyan/White) for actionable post-command instructions. Explicitly set `pageSize` (e.g. 15) for selection prompts to ensure all options are visible at a glance without scrolling.
