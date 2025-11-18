# Agentic Project Management (APM) Monorepo

This repository hosts two complementary Agentic Project Management systems:

- **`rigorous-apm/`** – A domain-specific extension of upstream-apm v0.5 for academic manuscript review, featuring 26 specialized agents and Python automation.
- **`upstream-apm/`** – The v0.5 reference implementation providing foundational APM patterns for general-purpose multi-agent project coordination.

**Architecture**: Rigorous APM extends upstream-apm's core patterns (5-phase Setup, Bootstrap Prompts, Memory System, Task Assignment protocol) with manuscript review specialization (26-agent coordination, 3-phase parallel execution, academic analysis criteria).

Use this README to pick the right starting point and keep both tracks aligned as you contribute updates.

---

## Choose Your Starting Point

| If you need… | Start with… | Why it matters |
| --- | --- | --- |
| **Rigorous APM (Manuscript Review)** | | |
| Quick start for manuscript review | [`rigorous-apm/01-START_HERE.md`](rigorous-apm/01-START_HERE.md) | Explains upstream relationship, 5-phase Setup workflow, 26-agent coordination, and end-to-end review process. |
| CLI automation for review workspace | [`rigorous-apm/02-setup_review.py`](rigorous-apm/02-setup_review.py) | Generates upstream-compatible artifacts: `metadata.json`, `Bootstrap_Prompt.md`, `Implementation_Plan.md` with guide references. |
| Kickoff prompts for Setup & Manager | [`rigorous-apm/03-review-kickoff/`](rigorous-apm/03-review-kickoff/) | Drag-and-drop prompts following upstream patterns for both Setup and Manager agents. |
| Guide navigation (upstream + domain) | [`rigorous-apm/06-guides/README.md`](rigorous-apm/06-guides/README.md) | Maps to both upstream core guides and manuscript-specific guides. |
| Migration from legacy version | [`rigorous-apm/MIGRATION_GUIDE.md`](rigorous-apm/MIGRATION_GUIDE.md) | Step-by-step migration instructions, breaking changes, troubleshooting. |
| **Upstream APM (Foundation)** | | |
| Framework overview | [`upstream-apm/README.md`](upstream-apm/README.md) | Introduces v0.5 terminology, onboarding paths, and documentation legend. |
| Detailed workflow walkthrough | [`upstream-apm/docs/Workflow_Overview.md`](upstream-apm/docs/Workflow_Overview.md) | Canonical protocols, rituals, and shared-state expectations. |
| Schema definitions & validation | [`upstream-apm/prompts/schemas/`](upstream-apm/prompts/schemas/) | JSON schema assets plus `validate_schema.py` for structured prompts. |
| **Integration & Contribution** | | |
| Integration strategy & architecture | [`INTEGRATION_STRATEGY.md`](INTEGRATION_STRATEGY.md) | Technical approach for upstream-rigorous integration. |
| Contribution guidelines | [`AGENTS.md`](AGENTS.md) | Pattern adoption requirements, validation checklist, commit guidance. |
| Implementation plan & design | [`.kiro/specs/upstream-integration-plan/`](.kiro/specs/upstream-integration-plan/) | Requirements, design, and task breakdown for integration. |

---

## Contribution Checklist

1. **Stay consistent with the audience legend.** The 👤/🤖/🔁 icons appear across both systems—reuse them in new assets and mention when automation updates the legend automatically.

2. **Follow upstream pattern adoption requirements** (for Rigorous APM):
   - Add YAML frontmatter to Implementation Agent prompts (priority, command_name, description, agent_id, domain)
   - Use `{GUIDE_PATH:filename.md}` syntax for guide references
   - Reference `{GUIDE_PATH:upstream/Memory_Log_Guide.md}` for documentation format
   - Document execution type (single-step vs multi-step)
   - Include debug delegation protocol and handover awareness
   - See `AGENTS.md` for full checklist

3. **Call out affected paths.** When you change prompts or helpers, reference the exact file or directory so other operators can locate them quickly.

4. **Run targeted tests.**
   - For Rigorous APM scripts, execute any impacted command (for example `python rigorous-apm/02-setup_review.py --help`)
   - For upstream Python modules or schemas, run `pytest` from the repo root and `python upstream-apm/prompts/schemas/validate_schema.py --help` after schema changes
   - Verify YAML frontmatter in updated agent prompts
   - Test guide reference resolution

5. **Document cross-links.** If you add or rename assets, update the relevant navigation table—`rigorous-apm/06-guides/README.md` or this file—so maintainers can discover your work.

6. **Preserve domain specialization.** When adopting upstream patterns in Rigorous APM, maintain manuscript-specific analysis criteria and 26-agent coordination model.

---

## Repository Layout

```
README.md                         # This orientation guide
AGENTS.md                         # Contribution guidelines & pattern adoption requirements
INTEGRATION_STRATEGY.md           # Technical integration approach

rigorous-apm/                     # Manuscript review domain extension
├── 01-START_HERE.md              # Operator onboarding (upstream-integrated workflow)
├── 02-setup_review.py            # Python automation (generates upstream artifacts)
├── 03-review-kickoff/            # Kickoff prompts (upstream patterns)
├── 03-setup-agent/               # Setup Agent (5-phase upstream workflow)
├── 04-manager-agent/             # Manager Agent (Bootstrap Prompt processing)
├── 05-implementation-agents/     # 26 specialist agents (YAML frontmatter)
│   ├── implementation_agent_base_prompt.md  # Base template
│   ├── section/                  # S1-S10 section analysis
│   ├── rigor/                    # R1-R7 scientific rigor
│   ├── writing/                  # W1-W7 writing quality
│   └── [QC, ES agents]           # Quality Control & Executive Summary
├── 06-guides/                    # Guide system
│   ├── upstream/                 # 7 core upstream-apm guides
│   └── [domain guides]           # Manuscript-specific guides
└── MIGRATION_GUIDE.md            # Legacy to upstream-integrated migration

upstream-apm/                     # Upstream APM v0.5 foundation
├── README.md                     # Upstream overview and documentation index
├── docs/                         # Workflow guides and protocols
├── prompts/                      # Prompt bundles, schemas, and templates
└── [CLI, templates, tests]       # Infrastructure components

.kiro/specs/upstream-integration-plan/  # Integration specification
├── requirements.md               # Integration requirements
├── design.md                     # Architecture & component design
└── tasks.md                      # Implementation task breakdown
```

Need a refresher on either system? Jump back to the table above and follow the linked files for deep dives.
