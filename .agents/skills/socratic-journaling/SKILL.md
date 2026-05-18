---
name: socratic-journaling
description: Use this skill to guide a Socratic journal session inside an Obsidian vault. Use when the user wants to reflect, process an event, clarify a decision, write a daily entry, or create a thought record.
---

# Socratic Journaling

Help the user create useful journal entries through a short conversation, then write the note in Obsidian format when asked or when the user clearly wants the entry saved.

## Principles

- Ask fewer, better questions.
- Anchor in concrete events and observable facts.
- Separate facts, interpretations, emotions, and actions.
- Close with the most accurate current view and a small next action.
- Do not diagnose. Do not overreach.
- Keep sensitive details inside the vault, not in public summaries.
- If the user may harm themselves or someone else, pause journaling and recommend immediate local emergency help plus a trusted person.

## Routing

- Use `/adaptive-journaling` first when the user wants to journal but is unsure what format fits.
- Use `/no-bs-coach` when the user asks for direct accountability, challenge, or behavior change.
- Use this skill when the user asks for reflection, a specific journaling mode, or a saved journal entry.

## Modes

- `quick`: one question, one answer, one next action.
- `daily`: standard daily reflection.
- `thought-record`: CBT-style reality testing for strong emotion or rumination.
- `decision`: decision journal before or after a choice.

If no mode is provided, default to `daily`.

## Context

Read only context that helps the current session:

- `Me/Goals.md` for current goals.
- `Me/Operating Principles.md` for preferences and values.
- `Journal/Index.md` for recent themes.
- Relevant project or work notes if the topic names them.

Do not read the entire vault by default.

## Workflow

1. If date-sensitive, run `python3 .agents/skills/current-datetime/get_datetime.py`.
2. Ask one opening question: "How much time do you have, and what are we journaling about?"
3. Capture minimal context:
   - date
   - context: work, personal, mixed, health, relationship, learning, project
   - situation
   - emotions, if relevant
4. Run the selected mode.
5. Synthesize:
   - what is true now
   - what matters
   - what is next
6. Write the note if the user wants it saved.
7. Update `Journal/Index.md` with a one-line summary.

## File Conventions

- Daily: `Journal/Daily/YYYY-MM-DD.md`
- Thought records: `Journal/Incidents/YYYY-MM-DD - topic.md`
- Decisions: `Journal/Decisions/YYYY-MM-DD - topic.md`

## Daily Template

```markdown
---
type: journal
mode: daily
date: YYYY-MM-DD
context: mixed
tags: [journal/daily, socratic]
---

# Socratic Journal - YYYY-MM-DD

## Context

- Situation:
- Emotions:

## Dialogue

1. **Q:**
   **A:**

2. **Q:**
   **A:**

3. **Q:**
   **A:**

## Synthesis

- **Most accurate view now:**
- **What matters:**
- **Next actions:**
  - [ ]
```

## Thought Record Template

```markdown
---
type: journal
mode: thought-record
date: YYYY-MM-DD
context: mixed
tags: [journal/thought-record]
---

# Thought Record - YYYY-MM-DD - Topic

## Situation

Facts only.

## Feelings

- Emotion:
- Intensity:

## Automatic Thought

The thought as a statement.

## Evidence For

- 

## Evidence Against

- 

## Balanced View

More accurate, not artificially positive.

## Next Action

- [ ]
```

## Decision Template

```markdown
---
type: decision
date: YYYY-MM-DD
tags: [journal/decision]
---

# Decision Journal - YYYY-MM-DD - Topic

## Decision

## Context

## Options

## Expected Outcome

## Review Date
```
