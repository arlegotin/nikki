---
name: obsidian-markdown
description: Create and edit Obsidian-flavored Markdown with wikilinks, embeds, callouts, properties, tags, and note templates.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Obsidian Markdown

Use this skill when creating or editing notes in this vault.

## Core Rules

- Prefer Obsidian wikilinks for internal references: `[[Note Name]]`.
- Use aliases when display text should differ: `[[Note Name|display text]]`.
- Link headings with `[[Note Name#Heading]]`.
- Use Markdown links for external URLs.
- Keep notes scannable: short paragraphs, clear headings, checklists when useful.
- Use frontmatter for structured metadata when it helps future search or automation.
- Do not add real private details to examples.

## Common Syntax

```markdown
---
type: project
status: active
tags: [project]
---

# Note Title

Internal link: [[Goals]]
Aliased link: [[Operating Principles|principles]]
External link: [Obsidian](https://obsidian.md)

> [!note]
> Obsidian callout.

- [ ] Task
- [x] Done task
```

## Note Hygiene

- Add links to obvious related notes even when the source note does not already link them.
- Keep indexes updated when adding important notes.
- Avoid over-linking generic words.
- If a note contains sensitive material, do not quote it in public-facing text.

