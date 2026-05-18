---
name: personal-context-onboarding
description: Gently checks whether this Obsidian vault still looks like mostly boilerplate at the start of a meaningful session, then invites the user to share a small amount of useful personal context. Use during session start, onboarding, or when core areas such as Me, Goals, Projects, Work, Journal, Learning, and Media are sparse.
---

# Personal Context Onboarding

Goal: help a new or sparse vault become useful without making the user feel exposed, judged, or pressured.

## Start

From the vault root, run:

```bash
python3 .agents/skills/personal-context-onboarding/scripts/check_vault_context.py
```

Use the script output as a signal, not as a verdict. It counts files and non-placeholder lines in a small set of starter areas and does not print private note contents.

## If the Vault Is Not Sparse

Do not run an onboarding flow. Continue with the user's actual request using the smallest relevant context.

## If the Vault Is Sparse

Nudge once, then continue only if the user engages. Keep the interaction optional and low-friction:

1. Ask permission before collecting context.
2. Explain the benefit in one sentence.
3. Offer one small question, not a questionnaire.
4. Make skipping explicit and acceptable.
5. In a forked/private personal vault, actively save useful context by default once the user shares it. Do not ask a separate storage-permission question unless the content is unusually sensitive.

Recommended opener:

> This still looks like starter context, so I may miss what matters to you. If you want, answer one lightweight question and I will use it to be more useful: what should I know about your current goals, projects, work context, learning interests, or preferences? Fragments are fine, and you can skip anything private.

If the user seems hesitant, narrow the ask:

> Pick one: a current goal, a project you care about, a constraint I should respect, or how you prefer to be helped.

## Psychological Safety Rules

- Use autonomy-supportive language: "if you want", "pick one", "skip", "high-level is enough".
- Normalize partial answers: fragments, bullets, and rough notes are useful.
- Prefer practical context over identity disclosure.
- Do not ask for protected traits, medical details, finances, relationships, employer secrets, or third-party private details unless the user initiates that topic.
- Do not imply the user failed to fill the vault. Say "starter context" or "sparse context", not "empty" or "missing".
- Reflect back value, not personality judgments: "That helps me prioritize X" instead of "You are the kind of person who...".
- Ask at most two follow-up questions before doing useful work.

## Valuable Context to Elicit

Prioritize context that improves future assistance:

- Current goals and success metrics.
- Active projects and next actions.
- Important constraints, preferences, and boundaries.
- Work or learning context at a safe level of detail.
- What the assistant should never assume.

Use this order when choosing one question:

1. Goals: "What outcome would make this vault useful in the next month?"
2. Projects: "What is one project you want me to remember and help move forward?"
3. Preferences: "How do you prefer help: direct challenge, gentle reflection, detailed planning, or concise execution?"
4. Constraints: "What constraints should I respect when suggesting plans?"
5. Boundaries: "What should I avoid storing or assuming?"

## Saving Context

In a forked/private personal vault, storing personal context is expected. When the user answers an onboarding question, save concise, useful context to the obvious destination unless the user says not to save it.

Beyond onboarding, capture valuable durable context whenever it naturally appears. Prefer signal that will help future agents: goals, preferences, active projects, constraints, recurring patterns, commitments, decisions, review dates, and what the assistant should avoid assuming.

1. Use the most obvious destination:
   - `Me/Bio.md` for safe-to-reference personal context.
   - `Me/Goals.md` for goals and outcomes.
   - `Me/Operating Principles.md` for preferences and boundaries.
   - `Projects/Index.md` or a project note for personal projects.
   - `Work/` only for work context the user explicitly wants stored.
2. Convert the answer into concise bullets.
3. Use Obsidian wikilinks where useful.
4. Ask before storing secrets, credentials, medical records, employer/client confidential material, or private details about third parties.
5. If the destination is ambiguous, choose a reasonable default.
6. After saving, briefly mention what was logged and where.

## Do Not

- Do not scan the whole vault to decide whether to nudge.
- Do not repeatedly ask onboarding questions in the same session.
- Do not treat placeholder examples as facts.
- Do not turn onboarding into coaching unless the user asks for coaching.
- Do not commit `.planning/` or other local workflow artifacts.
