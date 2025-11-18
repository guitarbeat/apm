---
status: draft
created: 2025-11-17
owner: guitarbeat
priority: high
---

# Spec: Rigorous-APM Upstream Integration

## Overview

Transform rigorous-apm from a parallel APM system into a domain-specific extension of upstream-apm v0.5, leveraging upstream's proven patterns while preserving rigorous-apm's manuscript review specialization and automation capabilities.

## Goals

1. **Adopt upstream v0.5 patterns** for Setup Agent, Manager Agent, and Implementation Agents
2. **Preserve rigorous-apm strengths**: 26 specialized agents, Python automation, manuscript-specific workflow
3. **Maintain backward compatibility** for existing manuscript reviews where feasible
4. **Enable future CLI integration** by aligning with upstream's template structure
5. **Reduce maintenance burden** by inheriting upstream improvements

## Non-Goals

- Rewriting `02-setup_review.py` (it's superior to manual setup)
- Removing manuscript-specific guides or agents
- Breaking existing in-progress reviews
- Contributing to upstream repository (Phase 1 only; future phases may include this)

## Background

### Current State
- **rigorous-apm**: 26-agent manuscript review system with custom Setup/Manager/Implementation patterns
- **upstream-apm v0.5**: General-purpose APM with CLI, template system, improved guides
- **Divergence**: Different prompt structures, guide references, initialization patterns

### Why Integrate?
- Upstream v0.5 has superior patterns: YAML frontmatter, execution types, handover protocols
- Rigorous-apm has superior domain specialization: 26 agents, parallel coordination, Python automation
- Integration creates best-of-both-worlds: upstream foundation + manuscript specialization

## Design

### Architecture

```
rigorous-apm/
├── 01-START_HERE.md                          # Updated: explains upstream relationship
├── 02-setup_review.py                        # Enhanced: generates upstream-compatible artifacts
├── 03-review-kickoff/                        # Updated: uses upstream patterns
│   ├── review_kickoff_prompt.md              # Updated: references upstream guides
│   ├── share_plan_with_setup.apm             # Kept: automation snippet
│   └── manager_load_plan.apm                 # Kept: automation snippet
├── 03-setup-agent/                           # Updated: adopts upstream 5-phase pattern
│   └── setup_agent_initiation_prompt.md      # Rewritten: upstream-compatible
├── 04-manager-agent/                         # Updated: adopts upstream coordination pattern
│   ├── manager_agent_initiation_prompt.md    # Rewritten: upstream-compatible
│   └── manager_bootstrap_prompt.md           # Updated: upstream format
├── 05-implementation-agents/                 # Updated: adds YAML frontmatter
│   ├── section/                              # S1-S10: upstream execution patterns
│   ├── rigor/                                # R1-R7: upstream execution patterns
│   ├── writing/                              # W1-W7: upstream execution patterns
│   ├── quality_control_agent_prompt.md       # Updated: upstream patterns
│   ├── executive_summary_agent_prompt.md     # Updated: upstream patterns
│   └── implementation_agent_base_prompt.md   # NEW: base template for all 26
└── 06-guides/                                # Enhanced: includes upstream guides
    ├── upstream/                             # NEW: copied from upstream-apm
    │   ├── Context_Synthesis_Guide.md
    │   ├── Implementation_Plan_Guide.md
    │   ├── Memory_Log_Guide.md
    │   ├── Memory_System_Guide.md
    │   ├── Project_Breakdown_Guide.md
    │   ├── Project_Breakdown_Review_Guide.md
    │   └── Task_Assignment_Guide.md
    ├── README.md                             # Updated: navigation for both guide sets
    ├── Agent_Cheat_Sheet.md                  # Kept: manuscript-specific
    ├── Manuscript_Review_Implementation_Plan_Guide.md  # Kept: manuscript-specific
    └── [other manuscript guides...]          # Kept: manuscript-specific
```

### Key Changes

#### 1. Setup Agent (`03-setup-agent/setup_agent_initiation_prompt.md`)

**Adopt from upstream**:
- 5-phase structure: Context Synthesis → Project Breakdown → Review → Enhancement → Bootstrap
- Guide reference patterns: `{GUIDE_PATH:filename.md}`
- Checkpoint/approval gates
- Bootstrap Prompt generation

**Preserve from rigorous**:
- Manuscript-specific Context Synthesis questions
- Integration with `02-setup_review.py`
- Academic review workflow understanding
- Manuscript asset handling

**New behavior**:
```markdown
## Phase 1: Context Synthesis
- Read {GUIDE_PATH:Context_Synthesis_Guide.md}
- Conduct manuscript-specific discovery:
  - Manuscript type (empirical/theoretical/review)
  - Target outlet and requirements
  - Research field and standards
  - Review priorities and constraints
- **Checkpoint**: User confirms context complete

## Phase 2: Project Breakdown
- Read {GUIDE_PATH:Project_Breakdown_Guide.md}
- Generate Implementation Plan with 5 phases:
  - Phase 1: Section Analysis (S1-S10 parallel)
  - Phase 2: Rigor Analysis (R1-R7 parallel)
  - Phase 3: Writing Analysis (W1-W7 parallel)
  - Phase 4: Quality Control Synthesis
  - Phase 5: Executive Summary
- **Checkpoint**: User reviews plan structure

## Phase 3: Systematic Review (Optional)
- Read {GUIDE_PATH:Project_Breakdown_Review_Guide.md}
- User chooses: skip or proceed with systematic review
- **Checkpoint**: User approves refined plan

## Phase 4: Enhancement
- Read {GUIDE_PATH:Implementation_Plan_Guide.md}
- Transform plan into detailed APM artifact format
- **Checkpoint**: User approves enhanced plan

## Phase 5: Bootstrap Generation
- Generate Manager Agent Bootstrap Prompt
- Include manuscript context and 26-agent coordination strategy
- Reference upstream guides for Manager responsibilities
```

#### 2. Manager Agent (`04-manager-agent/manager_agent_initiation_prompt.md`)

**Adopt from upstream**:
- Bootstrap Prompt pattern with YAML frontmatter
- Guide reference system
- Handover protocol structure
- Task Assignment Prompt patterns
- Memory System integration

**Preserve from rigorous**:
- 3-phase parallel execution model
- 26-agent coordination strategy
- Manuscript review workflow
- Quality Control synthesis pattern

**New behavior**:
```markdown
---
priority: 2
command_name: initiate-manager-manuscript-review
description: Initializes Manager Agent for academic manuscript review coordination
---

# Rigorous APM - Manager Agent Initiation Prompt

You are the **Manager Agent** for academic manuscript review, coordinating 26 specialized Implementation Agents.

## Initialization

Request Bootstrap Prompt or Handover Prompt from user.

### Bootstrap Prompt Processing
1. Parse YAML frontmatter: `Workspace_root`, `manuscript_type`, `target_outlet`
2. Read {GUIDE_PATH:Implementation_Plan_Guide.md}
3. Read {GUIDE_PATH:Memory_System_Guide.md}
4. Read {GUIDE_PATH:Memory_Log_Guide.md}
5. Read {GUIDE_PATH:Task_Assignment_Guide.md}
6. Confirm understanding of 5-phase manuscript review workflow

## Manuscript Review Coordination

### Phase 1: Section Analysis (S1-S10)
- Execute all 10 section agents **in parallel**
- Create Task Assignment Prompts using {GUIDE_PATH:Task_Assignment_Guide.md}
- Each agent analyzes specific manuscript section
- Collect structured outputs in Memory Logs

### Phase 2: Rigor Analysis (R1-R7)
- Execute all 7 rigor agents **in parallel** after Phase 1
- Focus on scientific standards and methodology
- Cross-reference with section findings

### Phase 3: Writing Analysis (W1-W7)
- Execute all 7 writing agents **in parallel** after Phase 1
- Focus on language, style, presentation
- Cross-reference with section and rigor findings

### Phase 4: Quality Control Synthesis
- Execute QC agent after Phases 1-3 complete
- Synthesize all 24 agent findings
- Resolve conflicts and prioritize issues

### Phase 5: Executive Summary
- Execute ES agent after Phase 4
- Generate comprehensive final report
- Provide publication readiness assessment
```

#### 3. Implementation Agents (All 26)

**Adopt from upstream**:
- YAML frontmatter with metadata
- Execution type patterns (single-step vs multi-step)
- Memory Log Guide references
- Debug delegation protocol
- Handover awareness

**Preserve from rigorous**:
- Domain-specific analysis criteria
- Manuscript section focus
- Academic standards evaluation
- Field-specific requirements

**Template structure**:
```markdown
---
priority: 3
command_name: [agent-specific-name]
description: [agent-specific description]
agent_id: [S1-S10, R1-R7, W1-W7, QC, ES]
domain: manuscript-review
---

# [Agent Name] - Implementation Agent

You are a specialized Implementation Agent for academic manuscript review.

## Specialization
[Domain-specific focus and expertise]

## Execution Pattern
[Reference upstream patterns from Implementation_Agent_Initiation_Prompt.md]

## Analysis Criteria
[Manuscript-specific evaluation criteria]

## Memory Logging
Read {GUIDE_PATH:Memory_Log_Guide.md} and log all findings.

## Operating Rules
- Follow upstream Implementation Agent patterns
- Apply manuscript-specific standards
- Reference field-specific requirements
- Delegate debugging per upstream protocol
```

#### 4. Python Automation (`02-setup_review.py`)

**Enhancements**:
- Generate upstream-compatible `Implementation_Plan.md`
- Create `.apm/metadata.json` tracking:
  - APM version (upstream + rigorous)
  - Manuscript type and target outlet
  - Review start date
  - Agent completion status
- Generate Bootstrap Prompts in upstream format
- Reference upstream guides in generated artifacts

**Preserved**:
- All existing CLI flags and behavior
- Manuscript asset copying
- System state generation
- Audience legend integration

**New output**:
```json
// .apm/metadata.json
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
    "section_analysis": "in_progress",
    "rigor_analysis": "pending",
    "writing_analysis": "pending",
    "quality_control": "pending",
    "executive_summary": "pending"
  }
}
```

#### 5. Guides Integration

**Copy from upstream** to `06-guides/upstream/`:
- Context_Synthesis_Guide.md
- Implementation_Plan_Guide.md
- Memory_Log_Guide.md
- Memory_System_Guide.md
- Project_Breakdown_Guide.md
- Project_Breakdown_Review_Guide.md
- Task_Assignment_Guide.md

**Keep in `06-guides/`** (manuscript-specific):
- Agent_Cheat_Sheet.md
- Manuscript_Review_Implementation_Plan_Guide.md
- Context_and_Prompt_Engineering_Guide.md
- Customization_Guide.md
- Handover_Guide.md
- Memory_System_Guide.md (manuscript-specific extensions)
- Troubleshooting_Playbook.md

**Update `06-guides/README.md`**:
```markdown
# Rigorous APM Guides

## Upstream APM Guides (Foundation)
Located in `upstream/` - core APM patterns from upstream-apm v0.5

- [Context Synthesis Guide](upstream/Context_Synthesis_Guide.md)
- [Implementation Plan Guide](upstream/Implementation_Plan_Guide.md)
- [Memory System Guide](upstream/Memory_System_Guide.md)
- [Memory Log Guide](upstream/Memory_Log_Guide.md)
- [Project Breakdown Guide](upstream/Project_Breakdown_Guide.md)
- [Task Assignment Guide](upstream/Task_Assignment_Guide.md)

## Manuscript Review Guides (Specialization)
Domain-specific guides for academic manuscript review

- [Agent Cheat Sheet](Agent_Cheat_Sheet.md) - Quick reference for all 26 agents
- [Manuscript Review Implementation Plan Guide](Manuscript_Review_Implementation_Plan_Guide.md)
- [Context and Prompt Engineering Guide](Context_and_Prompt_Engineering_Guide.md)
- [Customization Guide](Customization_Guide.md)
- [Handover Guide](Handover_Guide.md)
- [Troubleshooting Playbook](Troubleshooting_Playbook.md)
```

## Implementation Plan

### Task 1: Copy Upstream Guides
**Objective**: Bring upstream v0.5 guides into rigorous-apm

**Steps**:
1. Create `rigorous-apm/06-guides/upstream/` directory
2. Copy 7 core guides from `upstream-apm/templates/guides/`
3. Update `06-guides/README.md` with navigation for both guide sets
4. Verify all guide files are readable and properly formatted

**Acceptance Criteria**:
- [ ] All 7 upstream guides copied to `06-guides/upstream/`
- [ ] README.md updated with clear navigation
- [ ] No broken links or formatting issues

### Task 2: Update Setup Agent
**Objective**: Rewrite Setup Agent to use upstream v0.5 patterns

**Steps**:
1. Read upstream's `Setup_Agent_Initiation_Prompt.md` for pattern reference
2. Rewrite `03-setup-agent/setup_agent_initiation_prompt.md`:
   - Adopt 5-phase structure
   - Use `{GUIDE_PATH:filename.md}` reference pattern
   - Add manuscript-specific Context Synthesis questions
   - Include checkpoint/approval gates
   - Generate Bootstrap Prompt in upstream format
3. Update guide references to point to `06-guides/upstream/`
4. Test with sample manuscript review scenario

**Acceptance Criteria**:
- [ ] Setup Agent uses upstream 5-phase pattern
- [ ] All guide references use `{GUIDE_PATH:}` format
- [ ] Manuscript-specific questions preserved
- [ ] Bootstrap Prompt generation matches upstream format
- [ ] Checkpoints and approval gates implemented

### Task 3: Update Manager Agent
**Objective**: Rewrite Manager Agent to use upstream coordination patterns

**Steps**:
1. Read upstream's `Manager_Agent_Initiation_Prompt.md` for pattern reference
2. Rewrite `04-manager-agent/manager_agent_initiation_prompt.md`:
   - Add YAML frontmatter
   - Adopt Bootstrap Prompt processing pattern
   - Use upstream guide references
   - Preserve 3-phase parallel execution model
   - Document 26-agent coordination strategy
3. Update `04-manager-agent/manager_bootstrap_prompt.md` template
4. Test with sample Bootstrap Prompt

**Acceptance Criteria**:
- [ ] Manager Agent uses upstream Bootstrap pattern
- [ ] YAML frontmatter properly structured
- [ ] All guide references use `{GUIDE_PATH:}` format
- [ ] Parallel execution model preserved
- [ ] 26-agent coordination documented

### Task 4: Create Implementation Agent Base Template
**Objective**: Create base template for all 26 Implementation Agents

**Steps**:
1. Read upstream's `Implementation_Agent_Initiation_Prompt.md`
2. Create `05-implementation-agents/implementation_agent_base_prompt.md`:
   - Include YAML frontmatter structure
   - Document execution patterns (single-step vs multi-step)
   - Reference upstream Memory Log Guide
   - Include debug delegation protocol
   - Add manuscript-specific sections
3. Document how to use base template for specialization

**Acceptance Criteria**:
- [ ] Base template created with all upstream patterns
- [ ] YAML frontmatter structure documented
- [ ] Execution patterns clearly explained
- [ ] Manuscript-specific sections included
- [ ] Usage documentation provided

### Task 5: Update Section Analysis Agents (S1-S10)
**Objective**: Update all 10 section agents to use upstream patterns

**Steps**:
1. For each agent (S1-S10):
   - Add YAML frontmatter with metadata
   - Adopt upstream execution patterns
   - Reference upstream Memory Log Guide
   - Preserve manuscript-specific analysis criteria
   - Update guide references
2. Verify consistency across all 10 agents
3. Test with sample section analysis task

**Acceptance Criteria**:
- [ ] All 10 agents have YAML frontmatter
- [ ] Execution patterns match upstream
- [ ] Memory Log references updated
- [ ] Analysis criteria preserved
- [ ] Consistent structure across all agents

### Task 6: Update Rigor Analysis Agents (R1-R7)
**Objective**: Update all 7 rigor agents to use upstream patterns

**Steps**:
1. For each agent (R1-R7):
   - Add YAML frontmatter with metadata
   - Adopt upstream execution patterns
   - Reference upstream Memory Log Guide
   - Preserve scientific rigor criteria
   - Update guide references
2. Verify consistency across all 7 agents
3. Test with sample rigor analysis task

**Acceptance Criteria**:
- [ ] All 7 agents have YAML frontmatter
- [ ] Execution patterns match upstream
- [ ] Memory Log references updated
- [ ] Rigor criteria preserved
- [ ] Consistent structure across all agents

### Task 7: Update Writing Analysis Agents (W1-W7)
**Objective**: Update all 7 writing agents to use upstream patterns

**Steps**:
1. For each agent (W1-W7):
   - Add YAML frontmatter with metadata
   - Adopt upstream execution patterns
   - Reference upstream Memory Log Guide
   - Preserve writing quality criteria
   - Update guide references
2. Verify consistency across all 7 agents
3. Test with sample writing analysis task

**Acceptance Criteria**:
- [ ] All 7 agents have YAML frontmatter
- [ ] Execution patterns match upstream
- [ ] Memory Log references updated
- [ ] Writing criteria preserved
- [ ] Consistent structure across all agents

### Task 8: Update Quality Control & Executive Summary Agents
**Objective**: Update QC and ES agents to use upstream patterns

**Steps**:
1. Update `quality_control_agent_prompt.md`:
   - Add YAML frontmatter
   - Adopt upstream execution patterns
   - Document synthesis methodology
   - Reference upstream guides
2. Update `executive_summary_agent_prompt.md`:
   - Add YAML frontmatter
   - Adopt upstream execution patterns
   - Document reporting structure
   - Reference upstream guides
3. Test with sample synthesis task

**Acceptance Criteria**:
- [ ] Both agents have YAML frontmatter
- [ ] Execution patterns match upstream
- [ ] Synthesis/reporting methodology preserved
- [ ] Guide references updated

### Task 9: Enhance Python Automation
**Objective**: Update `02-setup_review.py` to generate upstream-compatible artifacts

**Steps**:
1. Add metadata.json generation:
   - APM version tracking
   - Manuscript metadata
   - Phase status tracking
2. Update Implementation Plan generation:
   - Use upstream format
   - Reference upstream guides
   - Include manuscript-specific sections
3. Update Bootstrap Prompt generation:
   - Match upstream format
   - Include YAML frontmatter
   - Reference correct guide paths
4. Add version compatibility checking
5. Test with sample manuscript

**Acceptance Criteria**:
- [ ] metadata.json generated with correct structure
- [ ] Implementation Plan matches upstream format
- [ ] Bootstrap Prompt matches upstream format
- [ ] All guide references correct
- [ ] Backward compatibility maintained

### Task 10: Update Documentation
**Objective**: Update all documentation to reflect upstream integration

**Steps**:
1. Update `01-START_HERE.md`:
   - Explain upstream relationship
   - Document new workflow
   - Update quick start guide
   - Reference upstream guides
2. Update `03-review-kickoff/review_kickoff_prompt.md`:
   - Use upstream patterns
   - Update guide references
   - Preserve automation snippets
3. Update `AGENTS.md`:
   - Document upstream integration
   - Update contribution guidelines
4. Create migration guide for existing users
5. Update README.md in root

**Acceptance Criteria**:
- [ ] All documentation updated
- [ ] Upstream relationship clearly explained
- [ ] Migration guide created
- [ ] No broken links or outdated references

### Task 11: Testing & Validation
**Objective**: Validate entire integrated system works end-to-end

**Steps**:
1. Run complete manuscript review workflow:
   - Execute `02-setup_review.py`
   - Launch Setup Agent
   - Bootstrap Manager Agent
   - Execute sample tasks for each agent type
   - Verify Memory Log creation
   - Check artifact generation
2. Validate guide references work correctly
3. Test handover scenarios
4. Verify metadata tracking
5. Document any issues found

**Acceptance Criteria**:
- [ ] Complete workflow executes successfully
- [ ] All guide references resolve correctly
- [ ] Memory Logs created properly
- [ ] Metadata tracking works
- [ ] No critical issues found

## Success Metrics

1. **Pattern Adoption**: All agents use upstream v0.5 patterns (YAML frontmatter, guide references, execution types)
2. **Functionality Preserved**: All 26 agents maintain manuscript review capabilities
3. **Automation Enhanced**: `02-setup_review.py` generates upstream-compatible artifacts
4. **Documentation Complete**: All docs updated, migration guide created
5. **Testing Passed**: End-to-end workflow validated successfully

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Breaking existing reviews | High | Maintain backward compatibility, provide migration guide |
| Guide reference errors | Medium | Thorough testing, automated link checking |
| Pattern misalignment | Medium | Regular comparison with upstream, follow upstream updates |
| Agent behavior changes | High | Preserve domain-specific criteria, extensive testing |
| Python script bugs | Medium | Incremental changes, comprehensive testing |

## Future Enhancements (Post-Phase 1)

1. **CLI Integration**: Contribute to upstream for `apm init --domain manuscript-review`
2. **Template Bundle**: Package rigorous-apm as installable domain extension
3. **Multi-Domain Support**: Enable combining manuscript-review with other domains
4. **Automated Testing**: Create test suite for manuscript review workflow
5. **Community Contribution**: Share with academic community, gather feedback

## References

- [Upstream APM v0.5 Documentation](../upstream-apm/README.md)
- [Integration Strategy](../INTEGRATION_STRATEGY.md)
- [Rigorous APM Current State](../rigorous-apm/01-START_HERE.md)

---

**Next Steps**: Begin Task 1 - Copy upstream guides to establish foundation
