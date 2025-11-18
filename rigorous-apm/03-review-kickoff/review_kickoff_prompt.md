# Review Kickoff Prompt

Use this single asset to move smoothly from workspace prep to Setup and Manager activation using upstream-apm v0.5 patterns.

---

## 1. Workspace Preparation

1. Generate or refresh your review workspace (add `--force` to overwrite scaffolds when re-running):
   ```bash
   python 02-setup_review.py \
     --manuscript "/path/to/manuscript.tex" \
     --output-root "/path/to/reviews" \
     --system-state-format markdown  # switch to Markdown; omit for JSON
   ```
2. Open the workspace and confirm upstream-compatible artifacts exist:
   - `metadata.json` – APM version tracking and phase status
   - `Implementation_Plan.md` – Upstream format with guide references
   - `Bootstrap_Prompt.md` – YAML frontmatter for Manager initialization
   - `system_state.json` / `system_state.md` – Workspace state (format depends on flag)
   - `agent_outputs/` – Empty and ready for deliverables
   - `manuscript_assets/` – Staged files when `--copy-manuscript` was provided

> Managing multiple manuscripts? Run the helper again with a different `--manuscript` path—each review lives in its own `<name>_review/` directory.

---

## 2. Launch the Setup Agent (Upstream 5-Phase Pattern)

1. Drag `03-setup-agent/setup_agent_initiation_prompt.md` into the chat.
2. Share the draft plan using the bundled automation snippet:
   ```automation
   # share_plan_with_setup.apm
   /load file "Implementation_Plan.md"
   ```
3. The Setup Agent follows upstream's 5-phase workflow:
   - **Phase 1: Context Synthesis** – Gather manuscript details using `{GUIDE_PATH:upstream/Context_Synthesis_Guide.md}`
   - **Phase 2: Project Breakdown** – Create 5-phase review plan (Section→Rigor→Writing→QC→ES)
   - **Phase 3: Review** – Validate plan with checkpoints using `{GUIDE_PATH:upstream/Project_Breakdown_Review_Guide.md}`
   - **Phase 4: Enhancement** – Refine based on manuscript specifics
   - **Phase 5: Bootstrap** – Generate Bootstrap Prompt with YAML frontmatter for Manager Agent

**Checklist**
- [ ] Manuscript context (type, outlet, field, priorities) confirmed through Context Synthesis.
- [ ] Setup Agent completed all 5 phases with approval gates.
- [ ] Setup Agent saved updated `Implementation_Plan.md` in upstream format.
- [ ] Setup Agent generated `Bootstrap_Prompt.md` with YAML frontmatter.

---

## 3. Initialize the Manager Agent (Upstream Bootstrap Pattern)

1. Drag `04-manager-agent/manager_agent_initiation_prompt.md` into the conversation after the Setup Agent signs off.
2. Load the Bootstrap Prompt with YAML frontmatter:
   ```automation
   # Load Bootstrap Prompt (contains workspace context and coordination strategy)
   /load file "Bootstrap_Prompt.md"
   ```
3. Optionally load the refined Implementation Plan:
   ```automation
   # manager_load_plan.apm
   /load file "Implementation_Plan.md"
   ```
4. Manager Agent processes Bootstrap Prompt and initializes:
   - Workspace context (manuscript_type, target_outlet, research_field)
   - 26-agent coordination strategy (3-phase parallel execution)
   - Memory System structure following `{GUIDE_PATH:upstream/Memory_System_Guide.md}`
   - Task Assignment protocol using `{GUIDE_PATH:upstream/Task_Assignment_Guide.md}`

**Progression Gate**
- [ ] Setup Agent deliverables filed in the workspace.
- [ ] Manager Agent processed Bootstrap Prompt successfully.
- [ ] Manager Agent confirms understanding of 26-agent coordination model.
- [ ] Manager Agent ready to create Task Assignment Prompts for Implementation Agents.

---

## 4. During Execution (3-Phase Parallel Model)

**Phase 1: Section Analysis (S1-S10)**
- Manager creates Task Assignment Prompts for all 10 section agents in parallel
- Each agent analyzes its assigned manuscript section
- Agents create Memory Logs following `{GUIDE_PATH:upstream/Memory_Log_Guide.md}`
- Monitor `agent_outputs/section/` for deliverables

**Phase 2: Rigor + Writing Analysis (R1-R7, W1-W7)**
- Manager coordinates 14 agents in parallel after Section phase completes
- Rigor agents (R1-R7) evaluate scientific methodology and standards
- Writing agents (W1-W7) assess language, style, and presentation
- Monitor `agent_outputs/rigor/` and `agent_outputs/writing/` for deliverables

**Phase 3: Quality Control → Executive Summary**
- Quality Control Agent synthesizes findings from all 24 agents
- Executive Summary Agent generates final comprehensive report
- Monitor `agent_outputs/quality_control/` and `agent_outputs/executive_summary/`

**Ongoing Monitoring**
- Check `metadata.json` for phase status updates (pending → in_progress → complete)
- Update the system state file (`system_state.json` or `.md`) if you pause or resume manually
- Each Implementation Agent references `{GUIDE_PATH:upstream/Memory_Log_Guide.md}` for documentation format
- After all agents finish, inspect the `quality_control` and `executive_summary` outputs to prepare your decision package
