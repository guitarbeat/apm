# APM Customization Guide

Guide for adapting PhD APM to specific domains and workflows.

**Prerequisites**: See `Context_and_Prompt_Engineering_Guide.md` for architecture principles.

---

## Setup

**Recommended**: Use GitHub's "Use this template" feature instead of forking.

1. Visit the APM repository
2. Click "Use this template" → "Create a new repository"
3. Name descriptively (e.g., `apm-for-web-development`)
4. Clone and customize

**Benefits**: Independent development, version control, selective upstream merges, team sharing.

---

## Customization Points

### 1. Setup Agent (Context Synthesis)

**File**: `03-setup-agent/setup_agent_initiation_prompt.md`

**Customize**: Add domain-specific questions to Phase 2 (Context Synthesis)

**Examples**:
- **Web Dev**: Framework preferences, deployment platform, API architecture
- **Data Science**: Data sources, ML libraries, visualization tools, deployment environment
- **Manuscript Review**: Format, target outlet, review focus, discipline requirements

### 2. Implementation Agents

**Files**: `05-implementation-agents/*.md`

**Customize**: Execution behavior, interaction patterns, output formats

**Common modifications**:
- Verbose vs minimal interaction modes
- Quality gates and checkpoints
- Domain-specific validation rules
- Output format requirements

### 3. Manager Agent

**Files**: `04-manager-agent/*.md`

**Customize**: Coordination style, task assignment patterns

**Common modifications**:
- Dependency-aware coordination
- Quality gate integration
- Domain-specific task requirements
- Testing/documentation integration

### 4. Memory System

**File**: `06-guides/Memory_System_Guide.md`

**Customize**: Add domain-specific fields to `system_state.json`

**Example additions**:
```json
{
  "domain_specific": {
    "test_coverage": 85,
    "deployment_status": "staging",
    "custom_metrics": {}
  }
}
```

**Rules**: Don't modify core fields, use nested objects for extensions, document changes.

---

## MCP Tool Integration

### Adding New Tools

1. **Configure**: Add to `.kiro/settings/mcp.json`
2. **Document**: Update agent prompts with tool capabilities
3. **Test**: Verify tool availability and permissions

### Example Configuration

```json
{
  "mcpServers": {
    "your-tool": {
      "command": "uvx",
      "args": ["your-tool-package@latest"],
      "disabled": false,
      "autoApprove": ["tool_function_name"]
    }
  }
}
```

### Domain-Specific Tools

- **Web Dev**: Browser automation, API testing, deployment tools
- **Data Science**: Data analysis, visualization, model training
- **Research**: Literature search, citation management, data repositories

---

## Domain Specializations

### Web Development APM

**Focus**: Frontend/backend coordination, deployment pipelines, testing

**Key customizations**:
- Framework-specific agents (React, Vue, etc.)
- API integration patterns
- Deployment automation
- Testing strategies

### Data Science APM

**Focus**: Data pipelines, analysis workflows, model development

**Key customizations**:
- Data ingestion agents
- Analysis/visualization specialists
- Model training coordination
- Reproducibility requirements

### Mobile Development APM

**Focus**: Platform-specific development, testing, deployment

**Key customizations**:
- iOS/Android specialists
- Device testing strategies
- App store deployment
- Performance monitoring

### Machine Learning APM

**Focus**: Model development, training, deployment

**Key customizations**:
- Problem-type specialists (classification, regression, NLP, CV)
- Training infrastructure coordination
- Model monitoring and drift detection
- Deployment strategies

---

## PhD APM Specific Customizations

This instance demonstrates domain specialization:

**26 Specialized Agents**:
- S1-S10: Section analysis (title, abstract, intro, methods, results, discussion, conclusion, references, supplementary)
- R1-R7: Rigor review (originality, impact, ethics, data availability, statistics, technical accuracy, consistency)
- W1-W7: Writing quality (language, narrative, clarity, terminology, inclusivity, citations, audience alignment)
- QC, ES: Quality control and executive summary

**3-Phase Execution**: Section → Rigor+Writing → QC→ES

**Manuscript-Specific Memory**: Tracks review progress, agent outputs, manuscript metadata

**Academic Criteria**: Journal-specific requirements, field conventions, citation styles

---

## Version Management

### Tracking Customizations

1. **Branch Strategy**: `main` (upstream sync), `custom` (your changes), `feature/*` (experiments)
2. **Documentation**: Maintain `CUSTOMIZATIONS.md` listing all changes
3. **Testing**: Validate customizations don't break core workflows

### Merging Upstream Updates

```bash
# Add upstream remote
git remote add upstream https://github.com/original/apm-repo

# Fetch and merge selectively
git fetch upstream
git cherry-pick <commit-hash>  # For specific improvements
```

### Release Management

1. Tag stable customizations: `git tag v1.0-custom`
2. Document breaking changes
3. Test with representative projects
4. Communicate changes to team

---

## Best Practices

1. **Start Small**: Customize one component at a time
2. **Document Changes**: Maintain clear records of modifications
3. **Test Thoroughly**: Validate with real projects before team rollout
4. **Version Control**: Use branches for experiments
5. **Share Learnings**: Contribute successful patterns back to community
6. **Stay Updated**: Periodically sync with upstream improvements

---

## Common Pitfalls

- **Over-customization**: Keep core patterns intact
- **Breaking Changes**: Test compatibility with existing workflows
- **Undocumented Changes**: Always document customizations
- **Ignoring Upstream**: Miss valuable improvements
- **Inconsistent Application**: Apply customizations systematically

---

## Resources

- **Context & Prompt Engineering Guide**: Architecture principles
- **Agent Cheat Sheet**: Agent roster and capabilities
- **Memory System Guide**: State management patterns
- **Upstream APM**: Foundation patterns and updates
