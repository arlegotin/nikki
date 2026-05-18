# Privacy Guide

This repository is meant to be forked publicly. The safest rule is simple: keep the boilerplate public, keep lived details private.

## Do Not Commit

- API keys, passwords, tokens, SSH keys, or `.env` files.
- Medical, financial, legal, or identity documents.
- Journal entries you would not publish intentionally.
- Private employer, client, or interview material.
- Names, addresses, phone numbers, emails, private links, or local machine paths.
- Assistant-generated memory that quotes private notes.
- `.planning/` and other GSD planning notes.

## Recommended Workflow

1. Keep this template repository public.
2. Fork or clone it into a private vault for real use.
3. Commit only structure, templates, and reusable instructions to the public copy.
4. Keep personal notes in a private repository or local-only vault.

## Pre-Publish Scan

Run these before making public commits:

```bash
rg -n "secret|token|password|api[_-]?key|private key|BEGIN .*PRIVATE|/Users/|C:\\\\Users" .
rg -n "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}" .
git diff
git status --short
```

Manual review still matters. Scanners miss context.
