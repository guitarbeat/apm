# Agentic Project Management (APM) Monorepo

This repository hosts two complementary Agentic Project Management systems:

- **`rigorous-apm/`** – An academic-manuscript review workflow built around 26 specialized agents and a scripted workspace helper.
- **`upstream-apm/`** – The v0.5 reference implementation for general-purpose multi-agent project coordination.

Use this README to pick the right starting point and keep both tracks aligned as you contribute updates.

---

## Choose Your Starting Point

| If you need… | Start with… | Why it matters |
| --- | --- | --- |
| A turnkey manuscript review workspace | [`rigorous-apm/01-START_HERE.md`](rigorous-apm/01-START_HERE.md) | Explains how to stage the review workspace, launch the setup helper, and coordinate all 26 agents end-to-end. |
| CLI automation for the Rigorous workflow | [`rigorous-apm/02-setup_review.py`](rigorous-apm/02-setup_review.py) | Generates `Implementation_Plan.md`, `system_state.*`, and storage folders with the shared 👤/🤖/🔁 legend baked in. |
| Drag-and-drop prompts for the Rigorous agents | [`rigorous-apm/03-review-kickoff/`](rigorous-apm/03-review-kickoff/) | Contains the kickoff prompt bundle that seeds both the Setup and Manager agents. |
| A high-level tour of every Rigorous guide | [`rigorous-apm/06-guides/README.md`](rigorous-apm/06-guides/README.md) | Maps operator questions to the correct playbook, cheat sheet, or IDE ritual. |
| A framework overview for the upstream APM stack | [`upstream-apm/README.md`](upstream-apm/README.md) | Introduces the v0.5 terminology, onboarding paths, and documentation legend shared across the upstream assets. |
| A detailed walkthrough of the upstream workflow | [`upstream-apm/docs/Workflow_Overview.md`](upstream-apm/docs/Workflow_Overview.md) | Aligns operators and agents on the canonical protocols, rituals, and shared-state expectations. |
| Schema definitions and validation helpers | [`upstream-apm/prompts/schemas/`](upstream-apm/prompts/schemas/) | Hosts JSON schema assets plus `validate_schema.py` for verifying structured prompts. |

---

## Contribution Checklist

1. **Stay consistent with the audience legend.** The 👤/🤖/🔁 icons appear across both systems—reuse them in new assets and mention when automation updates the legend automatically.
2. **Call out affected paths.** When you change prompts or helpers, reference the exact file or directory so other operators can locate them quickly.
3. **Run targeted tests.**
   - For Rigorous APM scripts, execute any impacted command (for example `python rigorous-apm/02-setup_review.py --help`).
   - For legacy Python modules or schemas inside `the original/`, run `pytest` from the repo root and `python "the original"/prompts/schemas/validate_schema.py --help` after schema changes.
4. **Document cross-links.** If you add or rename assets, update the relevant navigation table—`rigorous-apm/06-guides/README.md` or this file—so maintainers can discover your work.

---

## Repository Layout

```
README.md                         # This orientation guide
rigorous-apm/                     # Manuscript review workflow
└── 01-START_HERE.md              # Human operator onboarding
└── …                             # Specialist prompts, guides, and CLI helper
upstream-apm/                     # Upstream APM v0.5 assets
└── README.md                     # Upstream overview and documentation index
└── docs/                         # Guides referenced by the workflow overview
└── prompts/                      # Prompt bundles, schemas, and ad-hoc assets
```

Need a refresher on either system? Jump back to the table above and follow the linked files for deep dives.
