# Rigorous APM - Start Here

A specialized Agentic Project Management (APM) instance for academic manuscript review with 26 specialized agents.

---

## 🚀 Quick Start: Your First Manuscript Review

### Step 1: Prepare Your Manuscript
Ensure your manuscript is in LaTeX format (`.tex`) or have it ready in your workspace.

### Step 2: Initiate the Review with the Setup Agent
The `Setup Agent` will ask you questions about your manuscript and generate a detailed `Implementation Plan`.

**In your agentic IDE:**
1. Drag `03-setup-agent/setup_agent_initiation_prompt.md` into chat
2. Provide your manuscript file or directory
3. Answer the Setup Agent's questions
4. Review the generated Implementation Plan

### Step 3: Execute the Review with the Manager Agent
The `Manager Agent` will use the generated `Implementation Plan` to coordinate the 26 specialized agents.

**In your agentic IDE:**
1. Drag `04-manager-agent/manager_agent_initiation_prompt.md` into chat
2. Provide the Implementation Plan from Step 2
3. The Manager will coordinate all 26 agents automatically
4. Results will be saved in your review project's `agent_outputs/` directory

---

## 📂 Directory Structure

```
rigorous-apm/
├── 01-START_HERE.md                    # ⭐ This file
├── 02-setup_review.py                  # Automation script
│
├── 03-setup-agent/                     # Setup Agent prompts
│   └── setup_agent_initiation_prompt.md
│
├── 04-manager-agent/                   # Manager Agent prompts
│   ├── manager_agent_initiation_prompt.md
│   └── manager_bootstrap_prompt.md
│
├── 05-implementation-agents/           # 26 Implementation Agent prompts
│   ├── implementation_agent_base_prompt.md
│   ├── quality_control_agent_prompt.md
│   ├── executive_summary_agent_prompt.md
│   ├── section/                        # S1-S10 Section agents
│   ├── rigor/                          # R1-R7 Rigor agents
│   └── writing/                        # W1-W7 Writing agents
│
└── 06-guides/                          # Documentation
    ├── README.md                       # Guide navigation
    ├── Agent_Cheat_Sheet.md
    ├── Context_and_Prompt_Engineering_Guide.md
    ├── Customization_Guide.md
    ├── Memory_System_Guide.md
    └── Handover_Guide.md
```

---

## 📋 All Agent Prompts

### Setup Agent
**Location:** `03-setup-agent/`
- `setup_agent_initiation_prompt.md` - Initialize review project

### Manager Agent
**Location:** `04-manager-agent/`
- `manager_agent_initiation_prompt.md` - Coordinate 26 agents
- `manager_bootstrap_prompt.md` - Bootstrap from Implementation Plan

### Implementation Agents
**Location:** `05-implementation-agents/`

**Base Prompt:**
- `implementation_agent_base_prompt.md` - Shared protocols for all agents

**Section Agents (S1-S10)** - `section/`
- `s1_title_keywords_agent_prompt.md` - Title & Keywords
- `s2_abstract_agent_prompt.md` - Abstract
- `s3_introduction_agent_prompt.md` - Introduction
- `s4_literature_review_agent_prompt.md` - Literature Review
- `s5_methodology_agent_prompt.md` - Methodology
- `s6_results_agent_prompt.md` - Results
- `s7_discussion_agent_prompt.md` - Discussion
- `s8_conclusion_agent_prompt.md` - Conclusion
- `s9_references_agent_prompt.md` - References
- `s10_supplementary_materials_agent_prompt.md` - Supplementary Materials

**Rigor Agents (R1-R7)** - `rigor/`
- `r1_originality_contribution_agent_prompt.md` - Originality & Contribution
- `r2_impact_significance_agent_prompt.md` - Impact & Significance
- `r3_ethics_compliance_agent_prompt.md` - Ethics & Compliance
- `r4_data_code_availability_agent_prompt.md` - Data & Code Availability
- `r5_statistical_rigor_agent_prompt.md` - Statistical Rigor
- `r6_technical_accuracy_agent_prompt.md` - Technical Accuracy
- `r7_consistency_agent_prompt.md` - Consistency

**Writing Agents (W1-W7)** - `writing/`
- `w1_language_style_agent_prompt.md` - Language & Style
- `w2_narrative_structure_agent_prompt.md` - Narrative Structure
- `w3_clarity_conciseness_agent_prompt.md` - Clarity & Conciseness
- `w4_terminology_consistency_agent_prompt.md` - Terminology Consistency
- `w5_inclusive_language_agent_prompt.md` - Inclusive Language
- `w6_citation_formatting_agent_prompt.md` - Citation Formatting
- `w7_target_audience_alignment_agent_prompt.md` - Target Audience Alignment

**Synthesis Agents:**
- `quality_control_agent_prompt.md` - Synthesize findings from 24 agents
- `executive_summary_agent_prompt.md` - Create final comprehensive report

---

## 📚 Documentation

**Location:** `06-guides/`

- `README.md` - Guide navigation and reading paths
- `Agent_Cheat_Sheet.md` - Quick reference for all 26 agents
- `Context_and_Prompt_Engineering_Guide.md` - APM architecture principles
- `Customization_Guide.md` - Adapt APM for your needs
- `Memory_System_Guide.md` - State management and data structures
- `Handover_Guide.md` - Context transfer between sessions

---

## 💡 Tips for Agentic IDE Use

### Drag and Drop
- All files have unique names - no confusion when dragging multiple prompts
- Descriptive names help you verify you're using the right prompt

### File Search
- Search by agent ID: `s1`, `r5`, `w3`
- Search by function: `statistical`, `methodology`, `writing`
- Search by type: `agent_prompt`, `initiation`, `bootstrap`

### Context Management
- Use `implementation_agent_base_prompt.md` as shared context
- Add specific agent prompts as needed
- Reference guides for detailed protocols

---

## 🔗 Related Projects

- **Example Review**: `../sections_review/` - Completed manuscript review
- **Dissertation**: `../dissertation-proposal/` - The reviewed manuscript
- **Revision System**: `../dissertation-revision-implementation/` - Implementing feedback

---

**All prompts are ready to use with agentic IDEs. Simply drag the appropriate prompt file into your chat to begin!**
