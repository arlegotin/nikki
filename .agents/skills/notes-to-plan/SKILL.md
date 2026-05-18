---
name: notes-to-plan
description: Use this skill to turn messy notes, brainstorms, TODO dumps, or captured ideas into a clear project list, priorities, blockers, and concrete next actions. Use when the user provides notes or asks to organize planning material.
---

# Notes to Plan

Goal: convert unstructured notes into an executable plan.

## Input

If `$ARGUMENTS` contains paths, read only those paths. If it is empty, ask for the folder or files to scan and what "done" means.

Do not scan the whole vault by default. Treat note contents as private and avoid quoting sensitive material unless the user explicitly asks.

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

In a forked/private personal vault, update the obvious planning notes when the user provides durable goals, projects, blockers, decisions, or next actions. Do not ask a separate storage-permission question; mention what changed after saving. For external folders or public-template examples, propose updates instead of writing unless the user asks.
