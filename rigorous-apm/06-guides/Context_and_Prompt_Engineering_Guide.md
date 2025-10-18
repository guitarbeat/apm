# Context and Prompt Engineering Guide

This guide explains the advanced context and prompt engineering techniques that power APM's sophisticated agent coordination. Understanding these principles helps you customize APM for your specific needs and troubleshoot workflow issues.

## Overview

APM's reliability comes from two synergistic approaches:

1. **Context Engineering**: Constructing clear operational boundaries and responsibilities for each agent
2. **Prompt Engineering**: Optimizing how information is structured and delivered to LLMs

Together, these techniques create efficient, scalable AI workflows without relying on personality-based role definitions.

---

## Context Engineering: Defining Agent Operational Reality

### Core Principle: Operational Boundaries Over Personality

APM doesn't define agents by personality traits ("you are a helpful assistant"). Instead, it establishes **clear operational boundaries** that enable emergent specialization through focused context scope.

### Agent Operational Contexts

Each agent type operates within distinct boundaries:

**Setup Agents**
- **Scope**: Project discovery and planning
- **Boundaries**: Systematic progression through planning gates, no execution work
- **Output**: Implementation Plan with task specifications

**Manager Agents**
- **Scope**: Coordination and task assignment
- **Boundaries**: Decision-making and review protocols, no implementation tasks
- **Output**: Task Assignment Prompts and progress tracking

**Implementation Agents**
- **Scope**: Domain-specific execution
- **Boundaries**: Assigned work within expertise area, no project-level decisions
- **Output**: Completed tasks and Memory Log entries

This architecture ensures comprehensive project coverage while preventing scope creep. The entire project context is distributed across multiple agent instances, effectively offloading workload from a single LLM and enabling focused, specialized interactions.

### Mandatory Progression Sequences

APM establishes **fixed workflow sequences** that prevent fragmentation while maintaining flexibility within defined boundaries.

**Setup Phase Progression Gates**

Each phase must complete before proceeding:

```
Asset Verification 
  ↓
Context Synthesis 
  ↓
Project Breakdown 
  ↓
AI-driven Plan Review (Optional)
  ↓
Enhancement 
  ↓
Bootstrap Prompt Creation
```

This prevents incomplete planning from cascading into execution problems.

**Task Loop Phase Cycles**

The Manager Agent follows structured cycles:

```
Task Assignment 
  ↓
Execution 
  ↓
Logging 
  ↓
Review 
  ↓
Next Action Decision
```

Each step builds upon the previous while maintaining clear handoff points between Manager and Implementation Agents.

### Dynamic Domain Identification

Rather than predefined roles, APM enables **project-specific agent specialization** through the Setup Agent's systematic Project Breakdown process.

**Domain Identification Factors**

The Setup Agent considers three main factors when creating the Implementation Agent team:

1. **Separation of skill areas**: Different agents for specialized knowledge domains
2. **Technical environment boundaries**: Domain-specific agents for different technology stacks
3. **Workflow patterns**: Distinguishing between different task orientations

**Example Domain Assignments**

For a web application project:
- `Agent_Backend_API`: REST endpoint development
- `Agent_Backend_Database`: Schema design and queries
- `Agent_Frontend_Components`: UI component library
- `Agent_Frontend_Integration`: API integration and state management
- `Agent_DevOps`: Deployment and infrastructure

**Agent Workload Balancing**

When domain analysis reveals agents with excessive task assignments (typically 8+ tasks), the Setup Agent implements subdomain splitting:

- Analyze for logical sub-domain boundaries
- Consider natural task groupings
- Evaluate process specialization needs
- Create focused sub-agents with curated contexts

This ensures each agent receives contexts specifically suited to their assigned domain, enabling natural LLM expertise activation without token overhead from irrelevant cross-domain information.

---

## Prompt Engineering: Optimizing LLM Interaction

### Structured Markdown for Enhanced Parsing

APM uses **structured Markdown formatting** as the default communication protocol because it provides superior LLM parsing capabilities compared to plain text.

**Key Parsing Benefits**

- **Token Retention**: Structural elements help LLMs organize and retain key information over long conversations
- **Cross-Model Compatibility**: Universal formatting conventions ensure reliable parsing across different LLM architectures
- **Reduced Ambiguity**: Clear information hierarchy minimizes misinterpretation of complex instructions

**Effective Markdown Patterns**

```markdown
## Primary Section Headers
Clear hierarchical organization

### Subsection Headers
Logical information grouping

**Bold for emphasis**: Critical terms and concepts
*Italics for context*: Supporting details

- Bulleted lists for related items
- Easy scanning and comprehension

1. Numbered lists for sequences
2. Step-by-step procedures
3. Ordered dependencies
```

### YAML Frontmatter Integration

APM uses **lightweight YAML frontmatter** at the top of important documents to deliver structured metadata, enabling agents to instantly recognize an asset's key attributes.

**Dual-Layer Parsing Architecture**

- **YAML Layer**: Structured metadata provides context scaffolding and quick filtering
- **Markdown Layer**: Detailed information delivery with hierarchical organization

**Example: Task Assignment Prompt**

```yaml
---
task_id: "T-003"
agent: "Agent_Backend_API"
dependencies: ["T-001", "T-002"]
status: "ready"
priority: "high"
---

# Task: Implement User Authentication Endpoint

## Context
[Detailed task description in Markdown]
```

This combination creates enhanced parsing precision where structured metadata provides context scaffolding while Markdown content delivers detailed information, reducing parsing errors across different LLM capabilities.

---

## APM Prompt Asset Architecture

### User-Provided Assets

**Pre-written initialization prompts** provide complete, ready-to-use prompts that users can immediately copy and paste into their AI IDE platforms.

**Initiation Prompt Components**

- **Setup Agents**: Five-step workflow sequence, progression gate requirements, asset verification protocols
- **Manager Agents**: Coordination responsibilities, task loop protocols, handover procedures
- **Implementation Agents**: Execution patterns, error handling protocols, delegation protocols, logging requirements

Each agent type receives a comprehensive initiation prompt that establishes operational context without requiring additional setup.

### Autonomous Access Assets

A key feature of APM's prompt engineering is **prompts and guides that agents access autonomously** via their AI IDE's file operation and search capabilities.

**Autonomous Guide Access Patterns**

- **Setup Agents**: Context Synthesis Prompt and Project Breakdown, Review & Enhancement Guides during systematic planning phases
- **Manager Agents**: Memory System & Log Guides for memory management, Task Assignment Guides when creating coordination prompts
- **Implementation Agents**: Memory Log Guides for proper documentation protocols

This approach enables agents to independently retrieve detailed protocols as needed during initialization, supporting scalable and efficient multi-agent coordination without manual intervention.

### Meta-Prompts (Agent-Generated Dynamic Assets)

APM's most advanced prompt engineering features **meta-prompts that agents create dynamically** during workflow execution. These prompts are not pre-written but are generated by agents following structured formats defined in the guide system.

**Meta-Prompt Generation by Agent Type**

**Manager Agents**: Generate Task Assignment Prompts

- Combine Implementation Plan task specifications with dependency context
- Add success criteria and execution instructions
- Present as **Markdown code blocks in chat for easy copy-paste workflows**

**Implementation Agents**: Generate Memory Log entries

- Use standardized log formats with task-specific execution details
- Include outcomes, issues encountered, and solutions implemented
- Present as **file appendixes in Memory Log files**

The formats are standardized for parsing efficiency, but the content varies based on Implementation Plan specifications, dependency relationships, and execution outcomes.

---

## JSON Asset Format: Testing Preview

### Experimental Schema Design

APM v0.4 includes an **experimental JSON asset format variant** as a testing preview for contributor feedback and advanced research scenarios. This format represents ongoing exploration into more structured prompt engineering approaches.

**Design Rationale for JSON Assets**

1. **Automated Schema Validation**: Enforce strict schema validation to catch agent hallucinations or malformed outputs
2. **Parsing Consistency**: JSON's rigid structure may enable more consistent parsing by LLMs
3. **Objective Project Metrics**: Facilitate automated extraction of project metrics for precise measurement
4. **Programmatic Integration**: Enable easier integration with enterprise tools and automated pipelines

### Critical Performance Impact

Initial testing shows that the JSON format introduces **substantial token overhead**, making it impractical for most production scenarios.

**Token Overhead Analysis**

- **Minimum overhead**: 15-20% increase for simple asset structures
- **Average overhead**: 2x-3x token usage for complex APM JSON assets
- **Maximum overhead**: Up to 5x compared to equivalent Markdown representations

**Implementation Challenges**

- **Token Economy**: JSON syntax overhead creates unsustainable cost increases. Repetitive elements (brackets, colons, quotation marks) are re-read in every cache access without providing additional value
- **Context Saturation**: Faster context window consumption forces more frequent handover procedures, each adding its own token overhead
- **User Experience**: Reduced readability makes project review and modification more difficult

### Contributor Testing and Feedback

The JSON format variant is provided primarily for **contributor testing and feedback** rather than production deployment.

**Testing Recommendations**

- Use free trial credits or free-tier models for experimentation
- Expect experimental behavior and potential breaking changes
- Monitor token consumption carefully during testing
- Provide feedback on parsing consistency vs. token overhead tradeoffs

Based on testing and contributor feedback, the JSON format may undergo significant design changes, be refined for specific use cases, or potentially be deprecated if testing reveals insurmountable practical limitations.

---

## Practical Application in Rigorous APM

### Manuscript Review Context Engineering

The Rigorous APM instance applies these principles to academic manuscript review:

**26 Specialized Implementation Agents**

- **Section Agents (S1-S10)**: Analyze manuscript structure and content
- **Rigor Agents (R1-R7)**: Assess scientific validity and methodology
- **Writing Agents (W1-W7)**: Evaluate writing quality and presentation
- **Synthesis Agents (QC, ES)**: Consolidate findings into final report

Each agent receives context specifically curated for their domain, enabling natural expertise activation without cross-domain token overhead.

### Prompt Engineering in Practice

**Standardized Output Formats**

All Implementation Agents follow a consistent Markdown schema:

```markdown
# [Agent Name] Analysis

## 1. Overall Assessment
- **Score:** [1-5 scale]
- **Confidence:** [1-5 scale]
- **Summary:** [Brief one-sentence summary]

## 2. Key Findings
[Bulleted list of important findings]

## 3. Recommendations
[Bulleted list of actionable recommendations]

## 4. Critical Issues
[Bulleted list of critical issues]

## 5. Detailed Scores
[Metric-specific scores]
```

This standardization enables:
- Consistent parsing by the Manager Agent
- Easy aggregation by synthesis agents
- Clear presentation for human reviewers

**Memory System Integration**

The system state file (`system_state.json` by default, `system_state.md` when Markdown output is selected) is designed for quick assessment without wading through every agent deliverable. Choose the format that best fits your tooling:

- **JSON format** – Structured for downstream automations and scriptable tooling:

    ```json
    {
      "manuscript_context": {
        "title": "String",
        "target_outlet": "String",
        "current_stage": "String"
      },
      "review_progress": {
        "current_phase": "String",
        "completed_agents": ["Agent IDs"],
        "pending_agents": ["Agent IDs"]
      }
    }
    ```

- **Markdown format** – Human-friendly headings and bullet lists for quick scanning in plain-text editors:

    ```markdown
    # System State

    ## Manuscript Context
    - **Title:** ...
    - **Target outlet:** ...
    - **Current stage:** ...

    ## Review Progress
    - **Current phase:** ...
    - **Completed agents:**
      - ...
    - **Pending agents:**
      - ...
    ```

Both representations give the Manager Agent instant context without reading detailed agent outputs.

When bootstrapping a workspace with `02-setup_review.py`, choose the format upfront using `--system-state-format markdown` or the default JSON by omitting the flag.

---

## Best Practices for Understanding and Application

### When Context Engineering Matters

**Understanding agent boundaries helps when:**
- Diagnosing coordination issues between agents
- Planning new agent specializations
- Optimizing workflow efficiency
- Troubleshooting scope creep problems

**Progression sequences are critical for:**
- Ensuring complete project planning
- Preventing incomplete handoffs
- Maintaining workflow consistency
- Debugging execution problems

### When Prompt Engineering Matters

**Markdown structure affects:**
- Agent parsing accuracy and consistency
- Information retention across long conversations
- Cross-model compatibility
- Token efficiency and context window usage

**YAML frontmatter is valuable for:**
- Quick state assessment and filtering
- Automated workflow coordination
- Dependency tracking and management
- Machine-readable metadata extraction

**Meta-prompt quality impacts:**
- Task assignment clarity and completeness
- Memory log usefulness and searchability
- Coordination efficiency between agents
- Project documentation quality

### Avoiding Common Pitfalls

**Don't:**
- Add personality traits to agent prompts (reduces operational clarity)
- Skip progression gates to save time (causes downstream errors)
- Mix JSON and Markdown formats without clear rationale (increases confusion)
- Create agents with overlapping operational boundaries (causes coordination issues)

**Do:**
- Maintain clear operational boundaries for each agent type
- Use structured Markdown consistently across all assets
- Understand the principles before customizing
- Monitor token consumption when modifying prompt formats

### Customization Guidance

For detailed information on customizing APM for your specific needs, including:
- Modifying core prompts for domain-specific workflows
- Creating custom delegation guides
- Integrating MCP tools for enhanced capabilities
- Domain-specific customization examples

See the **Customization Guide** in this directory.

---

## Summary

APM's context and prompt engineering techniques work synergistically to create reliable, efficient AI workflows:

- **Context Engineering** establishes clear operational boundaries and mandatory progression sequences
- **Prompt Engineering** optimizes information structure through Markdown formatting and YAML frontmatter
- **Dynamic Specialization** emerges from project-specific domain identification
- **Meta-Prompts** enable agents to generate coordination assets autonomously

The Rigorous APM instance demonstrates these principles in action with 26 specialized agents coordinating complex manuscript reviews through structured workflows and standardized output formats.

For production use, stick with Markdown-based assets. The JSON format remains experimental and should only be used for testing and research purposes.
