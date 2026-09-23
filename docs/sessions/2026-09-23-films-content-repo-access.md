---
date: 2026-09-23
session: 60a2b0f0-ff73-4282-8e83-218c9b1b28a4
title: Moonshot Films/Content Private access
repo: coldoo/moonshot-james
pr: none
spend: {}
tags: [github, access, routing]
written_by: backfill, 2026-09-23
---

# Where the shared Moonshot repos are

## What happened
Found the two shared repos. Both are owned by `dylanpakd-cyber`, with James as a collaborator:
`moonshot-films-private` and `moonshot-content-private`. Access was verified with `git ls-remote` using the
saved GitHub login. Films is cloned at `references/external/moonshot-films` (gitignored). Content is not
cloned anywhere.

## Learnings

### L1. Shared repos never show on your own profile page
- Evidence: `github.com/coldoo?tab=repositories` lists owned repos only. The built-in browser is not signed in
  to GitHub, so it could not see private repos either. `git ls-remote` with the saved credential answered it.
- Goes to: `~/.claude/CLAUDE.md` Moonshot repos table (the URLs are recorded there).

### L2. The two repos are part of a larger company map
- Evidence: Films AGENTS.md names `moonshot-marketing/COMPANY-MAP.md` as the front door. Product canon lives in
  `moonshot-marketing`, and every change syncs to the org twin `moonshot-67labs/moonshot-films`. The Content
  repo holds `skills/brand-system-builder/`, `programs/short-form/PLAYBOOK.md`, `people/*.md` and
  `docs/research/`. Its branches are `codex/...` plus one PR, so Dylan's agents work there through branches.
- Goes to: routing rule. The Content internals are [UNVERIFIED] until it is cloned and its AGENTS.md is read.

## Next session starts here
```
Clone moonshot-content-private next to the pipeline (C:\moonshot-content-private) and read
its AGENTS.md before any copy work. Consider moving the Films clone out of
references/external to C:\moonshot-films-private so sessions open in it directly.
```
