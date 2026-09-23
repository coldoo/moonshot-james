# Session learnings

One markdown file per working session: what it learned, what it proposes, and where the next session
starts. `/closeout` writes these after a PR is pushed. The skill lives at `~/.claude/skills/closeout/`.
The index is newest first.

How learnings move up:

```
docs/sessions/<date>-<slug>.md          everything this session learned (always)
        |  seen twice, or cost a paid run or a producer "no"
        v
docs/solutions/patterns/critical-patterns.md    numbered, sourced patterns
        |  binding on every session, producer says yes
        v
CLAUDE.md (here) / AGENTS.md (Films, Content)   rules
```

Side routes: model behaviour goes to `references/<model>.md`, a stage procedure goes to `skills/<stage>/SKILL.md`,
anything about James goes to memory, and another repo's domain goes to that repo as a PR. Routing between
the Moonshot repos is in `~/.claude/CLAUDE.md`.

Files are markdown with a small YAML header (date, session id, repo, PR, spend, tags), so they can be grepped,
diffed and reviewed in the PR they close out. Open rule proposals are `- [ ] P<n>` lines. Find them all with
`grep -rn "^- \[ \] P" docs/sessions/`.

| Date | Session | Learnings | Open proposals |
|---|---|---|---|
| 2026-09-23 | [Session learnings and /closeout](2026-09-23-session-learnings-closeout.md) | 3 | 0 |
| 2026-09-23 | [Wispr Flow mic](2026-09-23-wispr-flow-mic.md) | 2 | 0 |
| 2026-09-23 | [Films and Content repo access](2026-09-23-films-content-repo-access.md) | 2 | 0 |
| 2026-09-18 to 22 | [Previz and launch preview](2026-09-18-previz-and-launch-preview.md) | 14 | 4 |
