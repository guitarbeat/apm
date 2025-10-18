# APM Guides Directory

This directory contains comprehensive documentation for understanding and customizing the APM framework.

## Guide Navigation

### For New Users

**Start here**: `Agent_Cheat_Sheet.md`
- Quick reference for all 26 specialized agents
- Overview of agent categories and responsibilities
- Perfect for understanding the agent team structure

### For Understanding APM Architecture

**Read**: `Context_and_Prompt_Engineering_Guide.md`
- Deep dive into APM's design principles
- Context engineering: operational boundaries and workflows
- Prompt engineering: Markdown formatting and YAML frontmatter
- Meta-prompts and dynamic asset generation
- Guidance on JSON vs. Markdown system state outputs

**Why read this**: Understanding these principles helps you diagnose issues, optimize workflows, and make informed customization decisions.

### For Customizing APM

**Read**: `Customization_Guide.md`
- Practical instructions for adapting APM to your needs
- Domain-specific customization examples (web dev, data science, mobile, ML)
- MCP tool integration for enhanced capabilities
- Custom delegation guide creation
- Best practices for version management and team distribution

**Why read this**: This guide provides concrete examples and step-by-step instructions for tailoring APM to your specific project requirements.

### For IDE and AI Assistant Integration

**Read**: `IDE_and_AI_Assistant_Guide.md`
- Universal integration baseline plus selection heuristics for Cursor, Kiro, VS Code, and Gemini
- Setup checklists, operate loops, and abstract thinking cues for each environment
- Guidance for keeping `system_state.*` and `handover.md` synchronized while context-switching

**Why read this**: Apply the playbooks to choose the right tool for the moment, then drive deliberate agent delegation inside that IDE or assistant.

### For Understanding State Management

**Read**: `Memory_System_Guide.md`
- Data structures for project state tracking
- System state file (`system_state.json` or `.md`) schema and usage
- Agent output format specifications
- Memory log conventions

**Why read this**: Essential for understanding how APM maintains project state and coordinates between agents.

### For Context Transfer

**Read**: `Handover_Guide.md`
- Context transfer protocols between agent sessions
- When and how to perform handovers
- Maintaining continuity across sessions

**Why read this**: Critical for managing long-running projects that exceed single session context windows.

## Recommended Reading Order

### Quick Start Path
1. `Agent_Cheat_Sheet.md` - Understand the agent team
2. `Memory_System_Guide.md` - Learn state management basics
3. Start using APM with the main `START_HERE.md`

### Deep Understanding Path
1. `Agent_Cheat_Sheet.md` - Agent overview
2. `Context_and_Prompt_Engineering_Guide.md` - Architecture principles
3. `Memory_System_Guide.md` - State management
4. `Handover_Guide.md` - Session continuity
5. `Customization_Guide.md` - Adaptation techniques

### Customization Path
1. `Agent_Cheat_Sheet.md` - Understand existing structure
2. `Customization_Guide.md` - Learn customization techniques
3. `Context_and_Prompt_Engineering_Guide.md` - Understand design principles (reference as needed)
4. `Memory_System_Guide.md` - Understand state implications (reference as needed)

## Guide Relationships

```
Context_and_Prompt_Engineering_Guide.md
    ↓ (explains principles behind)
Customization_Guide.md
    ↓ (provides practical examples for)
Your Custom APM Implementation
    ↓ (uses)
Memory_System_Guide.md + Handover_Guide.md
    ↓ (for managing)
Agent Coordination and State
```

## Quick Reference

- **Agent list**: `Agent_Cheat_Sheet.md`
- **Why APM works this way**: `Context_and_Prompt_Engineering_Guide.md`
- **How to customize**: `Customization_Guide.md`
- **State management**: `Memory_System_Guide.md`
- **Session continuity**: `Handover_Guide.md`

---

**All guides are designed to be read independently, but cross-reference each other for deeper understanding.**
