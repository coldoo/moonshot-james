---
date: 2026-09-23
session: 5abb18a9-9fde-4822-a6be-81d2429a1f56
title: Session learnings store and /closeout
repo: coldoo/moonshot-james
branch: main (uncommitted)
pr: none yet
spend: {}
tags: [closeout, learnings, routing, memory]
---

# Session learnings store, /closeout, and Moonshot repo routing

## What happened
Reviewed the four sessions from 2026-09-18 to 2026-09-23 and backfilled a learnings file for each. Created
`docs/sessions/` and `docs/solutions/patterns/critical-patterns.md`, with 13 compounded patterns. Wrote the
user-level `/closeout` skill (`~/.claude/skills/closeout/`) and the Moonshot routing rules in
`~/.claude/CLAUDE.md`, with a pointer in this repo's CLAUDE.md. Copied three orphaned memories into the project memory.

## Learnings

### L1. Dylan's repos already have a closeout and compounding convention, so match it
- Evidence: Films has `docs/sessions/<date>-<slug>-closeout.md`, `docs/solutions/patterns/critical-patterns.md`
  ("the socket `/ce-compound` fills") and a Did / Verified / Learned / Next block in `STATE.md`.
- Goes to: this repo now uses the same layout, so entries can move between repos unchanged.

### L2. The cp949 console breaks Python output with non-ASCII characters
- Evidence: a transcript-mining script crashed on an en dash (`UnicodeEncodeError: 'cp949'`), the same failure
  as the 2026-09-18 session.
- Goes to: critical-patterns #11 (second source, compounded).

### L3. The desktop app's session list and the transcript files map one to one
- Evidence: `list_sessions` gives titles, and `~/.claude/projects/C--moonshot-pipeline/<id>.jsonl` gives full
  history, including sessions that started in other folders.
- Goes to: `/closeout` step 1 and `scripts/harvest.py`.

## For other repos
- Films `skills/melius-cut-frames/SKILL.md`: the launch-preview lessons listed in
  [2026-09-18](2026-09-18-previz-and-launch-preview.md) "For other repos". Not opened yet.

## Next session starts here
```
Try /closeout on the next PR. Open decisions: P1-P4 in docs/sessions/2026-09-18-*.md; whether
James pushes to Dylan's main or opens PRs; clone moonshot-content-private; move
projects/moonshot-launch to Films or keep it here.
```
