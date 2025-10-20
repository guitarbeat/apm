# Rigorous APM Guides (Consolidated)

This README replaces the standalone guidebook so that all navigation lives in a single file. Use it to jump between the onboarding prompts, specialist guides, and domain playbooks that make up the Rigorous APM workflow.

## How to Use This Guide

1. Skim the section that matches your immediate objective (onboarding, customization, tooling, or manuscript review).
2. Follow the inline links to the underlying files—each points to the canonical asset in the `rigorous-apm/` tree.
3. Return here whenever you need to understand how the parts fit together or to locate the next asset in your workflow.

### Audience Legend

- **👤 Human-only** – Operator-facing guidance, walkthroughs, or checklists.
- **🤖 Agent-ready** – Drag-and-drop prompts or files meant to be ingested by an AI agent without rewriting.
- **🔁 Shared** – Humans trigger or configure the asset, and agents consume or update the results.

---

## 1. Onboarding & Review Kickoff

| Purpose | Audience | Read This | Why It Matters |
| --- | --- | --- | --- |
| Launch a new review workspace | 👤 | [`../01-START_HERE.md`](../01-START_HERE.md) | Walks through the 26-agent operating model, directory layout, and the order of operations for new operators. |
| Spin up a review workspace from the CLI | 🔁 | [`../02-setup_review.py`](../02-setup_review.py) | Provides the automation entry point and now auto-tags generated assets with the shared audience legend. |
| Bootstrap the reviewer and manager agents | 🤖 | [`../03-review-kickoff/review_kickoff_prompt.md`](../03-review-kickoff/review_kickoff_prompt.md), [`../03-setup-agent/setup_agent_initiation_prompt.md`](../03-setup-agent/setup_agent_initiation_prompt.md) | Supplies the initial prompts you will paste into your IDE/assistant to start the coordination loop. |
| Align the manager before handing off to implementation | 🔁 | [`../04-manager-agent/manager_bootstrap_prompt.md`](../04-manager-agent/manager_bootstrap_prompt.md), [`../04-manager-agent/manager_agent_initiation_prompt.md`](../04-manager-agent/manager_agent_initiation_prompt.md) | Ensures the manager agent captures project goals, constraints, and deliverables before delegating work. |
| Select the right implementation prompt | 🤖 | [`../05-implementation-agents/`](../05-implementation-agents/) | Contains the execution templates (base, quality control, executive summary) for implementation specialists. |

**Quick Start Flow**: Start with `01-START_HERE.md` (👤), run `02-setup_review.py` (🔁) if you need automation, seed the review kickoff prompt (🤖), then progress through the manager (🔁) and implementation prompts (🤖). When you re-run the helper it auto-patches older outputs with the legend, so reserve `--force` for full regenerations after safeguarding manual edits.

---

## 2. Agent Roster at a Glance

Use the condensed view below before diving into the detailed tables in [`Agent_Cheat_Sheet.md`](Agent_Cheat_Sheet.md).

- **Section Analysts (S1-S10)**: Ten agents that examine every manuscript section from title to supplementary materials to guarantee complete coverage.
- **Rigor Reviewers (R1-R7)**: Specialists that validate originality, ethics, reproducibility, statistics, and overall consistency.
- **Writing Coaches (W1-W7)**: Improve clarity, structure, accessibility, and journal alignment.
- **Integration Leads (X1-X2)**: Combine insights into unified recommendations and ensure deliverables align with APM standards.

---

## 3. Operating Principles & Prompt Craft

These practices keep your prompts interoperable across IDE drag-and-drop workflows and AI assistants.

1. **Context Assembly** – Review the layered briefing model in [`Context_and_Prompt_Engineering_Guide.md`](Context_and_Prompt_Engineering_Guide.md) before composing a prompt. It explains how to blend manuscript context, agent instructions, and memory state without exceeding context limits.
2. **Prompt Formatting** – Maintain the Markdown + YAML front matter conventions described in the same guide. This standardization keeps the manager and implementation agents in sync.
3. **System State Contracts** – Treat `system_state.*` files as APIs: they expose structured fields that downstream agents read. The Context & Prompt guide shows how to request updates without breaking compatibility.
4. **Meta-Prompting** – Use the meta-prompt scaffolds in the guide to spin up custom reviewers while preserving tone, citation expectations, and completion style.

Keep this section in view when you are editing prompts under the `03-` through `05-` directories.

---

## 4. Memory, State, and Handoffs

Reliable state management underpins multi-session reviews.

- **Memory Files** (🔁) – [`Memory_System_Guide.md`](Memory_System_Guide.md) documents the schema for `system_state.json`/`.md`, memory logs, and interim artifacts. Use it to understand what each field means and how to add safe extensions.
- **Session Continuity** (🔁) – [`Handover_Guide.md`](Handover_Guide.md) specifies when to create a `handover.md`, how to summarize pending work, and how to brief a follow-up operator.
- **Quality Gates** (🤖/👤) – Combine the above with the quality-control prompt in [`../05-implementation-agents/quality_control_agent_prompt.md`](../05-implementation-agents/quality_control_agent_prompt.md) to ensure deliverables stay aligned with the saved state.

When in doubt, update the memory log first, then trigger a handover to keep every agent aligned with the latest decisions.

---

## 5. Tooling & IDE Integration

The IDE playbooks in [`IDE_and_AI_Assistant_Guide.md`](IDE_and_AI_Assistant_Guide.md) outline how to operate Cursor, Kiro, VS Code, and Gemini alongside the APM prompts. Use this condensed checklist:

- **Baseline Setup** (👤) – Establish a shared folder structure, sync `system_state.*` files, and configure autosave before delegating tasks.
- **Assistant Pairing** (👤) – Match the assistant to the phase of work (e.g., Cursor for implementation bursts, Gemini for wide exploration) as described in the guide’s heuristic tables.
- **Context Refresh** (🔁) – After each major change, re-run the assistant-specific “state sync” ritual from the guide to keep prompts and handovers current.

---

## 6. Customization & Extension Patterns

When adapting Rigorous APM to new domains, lean on [`Customization_Guide.md`](Customization_Guide.md):

1. **Identify the Levers** – The guide breaks down which prompts, memory fields, and agents are safe to modify for domain-specific work.
2. **Domain Playbooks** – Follow the pre-built examples for web development, data science, mobile, and ML projects to scaffold your own specialization.
3. **Tool Integrations** – Map new MCP tools or APIs into the agent workflow using the step-by-step integration checklist.
4. **Version Management** – Use the branching strategies and release checklist in the guide to keep customizations in sync with upstream changes.

Document any new assets you add under `06-guides/` here so future operators can extend them without guesswork.

---

## 7. Specialized Playbooks

Some projects require deep domain instructions beyond the general-purpose prompts.

- **Manuscript Review Execution** – The end-to-end implementation plan in [`Manuscript_Review_Implementation_Plan_Guide.md`](Manuscript_Review_Implementation_Plan_Guide.md) combines agent orchestration, timeline planning, and quality checks tailored for academic manuscripts.
- **Executive & Summary Outputs** – Pair that playbook with [`../05-implementation-agents/executive_summary_agent_prompt.md`](../05-implementation-agents/executive_summary_agent_prompt.md) when stakeholders expect condensed deliverables.
- **Frontend Troubleshooting Recipes** – Use [`Troubleshooting_Playbook.md`](Troubleshooting_Playbook.md) to diagnose runtime errors such as `TypeError: Cannot read properties of null (reading 'useState')` and to brief operators on the resolution.

If you build additional domain playbooks, append a short synopsis and link in this section.

---

## 8. Quick Reference Tables

| Need | Audience | Jump To |
| --- | --- | --- |
| Full agent directory | 👤 | [`Agent_Cheat_Sheet.md`](Agent_Cheat_Sheet.md) |
| Prompt architecture patterns | 👤 | [`Context_and_Prompt_Engineering_Guide.md`](Context_and_Prompt_Engineering_Guide.md) |
| Memory schema & field meanings | 🔁 | [`Memory_System_Guide.md`](Memory_System_Guide.md) |
| Handover templates | 🔁 | [`Handover_Guide.md`](Handover_Guide.md) |
| IDE operating checklists | 👤 | [`IDE_and_AI_Assistant_Guide.md`](IDE_and_AI_Assistant_Guide.md) |
| Customization recipes | 👤 | [`Customization_Guide.md`](Customization_Guide.md) |
| Manuscript review timeline | 🔁 | [`Manuscript_Review_Implementation_Plan_Guide.md`](Manuscript_Review_Implementation_Plan_Guide.md) |

---

## Navigation by Operator Goal

| Your Goal | Audience | Primary Guide | Why It Matters |
| --- | --- | --- | --- |
| Understand the 26-agent roster | 👤 | [`Agent_Cheat_Sheet.md`](Agent_Cheat_Sheet.md) | Provides IDs, specialties, and coverage so you know who to delegate to. |
| Master context & prompt design | 👤 | [`Context_and_Prompt_Engineering_Guide.md`](Context_and_Prompt_Engineering_Guide.md) | Explains the layered prompt format, state contracts, and meta-prompt patterns that keep agents interoperable. |
| Customize the framework | 👤 | [`Customization_Guide.md`](Customization_Guide.md) | Walks through domain extensions, MCP integrations, and release management practices. |
| Sync IDEs & assistants | 👤 | [`IDE_and_AI_Assistant_Guide.md`](IDE_and_AI_Assistant_Guide.md) | Offers environment-specific checklists for Cursor, Kiro, VS Code, and Gemini. |
| Maintain shared state | 🔁 | [`Memory_System_Guide.md`](Memory_System_Guide.md) | Defines the `system_state.*` schema, memory log format, and update rituals. |
| Perform context handovers | 🔁 | [`Handover_Guide.md`](Handover_Guide.md) | Details when and how to compose `handover.md` files to keep multi-session work aligned. |
| Execute manuscript reviews end-to-end | 🔁 | [`Manuscript_Review_Implementation_Plan_Guide.md`](Manuscript_Review_Implementation_Plan_Guide.md) | Provides a phased implementation plan, quality gates, and reporting templates tailored for academic manuscripts. |

---

## Suggested Reading Paths

- **Quick Start**: `01-START_HERE.md` (👤) → `Agent_Cheat_Sheet.md` (👤) → `Memory_System_Guide.md` (🔁)
- **Deep Architecture Study**: `01-START_HERE.md` (👤) → `Context_and_Prompt_Engineering_Guide.md` (👤) → `Customization_Guide.md` (👤)
- **Customization Sprint**: `Customization_Guide.md` (👤) → `Context_and_Prompt_Engineering_Guide.md` (👤, reference) → `Memory_System_Guide.md` (🔁)
- **Tooling Setup**: `IDE_and_AI_Assistant_Guide.md` (👤) → `Handover_Guide.md` (🔁)

---

## Relationships Between Guides

```
README.md (this file)
    ↓ (summarizes and links to)
Context_and_Prompt_Engineering_Guide.md
    ↓ (informs)
Customization_Guide.md
    ↓ (extends into domain-specific plans such as)
Manuscript_Review_Implementation_Plan_Guide.md
    ↓ (feeds deliverables captured by)
Memory_System_Guide.md + Handover_Guide.md
```

---

## Cross-Directory Touchpoints

- **Onboarding prompts** live in `../01-START_HERE.md` and the `../03-` and `../04-` directories. Use the tables above to jump between them.
- **Implementation prompts** in `../05-implementation-agents/` pair with the quality and handover practices described here.
- **Automation** via `../02-setup_review.py` complements the manual rituals outlined across these guides.

---

**All guides are designed to be read independently, but this README provides the consolidated navigation. Keep references and file paths current as the system evolves.**
