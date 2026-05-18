# Vault Context

This is an Obsidian vault boilerplate for personal knowledge management, journaling, coaching, project planning, and learning.

The repository is public-template safe. Treat placeholder files as examples only. Do not infer personal facts from placeholders.

## Session Start

At the start of a meaningful session:

1. If the task depends on dates or time, run:

   ```bash
   python3 .claude/skills/current-datetime/get_datetime.py
   ```

2. Read only the context needed for the user's request. Good default context files are:
   - `Me/Index.md`
   - `Me/Goals.md`
   - `Journal/Index.md`
   - relevant project or work folders

Do not read the whole vault by default once it contains real private notes. Prefer targeted reads.

## Skills

Use these local skills when relevant:

- `/socratic-journaling` for guided reflection and journal entries.
- `/adaptive-journaling` when the user wants to journal but is unsure which format fits.
- `/no-bs-coach` for direct coaching, accountability, habits, and goals.
- `/notes-to-plan` for converting messy notes or TODOs into plans.
- `/obsidian-markdown` when creating or editing Obsidian notes.
- `/current-datetime` when exact local date or time matters.

## Privacy Rules

- Never expose private note contents in public output unless the user explicitly asks.
- Never commit secrets, credentials, private logs, personal medical data, employer/client data, or local machine paths.
- Before making a public commit, scan for sensitive strings and review the diff.
- When creating examples, use neutral placeholders instead of real people, companies, locations, or projects.

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
