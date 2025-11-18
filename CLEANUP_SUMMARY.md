# Documentation Cleanup Summary

**Date**: November 18, 2025  
**Goal**: Make phd-apm lean and usable by removing broken references

---

## Changes Made

### README.md
- ❌ Removed reference to `phd-apm/03-review-kickoff/` (doesn't exist)
- ❌ Removed reference to `phd-apm/06-guides/README.md` (doesn't exist)
- ❌ Removed reference to `phd-apm/MIGRATION_GUIDE.md` (doesn't exist)
- ❌ Removed reference to `INTEGRATION_STRATEGY.md` (doesn't exist)
- ✅ Updated to point to actual directories: `03-setup-agent/` and `04-manager-agent/`
- ✅ Simplified guide reference to just `06-guides/` directory
- ✅ Pointed integration docs to `.kiro/specs/upstream-integration-plan/`
- ✅ Cleaned up repository layout diagram to match reality

### phd-apm/01-START_HERE.md
- ❌ Removed reference to `06-guides/Agent_Cheat_Sheet.md` (doesn't exist)
- ❌ Removed reference to `validation_results.md` (doesn't exist)
- ❌ Removed `03-review-kickoff/` from directory structure
- ✅ Fixed typo: "Setup Ageunt" → "Setup Agent"
- ✅ Expanded guide reference section with actual file lists
- ✅ Added explanation of `{GUIDE_PATH:}` syntax
- ✅ Corrected upstream guide location: `docs/` → `prompts/guides/`

### AGENTS.md
- ❌ Removed reference to `INTEGRATION_STRATEGY.md` (doesn't exist)
- ❌ Removed reference to `06-guides/README.md` (doesn't exist)
- ❌ Removed reference to `06-guides/upstream/` (doesn't exist)
- ✅ Corrected upstream guide location to `upstream-apm/prompts/guides/`
- ✅ Clarified guide system architecture

---

## What's Left

### Files That Exist ✅
- All 26 agent prompts properly structured
- 7 domain-specific guides in `phd-apm/06-guides/`
- 6 upstream guides in `upstream-apm/prompts/guides/`
- Integration spec in `.kiro/specs/upstream-integration-plan/`
- Setup and Manager agent prompts

### No Broken Links ✅
- All documentation now points to files/directories that actually exist
- Users won't hit 404s
- Clear guide locations documented

---

## Result

**Before**: 6+ broken references, confusing structure  
**After**: Clean, lean documentation pointing only to what exists

Users can now:
1. Follow the Quick Start without hitting missing files
2. Understand where guides are located
3. Navigate the actual directory structure
4. Find integration details in the spec directory

**No new files created** - just cleaned up references to match reality.
