# Agent Instructions

This is an Obsidian vault boilerplate for personal knowledge management, journaling, coaching, project planning, and learning.

The repository is public-template safe. Treat placeholder files as examples only. Do not infer personal facts from placeholders.

After this boilerplate is forked or copied into a private personal vault, the vault is expected to be filled with real personal context. In that mode, agents must actively capture durable, valuable user-provided context whenever there is a natural chance. Do not ask a separate "should I store this?" question before saving the user's goals, preferences, projects, reflections, decisions, constraints, or coaching context into the appropriate vault notes. Treat storage as expected unless the user says not to save it or the content is unusually sensitive.

These instructions are model-agnostic. Any coding or writing agent can use this file as its canonical operating guide.

## Session Start

At the start of a meaningful session:

1. If the task depends on dates or time, run:

   ```bash
   python3 .agents/skills/current-datetime/get_datetime.py
   ```

2. If the vault appears new, sparse, or mostly boilerplate, use `/personal-context-onboarding` before relying on personal context. The skill should check only starter areas and gently invite the user to share one small, optional piece of useful context.

3. Read only the context needed for the user's request. Good default context files are:
   - `Me/Index.md`
   - `Me/Goals.md`
   - `Journal/Index.md`
   - relevant project or work folders

Do not read the whole vault by default once it contains real private notes. Prefer targeted reads.

## Session End

Near the end of every agentic session, if any files were created, edited, moved, or removed, finish cleanly:

1. Review the diff and run relevant lightweight validation.
2. Scan for secrets or inappropriate private content before any public commit.
3. Never commit `.planning/` or other local workflow artifacts.
4. Commit a cohesive change with a concise message.
5. Push the current branch to its configured remote.

Do this without asking for extra permission unless the user explicitly said not to commit or push. If commit or push is blocked, explain the blocker and leave the repository in the cleanest safe state.

## Skills

Skills are Markdown playbooks in `.agents/skills/`. If your agent runtime supports local skills, point it at that directory. If it does not, read the relevant `SKILL.md` file and follow it manually.

Use these skills when relevant:

- `/skill-creator` for creating or updating personalized skills. Use it before adding new skill folders, scripts, references, assets, or skill metadata.
- `/socratic-journaling` for guided reflection and journal entries.
- `/adaptive-journaling` when the user wants to journal but is unsure which format fits.
- `/no-bs-coach` for direct coaching, accountability, habits, and goals.
- `/notes-to-plan` for converting messy notes or TODOs into plans.
- `/obsidian-markdown` when creating or editing Obsidian notes.
- `/personal-context-onboarding` at the beginning of a meaningful session when the vault is still sparse or mostly boilerplate.
- `/current-datetime` when exact local date or time matters.

## Agent Compatibility

- Keep `AGENTS.md` as the single source of truth for agent behavior.
- Do not duplicate long-lived policy into model-specific files.
- If a tool expects a vendor-specific instruction file, make that file a short pointer to `AGENTS.md`.
- Keep reusable skills under `.agents/skills/`, not a model-specific directory.
- When creating new personalized skills, first use `.agents/skills/skill-creator/SKILL.md`, then place the finished skill under `.agents/skills/<skill-name>/`.
- Personalized skills must remain public-template safe: store reusable methods, prompts, scripts, and neutral examples, not private personal facts.

## Behavioral Changes

Be attentive when the user asks for a permanent behavioral change. Treat phrases like "always", "never", "from now on", "permanent instruction", "make agents", or "the agent should" as signals that repo behavior should be updated.

When a requested behavior should persist, update the best durable place in the same turn:

- `AGENTS.md` for repo-wide agent behavior.
- The relevant `.agents/skills/<skill-name>/SKILL.md` for workflow-specific behavior.
- Templates or folder notes when the rule only affects a note type or location.

Do not leave permanent behavior changes only in chat. If the right destination is ambiguous, choose the most general safe place and keep the instruction concise.

## Privacy Rules

- Never expose private note contents in public output unless the user explicitly asks.
- Never commit secrets, credentials, private logs, personal medical data, employer/client data, or local machine paths.
- Never commit `.planning/` or other GSD planning notes. They are local workflow state, not public boilerplate.
- Before making a public commit, scan for sensitive strings and review the diff.
- When creating examples, use neutral placeholders instead of real people, companies, locations, or projects.
- In a forked/private personal vault, saving the user's own goals, preferences, projects, reflections, decisions, constraints, and coaching context is a core agent responsibility. Log valuable context proactively whenever it appears; choose the obvious destination note and keep the entry concise but useful.
- Prefer durable signal over transcript dumps: capture what will help future agents act better, such as current priorities, recurring patterns, commitments, boundaries, active projects, important decisions, and review dates.
- After saving context, briefly mention what was logged and where. Do not interrupt useful work just to ask permission.
- Still ask before storing secrets, credentials, medical records, employer/client confidential material, or private details about third parties.

## Writing Rules

- Use Obsidian wikilinks like `[[Goals]]` for internal note references.
- Prefer concise notes with clear headings and checklists.
- Keep folder-level indexes updated when adding important notes.
- Respond in the language of the user's latest message.
- When unsure whether content is private, treat it as private.

## Vault Structure

- `Inbox/` - unsorted capture.
- `Journal/` - daily journal, incident notes, decision journals, and an index.
- `Me/` - profile, goals, concerns, coaching memory, personal operating context.
- `Work/` - work projects, notes, and career context.
- `Projects/` - side projects, product ideas, experiments.
- `Learning/` - study notes and research.
- `Media/` - books, movies, music, talks, and other media.
- `Templates/` - reusable note templates.
- `Resources/` - reusable reference material.
- `Archive/` - inactive or completed material.
- `Attachments/` - images, PDFs, and other files.
- `.agents/` - model-agnostic agent instructions, skills, and examples.
