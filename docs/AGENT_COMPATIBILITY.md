# Agent Compatibility

This boilerplate is designed around plain files instead of one vendor's runtime.

## Canonical Files

- `AGENTS.md` - behavior, privacy rules, and vault workflow.
- `.agents/skills/` - reusable skill playbooks.
- `.agents/config.example.json` - neutral example metadata for tools that support custom configuration.

## Using Any Agent

1. Ask the agent to read `AGENTS.md`.
2. Ask it to use `.agents/skills/<skill-name>/SKILL.md` when relevant.
3. Keep generated planning state local.
4. Review diffs before committing public changes.

## Tool-Specific Adapters

If a tool expects a model-specific instruction file, keep that file tiny:

```markdown
# Instructions

Read `AGENTS.md` and follow it as the canonical project guide.
```

Do not fork privacy or workflow policy across multiple files.

## GSD Planning Notes

GSD may create `.planning/` files for local workflow state. They must remain untracked and are ignored by `.gitignore`.

