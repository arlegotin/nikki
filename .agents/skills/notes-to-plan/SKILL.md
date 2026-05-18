---
name: notes-to-plan
description: Turn messy notes, brainstorms, and TODO dumps into a clear project list, priorities, blockers, and concrete next actions.
argument-hint: "[path|files]"
disable-model-invocation: false
allowed-tools: Read, Grep, Glob
---

# Notes to Plan

Goal: convert unstructured notes into an executable plan.

## Input

If `$ARGUMENTS` contains paths, read only those paths. If it is empty, ask for the folder or files to scan and what "done" means.

## Procedure

1. Collect relevant files: `*.md`, `*.txt`, `*.org`, `*.todo`.
2. Ignore obvious noise: `.git`, `.trash`, `node_modules`, `dist`, `build`, `vendor`.
3. Extract:
   - tasks and checkboxes
   - outcomes and projects
   - deadlines and dates
   - blockers and dependencies
   - waiting-on items
   - open questions
4. Normalize into:
   - outcomes: what changes when done
   - next actions: physical steps under 30 minutes
   - blockers: missing info, dependencies, decisions
5. Prioritize by impact, urgency, and leverage.
6. Identify the first action that makes the rest easier.

## Output Format

### A) Inventory

- Goals:
- Projects:
- Loose tasks:
- Blockers or decisions:
- Waiting on:

### B) The 3-5 Priorities

1.
2.
3.
4.
5.

### C) Next Actions for Priority 1

- Action 1:
- Action 2:
- Action 3:

### D) Missing Info

Ask at most five questions needed to proceed.

### E) Suggested File Updates

Propose note updates only when useful. Do not write files unless the user asks you to.

