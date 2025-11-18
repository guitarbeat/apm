# Agent Guidelines

This repository hosts two complementary Agentic Project Management (APM) systems. Every change should improve one or both of these systems while keeping their goals aligned.

## Upstream Integration Approach

**PhD APM is a domain-specific extension of upstream-apm v0.5.** This means:

- **Foundation + Specialization Architecture**: PhD APM adopts upstream's core patterns (5-phase Setup, Bootstrap Prompts, Memory System, Task Assignment protocol) and extends them with manuscript review specialization (26 agents, 3-phase parallel execution, academic criteria).
- **Pattern Adoption Requirements**: All agent prompts must follow upstream v0.5 patterns:
  - YAML frontmatter with metadata (priority, command_name, description, agent_id, domain)
  - Guide references using `{GUIDE_PATH:filename.md}` syntax
  - Memory Log format following `{GUIDE_PATH:upstream/Memory_Log_Guide.md}`
  - Execution type documentation (single-step vs multi-step)
  - Debug delegation protocol and handover awareness
- **Shared Guide System**: Upstream's 7 core guides live in `phd-apm/06-guides/upstream/` alongside manuscript-specific guides in `phd-apm/06-guides/`. Both sets are referenced by agents.
- **Artifact Compatibility**: Generated artifacts (metadata.json, Implementation Plans, Bootstrap Prompts) follow upstream formats to enable future CLI integration.

See [INTEGRATION_STRATEGY.md](INTEGRATION_STRATEGY.md) and `.kiro/specs/upstream-integration-plan/` for full technical details.

## Shared Expectations
- Follow the existing file organization; document any renames of the top-level `phd-apm/` or `upstream-apm/` directories so collaborators can update scripts accordingly.
- Keep instructions actionable for agent operators and contributors. When you add or edit guidance, mention the relevant file path so readers can navigate quickly.
- Prefer incremental updates that maintain compatibility with existing prompts, automation snippets, and scaffolding scripts.
- Run targeted checks (unit tests, schema validation, linting, or dry-run scripts) whenever you touch executable assets. Documentation-only updates do not require tests.

## PhD APM (`phd-apm/`)

### Workflow Preservation
- Preserve the onboarding flow described in `phd-apm/01-START_HERE.md`. Updates should clarify how to launch or coordinate the 26 specialist agents without introducing breaking workflow changes.
- Maintain the 3-phase parallel execution model: Section (S1-S10) → Rigor (R1-R7) + Writing (W1-W7) → QC → ES.
- Preserve manuscript-specific analysis criteria and domain specialization in all Implementation Agent prompts.

### Automation & Artifacts
- When modifying `02-setup_review.py`, ensure the helper generates upstream-compatible artifacts (metadata.json, Bootstrap Prompts with YAML frontmatter, Implementation Plans with guide references).
- Provide example invocations that cover new flags or behaviors.
- Validate that generated artifacts follow upstream v0.5 format specifications.

### Prompt Compatibility
- Prompts inside `03-` through `05-` directories must follow upstream v0.5 patterns:
  - **YAML Frontmatter**: All Implementation Agent prompts require frontmatter with: priority, command_name, description, agent_id, domain
  - **Guide References**: Use `{GUIDE_PATH:filename.md}` syntax for all guide references
  - **Execution Patterns**: Document whether agent uses single-step or multi-step execution
  - **Memory Logging**: Reference `{GUIDE_PATH:upstream/Memory_Log_Guide.md}` for documentation format
- Keep JSON or `.apm` snippets free of trailing spaces and ready for copy/paste.
- Ensure prompts remain interoperable with IDE drag-and-drop workflows.

### Guide System
- Guides under `06-guides/` must cross-link to any newly added artifacts so the training loop stays comprehensive.
- Maintain separation between upstream guides (`06-guides/upstream/`) and manuscript-specific guides (`06-guides/`).
- When adding new guides, update `06-guides/README.md` navigation.
- Ensure guide references resolve correctly to either upstream or domain-specific paths.

### Base Template Usage
- Use `05-implementation-agents/implementation_agent_base_prompt.md` as the reference template when creating or updating Implementation Agent prompts.
- The base template documents all required upstream patterns and manuscript specialization sections.
- Ensure consistency across all 26 Implementation Agents (S1-S10, R1-R7, W1-W7, QC, ES).

## Upstream APM (`upstream-apm/`)
- Align edits with the terminology used in `upstream-apm/docs/Workflow_Overview.md` and the root `README.md` to keep the upstream documentation internally consistent.
- When adjusting schema or validation utilities in `upstream-apm/prompts/schemas/`, verify that `python upstream-apm/prompts/schemas/validate_schema.py --help` succeeds and document any new arguments.
- Maintain backwards-compatible prompt structures under `upstream-apm/prompts/` so existing projects can ingest updates without retooling.
- Keep test coverage current: run `pytest` from the repository root after changing Python modules or prompt schemas within `upstream-apm/` tree.

## Pattern Adoption Checklist

When updating or creating agent prompts in PhD APM, verify:

- [ ] YAML frontmatter includes all required fields (priority, command_name, description, agent_id, domain)
- [ ] Guide references use `{GUIDE_PATH:filename.md}` syntax
- [ ] Memory Log references point to `{GUIDE_PATH:upstream/Memory_Log_Guide.md}`
- [ ] Execution type is documented (single-step vs multi-step)
- [ ] Debug delegation protocol is included
- [ ] Handover awareness section is present
- [ ] Manuscript-specific analysis criteria are preserved
- [ ] Domain specialization sections are maintained
- [ ] Prompt follows structure from `implementation_agent_base_prompt.md`

## Commit & PR Guidance
- Reference affected files or directories in commit messages and PR descriptions.
- Summaries should call out whether the change benefits PhD APM, Upstream APM, or both.
- For PhD APM changes, note whether upstream patterns were adopted or preserved.
- Include validation results (e.g., "Verified YAML frontmatter in all updated agents").
