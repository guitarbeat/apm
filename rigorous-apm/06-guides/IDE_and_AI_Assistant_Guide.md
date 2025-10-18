# IDE and AI Assistant Integration Guide

Use this guide to fast-track Rigorous APM inside different creation environments. The focus is on _thinking through_ how each tool amplifies delegation rather than memorizing rote steps. Every section links back to the canonical assets in:

- `rigorous-apm/01-START_HERE.md` for onboarding.
- `rigorous-apm/03-review-kickoff/` for review-ready scaffolding.
- `rigorous-apm/04-manager-agent/` and `rigorous-apm/05-implementation-agents/` for role prompts.
- `rigorous-apm/06-guides/` for cross-cutting practices like handovers, memory, and customization.

## Universal baseline

| Phase | Action | Why it matters |
| --- | --- | --- |
| Orient | Load `01-START_HERE.md` and `Agent_Cheat_Sheet.md` as fixed references. | Keeps vocabulary and responsibilities consistent regardless of IDE or copilot. |
| Prime | Stage `system_state.*` and `handover.md` in the tool's quick-access panes. | Ensures that every change stays anchored to the latest swarm memory. |
| Delegate | Inject the relevant manager/implementer prompt before auto-complete or chat interactions. | Keeps copilots aligned with Rigorous APM delegation contracts. |
| Reflect | Capture deltas in `handover.md` and sync with the guidance from `Handover_Guide.md`. | Creates a reliable relay baton for the next operator or agent. |

### Selection heuristics

Use these prompts when deciding which interface should lead the current iteration:

- **Need deep diff reasoning?** Choose Cursor for its inline compare mode that pairs well with `03-review-kickoff` artifacts.
- **Coordinating a team?** Choose Kiro for swim-lane dashboards that mirror the manager/implementer hierarchy in `04-manager-agent/`.
- **Extending custom automation?** Choose VS Code, where `tasks.json` and extensions expose `02-setup_review.py` and other scripts as commands.
- **Summarizing ambiguous roadmaps?** Choose Gemini to weave long-form insights from `system_state.md`, execution checklists, and retrospectives.

Treat the following playbooks as modular templates—combine them when you context-switch between tools.

## Cursor

**Strengths**: Conversational editing with immediate diff visualization.

**Setup checklist**
- Pin the coordinator prompt from `03-setup-agent/` in a Composer tab with "auto-include" enabled so Cursor keeps it in working memory.
- Add `01-START_HERE.md` to the Sidekick "Active Files" list to summarize the mission on demand.
- Map the `handover.md` file to a project note so cross-agent summaries stay one click away.

**Operate**
1. Kick off a session by asking Cursor to outline the objective using `Agent_Cheat_Sheet.md` as grounding. Confirm the responsibilities before editing.
2. Drag the desired `.apm` prompt from `05-implementation-agents/` into the chat, then request a step-by-step plan. Use the "Compare" view to inspect proposed modifications against repository intent.
3. Run targeted commands (e.g., `python rigorous-apm/02-setup_review.py --dry-run`) in the inline terminal and paste output back into the chat for shared context.
4. After committing changes, append a brief transcript summary to `handover.md`, referencing any outstanding TODOs Cursor suggested.

**Abstract thinking cue**: When suggestions feel off-target, ask Cursor _why_ it chose a given diff. The explanation often reveals whether the prompt hierarchy or the underlying file selection needs adjustment.

## Kiro

**Strengths**: Structured collaboration with persistent, role-based canvases.

**Setup checklist**
- Create a "Rigorous APM" board template with lanes for **Intake**, **Manager**, **Implementers**, and **Review**.
- Attach the overview cards sourced from `Agent_Cheat_Sheet.md` and the execution checklist in `04-manager-agent/02_manager_execution_checklist.md`.
- Store the latest `system_state.json` as a board-level asset so Kiro's memory widgets can surface project status snapshots.

**Operate**
1. During triage, drop insights from `Context_and_Prompt_Engineering_Guide.md` into the Intake lane to remind the team of design guardrails.
2. Convert each `.apm` prompt into a reusable snippet linked to the Implementer lane. Kiro's slot memory will prefill context for recurring tasks.
3. Capture review notes from `03-review-kickoff` and attach them to cards before handing them back to the Manager lane, keeping the lifecycle explicit.
4. At the end of each cycle, export the board transcript and archive it alongside `handover.md` as described in `Handover_Guide.md`.

**Abstract thinking cue**: Revisit the swim-lane design whenever bottlenecks appear—if the Manager lane stays congested, split responsibilities along the implementation agent taxonomy in `05-implementation-agents/`.

## Visual Studio Code

**Strengths**: Extensibility and local automation.

**Setup checklist**
- Configure a multi-root workspace with `rigorous-apm/` and the target project so quick-open (`⌘P`/`Ctrl+P`) spans both contexts.
- Install Markdown Preview Enhanced and pin `01-START_HERE.md` plus `Memory_System_Guide.md` to a custom editor layout.
- Create `.code-snippets` entries for the manager prompt (`04-manager-agent/01_manager_prompt.md`) and frequently used implementer prompts.

**Operate**
1. Bind terminal tasks in `.vscode/tasks.json` for `python rigorous-apm/02-setup_review.py --help` and other repetitive commands. Chain them with `tasks.runTask` for review drills.
2. Use GitHub Copilot Chat or Continue with the "Follow file" capability aimed at `system_state.md`. Instruct the assistant to align proposals with the guardrails in `Customization_Guide.md` before applying code actions.
3. Split the editor: left pane for active code, right pane for `handover.md` or relevant `.apm` prompts. Capture decisions as you code so the session log writes itself.
4. Leverage the Source Control timeline to reconcile AI-generated suggestions with actual commits; annotate discrepancies inside `handover.md` so the next agent knows what was deferred.

**Abstract thinking cue**: Periodically ask, "Which automation should own this step—VS Code task, Copilot chat, or human judgment?" Use the answer to update `Customization_Guide.md` with new playbooks.

## Gemini

**Strengths**: High-context synthesis across long documents.

**Setup checklist**
- Prime Gemini with the condensed architecture recap from `Context_and_Prompt_Engineering_Guide.md` followed by the latest `system_state.md` snapshot.
- Upload the execution checklist (`04-manager-agent/02_manager_execution_checklist.md`) and any domain-specific `.apm` prompts as persistent references.
- Establish a shared Google Doc or Notebook that mirrors the structure of `Handover_Guide.md` for audit trails.

**Operate**
1. Ask Gemini to map the active objectives to the agent roster defined in `Agent_Cheat_Sheet.md`, highlighting any roles currently idle.
2. Provide commit diffs or PR descriptions and request scenario plans (e.g., "How do we unblock Agent 17?") rooted in the tactics inside `05-implementation-agents/`.
3. Use Gemini's reasoning to stress-test proposed pivots—compare its plan against the constraints in `Customization_Guide.md` and log approved adjustments in `handover.md`.
4. Close each session by exporting meeting notes that cite the specific Rigorous APM files consulted. Store them alongside `system_state.json` for traceability.

**Abstract thinking cue**: Challenge Gemini to articulate the _why_ behind sequencing decisions. If justification is weak, revisit the inputs—often the missing piece is an outdated state file or overlooked checklist.

---

**Next steps**: Iterate on these patterns using `Customization_Guide.md`. Every improvement you discover should feed back into the prompt library or the state-handling routines so the entire Rigorous APM network benefits.
