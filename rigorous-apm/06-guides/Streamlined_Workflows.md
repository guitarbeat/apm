# Streamlined Workflows Guide

Rigorous APM now supports two coordination profiles:

- **Standard** – The legacy, fully rigorous mode that routes work through all 26 implementation agents with dedicated Task Assignment Prompts.
- **Lite** – A rapid triage path that bundles discovery questions, combines early agent calls, and keeps reporting lightweight while preserving escalation safety.

Use this guide to understand when to choose each mode and how they interact with the updated automation script, prompts, and memory strategy.

## Choosing a Mode

| Scenario | Recommended Mode | Rationale |
| --- | --- | --- |
| Initial manuscript scoping or feasibility checks | Lite | Quickly surfaces show-stopper issues and effort estimates without the full overhead. |
| Full pre-submission review or revision after peer feedback | Standard | Ensures every section, rigor dimension, and writing focus receives a dedicated expert pass. |
| Rolling weekly updates on an in-progress draft | Lite → Standard on demand | Start lite for rapid deltas; escalate to standard when the manuscript stabilises. |

## Preparing the Workspace

Use the updated automation script to scaffold review assets:

```bash
python 02-setup_review.py /path/to/manuscript.tex --mode lite
```

Key differences when `--mode lite` is selected:
- The generated `Implementation_Plan.md` contains YAML frontmatter with `review_mode: lite` and bundled task descriptions.
- `system_state.json` sets `review_progress.workflow_mode` to `lite` and replaces the pending agents list with bundle identifiers (`section_bundle`, `rigor_bundle`, `writing_bundle`, `qc`, `es`).
- Console output reminds you to use the lite Setup Agent prompt.

## Running the Setup Agent

1. Drag `03-setup-agent/setup_agent_lite_prompt.md` into your agentic IDE chat.
2. Answer the four-item discovery checklist in a single message.
3. Receive a condensed Implementation Plan update, Manager bootstrap, and memory instructions in one reply.

If the Setup Agent determines that lite mode is insufficient (e.g., too many critical blockers), it will recommend switching back to the standard prompt. Re-run the Setup Agent with the standard initiation file after updating your workspace metadata to `review_mode: standard`.

## Manager Coordination

- The Manager initiation prompt now detects the `review_mode` frontmatter and includes guidance for lite bundling.
- In lite mode, send two consolidated Task Assignment Prompts instead of 26 individual ones: one for the section+rigor bundle and one for the writing bundle.
- Maintain a single memory thread named `lite_review_round_01` (or the identifier supplied by the Setup Agent) to reduce context swapping.
- Escalate to the standard workflow if more than four high-severity findings emerge in any bundle or if the user asks for a deeper pass. Record the escalation decision in `system_state.json` and the memory log.

## Transitioning Back to Standard Mode

1. Update `Implementation_Plan.md` frontmatter to `review_mode: standard` (regenerate via the automation script or ask the Setup Agent to issue a standard plan).
2. Replace bundle tasks with the canonical phase/agent breakdown.
3. Notify the Manager Agent about the mode change in the bootstrap message.
4. Clear or archive lite-mode backlog files such as `agent_outputs/triage_backlog.md` before rerunning the comprehensive review.

## Memory Management Tips

- Keep lite-mode assumptions in a dedicated memory entry `lite_onboarding_decisions` to make escalation transparent.
- Store bundle outputs in `agent_outputs/bundles/` with filenames that match the bundle identifiers for quick traceability.
- When switching to standard mode, convert the most important lite findings into starter context for the relevant agents.

---

Lite mode is intentionally lightweight. Use it to accelerate discovery and triage, then fall back to the proven standard workflow whenever the manuscript demands deeper scrutiny.
