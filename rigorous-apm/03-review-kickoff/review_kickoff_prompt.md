# Review Kickoff Prompt

Use this single asset to move smoothly from workspace prep to Setup and Manager activation.

---

## 1. Workspace Preparation

1. Generate or refresh your review workspace (add `--force` to overwrite scaffolds when re-running):
   ```bash
   python 02-setup_review.py \
     --manuscript "/path/to/manuscript.tex" \
     --output-root "/path/to/reviews" \
     --system-state-format markdown  # switch to Markdown; omit for JSON
   ```
2. Open the workspace and confirm:
   - `Implementation_Plan.md` and the generated system state file (`system_state.json` by default, `system_state.md` when Markdown output is selected) exist.
   - `agent_outputs/` is empty and ready.
   - `manuscript_assets/` contains staged files when `--copy-manuscript` was provided.

> Managing multiple manuscripts? Run the helper again with a different `--manuscript` path—each review lives in its own `<name>_review/` directory.

---

## 2. Launch the Setup Agent

1. Drag `03-setup-agent/setup_agent_initiation_prompt.md` into the chat.
2. Share the draft plan using the bundled automation snippet:
   ```automation
   # share_plan_with_setup.apm
   /load file "Implementation_Plan.md"
   ```
3. Confirm the Setup Agent updates the plan and notes any manuscript assets it needs.

**Checklist**
- [ ] Manuscript context (scope, outlet, deadlines) confirmed.
- [ ] Setup Agent saved an updated `Implementation_Plan.md` in the workspace.

---

## 3. Promote the Plan to the Manager Agent

1. Drag `04-manager-agent/manager_agent_initiation_prompt.md` into the conversation after the Setup Agent signs off.
2. Load the refined plan directly from disk—no copy/paste required:
   ```automation
   # manager_load_plan.apm
   /load file "Implementation_Plan.md"
   ```
3. Re-run the snippet anytime the plan changes so the Manager Agent stays synced.

**Progression Gate**
- [ ] Setup Agent deliverables filed in the workspace.
- [ ] Manager Agent confirms plan import via `manager_load_plan.apm`.

---

## 4. During Execution

- Monitor the `agent_outputs/` directory for per-agent deliverables.
- Update the system state file (`system_state.json` or `.md`) if you pause or resume the review manually.
- After all agents finish, inspect the `quality_control` and `executive_summary` outputs to prepare your decision package.
