# Memory System Guide

This guide defines the canonical data structures for the memory system used in the Rigorous APM framework.

## 1. The `system_state.json` File

This file is the **single source of truth** for the entire state of the review project. It is created by the `02-setup_review.sh` script and is continuously updated by the `Manager Agent` after every action.

By consolidating the state into a single file, we make it much easier for an LLM agent to quickly and accurately understand the current state of the review.

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

## 2. The `agent_outputs/` Directory

This directory contains the detailed markdown output from each `Implementation Agent`. Each file is named after the agent's ID (e.g., `s1.md`).

While the `system_state.json` file provides a summary of the agent outputs, these files contain the full, detailed analysis.

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
