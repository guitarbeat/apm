# Agent Handover Guide

This guide outlines the process for handing over a manuscript review project from one agent session to another, ensuring that all essential context is preserved.

## 1. Core Principle: Context Preservation

The primary goal of a handover is to transfer the complete state of the review project so that the new agent session can resume the work seamlessly. This includes:

-   **Manuscript Details:** Title, type, target outlet, etc.
-   **Review Configuration:** Scope, priorities, and timeline.
-   **Implementation Plan:** The current version of the plan, including its status (e.g., `in_progress`, `completed`).
-   **Memory System:** The `system_state.json` file and the `agent_outputs/` directory.

## 2. Handover Scenarios

The handover process can occur at different stages of the review:

-   **Setup Handover:** Transferring an in-progress project setup to a new `Setup Agent` session.
-   **Manager Handover:** Transferring an in-progress review execution to a new `Manager Agent` session. This is the most common scenario.
-   **Revision Cycle:** Initiating a new review cycle on a revised manuscript, which requires the context of the previous review.

## 3. Handover Prompt Template

To initiate a handover, use the following template, filling in all relevant details from the current state of the project.

```markdown
# Agent Handover

## 1. Handover Type
- **Type:** [Setup Handover / Manager Handover / Revision Cycle]

## 2. Manuscript Context
- **Title:** [Manuscript title]
- **Type:** [empirical/theoretical/review]
- **Target Outlet:** [Publication outlet]
- **Current Stage:** [draft/revision/pre-submission]

## 3. Review Status
- **Implementation Plan Status:** [e.g., Phase 2 in progress]
- **Completed Agents:** [List of completed agent IDs]
- **Pending Agents:** [List of pending agent IDs]
- **Key Findings Summary:** [A brief summary of the key findings so far]
- **Critical Issues Summary:** [A brief summary of the critical issues identified so far]

## 4. Memory System
- **Location:** [Path to the memory directory]
- **Status:** [e.g., Fully populated for completed agents]

## 5. Immediate Tasks
- [The immediate next step for the new agent session to take]
- [e.g., "Continue with Phase 2 execution by running agents R3, R5, and R7."]
- [e.g., "Generate the Manager Bootstrap Prompt."]
```

## 4. Quality Assurance

Before completing a handover, ensure that:
- All relevant files (`Implementation Plan`, all memory files) are saved and accessible.
- The handover prompt is complete and accurately reflects the current state of the project.
- The "Immediate Tasks" section provides a clear and unambiguous starting point for the new agent session.
