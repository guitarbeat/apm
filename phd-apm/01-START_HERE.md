# PhD APM - Start Here

Academic manuscript review system with 26 specialized agents, built on upstream-apm v0.5.

**Status**: ✅ Production Ready (Nov 2025)

## Audience Legend

- **👤** Human-only – Read or execute yourself
- **🤖** Agent-ready – Paste directly into AI agent/IDE
- **🔁** Shared – Human triggers, agent consumes

---

## Architecture

PhD APM extends [upstream-apm v0.5](../upstream-apm/README.md) with manuscript review specialization:

- **26 agents**: S1-S10 (sections), R1-R7 (rigor), W1-W7 (writing), QC, ES
- **3-phase execution**: Section → Rigor+Writing → QC→ES
- **Upstream patterns**: 5-phase Setup, Bootstrap Prompts, Memory System, guide references
- **Automation**: `02-setup_review.py` generates upstream-compatible artifacts

See [integration spec](../.kiro/specs/upstream-integration-plan/) for details.

---

## Quick Start

### 1. Bootstrap Workspace (👤)

```bash
python 02-setup_review.py --manuscript "/path/to/manuscript.tex" --non-interactive
```

**Key flags**:
- `--output-root DIR` – Custom output location
- `--copy-manuscript` – Stage support files
- `--system-state-format markdown` – Use MD instead of JSON
- `--force` – Overwrite existing files

**Generates**: `metadata.json`, `Implementation_Plan.md`, `Manager_Bootstrap_Prompt.md`, `system_state.json`, `agent_outputs/`

### 2. Launch Setup Agent (🤖)

Drag `03-setup-agent/setup_agent_initiation_prompt.md` into your IDE. The agent will:
1. Gather manuscript context
2. Create 5-phase review plan
3. Generate Bootstrap Prompt for Manager

### 3. Initialize Manager Agent (🤖)

Drag `04-manager-agent/manager_agent_initiation_prompt.md` into IDE, then load `Manager_Bootstrap_Prompt.md`. Manager coordinates 26 agents through 3 phases:
- **Phase 1**: Section Analysis (S1-S10)
- **Phase 2**: Rigor (R1-R7) + Writing (W1-W7)
- **Phase 3**: QC → ES

### 4. Monitor & Collect (🔁)

- Track: `agent_outputs/`, `metadata.json`
- Review: `quality_control`, `executive_summary` deliverables

---

## Directory Structure

```
phd-apm/
├── 01-START_HERE.md              # 👤 This file
├── 02-setup_review.py            # 🔁 Workspace generator
├── 03-setup-agent/               # 🤖 Setup Agent
├── 04-manager-agent/             # 🤖 Manager Agent
├── 05-implementation-agents/     # 🤖 26 specialist agents
│   ├── section/                  # S1-S10
│   ├── rigor/                    # R1-R7
│   ├── writing/                  # W1-W7
│   └── [QC, ES]                  # Quality Control, Executive Summary
└── 06-guides/                    # 👤/🔁 Domain-specific guides
```

---

## Reference Guides

**Upstream guides** (`../upstream-apm/prompts/guides/`): Core APM patterns
- Implementation_Plan_Guide.md
- Memory_Log_Guide.md
- Memory_System_Guide.md
- Project_Breakdown_Guide.md
- Task_Assignment_Guide.md

**Domain guides** (`06-guides/`): Manuscript review specialization
- Context_and_Prompt_Engineering_Guide.md
- Customization_Guide.md
- Handover_Guide.md
- IDE_and_AI_Assistant_Guide.md
- Manuscript_Review_Implementation_Plan_Guide.md
- Memory_System_Guide.md
- Troubleshooting_Playbook.md

**Note**: Agents reference guides using `{GUIDE_PATH:filename.md}` syntax, resolved at runtime by your AI IDE.

---

## Integration Status

Upstream-apm v0.5 integration complete (Nov 2025):
- All 26 agents use YAML frontmatter and upstream patterns
- Automation generates upstream-compatible artifacts
- End-to-end validation passed
- No breaking changes to manuscript review workflow

See [integration spec](../.kiro/specs/upstream-integration-plan/) for complete details.

---

## Troubleshooting

**Version issues**: Ensure `../upstream-apm/` repository present with v0.5.0+

**Missing guides**: Check `../upstream-apm/prompts/guides/` (upstream) and `06-guides/` (domain)

**Artifact problems**: Run with `--force`, verify `metadata.json` version string

**Coordination issues**: Verify Bootstrap Prompt loaded, check Implementation Plan has all 26 agents

**Agent errors**: See `06-guides/Troubleshooting_Playbook.md` for runtime debugging
