# Rigorous-APM ↔ Upstream-APM Integration Strategy

## Vision
Transform rigorous-apm from a parallel system into a **domain-specific extension** of upstream-apm, leveraging upstream's v0.5 CLI infrastructure while preserving rigorous-apm's manuscript review specialization.

## Architecture Model

```
upstream-apm/                          # Foundation framework
├── templates/
│   ├── Setup_Agent/                   # Base setup patterns
│   ├── Manager_Agent/                 # Base coordination patterns
│   ├── Implementation_Agent/          # Base execution patterns
│   ├── guides/                        # Core APM guides
│   └── domain-specific/               # NEW: Domain extensions
│       └── manuscript-review/         # Rigorous-APM specialization
│           ├── agents/                # 26 specialized agents
│           ├── guides/                # Manuscript-specific guides
│           ├── scripts/               # setup_review.py automation
│           └── templates/             # Review-specific templates

rigorous-apm/                          # Domain specialization (simplified)
├── README.md                          # Points to upstream + explains specialization
├── setup_review.py                    # Manuscript workspace automation
├── agents/                            # 26 Implementation Agents
│   ├── section/                       # S1-S10
│   ├── rigor/                         # R1-R7
│   └── writing/                       # W1-W7
├── guides/                            # Manuscript review guides
└── templates/                         # Review-specific templates
    ├── Setup_Agent_Manuscript.md      # Extends upstream Setup
    └── Manager_Agent_Manuscript.md    # Extends upstream Manager
```

## Integration Phases

### Phase 1: Adopt Upstream Foundations (Immediate)
**Goal**: Update rigorous-apm to use upstream's v0.5 patterns without breaking existing workflow

**Actions**:
1. **Update Setup Agent** (`03-setup-agent/setup_agent_initiation_prompt.md`)
   - Adopt upstream's 5-phase structure
   - Keep manuscript-specific Context Synthesis questions
   - Reference `02-setup_review.py` as the automation helper
   - Use upstream's guide reference patterns

2. **Update Manager Agent** (`04-manager-agent/manager_agent_initiation_prompt.md`)
   - Adopt upstream's Bootstrap Prompt pattern
   - Keep 3-phase parallel execution model (S→R+W→QC→ES)
   - Use upstream's Task Assignment patterns
   - Reference upstream Memory System guides

3. **Update Implementation Agents** (all 26 in `05-implementation-agents/`)
   - Adopt upstream's YAML frontmatter for metadata
   - Use upstream's execution patterns (single-step vs multi-step)
   - Reference upstream's Memory Log Guide
   - Keep domain-specific analysis criteria

4. **Adopt Upstream Guides**
   - Copy upstream's core guides to `rigorous-apm/06-guides/upstream/`
   - Keep manuscript-specific guides in `rigorous-apm/06-guides/`
   - Update all references to use upstream guide patterns

**Outcome**: Rigorous-APM uses upstream patterns but maintains manuscript review specialization

### Phase 2: CLI Integration (Future Enhancement)
**Goal**: Make rigorous-apm installable via upstream CLI

**Actions**:
1. **Contribute to upstream-apm**:
   - Add `templates/domain-specific/manuscript-review/` directory
   - Submit PR with manuscript review template bundle
   - Extend CLI to support `--domain` flag

2. **CLI Command**:
   ```bash
   apm init --domain manuscript-review
   ```
   This would:
   - Install base upstream structure
   - Add 26 manuscript agents
   - Include `setup_review.py` script
   - Pre-configure for academic review workflow

3. **Update Command**:
   ```bash
   apm update --domain manuscript-review
   ```
   Updates both base framework and domain specialization

**Outcome**: Rigorous-APM becomes an official upstream domain extension

### Phase 3: Advanced Integration (Optional)
**Goal**: Deep integration with upstream ecosystem

**Actions**:
1. **Multi-Domain Support**: Enable mixing domains (e.g., manuscript-review + code-review)
2. **Domain Registry**: Publish rigorous-apm as installable domain package
3. **Custom Build Process**: Extend upstream's build.js for domain-specific bundles
4. **Version Compatibility**: Track upstream versions and domain compatibility

**Outcome**: Rigorous-APM becomes a first-class citizen in upstream ecosystem

## Immediate Next Steps

### Step 1: Update Core Agent Prompts
- [ ] Update `03-setup-agent/setup_agent_initiation_prompt.md` with upstream v0.5 patterns
- [ ] Update `04-manager-agent/manager_agent_initiation_prompt.md` with upstream patterns
- [ ] Add YAML frontmatter to all 26 Implementation Agents
- [ ] Update agent references to use upstream guide patterns

### Step 2: Integrate Upstream Guides
- [ ] Copy upstream guides to `rigorous-apm/06-guides/upstream/`
- [ ] Update `06-guides/README.md` to reference both upstream and manuscript guides
- [ ] Ensure all agent prompts reference correct guide paths

### Step 3: Enhance Automation
- [ ] Update `02-setup_review.py` to generate upstream-compatible artifacts
- [ ] Add metadata tracking (like upstream's `.apm/metadata.json`)
- [ ] Generate Bootstrap Prompts in upstream format

### Step 4: Documentation
- [ ] Update `01-START_HERE.md` to explain upstream relationship
- [ ] Create migration guide for existing rigorous-apm users
- [ ] Document differences between base upstream and manuscript specialization

## Key Principles

1. **Upstream First**: When upstream has a pattern, use it
2. **Specialize Minimally**: Only diverge where manuscript review requires it
3. **Contribute Back**: Submit improvements to upstream when applicable
4. **Maintain Compatibility**: Track upstream versions and update accordingly
5. **Preserve Automation**: Keep `02-setup_review.py` - it's a strength

## Benefits

**For Rigorous-APM Users**:
- Access to upstream improvements automatically
- Better documentation and community support
- Proven patterns for handovers, memory, task assignment
- Future CLI automation

**For Upstream-APM**:
- Real-world domain specialization example
- 26-agent coordination patterns
- Academic review use case
- Python automation patterns

**For Both**:
- Reduced maintenance burden
- Shared improvements
- Stronger ecosystem
- Clear specialization model

## Migration Path for Existing Projects

For users with active rigorous-apm reviews:

1. **Complete current reviews** with existing system
2. **New reviews** use updated upstream-compatible version
3. **Gradual adoption** - no forced migration
4. **Backward compatibility** maintained where possible

## Success Metrics

- [ ] All rigorous-apm agents use upstream patterns
- [ ] Setup/Manager agents reference upstream guides
- [ ] `02-setup_review.py` generates upstream-compatible artifacts
- [ ] Documentation clearly explains upstream relationship
- [ ] New manuscript reviews work seamlessly with updated system
- [ ] (Future) Rigorous-APM installable via `apm init --domain manuscript-review`

---

**Status**: Strategy defined, ready for Phase 1 implementation
**Owner**: guitarbeat
**Last Updated**: 2025-11-17
