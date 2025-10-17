# Rigorous APM - Start Here

A specialized Agentic Project Management (APM) instance for academic manuscript review with 26 focused agents.

---

## 🚀 Quick Start (Streamlined)

1. **Bootstrap a dedicated workspace**
   ```bash
   python 02-setup_review.py \
     --manuscript "/path/to/manuscript.tex" \
     --output-root "/path/to/reviews" \
     --non-interactive
   ```
   - Omit `--output-root` to place the workspace inside `rigorous-apm/` next to the manuscript.
   - Add `--copy-manuscript` to stage `.bib/.cls/.sty/.bst` companions and common figure folders under `manuscript_assets/`.
   - Remove `--non-interactive` if you prefer guided prompts.

   **The helper generates**
   - `Implementation_Plan.md` – pre-filled checklist covering every Rigorous APM agent.
   - `system_state.json` – baseline workspace state for resuming a review.
   - `agent_outputs/` – storage for per-agent deliverables.
   - Optional `manuscript_assets/` when `--copy-manuscript` is used.

2. **Kick off Setup and Manager from a single prompt**
   - Drag `03-review-kickoff/review_kickoff_prompt.md` into your agentic IDE.
   - Share `Implementation_Plan.md` with the Setup Agent using `03-review-kickoff/share_plan_with_setup.apm`.
   - After the Setup Agent refines the plan, run `03-review-kickoff/manager_load_plan.apm` so the Manager Agent imports the latest version without copy/paste.

3. **Track progress and collect outputs**
   - Monitor `agent_outputs/` as the Manager coordinates all 26 agents.
   - Re-run `manager_load_plan.apm` whenever the plan changes to keep the Manager in sync.
   - Consult `quality_control` and `executive_summary` deliverables for the decision package.

---

## 📂 Workspace Layout

```
rigorous-apm/
├── 01-START_HERE.md                    # You are here
├── 02-setup_review.py                  # Workspace helper
├── 03-review-kickoff/                  # Combined Setup + Manager prompt and snippets
├── 03-setup-agent/                     # Setup Agent prompt
├── 04-manager-agent/                   # Manager prompts
├── 05-implementation-agents/           # Section, Rigor, Writing, and synthesis agents
└── 06-guides/                          # Deep-dive documentation
```

Refer to `06-guides/Agent_Cheat_Sheet.md` for a succinct list of every implementation agent and deliverable.

---

## ⚙️ Automation Snippets

| File | Purpose |
| --- | --- |
| `03-review-kickoff/share_plan_with_setup.apm` | Loads `Implementation_Plan.md` for the Setup Agent. |
| `03-review-kickoff/manager_load_plan.apm` | Reloads the latest plan for the Manager Agent. |

Drag these snippets directly into your IDE instead of recreating `/load` commands manually.

---

## 🛠️ CLI Helper Options

| Flag | Description |
| --- | --- |
| `--manuscript PATH` | Provide the manuscript location without an interactive prompt. |
| `--output-root DIR` | Choose where review folders are stored (ideal for batching). |
| `--non-interactive` | Fail fast when required information is missing. |
| `--force` | Overwrite existing scaffold files in the review directory. |
| `--copy-manuscript` | Stage the manuscript file plus common support assets inside `manuscript_assets/`. |

---

## 📚 Reference Guides

All supporting documentation lives in `06-guides/`:

- `README.md` – Navigation map for the guide set.
- `Agent_Cheat_Sheet.md` – Quick reference for every agent and deliverable.
- `Context_and_Prompt_Engineering_Guide.md` – Architecture principles and prompt design.
- `Customization_Guide.md` – How to tailor Rigorous APM for specific journals or teams.
- `Memory_System_Guide.md` – Persistent state strategy.
- `Handover_Guide.md` – Best practices for passing context between sessions.
