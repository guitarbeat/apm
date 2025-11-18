# Rigorous APM - Start Here

A specialized Agentic Project Management (APM) domain extension for academic manuscript review with 26 focused agents, built on upstream-apm v0.5 patterns.

## 🔍 Audience Legend

- **👤 Human-only** – Operators and reviewers should read or execute this themselves.
- **🤖 Agent-ready** – Paste directly into an AI agent or IDE without additional editing.
- **🔁 Shared** – Humans trigger or configure the asset, and agents consume the output.

---

## 🔗 Upstream Relationship

Rigorous APM is a **domain-specific extension** of [upstream-apm v0.5](../upstream-apm/README.md), the foundational APM framework. This means:

- **Core patterns from upstream**: Setup Agent 5-phase workflow, Manager Agent coordination, Bootstrap Prompts with YAML frontmatter, Memory System, and guide reference syntax (`{GUIDE_PATH:filename.md}`)
- **Manuscript specialization**: 26 specialized Implementation Agents (S1-S10 for sections, R1-R7 for rigor, W1-W7 for writing, plus QC and ES), 3-phase parallel execution model, and academic review criteria
- **Shared guides**: Upstream's 7 core guides live in `06-guides/upstream/` alongside manuscript-specific guides in `06-guides/`
- **Enhanced automation**: `02-setup_review.py` generates upstream-compatible artifacts (metadata.json, Bootstrap Prompts, Implementation Plans)

This integration gives you proven APM infrastructure plus specialized manuscript review capabilities. See [INTEGRATION_STRATEGY.md](../INTEGRATION_STRATEGY.md) for the full technical approach.

---

## 🚀 Quick Start (Upstream-Integrated Workflow)

### Phase 1: Workspace Setup

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

   **The helper generates (upstream-compatible format)**
   - `metadata.json` (🔁) – APM version tracking, manuscript metadata, and phase status
   - `Implementation_Plan.md` (🔁) – Upstream format with guide references and 5-phase structure
   - `Bootstrap_Prompt.md` (🔁) – YAML frontmatter initialization for Manager Agent
   - `system_state.json` / `system_state.md` (🔁) – Shared workspace state
   - `agent_outputs/` (🤖) – Storage for agent deliverables
   - Optional `manuscript_assets/` (🔁) – Supporting files for agent reference
   - Re-running without `--force` keeps existing files but automatically refreshes generated artifacts.

### Phase 2: Setup Agent (5-Phase Workflow)

2. **🤖 Launch the Setup Agent**
   - Drag `03-setup-agent/setup_agent_initiation_prompt.md` (🤖) into your agentic IDE.
   - The Setup Agent follows upstream's 5-phase pattern:
     1. **Context Synthesis** – Gather manuscript details (type, outlet, field, priorities)
     2. **Project Breakdown** – Create 5-phase review plan (Section→Rigor→Writing→QC→ES)
     3. **Review** – Validate plan completeness with checkpoints
     4. **Enhancement** – Refine based on manuscript specifics
     5. **Bootstrap** – Generate Bootstrap Prompt for Manager Agent
   - Share the draft plan using `03-review-kickoff/share_plan_with_setup.apm` (🔁).
   - Setup Agent references upstream guides: `{GUIDE_PATH:upstream/Context_Synthesis_Guide.md}`, `{GUIDE_PATH:upstream/Implementation_Plan_Guide.md}`

### Phase 3: Manager Agent Coordination

3. **🤖 Initialize the Manager Agent**
   - Drag `04-manager-agent/manager_agent_initiation_prompt.md` (🤖) into the conversation after Setup Agent completes.
   - Load the Bootstrap Prompt: `Bootstrap_Prompt.md` contains YAML frontmatter with workspace context.
   - Manager Agent coordinates 26 Implementation Agents through 3-phase parallel execution:
     - **Phase 1**: Section Analysis (S1-S10) in parallel
     - **Phase 2**: Rigor (R1-R7) + Writing (W1-W7) in parallel
     - **Phase 3**: Quality Control → Executive Summary
   - Manager references upstream guides: `{GUIDE_PATH:upstream/Task_Assignment_Guide.md}`, `{GUIDE_PATH:upstream/Memory_System_Guide.md}`

### Phase 4: Execution & Monitoring

4. **🔁 Track progress and collect outputs**
   - Monitor `agent_outputs/` (🤖) as agents complete tasks.
   - Check `metadata.json` for phase status updates.
   - Each Implementation Agent creates Memory Logs following `{GUIDE_PATH:upstream/Memory_Log_Guide.md}`.
   - Consult `quality_control` and `executive_summary` deliverables (👤) for the decision package.

---

## 📂 Workspace Layout

```
rigorous-apm/
├── 01-START_HERE.md                    # 👤 Orientation for operators (this file)
├── 02-setup_review.py                  # 🔁 CLI helper (generates upstream-compatible artifacts)
├── 03-review-kickoff/                  # 🤖 Drag-and-drop prompts + 🔁 plan loaders
├── 03-setup-agent/                     # 🤖 Setup Agent (upstream 5-phase pattern)
├── 04-manager-agent/                   # 🤖 Manager Agent (upstream coordination + 26-agent orchestration)
├── 05-implementation-agents/           # 🤖 26 specialist agents (S1-S10, R1-R7, W1-W7, QC, ES)
│   ├── implementation_agent_base_prompt.md  # Base template with upstream patterns
│   ├── section/                        # S1-S10 section analysis agents
│   ├── rigor/                          # R1-R7 scientific rigor agents
│   ├── writing/                        # W1-W7 writing quality agents
│   ├── quality_control_agent_prompt.md # QC synthesis agent
│   └── executive_summary_agent_prompt.md # ES reporting agent
└── 06-guides/                          # 👤 / 🔁 Guides for operators and agents
    ├── upstream/                       # 7 core upstream-apm guides
    └── [manuscript-specific guides]    # Domain specialization guides
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

### Upstream Guides (Foundation Patterns)
- `upstream/Context_Synthesis_Guide.md` (🔁) – How Setup Agent gathers project context
- `upstream/Implementation_Plan_Guide.md` (🔁) – Structure for project breakdown
- `upstream/Memory_Log_Guide.md` (🔁) – Documentation format for agent findings
- `upstream/Memory_System_Guide.md` (🔁) – Persistent state strategy across agents
- `upstream/Project_Breakdown_Guide.md` (🔁) – Task decomposition methodology
- `upstream/Project_Breakdown_Review_Guide.md` (🔁) – Plan validation procedures
- `upstream/Task_Assignment_Guide.md` (🔁) – Manager-to-Implementation handoff protocol

### Manuscript-Specific Guides (Domain Specialization)
- `README.md` – Navigation map for both upstream and domain guides
- `Agent_Cheat_Sheet.md` (👤) – Quick reference for all 26 agents and deliverables
- `Context_and_Prompt_Engineering_Guide.md` (👤) – Architecture principles and prompt design
- `Customization_Guide.md` (👤) – How to tailor Rigorous APM for specific journals or teams
- `Manuscript_Review_Implementation_Plan_Guide.md` (🔁) – 5-phase review workflow details
- `Handover_Guide.md` (🔁) – Best practices for passing context between sessions

**Guide Reference Pattern**: Agents use `{GUIDE_PATH:filename.md}` syntax to reference guides. The system resolves paths to either `06-guides/upstream/` or `06-guides/` based on the filename.
