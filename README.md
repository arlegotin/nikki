# Nikki

Public boilerplate for an Obsidian vault that works with any AI agent through `AGENTS.md` and model-agnostic local skills.

This repository is intentionally empty of personal content. It gives you a ready-to-fork structure for journaling, coaching, projects, learning notes, media notes, and general knowledge capture.

## Quick Start

1. Clone or fork this repository.
2. Open the folder as an Obsidian vault.
3. Tell your agent to read `AGENTS.md`.
4. If your agent supports local skills, point it at `.agents/skills/`. Otherwise, read the relevant `SKILL.md` files manually.
5. Start filling the placeholder notes in `Me/`, `Journal/`, `Projects/`, `Learning/`, and `Work/`.
6. Keep private information out of commits unless your repository is private.

## Structure

- `Inbox/` - quick capture for unsorted notes.
- `Journal/` - daily entries, incidents, decisions, and an index.
- `Me/` - personal operating context: profile, goals, concerns, coaching memory.
- `Work/` - career and work-related notes.
- `Projects/` - personal or professional project notes.
- `Learning/` - topics, courses, research, and study notes.
- `Media/` - books, movies, music, and other media notes.
- `Templates/` - reusable Obsidian note templates.
- `.agents/skills/` - local agent skills for this vault.
- `.obsidian/` - minimal Obsidian settings safe for a public template.

## Included Skills

- `current-datetime` - get exact local date and time.
- `obsidian-markdown` - write Obsidian-flavored Markdown.
- `notes-to-plan` - convert messy notes into priorities and next actions.
- `socratic-journaling` - guided journal sessions.
- `adaptive-journaling` - choose a journaling framework based on state and time.
- `no-bs-coach` - direct coaching and accountability.

## Agent Compatibility

`AGENTS.md` is the canonical instruction file. Keep vendor-specific adapters short and point them back to `AGENTS.md` instead of copying policy.

The `.agents/skills/` directory contains plain Markdown skill playbooks. They are intentionally readable by humans and usable by any agent, even when the runtime has no native skill loader.

## Privacy Contract

This boilerplate is designed to be public. Before publishing changes, run a privacy scan and inspect anything staged:

```bash
rg -n "secret|token|password|private|api[_-]?key|BEGIN .*PRIVATE" .
git diff --staged
```

Do not commit journals, health details, private relationship notes, employer data, client data, credentials, local paths, or generated assistant memory unless you intend to publish them.

Do not commit `.planning/` or GSD planning notes. They are local workflow state and are ignored by git.

## License

MIT. See `LICENSE`.
