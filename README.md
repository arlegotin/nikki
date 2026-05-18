# Nikki

Public boilerplate for an Obsidian vault that works well with Claude Code and local skills.

This repository is intentionally empty of personal content. It gives you a ready-to-fork structure for journaling, coaching, projects, learning notes, media notes, and general knowledge capture.

## Quick Start

1. Clone or fork this repository.
2. Open the folder as an Obsidian vault.
3. Copy `.claude/settings.example.json` to `.claude/settings.local.json` if you want local Claude Code permissions.
4. Start filling the placeholder notes in `Me/`, `Journal/`, `Projects/`, `Learning/`, and `Work/`.
5. Keep private information out of commits unless your repository is private.

## Structure

- `Inbox/` - quick capture for unsorted notes.
- `Journal/` - daily entries, incidents, decisions, and an index.
- `Me/` - personal operating context: profile, goals, concerns, coaching memory.
- `Work/` - career and work-related notes.
- `Projects/` - personal or professional project notes.
- `Learning/` - topics, courses, research, and study notes.
- `Media/` - books, movies, music, and other media notes.
- `Templates/` - reusable Obsidian note templates.
- `.claude/skills/` - local Claude skills for this vault.
- `.obsidian/` - minimal Obsidian settings safe for a public template.

## Included Skills

- `current-datetime` - get exact local date and time.
- `obsidian-markdown` - write Obsidian-flavored Markdown.
- `notes-to-plan` - convert messy notes into priorities and next actions.
- `socratic-journaling` - guided journal sessions.
- `adaptive-journaling` - choose a journaling framework based on state and time.
- `no-bs-coach` - direct coaching and accountability.

## Privacy Contract

This boilerplate is designed to be public. Before publishing changes, run a privacy scan and inspect anything staged:

```bash
rg -n "secret|token|password|private|api[_-]?key|BEGIN .*PRIVATE" .
git diff --staged
```

Do not commit journals, health details, private relationship notes, employer data, client data, credentials, local paths, or generated assistant memory unless you intend to publish them.

## License

MIT. See `LICENSE`.
