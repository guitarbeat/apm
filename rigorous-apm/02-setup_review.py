#!/usr/bin/env python3
"""
This script automates the setup of a new manuscript review project.
Cross-platform: Works on Windows, macOS, and Linux.
"""

import os
import sys
import json
from pathlib import Path


def main():
    # Prompt the user for the path to their manuscript
    manuscript_path = input("Enter the full path to your LaTeX manuscript (.tex file): ").strip()
    
    # Remove quotes if user pasted a path with quotes
    manuscript_path = manuscript_path.strip('"').strip("'")
    
    # Convert to Path object
    manuscript_path = Path(manuscript_path)
    
    # Check if the file exists
    if not manuscript_path.exists() or not manuscript_path.is_file():
        print(f"\033[91mError: Manuscript file not found at '{manuscript_path}'\033[0m")
        sys.exit(1)
    
    # Get the manuscript's directory and filename
    manuscript_dir = manuscript_path.parent
    manuscript_filename = manuscript_path.name
    manuscript_name = manuscript_path.stem
    
    # Create a new directory for the review project
    review_dir_name = f"{manuscript_name}_review"
    review_dir_path = manuscript_dir / review_dir_name
    
    if review_dir_path.exists():
        print(f"\033[91mError: Review directory '{review_dir_path}' already exists.\033[0m")
        sys.exit(1)
    
    # Create directories
    review_dir_path.mkdir(parents=True, exist_ok=True)
    (review_dir_path / "agent_outputs").mkdir(exist_ok=True)
    print(f"\033[92mCreated review directory: {review_dir_path}\033[0m")
    
    # Create the system_state.json file
    system_state = {
        "manuscript_context": {
            "title": manuscript_name,
            "target_outlet": "To be filled by Setup Agent",
            "current_stage": "To be filled by Setup Agent"
        },
        "review_progress": {
            "current_phase": "Setup",
            "completed_agents": [],
            "pending_agents": [
                "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10",
                "r1", "r2", "r3", "r4", "r5", "r6", "r7",
                "w1", "w2", "w3", "w4", "w5", "w6", "w7",
                "qc", "es"
            ]
        },
        "agent_outputs_summary": {},
        "last_action": "Initial setup complete."
    }
    
    system_state_path = review_dir_path / "system_state.json"
    with open(system_state_path, 'w', encoding='utf-8') as f:
        json.dump(system_state, f, indent=2, ensure_ascii=False)
    
    # Create a conceptual Implementation Plan
    implementation_plan_content = f"""# {manuscript_name} - Implementation Plan

**This is a conceptual Implementation Plan. Please provide this to the Rigorous Setup Agent for enhancement.**

## Phase 1: Section Analysis (s1-s10)
- Task 1.1: Title & Keywords Analysis │ section_s1
- ...

## Phase 2: Rigor Analysis (r1-r7)
- ...

## Phase 3: Writing Analysis (w1-w7)
- ...

## Phase 4: Quality Control Synthesis (qc)
- ...

## Phase 5: Executive Summary (es)
- ...
"""
    
    implementation_plan_path = review_dir_path / "Implementation_Plan.md"
    with open(implementation_plan_path, 'w', encoding='utf-8') as f:
        f.write(implementation_plan_content)
    
    print(f"\033[92mSuccessfully created initial review files in '{review_dir_path}'\033[0m")
    print(f"\033[93mNext step: Provide the 'Implementation_Plan.md' to the Rigorous Setup Agent for enhancement.\033[0m")


if __name__ == "__main__":
    main()
