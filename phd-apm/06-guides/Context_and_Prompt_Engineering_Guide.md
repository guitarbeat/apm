# Context and Prompt Engineering Guide

Architecture principles for PhD APM's agent coordination system.

---

## Core Principles

### 1. Operational Boundaries Over Personality

Agents are defined by **what they do**, not personality traits.

**Agent Types**:
- **Setup**: Project discovery and planning → Implementation Plan
- **Manager**: Coordination and task assignment → Task Assignment Prompts
- **Implementation**: Domain-specific execution → Completed tasks + Memory Logs

**Benefits**: Clear scope, no overlap, focused specialization, distributed workload.

### 2. Mandatory Progression Sequences

Fixed workflows prevent fragmentation:

**Setup Phase**:
```
Context Synthesis → Project Breakdown → Review → Enhancement → Bootstrap
```

**Task Loop**:
```
Assignment → Execution → Logging → Review → Next Action
```

### 3. Context Layering

Information organized in hierarchical layers:

1. **System Context**: Agent role, capabilities, boundaries
2. **Project Context**: Goals, constraints, current state
3. **Task Context**: Specific assignment, requirements, dependencies
4. **Memory Context**: Previous work, decisions, patterns

**Rule**: Each layer builds on previous, no skipping.

---

## Prompt Engineering Techniques

### 1. Structured Formats

**YAML Frontmatter**: Metadata for parsing and routing
```yaml
---
priority: high
agent_id: S1
domain: manuscript-review
---
```

**Markdown Sections**: Clear hierarchy and scannability
- Use headers (##, ###) for structure
- Bullet points for lists
- Code blocks for examples
- Tables for comparisons

### 2. Information Density

**Optimize for token efficiency**:
- Remove filler words
- Use abbreviations consistently
- Bullet points over paragraphs
- Tables over prose
- Examples only when necessary

**Balance**: Clarity vs brevity. Never sacrifice understanding for tokens.

### 3. Reference Patterns

**Guide References**: `{GUIDE_PATH:filename.md}`
- System resolves to `upstream/` or domain guides
- Agents load on-demand
- Reduces prompt size

**File References**: Relative paths from workspace root
- `../01-START_HERE.md`
- `agent_outputs/section_analysis.md`

### 4. Instruction Clarity

**Effective instructions**:
- Start with action verb
- One instruction per line
- Specific, measurable outcomes
- Clear success criteria

**Example**:
```markdown
1. Read manuscript abstract
2. Identify 3-5 key contributions
3. Assess novelty (1-5 scale)
4. Document findings in Memory Log
```

---

## Memory System Architecture

### State Management

**system_state.json**: Single source of truth
- Manuscript metadata
- Review progress
- Agent status
- Phase tracking

**Memory Logs**: Task-level documentation
- Agent findings
- Decisions made
- Issues identified
- Recommendations

**Handover Files**: Session continuity
- Active context
- Pending work
- User preferences
- Blockers

### State Contracts

Treat state files as APIs:
- **Read**: Agents consume current state
- **Write**: Agents update specific fields
- **Validate**: Check schema compliance
- **Extend**: Add domain fields in nested objects

**Rule**: Never modify core fields, only extend.

---

## PhD APM Implementation

### 26-Agent Specialization

**Section Agents (S1-S10)**: Manuscript structure analysis
- Each agent owns one section
- Deep domain knowledge
- Consistent evaluation criteria

**Rigor Agents (R1-R7)**: Scientific quality validation
- Originality, ethics, reproducibility
- Statistical rigor, technical accuracy
- Cross-section consistency

**Writing Agents (W1-W7)**: Communication quality
- Language, narrative, clarity
- Terminology, inclusivity, citations
- Audience alignment

**Synthesis Agents (QC, ES)**: Integration and reporting
- Quality control across all agents
- Executive summary for stakeholders

### 3-Phase Execution

**Phase 1**: Section Analysis (S1-S10 parallel)
- Independent section reviews
- No cross-dependencies
- Maximum parallelization

**Phase 2**: Rigor + Writing (R1-R7, W1-W7 parallel)
- Cross-section analysis
- Requires Phase 1 completion
- Two parallel tracks

**Phase 3**: Synthesis (QC → ES sequential)
- Integrates all findings
- Requires Phase 2 completion
- Sequential for coherence

### Context Assembly

**Manuscript Context**:
- Type (empirical, theoretical, review)
- Target outlet (journal, conference)
- Field (discipline-specific conventions)
- Current stage (draft, revision, final)

**Review Context**:
- Focus areas (all, specific sections)
- Depth (quick, comprehensive, publication-ready)
- Timeline (deadline, revision schedule)
- Output format (reports, annotations, both)

**Agent Context**:
- Specialization (section, rigor, writing)
- Dependencies (which agents must complete first)
- Evaluation criteria (domain-specific rubrics)
- Output requirements (Memory Log format)

---

## Best Practices

### Prompt Design

1. **Start with structure**: YAML frontmatter, clear sections
2. **Layer information**: System → Project → Task → Memory
3. **Use references**: Link to guides, don't duplicate
4. **Optimize density**: Bullet points, tables, abbreviations
5. **Test iteratively**: Validate with real agents

### Context Management

1. **Minimize duplication**: Reference, don't repeat
2. **Update atomically**: One state change at a time
3. **Validate changes**: Check schema compliance
4. **Document extensions**: Explain custom fields
5. **Maintain history**: Track state evolution

### Agent Coordination

1. **Respect boundaries**: Agents stay in scope
2. **Follow sequences**: Complete phases in order
3. **Track dependencies**: Ensure prerequisites met
4. **Log thoroughly**: Document all decisions
5. **Handover cleanly**: Transfer context completely

---

## Common Patterns

### Meta-Prompting

Generate prompts programmatically:

```markdown
For each section in [Introduction, Methods, Results, Discussion]:
  Create agent with:
    - ID: S{n}
    - Focus: {section}
    - Criteria: {section-specific rubric}
    - Output: Memory Log
```

### Conditional Logic

Adapt behavior based on context:

```markdown
IF manuscript_type == "empirical":
  Emphasize methods and results rigor
ELSE IF manuscript_type == "theoretical":
  Emphasize logical consistency and citations
```

### Progressive Refinement

Iterative improvement cycles:

```markdown
1. Initial analysis (broad strokes)
2. Detailed review (specific issues)
3. Recommendations (actionable improvements)
4. Validation (verify completeness)
```

---

## Troubleshooting

**Agent confusion**: Check operational boundaries, clarify scope
**Incomplete work**: Verify progression sequences followed
**Context loss**: Review Memory Log completeness, check handover
**Inconsistent output**: Standardize formats, provide examples
**Token limits**: Use references, optimize density, split tasks

---

## Resources

- **Customization Guide**: Domain adaptation patterns
- **Memory System Guide**: State management details
- **Agent Cheat Sheet**: Agent roster and capabilities
- **Upstream Guides**: Foundation patterns
