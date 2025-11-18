# Troubleshooting Playbook for Frontend Delegations

This playbook catalogs recurring runtime errors that surface when PhD APM implementation agents work inside JavaScript or TypeScript frontends. Use it to accelerate diagnosis, frame hypotheses for copilots, and brief human operators during handovers. Cross-reference the base execution rules in [`../05-implementation-agents/implementation_agent_base_prompt.md`](../05-implementation-agents/implementation_agent_base_prompt.md) so every intervention stays aligned with the delegation contract.

---

## Error Matrix (Quick Scan)

| Symptom | Likely Cause | High-Leverage Checks |
| --- | --- | --- |
| `TypeError: Cannot read properties of null (reading 'useState')` | React runtime failed to initialize, leaving the default export undefined or null. This commonly happens when the React package is duplicated, the component is executed outside of a React renderer, or the import path is misconfigured. | - Inspect bundler warnings for duplicated React copies.<br>- Confirm the component renders inside `ReactDOM.render` / `createRoot`.<br>- Verify that React is imported from `"react"` without path aliasing typos. |

---

## Detailed Runbook: `TypeError` while reading `useState`

1. **Validate the import contract**
   - Open the failing file and confirm it uses one of the supported signatures:
     ```ts
     import React, { useState } from "react";
     ```
     or
     ```ts
     import * as React from "react";
     const [value, setValue] = React.useState(initialValue);
     ```
   - If `React` is being retrieved from the global scope (e.g., `const React = window.React;`), switch to a module import so bundlers can deduplicate packages.

2. **Check for duplicate React instances**
   - Run `npm ls react react-dom` (or `yarn why react`) from the project root. Multiple versions often indicate a hoisting or aliasing problem.
   - When duplicates appear, align the versions by upgrading/downgrading the outliers or adding a [package manager resolution field](https://docs.npmjs.com/cli/v9/configuring-npm/package-json#overrides).

3. **Ensure the component executes inside a renderer**
   - Confirm the component is mounted through `ReactDOM.createRoot(...).render(<App />)` or a framework-specific host (Next.js `pages/` or `app/` entry).
   - Guard against calling the component as a plain function during tests. Wrap hooks in a test renderer (e.g., React Testing Library's `render` or `renderHook`).

4. **Rebuild to reset module state**
   - Stop the dev server, clear caches (`rm -rf node_modules/.cache .next`, etc.), reinstall dependencies, and restart the server. Stale caches can keep an old, nullified React export in memory.

5. **Document resolution and handoff**
   - Summarize the root cause and fix inside `handover.md`, referencing impacted files. Note any package overrides or renderer adjustments so future agents avoid reintroducing the issue.

### When escalating to a human operator
- Attach the dependency tree snippet (`npm ls`) and the component stack trace.
- Highlight whether the error persists after a clean reinstall.
- Recommend running the affected tests or pages once React is properly mounted to confirm the fix.

---

## How to extend this playbook

1. Record new runtime or build failures in the matrix above.
2. Provide a concise root-cause hypothesis and a deterministic checklist (3-5 steps).
3. Cross-link any new entries from `06-guides/README.md` so operators can discover the updates quickly.
4. When a fix requires changes to implementation prompts, update the relevant files under `../05-implementation-agents/` and note the relationship in `handover.md`.
