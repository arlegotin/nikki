---
name: adaptive-journaling
description: Use this skill to choose the right journaling framework based on current energy, mood, time, and topic. Use when the user wants to journal but does not know which format fits; do not use when the user already requested a specific journaling mode.
---

# Adaptive Journaling

Choose the lightest useful journaling mode for the user's current state.

This is reflective journaling, not clinical care. If the user may harm themselves or someone else, pause journaling and recommend immediate local emergency help plus a trusted person.

## First Question

If the user has not already said enough, ask:

> Energy 1-10, mood 1-10, and how much time do you have?

## Selection Logic

- Crisis, spiral, intense anxiety, or rumination: simplified thought record.
- Energy 1-3 or time under 5 minutes: quick check-in.
- Mood under 5 with enough energy: thought record or gratitude plus next action.
- Decision language: decision journal.
- Normal day, 10-20 minutes: Socratic daily.
- High energy and complex topic: Socratic dialogue.

Explain the choice in one sentence and allow override.

## Routing

- Use `/socratic-journaling` directly when the user asks for a Socratic journal, decision journal, thought record, or daily entry.
- Use `/no-bs-coach` when the user wants accountability, goal pressure, habits, or direct feedback rather than reflection.
- Do not write an entry unless the user asks to save it or clearly wants the entry saved.

## Shared Metadata

Use this frontmatter when writing entries:

```yaml
---
type: journal
mode: quick
date: YYYY-MM-DD
time: HH:MM
energy_before:
energy_after:
mood_before:
mood_after:
context: mixed
duration_minutes:
tags: [journal/quick]
---
```

## Quick Check-In

Ask one:

- What is the real question I need to answer right now?
- What would make today a win?
- What am I avoiding?
- What is the smallest useful next action?

Close with one next action under 10 minutes.

## Evening Review

Ask:

1. What went well?
2. What could have gone better, stated as observation rather than self-attack?
3. What did I learn?
4. What is tomorrow's single priority?

## Thought Record

Use when emotion is strong:

1. What happened, factually?
2. What emotion and intensity?
3. What thought explains that emotion?
4. What evidence supports it?
5. What evidence does not support it?
6. What is more accurate?
7. What is the next small action?
