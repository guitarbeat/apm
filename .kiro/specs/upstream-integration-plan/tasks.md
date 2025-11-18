# Implementation Plan

- [x] 1. Establish upstream guide foundation





  - Copy 7 core guides from upstream-apm to phd-apm/06-guides/upstream/
  - Update 06-guides/README.md with navigation for both upstream and manuscript-specific guides
  - Verify all guide files are properly formatted and readable
  - _Requirements: 1.2, 4.1, 4.2, 4.3, 4.4, 4.5_
-

- [x] 2. Update Setup Agent to upstream v0.5 patterns



  - Read upstream's Setup_Agent_Initiation_Prompt.md to understand pattern structure
  - Rewrite 03-setup-agent/setup_agent_initiation_prompt.md with 5-phase structure
  - Implement guide reference pattern using {GUIDE_PATH:filename.md} syntax
  - Add manuscript-specific Context Synthesis questions
  - Include checkpoint/approval gates between phases
  - Implement Bootstrap Prompt generation in upstream YAML format
  - _Requirements: 1.1, 1.2, 2.4, 9.1, 9.2, 9.3, 9.4, 9.5_




- [ ] 3. Update Manager Agent to upstream coordination patterns

  - Read upstream's Manager_Agent_Initiation_Prompt.md for pattern reference
  - Rewrite 04-manager-agent/manager_agent_initiation_prompt.md with YAML frontmatter
  - Implement Bootstrap Prompt processing pattern
  - Adopt upstream guide references using {GUIDE_PATH:} syntax
  - Preserve 3-phase parallel execution model (Section→Rigor+Writing→QC→ES)
  - Document 26-agent coordination strategy




  - Update 04-manager-agent/manager_bootstrap_prompt.md template
  - _Requirements: 1.1, 1.2, 1.4, 2.3, 7.1, 7.2, 7.3, 7.4_

- [ ] 4. Create Implementation Agent base template

  - Read upstream's Implementation_Agent_Initiation_Prompt.md for patterns
  - Create 05-implementation-agents/implementation_agent_base_prompt.md
  - Include YAML frontmatter structure with all required fields



  - Document execution patterns (single-step vs multi-step)


  - Reference upstream Memory Log Guide
  - Include debug delegation protocol
  - Add manuscript-specific sections for domain specialization
  - Document how to use base template for agent specialization
  - _Requirements: 1.3, 7.1, 7.2, 7.3, 7.4, 7.5_



- [ ] 5. Update Section Analysis Agents (S1-S10)

- [ ] 5.1 Update agents S1-S5 with upstream patterns
  - Add YAML frontmatter with metadata (priority, command_name, description, agent_id, domain)
  - Adopt upstream execution patterns from base template
  - Reference upstream Memory Log Guide using {GUIDE_PATH:}


  - Preserve manuscript-specific analysis criteria
  - Update all guide references to use correct paths
  - _Requirements: 1.3, 1.5, 2.1, 2.2, 7.1, 7.2_







- [ ] 5.2 Update agents S6-S10 with upstream patterns
  - Add YAML frontmatter with metadata
  - Adopt upstream execution patterns from base template
  - Reference upstream Memory Log Guide
  - Preserve manuscript-specific analysis criteria


  - Update all guide references
  - _Requirements: 1.3, 1.5, 2.1, 2.2, 7.1, 7.2_

- [ ] 5.3 Verify consistency across all Section agents
  - Review all 10 agents for consistent structure
  - Validate YAML frontmatter completeness


  - Check guide reference syntax
  - Ensure analysis criteria preservation
  - _Requirements: 2.1, 2.2, 7.1_





- [ ] 6. Update Rigor Analysis Agents (R1-R7)

- [ ] 6.1 Update agents R1-R4 with upstream patterns
  - Add YAML frontmatter with metadata
  - Adopt upstream execution patterns
  - Reference upstream Memory Log Guide


  - Preserve scientific rigor criteria
  - Update guide references
  - _Requirements: 1.3, 1.5, 2.1, 2.2, 7.1, 7.2_

- [ ] 6.2 Update agents R5-R7 with upstream patterns
  - Add YAML frontmatter with metadata


  - Adopt upstream execution patterns
  - Reference upstream Memory Log Guide
  - Preserve scientific rigor criteria
  - Update guide references



  - _Requirements: 1.3, 1.5, 2.1, 2.2, 7.1, 7.2_



- [ ] 6.3 Verify consistency across all Rigor agents
  - Review all 7 agents for consistent structure
  - Validate YAML frontmatter completeness
  - Check guide reference syntax
  - Ensure rigor criteria preservation


  - _Requirements: 2.1, 2.2, 7.1_

- [ ] 7. Update Writing Analysis Agents (W1-W7)


- [ ] 7.1 Update agents W1-W4 with upstream patterns
  - Add YAML frontmatter with metadata


  - Adopt upstream execution patterns
  - Reference upstream Memory Log Guide
  - Preserve writing quality criteria
  - Update guide references
  - _Requirements: 1.3, 1.5, 2.1, 2.2, 7.1, 7.2_



- [ ] 7.2 Update agents W5-W7 with upstream patterns
  - Add YAML frontmatter with metadata
  - Adopt upstream execution patterns
  - Reference upstream Memory Log Guide


  - Preserve writing quality criteria
  - Update guide references
  - _Requirements: 1.3, 1.5, 2.1, 2.2, 7.1, 7.2_

- [x] 7.3 Verify consistency across all Writing agents


  - Review all 7 agents for consistent structure
  - Validate YAML frontmatter completeness
  - Check guide reference syntax
  - Ensure writing criteria preservation


  - _Requirements: 2.1, 2.2, 7.1_

- [ ] 8. Update Quality Control and Executive Summary Agents







- [ ] 8.1 Update Quality Control Agent
  - Add YAML frontmatter with metadata
  - Adopt upstream execution patterns
  - Document synthesis methodology
  - Reference upstream guides using {GUIDE_PATH:}



  - Preserve QC synthesis pattern
  - _Requirements: 1.3, 1.5, 2.1, 2.3, 7.1, 7.2_



- [ ] 8.2 Update Executive Summary Agent
  - Add YAML frontmatter with metadata
  - Adopt upstream execution patterns
  - Document reporting structure


  - Reference upstream guides
  - Preserve ES generation pattern
  - _Requirements: 1.3, 1.5, 2.1, 2.3, 7.1, 7.2_

- [x] 9. Enhance Python automation script



- [x] 9.1 Add metadata.json generation






  - Implement JSON structure with APM version tracking
  - Include manuscript metadata fields
  - Add phase status tracking
  - Validate JSON schema on generation
  - _Requirements: 3.1, 3.5_

- [x] 9.2 Update Implementation Plan generation


  - Use upstream format for plan structure
  - Reference upstream guides with correct paths
  - Include manuscript-specific sections
  - Preserve 5-phase review workflow


  - _Requirements: 3.2, 3.4_

- [ ] 9.3 Update Bootstrap Prompt generation
  - Match upstream YAML frontmatter format
  - Include workspace_root, manuscript_type, target_outlet metadata


  - Reference correct guide paths
  - Document 26-agent coordination strategy
  - _Requirements: 3.3, 3.4, 9.1, 9.2, 9.3, 9.4, 9.5_



- [ ] 9.4 Add version compatibility checking
  - Track upstream-apm version
  - Track phd-apm version
  - Validate compatibility on script execution
  - _Requirements: 3.1, 3.5_

- [ ] 9.5 Test automation script with sample manuscript
  - Execute script with test parameters
  - Verify all artifacts generated correctly
  - Validate metadata.json structure
  - Check guide references in generated files
  - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5_

- [ ] 10. Update documentation

- [ ] 10.1 Update 01-START_HERE.md
  - Explain upstream-apm relationship
  - Document new workflow with upstream patterns
  - Update quick start guide
  - Reference upstream guides appropriately
  - _Requirements: 6.1, 6.2_

- [ ] 10.2 Update review kickoff documentation
  - Update 03-review-kickoff/review_kickoff_prompt.md with upstream patterns
  - Update guide references
  - Preserve automation snippets (.apm files)
  - _Requirements: 1.2, 6.2_

- [ ] 10.3 Update AGENTS.md
  - Document upstream integration approach
  - Update contribution guidelines
  - Explain pattern adoption requirements
  - _Requirements: 6.4_

- [ ] 10.4 Create migration guide
  - Document differences between legacy and upstream-integrated versions
  - Provide step-by-step migration instructions
  - Include troubleshooting section
  - Document breaking changes
  - _Requirements: 5.3, 5.4, 6.3_

- [ ] 10.5 Update root README.md
  - Reflect upstream integration in project description
  - Update architecture overview
  - Add links to upstream-apm documentation
  - _Requirements: 6.5_

- [ ] 11. Validate integration end-to-end

- [ ] 11.1 Execute complete workflow test
  - Run 02-setup_review.py with test manuscript
  - Launch Setup Agent and complete 5 phases
  - Bootstrap Manager Agent with generated prompt
  - Execute sample tasks for each agent type (S, R, W, QC, ES)
  - Verify Memory Log creation and format
  - Check artifact generation completeness
  - _Requirements: 8.1, 10.1, 10.2, 10.3, 10.4, 10.5_

- [ ] 11.2 Validate guide references
  - Test all {GUIDE_PATH:} references resolve correctly
  - Verify relative path handling
  - Check for broken links in documentation
  - _Requirements: 1.2, 4.4, 8.2_

- [ ] 11.3 Test handover scenarios
  - Execute Setup Agent handover
  - Execute Manager Agent handover
  - Execute Implementation Agent handover
  - Verify context transfer completeness
  - _Requirements: 8.1_

- [ ] 11.4 Verify metadata tracking
  - Check metadata.json updates during workflow
  - Validate phase status transitions
  - Test version compatibility checking
  - _Requirements: 3.1, 8.4_

- [ ] 11.5 Document validation results
  - Record any issues found during testing
  - Document workarounds or fixes applied
  - Create issue list for future improvements
  - _Requirements: 8.5_
