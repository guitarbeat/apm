# Manuscript Review Implementation Plan Guide

## Overview

This guide defines the Implementation Plan structure for academic manuscript reviews within the Rigorous APM framework. It provides specifications for creating detailed, structured Implementation Plans that enable systematic coordination of 26 specialized Implementation Agents through comprehensive manuscript analysis workflows.

## Quick Reference

### Glossary of Terms
- **APM:** Agentic Project Management. A framework for using AI agents to manage and execute complex projects.
- **Implementation Plan:** A detailed, structured document that outlines the entire manuscript review process, including phases, tasks, and agent assignments.
- **Setup Agent:** The initial agent responsible for gathering manuscript details and creating the Implementation Plan.
- **Manager Agent:** The agent responsible for executing the Implementation Plan, coordinating the Implementation Agents, and managing the review process.
- **Implementation Agent:** A specialized agent that performs a specific analysis task (e.g., Section, Rigor, or Writing analysis).
- **Memory System:** The system state file (`system_state.json` by default, `system_state.md` when Markdown output is selected) and the `agent_outputs/` directory.

### Workflow Diagram
```mermaid
graph TD
    A[Start] --> B{Setup Agent};
    B --> C[Implementation Plan];
    C --> D{Manager Agent};
    D --> E[Phase 1: Section Agents (S1-S10)];
    E --> F{Manager Agent};
    F --> G[Phase 2: Rigor Agents (R1-R7)];
    F --> H[Phase 3: Writing Agents (W1-W7)];
    G --> I{Manager Agent};
    H --> I;
    I --> J[Phase 4: Quality Control Agent (QC)];
    J --> K{Manager Agent};
    K --> L[Phase 5: Executive Summary Agent (ES)];
    L --> M[End];
```

## Generating the Plan

- Run `python 02-setup_review.py --plan-detail-level descriptive` to populate the default checklist with each agent's specialization (sourced from `06-guides/Agent_Cheat_Sheet.md`).
- Use the `concise` default when you only need agent IDs and titles for rapid plan drafting.

## Extending the Framework

This framework is designed to be extensible. You can add new, custom Implementation Agents to perform specialized analysis tasks. To add a new agent:

1.  **Create a New Agent Prompt:** Create a new `.md` file in the appropriate `05-agents` sub-directory (or create a new sub-directory). This prompt should follow the same structure as the other refactored agent prompts, referencing the `base_prompt.md` for common sections.
2.  **Define the Specialization:** Clearly define the `Agent Specialization`, `Task Execution Protocol`, and `Output Format` for your new agent.
3.  **Update the Implementation Plan:** The `Setup Agent` can be instructed to include your new agent in the `Implementation Plan`. This may involve creating a new phase or adding the agent to an existing one.
4.  **Update the Manager Agent:** The `Manager Agent` will automatically coordinate the new agent as long as it is included in the `Implementation Plan`.

## Document Structure Specifications

### Document Header (Lines 1-15)
```markdown
# [Manuscript Title] – Implementation Plan 

**Memory Strategy:** [Determined during Memory Root Creation phase]
**Last Modification:** [Summary of last modification by Manager Agent]
**Manuscript Overview:** [High-level manuscript overview with context and objectives]
**Target Outlet:** [Publication outlet and requirements]
**Review Scope:** [Full/Targeted/Custom review configuration]
```

Keep this header < 15 lines so diff tools can catch version bumps cheaply.

### Phase Sections
- Use level 2 headings (`##`) for phases: `## Phase <n>: <Name>`
- Each phase groups related analysis tasks as determined during project decomposition
- For targeted reviews, omit unnecessary phases and list tasks directly under the header

### Task Blocks
- Use a level 3 heading (`###`) for each task, assigned to one Implementation Agent:  
    `### Task <n.m> – <Title> │ <category>_<id>`
- Each task is a focused, actionable unit of analysis for an Implementation Agent with one clear objective that delivers independent value
- Directly under the heading, add an unordered list with these meta-fields:
    - **Objective:** One-sentence task goal with comprehensive context
    - **Output:** Concrete deliverable with detailed specifications (e.g., structured analysis report, quality scores, recommendations)
    - **Guidance:** Key constraints, requirements, and analysis approach with detailed context

### Sub-Task Formatting
Sub-tasks break down a parent task into logical steps and must be included for every task:

**Single-step format [unordered list (`-`)]:**
```markdown
- Detailed analysis component 1 with comprehensive specifications
- Detailed analysis component 2 with comprehensive specifications
- (...)
```

**Multi-step format [ordered list (`1.`, `2.`, ...)]:**
```markdown
1. **Step Name:** Detailed step description with clear action and comprehensive context.
2. **Step Name:** Detailed step description with clear action and comprehensive context.
(...)
```

### Task Dependency Declaration Format
*  **Producer Task:** Specify concrete deliverables in the `Output` field for consumer task integration
*  **Consumer Task:** Reference dependency in `Guidance` field using format: 
    - Same-agent: `"Depends on: Task X.Y Output"`
    - Cross-agent: `"Depends on: Task X.Y Output by Agent Z"`

### Phase Summary Format (Manager Agent)
At phase completion, append summaries to Implementation Plan under current phase and before next phase:

```markdown
## Phase <n>: <Name> Summary
> Delivered: Tasks <n.m>, <n.k>
> Outstanding: Tasks <n.x>, ...
> Blockers: ...
> Common Issues/Patterns: ...
> Quality Notes: ...
```

## Manuscript Review Implementation Plan Structure

### Phase 1: Section Analysis (S1-S10)
**Objective**: Comprehensive structural analysis of manuscript sections

**Tasks:**
- Task 1.1: Title & Keywords Analysis │ section_s1
- Task 1.2: Abstract Analysis │ section_s2
- Task 1.3: Introduction Analysis │ section_s3
- Task 1.4: Literature Review Analysis │ section_s4
- Task 1.5: Methodology Analysis │ section_s5
- Task 1.6: Results Analysis │ section_s6
- Task 1.7: Discussion Analysis │ section_s7
- Task 1.8: Conclusion Analysis │ section_s8
- Task 1.9: References Analysis │ section_s9
- Task 1.10: Supplementary Materials Analysis │ section_s10

**Dependencies**: All section agents can run in parallel

### Phase 2: Rigor Analysis (R1-R7)
**Objective**: Scientific rigor and methodology evaluation

**Tasks:**
- Task 2.1: Originality & Contribution Assessment │ rigor_r1
  - **Objective:** Evaluate research novelty, contribution clarity, and significance
  - **Output:** Structured markdown analysis with originality scores, contribution assessment, and significance recommendations
  - **Guidance:** Assess novelty level, contribution clarity, field advancement, and competitive positioning

- Task 2.2: Impact & Significance Evaluation │ rigor_r2
  - **Objective:** Assess potential impact, importance, and broader implications
  - **Output:** Structured markdown analysis with impact scores, significance assessment, and implication recommendations
  - **Guidance:** Evaluate impact potential, significance, broader implications, and field advancement

- Task 2.3: Ethics & Compliance Review │ rigor_r3
  - **Objective:** Review ethical considerations, IRB approval, and consent
  - **Output:** Structured markdown analysis with ethics scores, compliance assessment, and ethical recommendations
  - **Guidance:** Check ethical protocols, compliance documentation, consent procedures, and field standards

- Task 2.4: Data & Code Availability Assessment │ rigor_r4
  - **Objective:** Evaluate data sharing, code availability, and reproducibility
  - **Output:** Structured markdown analysis with availability scores, sharing assessment, and reproducibility recommendations
  - **Guidance:** Assess data sharing practices, code availability, documentation quality, and open science standards

- Task 2.5: Statistical Rigor Analysis │ rigor_r5
  - **Objective:** Assess statistical methods, power analysis, and effect sizes
  - **Output:** Structured markdown analysis with statistical scores, methodology assessment, and rigor recommendations
  - **Guidance:** Evaluate statistical appropriateness, power analysis, effect sizes, and field standards

- Task 2.6: Technical Accuracy Review │ rigor_r6
  - **Objective:** Review technical correctness, methodology soundness
  - **Output:** Structured markdown analysis with technical scores, accuracy assessment, and methodology recommendations
  - **Guidance:** Check technical details, methodology soundness, accuracy verification, and field standards

- Task 2.7: Consistency Check │ rigor_r7
  - **Objective:** Check internal consistency, coherence, and logical flow
  - **Output:** Structured markdown analysis with consistency scores, coherence assessment, and flow recommendations
  - **Guidance:** Evaluate internal consistency, logical flow, terminology consistency, and cross-referencing

**Dependencies**: All rigor agents can run in parallel after Phase 1 completion

### Phase 3: Writing Analysis (W1-W7)
**Objective**: Writing quality and style assessment

**Tasks:**
- Task 3.1: Language & Style Analysis │ writing_w1
  - **Objective:** Evaluate academic writing style, language clarity, and presentation quality
  - **Output:** Structured markdown analysis with language scores, style assessment, and presentation recommendations
  - **Guidance:** Assess academic tone, language clarity, grammar quality, and field conventions

- Task 3.2: Narrative Structure Assessment │ writing_w2
  - **Objective:** Assess overall narrative flow, logical progression, and story arc
  - **Output:** Structured markdown analysis with structure scores, flow assessment, and narrative recommendations
  - **Guidance:** Evaluate narrative flow, logical progression, section transitions, and story coherence

- Task 3.3: Clarity & Conciseness Review │ writing_w3
  - **Objective:** Review clarity, brevity, and unnecessary complexity
  - **Output:** Structured markdown analysis with clarity scores, conciseness assessment, and accessibility recommendations
  - **Guidance:** Check language clarity, conciseness, complexity level, and reader accessibility

- Task 3.4: Terminology Consistency Check │ writing_w4
  - **Objective:** Check terminology usage, definition consistency, and field standards
  - **Output:** Structured markdown analysis with terminology scores, consistency assessment, and definition recommendations
  - **Guidance:** Evaluate terminology usage, definition consistency, field standards, and technical accuracy

- Task 3.5: Inclusive Language Assessment │ writing_w5
  - **Objective:** Evaluate inclusive language, bias awareness, and accessibility
  - **Output:** Structured markdown analysis with inclusivity scores, bias assessment, and accessibility recommendations
  - **Guidance:** Check inclusive language practices, bias awareness, accessibility, and modern standards

- Task 3.6: Citation Formatting Review │ writing_w6
  - **Objective:** Review citation style, format consistency, and accuracy
  - **Output:** Structured markdown analysis with citation scores, format assessment, and style recommendations
  - **Guidance:** Check citation style compliance, format consistency, accuracy, and outlet requirements

- Task 3.7: Target Audience Alignment │ writing_w7
  - **Objective:** Assess audience appropriateness, accessibility, and field expectations
  - **Output:** Structured markdown analysis with audience scores, appropriateness assessment, and accessibility recommendations
  - **Guidance:** Evaluate audience appropriateness, technical level, accessibility, and field expectations

**Dependencies**: All writing agents can run in parallel after Phase 1 completion

### Phase 4: Quality Control Synthesis
**Objective**: Synthesize all agent findings and resolve conflicts

**Tasks:**
- Task 4.1: Quality Control Synthesis │ qc
  - **Objective:** Synthesize findings from all 24 base agents and create consolidated analysis
  - **Output:** Comprehensive synthesis report with pattern analysis, conflict resolution, and prioritized recommendations
  - **Guidance:** Depends on: Phases 1, 2, 3 completion; synthesize all findings, resolve conflicts, prioritize issues
  - **Dependencies**: Phases 1, 2, 3 completion

### Phase 5: Executive Summary
**Objective**: Generate comprehensive final report

**Tasks:**
- Task 5.1: Executive Summary Generation │ es
  - **Objective:** Create final comprehensive report synthesizing all review findings
  - **Output:** Executive summary report with quality assessment, improvement roadmap, and publication readiness evaluation
  - **Guidance:** Depends on: Phase 4 completion; synthesize QC findings, create executive insights, provide actionable recommendations
  - **Dependencies**: Phase 4 completion

## Setup Agent Responsibilities

Transform manuscript review requirements into detailed Implementation Plan:

### Enhancement Process
**Content Preservation Requirements:**
- Maintain all analysis objectives, execution patterns, and agent assignments from review requirements
- Preserve all dependencies and phase structure exactly as determined
- Keep task boundaries and scope identical to review requirements

**Detail Enhancement Requirements:**
- Transform basic analysis descriptions into comprehensive specifications
- Add detailed context to task objectives, outputs, and guidance
- Enhance sub-task descriptions with comprehensive instructions and technical context
- Provide detailed specifications that enable Manager Agent to create precise Task Assignment Prompts

### Phase-by-Phase Enhancement Approach
**Sequential Phase Enhancement:**
- Enhance the Implementation Plan one phase section at a time, proceeding sequentially through the file
- Each phase enhancement represents one edit operation to the Implementation Plan file
- Complete enhancement of current phase before proceeding to next phase

**Enhancement Execution:**
- **Phase Analysis**: For each phase, read the corresponding section in the review requirements to fully understand its structure, tasks, and dependencies
- **Phase Enhancement**: Apply the document structure specifications to reformat and enrich the current phase, ensuring all tasks are transformed into detailed task blocks with enhanced meta-fields
- **Content Enhancement**: Enhance each task's contents following guidance, ensuring that the content of the review requirements is retained, only with more detailed context
- **Phase Completion**: Complete the enhancement of the current phase before moving on to the next, ensuring no phase is skipped or partially enhanced
- **File Update**: Update Implementation Plan file with enhanced phase content
- **Progression Gate**: Continue this process until all phases in the Implementation Plan have been fully enhanced

## Manager Agent Responsibilities

Maintain detailed Implementation Plan throughout review session:

### Plan Validation & Improvement
**Initial Plan Assessment:**
- Read guide, evaluate plan structure and detail level
- Assess plan integrity and request more detail from Setup Agent if needed

**Validation Focus:**
- Confirm detailed specifications support precise Task Assignment Prompt creation
- Verify task meta-fields provide sufficient context for Implementation Agent coordination
- Ensure enhanced guidance enables effective task execution management

### Live Plan Maintenance
**Plan Updates:**
- Sync plan with review changes while maintaining detailed specification level
- Add/remove/modify phases and tasks as needed with comprehensive context
- Update "Last Modification" for all changes
- Keep task numbering and dependencies consistent

**Structure Maintenance:**
- Maintain enhanced meta-field structure during plan updates
- Preserve detailed specifications when modifying task content
- Update task details as review progresses and requirements evolve

### Execution Coordination
**Task Assignment Creation:**
- Use detailed meta-fields to create comprehensive Task Assignment Prompts
- Extract enhanced producer task outputs for consumer task assignment integration
- Reference detailed guidance for Implementation Agent context and constraints
- Leverage enhanced specifications for precise task instruction development

**Cross-Agent Coordination:**
- Manage cross-agent handoffs using detailed dependency specifications
- Use enhanced output specifications for seamless task integration
- Reference comprehensive guidance for effective agent coordination

### Phase Management
**Phase Execution:**
- Track phase completion using detailed task specifications
- Manage phase transitions with comprehensive context understanding
- Use enhanced plan structure for effective phase coordination

**Documentation:**
- Write detailed phase summaries in Memory Root using enhanced task context
- Add concise phase summaries to plan before next phase following Memory System Guide
- Maintain comprehensive review documentation through enhanced plan structure

## Important Notes

1. **Comprehensive Planning**: Create Implementation Plans with sufficient detail for Manager coordination
2. **Agent Specialization**: Each task assigned to appropriate specialized Implementation Agent
3. **Dependency Management**: Clear dependencies between phases and tasks
4. **Quality Focus**: Maintain focus on publication readiness and improvement priorities
5. **Memory Integration**: Initialize memory system to track review progress and findings
6. **Manager Readiness**: Ensure Manager Agent has all necessary context for effective coordination
