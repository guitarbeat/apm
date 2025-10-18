# Memory System Guide

This guide defines the canonical data structures for the memory system used in the Rigorous APM framework.

## 1. The System State File

This file is the **single source of truth** for the entire state of the review project. It is created by the `02-setup_review.py` helper and is continuously updated by the `Manager Agent` after every action.

You can generate the system state in either JSON or Markdown format depending on your downstream tooling needs. Both versions contain the same information. Pass `--system-state-format markdown` (or omit the flag for JSON) when running `02-setup_review.py` to choose the initial file type.

### JSON Format (`system_state.json`)

Optimized for automation, scripting, and direct ingestion by other tools.

```json
{
  "manuscript_context": {
    "title": "String",
    "target_outlet": "String",
    "current_stage": "String"
  },
  "review_progress": {
    "current_phase": "String",
    "completed_agents": ["String (Agent ID)"],
    "pending_agents": ["String (Agent ID)"]
  },
  "agent_outputs_summary": {
    "s1": {
      "status": "completed",
      "overall_score": 4.5
    },
    "s2": {
      "status": "pending",
      "overall_score": null
    }
  },
  "last_action": "String (A description of the last action taken by the Manager Agent)"
}
```

### Markdown Format (`system_state.md`)

Optimized for quick human scanning in plain-text editors, Git diffs, or documentation bundles.

```markdown
# System State

## Manuscript Context
- **Title:** String
- **Target outlet:** String
- **Current stage:** String

## Review Progress
- **Current phase:** String
- **Completed agents:**
  - String (Agent ID)
- **Pending agents:**
  - String (Agent ID)

## Agent Outputs Summary
- **s1:** Status completed; overall_score 4.5
- **s2:** Status pending; overall_score null

## Last Action
String (A description of the last action taken by the Manager Agent)
```

## 2. The `agent_outputs/` Directory

This directory contains the detailed markdown output from each `Implementation Agent`. Each file is named after the agent's ID (e.g., `s1.md`).

While the system state file provides a summary of the agent outputs, these files contain the full, detailed analysis.

## 4. Standard Agent Output Markdown Schema

Each markdown file in the `agent_outputs/` directory should follow this structure:

```markdown
# [Agent Name] Analysis

## 1. Overall Assessment
- **Score:** [1-5 scale]
- **Confidence:** [1-5 scale]
- **Summary:** [A brief, one-sentence summary of the overall assessment.]

## 2. Key Findings
- [A bulleted list of the most important findings.]

## 3. Recommendations
- [A bulleted list of specific, actionable recommendations.]

## 4. Critical Issues
- [A bulleted list of any critical issues that must be addressed.]

## 5. Detailed Scores
- **[Metric 1]:** [1-5 scale]
- **[Metric 2]:** [1-5 scale]
```
