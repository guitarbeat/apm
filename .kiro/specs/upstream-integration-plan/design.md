# Design Document

## Overview

This design document outlines the technical approach for integrating rigorous-apm with upstream-apm v0.5. The integration transforms rigorous-apm from a parallel APM system into a domain-specific extension that leverages upstream's proven patterns while preserving rigorous-apm's manuscript review specialization.

The design follows a "foundation + specialization" architecture where upstream-apm provides core APM patterns and rigorous-apm extends them with manuscript-specific capabilities.

## Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Rigorous-APM System                       │
│                  (Domain Specialization)                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────┐  ┌────────────────┐  ┌──────────────┐ │
│  │  Setup Agent   │  │ Manager Agent  │  │ 26 Impl.     │ │
│  │  (Extended)    │  │  (Extended)    │  │ Agents       │ │
│  │                │  │                │  │ (Extended)   │ │
│  │ • Upstream     │  │ • Upstream     │  │              │ │
│  │   patterns     │  │   patterns     │  │ • Upstream   │ │
│  │ • Manuscript   │  │ • 3-phase      │  │   patterns   │ │
│  │   context      │  │   parallel     │  │ • Manuscript │ │
│  │                │  │   execution    │  │   analysis   │ │
│  └────────────────┘  └────────────────┘  └──────────────┘ │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                    Upstream-APM v0.5                         │
│                   (Foundation Framework)                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              Core APM Patterns                          │ │
│  │                                                          │ │
│  │  • 5-phase Setup workflow                              │ │
│  │  • Bootstrap Prompt pattern                            │ │
│  │  • Task Assignment protocol                            │ │
│  │  • Memory System                                       │ │
│  │  • Handover procedures                                 │ │
│  │  • Guide reference system                              │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              Core Guides                                │ │
│  │                                                          │ │
│  │  • Context_Synthesis_Guide.md                          │ │
│  │  • Implementation_Plan_Guide.md                        │ │
│  │  • Memory_Log_Guide.md                                 │ │
│  │  • Memory_System_Guide.md                              │ │
│  │  • Project_Breakdown_Guide.md                          │ │
│  │  • Task_Assignment_Guide.md                            │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Directory Structure

```
rigorous-apm/
├── 01-START_HERE.md                          # Entry point, explains upstream relationship
├── 02-setup_review.py                        # Python automation (enhanced)
│
├── 03-review-kickoff/                        # Review initialization
│   ├── review_kickoff_prompt.md              # Updated with upstream patterns
│   ├── share_plan_with_setup.apm             # Automation snippet (preserved)
│   └── manager_load_plan.apm                 # Automation snippet (preserved)
│
├── 03-setup-agent/                           # Setup Agent (rewritten)
│   └── setup_agent_initiation_prompt.md      # Adopts upstream 5-phase pattern
│
├── 04-manager-agent/                         # Manager Agent (rewritten)
│   ├── manager_agent_initiation_prompt.md    # Adopts upstream coordination
│   └── manager_bootstrap_prompt.md           # Template for Bootstrap generation
│
├── 05-implementation-agents/                 # 26 Implementation Agents (updated)
│   ├── implementation_agent_base_prompt.md   # NEW: Base template
│   ├── section/                              # S1-S10 (updated)
│   ├── rigor/                                # R1-R7 (updated)
│   ├── writing/                              # W1-W7 (updated)
│   ├── quality_control_agent_prompt.md       # Updated
│   └── executive_summary_agent_prompt.md     # Updated
│
└── 06-guides/                                # Guides (enhanced)
    ├── README.md                             # Navigation for both guide sets
    ├── upstream/                             # NEW: Upstream guides
    │   ├── Context_Synthesis_Guide.md
    │   ├── Implementation_Plan_Guide.md
    │   ├── Memory_Log_Guide.md
    │   ├── Memory_System_Guide.md
    │   ├── Project_Breakdown_Guide.md
    │   ├── Project_Breakdown_Review_Guide.md
    │   └── Task_Assignment_Guide.md
    └── [manuscript-specific guides...]       # Preserved
```

## Components and Interfaces

### 1. Setup Agent

**Purpose**: Initialize manuscript review projects using upstream's 5-phase pattern with manuscript-specific context gathering.

**Upstream Patterns Adopted**:
- 5-phase structure: Context Synthesis → Project Breakdown → Review → Enhancement → Bootstrap
- Guide reference pattern: `{GUIDE_PATH:filename.md}`
- Checkpoint/approval gates between phases
- Bootstrap Prompt generation in YAML format

**Manuscript Specialization**:
- Custom Context Synthesis questions for academic manuscripts
- Integration with `02-setup_review.py` automation
- Manuscript-specific Implementation Plan structure (5 phases: Section→Rigor→Writing→QC→ES)
- Academic review workflow understanding

**Interface**:
```markdown
Input: User provides manuscript details and requirements
Output: Bootstrap Prompt for Manager Agent initialization

Key Methods:
- conduct_context_synthesis() → manuscript context
- create_project_breakdown() → 5-phase manuscript review plan
- enhance_implementation_plan() → detailed APM artifact
- generate_bootstrap_prompt() → Manager initialization prompt
```

**Guide References**:
- `{GUIDE_PATH:upstream/Context_Synthesis_Guide.md}`
- `{GUIDE_PATH:upstream/Project_Breakdown_Guide.md}`
- `{GUIDE_PATH:upstream/Implementation_Plan_Guide.md}`

### 2. Manager Agent

**Purpose**: Coordinate 26 specialized Implementation Agents through 3-phase parallel execution model.

**Upstream Patterns Adopted**:
- Bootstrap Prompt processing with YAML frontmatter
- Task Assignment Prompt creation protocol
- Memory System integration
- Handover procedures

**Manuscript Specialization**:
- 3-phase parallel execution: Section (S1-S10) → Rigor (R1-R7) + Writing (W1-W7) → QC → ES
- 26-agent coordination strategy
- Manuscript review workflow management
- Quality Control synthesis pattern

**Interface**:
```markdown
Input: Bootstrap Prompt (from Setup Agent) or Handover Prompt
Output: Task Assignment Prompts for Implementation Agents

Key Methods:
- process_bootstrap_prompt() → initialize manager context
- create_task_assignment() → generate Implementation Agent prompts
- review_memory_log() → analyze task completion
- coordinate_parallel_execution() → manage 26-agent workflow
- generate_handover_prompt() → context transfer for replacement manager
```

**Guide References**:
- `{GUIDE_PATH:upstream/Implementation_Plan_Guide.md}`
- `{GUIDE_PATH:upstream/Memory_System_Guide.md}`
- `{GUIDE_PATH:upstream/Task_Assignment_Guide.md}`

### 3. Implementation Agents (26 Total)

**Purpose**: Execute specialized manuscript analysis tasks.

**Agent Categories**:
- **Section Agents (S1-S10)**: Analyze specific manuscript sections
- **Rigor Agents (R1-R7)**: Evaluate scientific methodology and standards
- **Writing Agents (W1-W7)**: Assess language, style, and presentation
- **Quality Control Agent (QC)**: Synthesize findings from all 24 agents
- **Executive Summary Agent (ES)**: Generate final comprehensive report

**Upstream Patterns Adopted**:
- YAML frontmatter with metadata (priority, command_name, description, agent_id, domain)
- Execution type patterns (single-step vs multi-step)
- Memory Log Guide references
- Debug delegation protocol
- Handover awareness

**Manuscript Specialization**:
- Domain-specific analysis criteria for each agent
- Academic standards evaluation
- Field-specific requirements
- Manuscript section focus

**Interface**:
```markdown
Input: Task Assignment Prompt from Manager Agent
Output: Task execution results + Memory Log

Key Methods:
- parse_task_assignment() → understand task requirements
- execute_analysis() → perform manuscript-specific evaluation
- create_memory_log() → document findings
- delegate_debugging() → escalate complex issues
```

**YAML Frontmatter Structure**:
```yaml
---
priority: 3
command_name: section-1-title-abstract-analysis
description: Analyzes manuscript title and abstract for clarity, accuracy, and impact
agent_id: S1
domain: manuscript-review
---
```

**Guide References**:
- `{GUIDE_PATH:upstream/Memory_Log_Guide.md}`

### 4. Python Automation (`02-setup_review.py`)

**Purpose**: Automate manuscript review workspace initialization with upstream-compatible artifacts.

**Current Capabilities** (Preserved):
- CLI-based workspace creation
- Manuscript asset copying
- System state generation
- Audience legend integration

**New Capabilities** (Added):
- Generate `metadata.json` with APM version tracking
- Create upstream-compatible `Implementation_Plan.md`
- Generate Bootstrap Prompts in upstream format
- Reference upstream guides in generated artifacts

**Interface**:
```python
# Command-line interface
python 02-setup_review.py --manuscript <name> --type <empirical|theoretical|review> --outlet <journal>

# Generated artifacts
.apm/
├── metadata.json                    # NEW: APM version and phase tracking
├── Implementation_Plan.md           # ENHANCED: Upstream format
├── Bootstrap_Prompt.md              # ENHANCED: Upstream format
└── Memory_Logs/                     # Existing structure
```

**Metadata JSON Structure**:
```json
{
  "apm_version": "upstream-v0.5.0+rigorous-v1.0.0",
  "domain": "manuscript-review",
  "manuscript": {
    "name": "example_manuscript",
    "type": "empirical",
    "target_outlet": "Nature",
    "field": "neuroscience"
  },
  "review_started": "2025-11-17",
  "phases": {
    "section_analysis": "pending",
    "rigor_analysis": "pending",
    "writing_analysis": "pending",
    "quality_control": "pending",
    "executive_summary": "pending"
  }
}
```

### 5. Guide System

**Purpose**: Provide comprehensive documentation for both upstream patterns and manuscript-specific procedures.

**Structure**:
```
06-guides/
├── README.md                                 # Navigation hub
├── upstream/                                 # Upstream guides (copied)
│   ├── Context_Synthesis_Guide.md
│   ├── Implementation_Plan_Guide.md
│   ├── Memory_Log_Guide.md
│   ├── Memory_System_Guide.md
│   ├── Project_Breakdown_Guide.md
│   ├── Project_Breakdown_Review_Guide.md
│   └── Task_Assignment_Guide.md
└── [manuscript-specific guides]              # Domain guides (preserved)
    ├── Agent_Cheat_Sheet.md
    ├── Manuscript_Review_Implementation_Plan_Guide.md
    ├── Context_and_Prompt_Engineering_Guide.md
    └── [other guides...]
```

**Guide Reference Resolution**:
- Agents use `{GUIDE_PATH:filename.md}` syntax
- System resolves to either `06-guides/upstream/` or `06-guides/` based on filename
- Relative paths maintained for portability

## Data Models

### Bootstrap Prompt

```yaml
---
workspace_root: "./review_workspace"
manuscript_name: "example_manuscript"
manuscript_type: "empirical"
target_outlet: "Nature"
research_field: "neuroscience"
review_priorities: ["methodology", "statistical_analysis", "clarity"]
---

# Manager Agent Bootstrap Prompt

## Project Context
[Manuscript details and review objectives]

## Implementation Plan Overview
[5-phase manuscript review workflow]

## Agent Coordination Strategy
[26-agent parallel execution model]

## Memory System Initialization
[Memory Log structure and organization]

## Next Actions
[Immediate tasks for Manager Agent]
```

### Task Assignment Prompt

```yaml
---
execution_type: "multi-step"
dependencies: ["S1", "S2"]
agent_id: "R1"
task_id: "2.1"
---

# Task Assignment: Methodology Rigor Analysis

## Task Reference
[From Implementation Plan: Phase 2, Task 2.1]

## Context from Dependencies
[Findings from S1 and S2 section analyses]

## Detailed Instructions
[Step-by-step execution guidance]

## Expected Outputs
[Deliverables and success criteria]

## Memory Logging
Path: `.apm/Memory_Logs/R1_Methodology_Analysis.md`
[Logging instructions]
```

### Memory Log

```markdown
# Memory Log: [Agent ID] - [Task Name]

## Status
- **Completion**: [Complete/Blocked/In Progress]
- **Date**: [YYYY-MM-DD]

## Task Summary
[Brief description of task executed]

## Outputs
[Deliverables produced]

## Issues Encountered
[Problems, blockers, or concerns]

## Next Steps
[Recommendations for subsequent tasks]

## Detailed Work Summary
[Comprehensive documentation of analysis and decisions]
```

### Metadata JSON

```json
{
  "apm_version": "string",
  "domain": "manuscript-review",
  "manuscript": {
    "name": "string",
    "type": "empirical|theoretical|review",
    "target_outlet": "string",
    "field": "string"
  },
  "review_started": "ISO-8601 date",
  "phases": {
    "section_analysis": "pending|in_progress|complete",
    "rigor_analysis": "pending|in_progress|complete",
    "writing_analysis": "pending|in_progress|complete",
    "quality_control": "pending|in_progress|complete",
    "executive_summary": "pending|in_progress|complete"
  }
}
```

## Error Handling

### Agent-Level Error Handling

**Implementation Agent Errors**:
1. **Minor Issues** (≤2 debugging exchanges): Debug locally
2. **Major Issues** (>2 exchanges OR complex/systemic): Delegate to Ad-Hoc Debugger
3. **Escalation**: Report to Manager Agent if debugging fails

**Manager Agent Errors**:
1. **Task Assignment Issues**: Revise Task Assignment Prompt
2. **Coordination Problems**: Modify Implementation Plan
3. **Context Loss**: Initiate handover procedure

**Setup Agent Errors**:
1. **Context Gathering Issues**: Additional discovery cycles
2. **Plan Generation Problems**: Systematic review phase
3. **Bootstrap Creation Errors**: Regenerate with corrections

### System-Level Error Handling

**Guide Reference Errors**:
- Validate all `{GUIDE_PATH:}` references during agent initialization
- Provide clear error messages for missing guides
- Fall back to alternative guide paths if available

**Metadata Errors**:
- Validate JSON structure on generation
- Provide default values for missing fields
- Log warnings for schema violations

**Automation Script Errors**:
- Validate CLI arguments before execution
- Check file system permissions
- Provide clear error messages with recovery suggestions

### Handover Error Handling

**Context Transfer Issues**:
- Verify handover artifacts completeness before session close
- Require explicit user verification of replacement agent understanding
- Provide clarification protocols for context gaps

**Timing Errors**:
- Enforce handover eligibility requirements
- Reject handover requests during active work
- Guide users to complete current cycle before handover

## Testing Strategy

### Unit Testing

**Python Automation**:
- Test `02-setup_review.py` CLI argument parsing
- Validate metadata.json generation
- Verify artifact file creation
- Test guide reference path resolution

**Guide References**:
- Validate all `{GUIDE_PATH:}` references resolve correctly
- Test relative path handling
- Verify guide file existence

### Integration Testing

**Setup Agent → Manager Agent**:
- Test Bootstrap Prompt generation and parsing
- Verify YAML frontmatter structure
- Validate context transfer completeness

**Manager Agent → Implementation Agents**:
- Test Task Assignment Prompt creation
- Verify dependency context integration
- Validate Memory Log creation and review

**End-to-End Workflow**:
- Execute complete manuscript review workflow
- Test all 26 Implementation Agents
- Verify phase transitions
- Validate final deliverables

### Validation Testing

**Pattern Compliance**:
- Verify all agents use upstream YAML frontmatter
- Check guide reference syntax
- Validate execution type patterns

**Functionality Preservation**:
- Test manuscript-specific analysis criteria
- Verify 3-phase parallel execution
- Validate Quality Control synthesis
- Check Executive Summary generation

**Documentation Accuracy**:
- Verify all guide links work
- Test navigation in README files
- Validate example code snippets

### Regression Testing

**Backward Compatibility**:
- Test legacy artifact handling
- Verify existing review workspace compatibility
- Validate migration path

**Automation Preservation**:
- Test all existing `02-setup_review.py` flags
- Verify manuscript asset copying
- Check system state generation

## Performance Considerations

### Context Window Management

**Setup Agent**:
- Use powerful frontier models (Claude Sonnet 4) for complex reasoning
- Monitor context usage during 5-phase workflow
- Implement checkpoint gates to manage context growth

**Manager Agent**:
- Consider handover after 10-15 task cycles (first manager)
- Consider handover after 15-20 task cycles (replacement managers)
- Monitor context usage visualization in AI IDE

**Implementation Agents**:
- Consider handover after 5-10 task cycles
- Use economical models where appropriate (Cursor Auto, GPT-4.1)
- Implement Memory Logging to offload context

### Parallel Execution Optimization

**Section Analysis (S1-S10)**:
- Execute all 10 agents in parallel
- Minimize inter-agent dependencies
- Collect outputs before proceeding to next phase

**Rigor + Writing Analysis (R1-R7, W1-W7)**:
- Execute both groups in parallel after Section phase
- Cross-reference with section findings
- Optimize Task Assignment Prompt size

### Automation Performance

**Python Script Optimization**:
- Minimize file I/O operations
- Cache guide references
- Optimize artifact generation

**Metadata Tracking**:
- Update phase status incrementally
- Avoid redundant JSON writes
- Implement atomic file operations

## Security Considerations

### File System Security

**Workspace Isolation**:
- Validate workspace paths before creation
- Prevent directory traversal attacks
- Implement permission checks

**Artifact Protection**:
- Set appropriate file permissions on generated artifacts
- Validate file content before writing
- Implement backup mechanisms

### Input Validation

**CLI Arguments**:
- Sanitize manuscript names and paths
- Validate manuscript type enum values
- Check outlet and field strings for injection

**YAML Frontmatter**:
- Validate YAML structure before parsing
- Sanitize user-provided metadata
- Implement schema validation

### Guide Reference Security

**Path Validation**:
- Prevent directory traversal in guide paths
- Validate guide file existence before reference
- Implement whitelist of allowed guide directories

## Deployment Considerations

### Migration Path

**Phase 1: Immediate Adoption** (Current Focus):
1. Copy upstream guides to `06-guides/upstream/`
2. Update Setup Agent with 5-phase pattern
3. Update Manager Agent with Bootstrap pattern
4. Update all 26 Implementation Agents with YAML frontmatter
5. Enhance `02-setup_review.py` for upstream artifacts
6. Update all documentation

**Phase 2: CLI Integration** (Future):
1. Contribute to upstream-apm repository
2. Add `templates/domain-specific/manuscript-review/` directory
3. Extend CLI with `--domain` flag
4. Enable `apm init --domain manuscript-review`

**Phase 3: Advanced Integration** (Optional):
1. Multi-domain support
2. Domain registry publication
3. Custom build process
4. Version compatibility tracking

### Rollout Strategy

**Existing Users**:
- Provide migration guide
- Maintain backward compatibility for in-progress reviews
- Offer gradual adoption path

**New Users**:
- Default to upstream-integrated version
- Provide comprehensive onboarding documentation
- Include quick start guide

### Maintenance Strategy

**Upstream Tracking**:
- Monitor upstream-apm releases
- Update rigorous-apm when upstream patterns change
- Document version compatibility

**Community Contribution**:
- Share improvements with upstream
- Gather feedback from manuscript review community
- Iterate on domain specialization

## Future Enhancements

### Short-Term (Post-Phase 1)

1. **Automated Testing Suite**: Create comprehensive test suite for manuscript review workflow
2. **Enhanced Metadata Tracking**: Add agent performance metrics and timing data
3. **Improved Error Messages**: Provide more detailed guidance for common issues
4. **Guide Cross-Linking**: Add hyperlinks between related guides

### Medium-Term (Phase 2)

1. **CLI Integration**: Contribute manuscript-review domain to upstream
2. **Template Bundle**: Package rigorous-apm as installable extension
3. **Update Command**: Enable `apm update --domain manuscript-review`
4. **Version Management**: Track upstream and domain versions separately

### Long-Term (Phase 3)

1. **Multi-Domain Support**: Enable combining manuscript-review with other domains
2. **Domain Registry**: Publish as installable package
3. **Custom Build Process**: Extend upstream's build.js for domain bundles
4. **Community Ecosystem**: Foster academic review community around rigorous-apm

## References

- [Upstream APM v0.5 Documentation](../../upstream-apm/README.md)
- [Upstream Workflow Overview](../../upstream-apm/docs/Workflow_Overview.md)
- [Integration Strategy](../../INTEGRATION_STRATEGY.md)
- [Rigorous APM Current State](../../rigorous-apm/01-START_HERE.md)
