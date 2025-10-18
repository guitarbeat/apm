# Rigorous APM - Start Here

A specialized Agentic Project Management (APM) instance for academic manuscript review with 26 focused agents.

## 🔍 Audience Legend

- **👤 Human-only** – Operators and reviewers should read or execute this themselves.
- **🤖 Agent-ready** – Paste directly into an AI agent or IDE without additional editing.
- **🔁 Shared** – Humans trigger or configure the asset, and agents consume the output.

---

## 🚀 Quick Start (Streamlined)

1. **👤 Bootstrap a dedicated workspace**
   ```bash
   # POSIX / macOS / Linux (line continuation)
   python 02-setup_review.py \
     --manuscript "/path/to/manuscript.tex" \
     --output-root "/path/to/reviews" \
     --non-interactive

   # Windows (PowerShell / cmd) single-line
   python 02-setup_review.py --manuscript "C:\path\to\manuscript.tex" --output-root "C:\path\to\reviews" --non-interactive
   ```
   - Omit `--output-root` to place the workspace inside `rigorous-apm/` next to the manuscript.
   - Add `--copy-manuscript` to stage `.bib/.cls/.sty/.bst` companions and common figure folders under `manuscript_assets/`.
   - Add `--system-state-format markdown` if you prefer a Markdown snapshot instead of JSON.
   - Add `--plan-detail-level descriptive` to embed each agent's specialization alongside checklist items.
   - Remove `--non-interactive` if you prefer guided prompts.

   **The helper generates**
   - `Implementation_Plan.md` (🔁) – Includes an embedded audience legend and icon-tagged checklists for every phase.
   - `system_state.json` / `system_state.md` (🔁) – Shared workspace state, now stamped with the same legend for humans and agents.
   - `agent_outputs/` (🤖) – Storage for agent deliverables; inspect results here.
   - Optional `manuscript_assets/` (🔁) – Humans curate supporting files that agents reference.
   - Re-running without `--force` keeps existing files but automatically refreshes any generated plan or system-state file that is missing the shared legend.

2. **🤖 Kick off Setup and Manager from a single prompt**
   - Drag `03-review-kickoff/review_kickoff_prompt.md` (🤖) into your agentic IDE.
   - Share `Implementation_Plan.md` with the Setup Agent using `03-review-kickoff/share_plan_with_setup.apm` (🔁).
   - After the Setup Agent refines the plan, run `03-review-kickoff/manager_load_plan.apm` (🔁) so the Manager Agent imports the latest version without copy/paste.

3. **🔁 Track progress and collect outputs**
   - Monitor `agent_outputs/` (🤖) as the Manager coordinates all 26 agents.
   - Re-run `manager_load_plan.apm` (🔁) whenever the plan changes to keep the Manager in sync.
   - Consult `quality_control` and `executive_summary` deliverables (👤) for the decision package.

---

## 📂 Workspace Layout

```
rigorous-apm/
├── 01-START_HERE.md                    # 👤 Orientation for operators (this file)
├── 02-setup_review.py                  # 🔁 CLI helper humans run, agents consume outputs
├── 03-review-kickoff/                  # 🤖 Drag-and-drop prompts + 🔁 plan loaders
├── 03-setup-agent/                     # 🤖 Setup Agent initiation prompt
├── 04-manager-agent/                   # 🤖 / 🔁 Manager prompts and state loaders
├── 05-implementation-agents/           # 🤖 Execution prompts for specialist agents
└── 06-guides/                          # 👤 Extended reading for operators
```

Refer to `06-guides/Agent_Cheat_Sheet.md` for a succinct list of every implementation agent and deliverable.

---

## ⚙️ Automation Snippets

| File | Audience | Purpose |
| --- | --- | --- |
| `03-review-kickoff/share_plan_with_setup.apm` | 🔁 | Loads `Implementation_Plan.md` for the Setup Agent. |
| `03-review-kickoff/manager_load_plan.apm` | 🔁 | Reloads the latest plan for the Manager Agent. |

Drag these snippets directly into your IDE instead of recreating `/load` commands manually.

---

## 🛠️ CLI Helper Options

| Flag | Audience | Description |
| --- | --- | --- |
| `--manuscript PATH` | 👤 | Provide the manuscript location without an interactive prompt. |
| `--output-root DIR` | 👤 | Choose where review folders are stored (ideal for batching). |
| `--non-interactive` | 👤 | Fail fast when required information is missing. |
| `--force` | 👤 | Overwrite existing scaffold files in the review directory. |
| `--copy-manuscript` | 🔁 | Stage the manuscript file plus common support assets inside `manuscript_assets/`. |
| `--system-state-format {json,markdown}` | 🔁 | Choose whether the generated system state file is JSON (default) or Markdown. |
| `--plan-detail-level {concise,descriptive}` | 🔁 | Control how much agent metadata is embedded in `Implementation_Plan.md`; audience icons are always included. |

---

## 📚 Reference Guides

All supporting documentation lives in `06-guides/`:

- `README.md` – Navigation map for the guide set.
- `Agent_Cheat_Sheet.md` (👤) – Quick reference for every agent and deliverable.
- `Context_and_Prompt_Engineering_Guide.md` (👤) – Architecture principles and prompt design.
- `Customization_Guide.md` (👤) – How to tailor Rigorous APM for specific journals or teams.
- `Memory_System_Guide.md` (🔁) – Persistent state strategy the manager and specialists rely on.
- `Handover_Guide.md` (🔁) – Best practices for passing context between sessions.
