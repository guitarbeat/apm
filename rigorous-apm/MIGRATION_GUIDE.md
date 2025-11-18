# Migration Guide: Legacy to Upstream-Integrated Rigorous APM

This guide helps you transition from legacy Rigorous APM to the upstream-integrated version built on upstream-apm v0.5 patterns.

---

## Overview

**What Changed**: Rigorous APM has been transformed from a parallel APM system into a domain-specific extension of upstream-apm v0.5. This integration adopts proven APM patterns while preserving all manuscript review capabilities.

**What Stayed the Same**: All 26 specialized agents, 3-phase parallel execution model, manuscript-specific analysis criteria, and Python automation remain fully functional.

**Migration Status**: 
- ✅ **Completed Reviews**: Legacy workspaces continue to function without changes
- ✅ **New Reviews**: Automatically use upstream-integrated version
- ⚠️ **In-Progress Reviews**: Can complete with legacy format; optional migration available

---

## Key Differences

### 1. Agent Prompt Structure

**Legacy Format**:
```markdown
# Section 1 Analysis Agent

You are a specialist agent...

## Your Task
Analyze the title and abstract...
```

**Upstream-Integrated Format**:
```markdown
---
priority: 3
command_name: section-1-title-abstract-analysis
description: Analyzes manuscript title and abstract for clarity, accuracy, and impact
agent_id: S1
domain: manuscript-review
---

# Section 1 Analysis Agent

You are a specialist agent...

## Guide References
- {GUIDE_PATH:upstream/Memory_Log_Guide.md}
```

**Impact**: Agents now have structured metadata and standardized guide references. Functionality is identical.

### 2. Setup Agent Workflow

**Legacy**: Ad-hoc context gathering and plan creation

**Upstream-Integrated**: 5-phase structured workflow
1. Context Synthesis (using `{GUIDE_PATH:upstream/Context_Synthesis_Guide.md}`)
2. Project Breakdown (using `{GUIDE_PATH:upstream/Project_Breakdown_Guide.md}`)
3. Review (with checkpoints)
4. Enhancement (refinement)
5. Bootstrap (generates Bootstrap Prompt with YAML frontmatter)

**Impact**: More systematic setup process with approval gates. Generates additional artifact (`Bootstrap_Prompt.md`).

### 3. Manager Agent Initialization

**Legacy**: Loads Implementation Plan directly

**Upstream-Integrated**: Processes Bootstrap Prompt with YAML frontmatter, then loads Implementation Plan
```yaml
---
workspace_root: "./review_workspace"
manuscript_type: "empirical"
target_outlet: "Nature"
research_field: "neuroscience"
---
```

**Impact**: Manager receives structured context upfront. Coordination logic unchanged.

### 4. Generated Artifacts

**Legacy**:
- `Implementation_Plan.md`
- `system_state.json` or `system_state.md`
- `agent_outputs/`

**Upstream-Integrated** (adds):
- `metadata.json` – APM version tracking and phase status
- `Bootstrap_Prompt.md` – YAML frontmatter for Manager initialization
- Enhanced `Implementation_Plan.md` with guide references

**Impact**: Additional metadata tracking. Legacy artifacts still generated.

### 5. Guide System

**Legacy**: All guides in `06-guides/`

**Upstream-Integrated**: 
- `06-guides/upstream/` – 7 core upstream guides
- `06-guides/` – Manuscript-specific guides (preserved)

**Impact**: More comprehensive guide coverage. All legacy guides remain accessible.

### 6. Guide Reference Syntax

**Legacy**: Plain text references or relative paths

**Upstream-Integrated**: Standardized `{GUIDE_PATH:filename.md}` syntax

**Impact**: Consistent reference pattern across all agents. Enables future tooling.

---

## Breaking Changes

### None for Existing Workflows

**Good News**: There are NO breaking changes for:
- Completed reviews (legacy workspaces remain functional)
- In-progress reviews (can complete with legacy format)
- Python automation script (backward compatible)

### Optional Adoption for New Features

**New Capabilities** (require upstream-integrated format):
- Structured metadata tracking (`metadata.json`)
- Bootstrap Prompt pattern for Manager initialization
- Guide reference resolution tooling (future)
- CLI integration with upstream-apm (future)

---

## Migration Paths

### Path 1: Complete In-Progress Reviews (No Migration)

**Best For**: Reviews already underway with legacy format

**Steps**:
1. Continue using existing workspace
2. No changes required
3. Complete review as normal

**Outcome**: Review completes successfully with legacy format

---

### Path 2: Start Fresh with Upstream-Integrated Format

**Best For**: New reviews starting after integration

**Steps**:
1. Run `02-setup_review.py` (automatically uses new format)
2. Launch Setup Agent with `03-setup-agent/setup_agent_initiation_prompt.md`
3. Setup Agent completes 5 phases and generates Bootstrap Prompt
4. Initialize Manager Agent with Bootstrap Prompt
5. Execute 26 Implementation Agents as normal

**Outcome**: Full upstream-integrated workflow with all new features

---

### Path 3: Migrate In-Progress Review (Optional)

**Best For**: In-progress reviews that want new metadata tracking

**Steps**:

1. **Backup existing workspace**
   ```bash
   cp -r manuscript_review/ manuscript_review_backup/
   ```

2. **Generate metadata.json**
   ```bash
   python 02-setup_review.py --manuscript manuscript.tex --generate-metadata-only
   ```
   (Note: This flag would need to be added to the script)

3. **Update agent prompts** (optional, for consistency)
   - Add YAML frontmatter to any custom agent prompts
   - Update guide references to use `{GUIDE_PATH:}` syntax

4. **Continue review**
   - Existing agents continue working
   - New metadata tracking available

**Outcome**: Hybrid approach with metadata tracking added

---

## Step-by-Step Migration for New Reviews

### Before You Start

- [ ] Read `rigorous-apm/01-START_HERE.md` (updated with upstream patterns)
- [ ] Review `06-guides/upstream/` to understand core APM patterns
- [ ] Ensure you have upstream-integrated version (check for `06-guides/upstream/` directory)

### Step 1: Workspace Setup

```bash
# Generate workspace with upstream-compatible artifacts
python 02-setup_review.py \
  --manuscript "/path/to/manuscript.tex" \
  --output-root "/path/to/reviews" \
  --non-interactive
```

**Verify**:
- [ ] `metadata.json` exists
- [ ] `Bootstrap_Prompt.md` exists
- [ ] `Implementation_Plan.md` contains guide references

### Step 2: Setup Agent (5-Phase Workflow)

1. Drag `03-setup-agent/setup_agent_initiation_prompt.md` into IDE
2. Setup Agent executes 5 phases:
   - Context Synthesis
   - Project Breakdown
   - Review
   - Enhancement
   - Bootstrap
3. Approve at each checkpoint gate

**Verify**:
- [ ] Setup Agent completed all 5 phases
- [ ] `Bootstrap_Prompt.md` generated with YAML frontmatter
- [ ] `Implementation_Plan.md` updated with manuscript specifics

### Step 3: Manager Agent Initialization

1. Drag `04-manager-agent/manager_agent_initiation_prompt.md` into IDE
2. Load Bootstrap Prompt: `/load file "Bootstrap_Prompt.md"`
3. Optionally load Implementation Plan: `/load file "Implementation_Plan.md"`
4. Manager confirms understanding of 26-agent coordination

**Verify**:
- [ ] Manager processed Bootstrap Prompt successfully
- [ ] Manager understands 3-phase parallel execution model
- [ ] Manager ready to create Task Assignment Prompts

### Step 4: Execute Implementation Agents

**Phase 1: Section Analysis (S1-S10)**
- Manager creates Task Assignment Prompts for all 10 agents
- Execute in parallel
- Each agent creates Memory Log

**Phase 2: Rigor + Writing (R1-R7, W1-W7)**
- Manager coordinates 14 agents in parallel
- Cross-reference with section findings
- Memory Logs document analysis

**Phase 3: QC → ES**
- Quality Control synthesizes all findings
- Executive Summary generates final report

**Verify**:
- [ ] All agents create Memory Logs following upstream format
- [ ] `metadata.json` updates phase status
- [ ] Deliverables in `agent_outputs/`

---

## Troubleshooting

### Issue: Setup Agent doesn't follow 5-phase pattern

**Cause**: Using legacy Setup Agent prompt

**Solution**: 
1. Verify you're using `03-setup-agent/setup_agent_initiation_prompt.md` from upstream-integrated version
2. Check file contains references to `{GUIDE_PATH:upstream/Context_Synthesis_Guide.md}`
3. Re-download latest version if needed

### Issue: Manager Agent doesn't recognize Bootstrap Prompt

**Cause**: Using legacy Manager Agent prompt

**Solution**:
1. Verify you're using `04-manager-agent/manager_agent_initiation_prompt.md` from upstream-integrated version
2. Check prompt mentions Bootstrap Prompt processing
3. Ensure Bootstrap Prompt has YAML frontmatter

### Issue: Implementation Agents don't create Memory Logs

**Cause**: Agents using legacy format without Memory Log guidance

**Solution**:
1. Verify agent prompts contain `{GUIDE_PATH:upstream/Memory_Log_Guide.md}` reference
2. Check `06-guides/upstream/Memory_Log_Guide.md` exists
3. Update agent prompts to include Memory Log section

### Issue: Guide references don't resolve

**Cause**: Missing upstream guides or incorrect path syntax

**Solution**:
1. Verify `06-guides/upstream/` directory exists with all 7 guides
2. Check guide reference syntax: `{GUIDE_PATH:filename.md}` (not `{GUIDE_PATH:upstream/filename.md}`)
3. System automatically resolves to correct directory

### Issue: metadata.json not generated

**Cause**: Using older version of `02-setup_review.py`

**Solution**:
1. Verify you have latest version of automation script
2. Check script contains metadata generation logic
3. Run script with `--force` to regenerate artifacts

### Issue: Existing review workspace incompatible

**Cause**: Trying to use upstream-integrated agents with legacy workspace

**Solution**:
1. Complete review with legacy format (no migration needed)
2. OR generate new workspace for upstream-integrated format
3. OR follow Path 3 migration steps above

---

## Validation Checklist

After migration, verify:

### Workspace Structure
- [ ] `metadata.json` exists with correct schema
- [ ] `Bootstrap_Prompt.md` has YAML frontmatter
- [ ] `Implementation_Plan.md` contains guide references
- [ ] `06-guides/upstream/` directory exists with 7 guides
- [ ] `agent_outputs/` directory ready for deliverables

### Agent Prompts
- [ ] Setup Agent follows 5-phase pattern
- [ ] Manager Agent processes Bootstrap Prompts
- [ ] Implementation Agents have YAML frontmatter
- [ ] All agents reference `{GUIDE_PATH:upstream/Memory_Log_Guide.md}`
- [ ] Guide reference syntax is consistent

### Workflow Execution
- [ ] Setup Agent completes all 5 phases with checkpoints
- [ ] Manager Agent initializes with Bootstrap Prompt
- [ ] Implementation Agents create Memory Logs
- [ ] 3-phase parallel execution works correctly
- [ ] Phase status updates in `metadata.json`

### Documentation
- [ ] `01-START_HERE.md` explains upstream relationship
- [ ] `03-review-kickoff/review_kickoff_prompt.md` updated
- [ ] `AGENTS.md` documents pattern adoption requirements
- [ ] All guide cross-links work correctly

---

## FAQ

### Q: Do I need to migrate existing reviews?

**A**: No. Legacy workspaces continue to function without changes. Migration is optional and only needed for new features.

### Q: What happens if I use legacy agents with new workspace?

**A**: Agents will function but won't leverage new features (metadata tracking, Bootstrap Prompts, structured Memory Logs). Mixing formats is not recommended.

### Q: Can I customize upstream patterns?

**A**: Yes, but maintain compatibility. Add manuscript-specific sections while preserving upstream structure (YAML frontmatter, guide references, Memory Log format).

### Q: Will future updates break my workflow?

**A**: No. Upstream-integrated format is designed for forward compatibility. Future upstream-apm updates will be adopted incrementally with migration guides.

### Q: How do I contribute improvements?

**A**: Follow guidelines in `AGENTS.md`. Ensure changes preserve both upstream patterns and manuscript specialization. Reference affected files in PRs.

### Q: What if I find bugs in upstream-integrated version?

**A**: Report issues with:
1. Affected component (Setup Agent, Manager Agent, specific Implementation Agent)
2. Expected vs actual behavior
3. Workspace artifacts (metadata.json, Bootstrap Prompt, Implementation Plan)
4. Steps to reproduce

### Q: Can I use upstream-apm CLI directly?

**A**: Not yet. Future Phase 2 integration will enable `apm init --domain manuscript-review`. Currently use `02-setup_review.py`.

### Q: Where can I learn more about upstream patterns?

**A**: Read guides in `06-guides/upstream/`:
- `Context_Synthesis_Guide.md` – Setup Agent Phase 1
- `Implementation_Plan_Guide.md` – Plan structure
- `Memory_Log_Guide.md` – Documentation format
- `Memory_System_Guide.md` – Persistent state
- `Task_Assignment_Guide.md` – Manager-to-Implementation handoff

---

## Support

- **Documentation**: `rigorous-apm/01-START_HERE.md`, `06-guides/README.md`
- **Integration Details**: `INTEGRATION_STRATEGY.md`, `.kiro/specs/upstream-integration-plan/`
- **Contribution Guidelines**: `AGENTS.md`
- **Upstream Reference**: `upstream-apm/README.md`, `upstream-apm/docs/Workflow_Overview.md`

---

## Version History

- **v1.0.0** (Upstream-Integrated): Adopted upstream-apm v0.5 patterns, added metadata tracking, Bootstrap Prompts, structured Memory Logs
- **v0.x.x** (Legacy): Original parallel APM implementation with 26 agents

---

*Last Updated: 2025-11-17*
