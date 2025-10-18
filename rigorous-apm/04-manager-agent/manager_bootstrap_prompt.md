# Manager Agent Bootstrap

## System State

```json
{
  "manuscript_context": {
    "title": "A Low-Cost, Open-Source, Two-Photon Microscope for In Vivo Imaging",
    "target_outlet": "Internal Department Review",
    "current_stage": "Draft"
  },
  "review_progress": {
    "current_phase": "Phase 1: Section Analysis",
    "completed_agents": [],
    "pending_agents": ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10"]
  },
  "agent_outputs_summary": {},
  "last_action": "Setup complete. Ready to begin Phase 1."
}
```

## Implementation Plan (Phase 1 Only)

### Phase 1: Section Analysis (s1-s10)
**Objective**: Comprehensive structural analysis of manuscript sections. Your primary focus should be on the "Research Strategy" section.

**Tasks:**
- Task 1.1: Title & Keywords Analysis │ section_s1
- Task 1.2: Abstract Analysis │ section_s2
- Task 1.3: Introduction Analysis │ section_s3
- Task 1.4: Literature Review Analysis │ section_s4
- Task 1.5: Methodology Analysis │ section_s5
- Task 1.6: Results Analysis │ section_s6
- Task 1.7: Discussion Analysis │ section_s7
- Task 1.8: Conclusion Analysis │ section_s8
- Task 1.9: References Analysis │ section_s9
- Task 1.10: Supplementary Materials Analysis │ section_s10

**Dependencies**: All section agents can run in parallel.

## Next Steps
1.  Review the system state file (`system_state.json` by default, `system_state.md` when Markdown output is selected) and the `Implementation Plan`. The review workspace helper sets the starting format through `--system-state-format`.
2.  Begin Phase 1: Section Analysis coordination by executing the 10 section agents.
3.  Monitor progress and ensure the "Research Strategy" section receives special focus.
4.  Update the system state file after each agent completes its task.
5.  Deliver the consolidated analysis reports.
