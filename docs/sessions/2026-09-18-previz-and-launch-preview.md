---
date: 2026-09-18
ended: 2026-09-22
session: 8ed9f668-4fd4-4f33-8a78-132b7d4dae94
title: AI agents for video production workflow
repo: coldoo/moonshot-james
branch: main
pr: none (every commit went straight to main)
projects: [moonshot-previz, moonshot-launch]
spend: {higgsfield: 673, melius: 6956}
tags: [previz, minimax-h3-max, nano-banana-pro, melius, assembly, session-hygiene]
written_by: backfill, 2026-09-23 (from the transcript, not a live /closeout)
---

# Previz, then the launch preview START frames

## What happened

One session ran four days and 1,288 messages. It covered two projects and three working folders:
scratch workspace, then OneDrive, then `C:\moonshot-pipeline`. It went through one context compaction.
It set up the pipeline repo and made a seven-scene previz on Higgsfield (MiniMax H3 Max video, 673
credits). Then it made the public launch preview's START frames on Melius (Nano Banana Pro, 6,956
Melius credits, no video) under Dylan's Films rules. The launch-preview script reached v6.

## Learnings

### L1. Confirm the deliverable's form before building it
- Evidence: the agent assembled a stills slideshow with slates and burned-in captions. Producer:
  "No, no, no, no! I did not ask for this ... I do not want a slideshow of images. I want the videos."
- Cost: one assembly pass and a trust hit.
- Goes to: `docs/solutions/patterns/critical-patterns.md` #1 (compounded).

### L2. First job on a new model is one job, not two
- Evidence: two MiniMax H3 Max jobs were fired at once, and both were rejected (422: "reference media cannot be
  mixed with start_image"). CLAUDE.md already says "one generation at a time until the first result
  of a new model". Nothing was charged only because validation failed before the run.
- Goes to: critical-patterns #2 (compounded). The rule already exists, so the gap is obeying it, not writing it.

### L3. Propose the cheapest rail that shows the idea, with the credit comparison
- Evidence: the agent wrote the previz video prompts for Seedance 2.5. Producer: "Do not use seedance 2.5
  for this ... That is going to cost us an insane amount of credits." Producer picked MiniMax H3 Max.
- Goes to: critical-patterns #3 (compounded). Already reflected in `skills/previz/SKILL.md`.

### L4. When a model refuses start frame plus references, send all images as references and label them
- Evidence: producer's fix: "just have three images in there, and then label which one is the start
  frame". Worked on every scene after.
- Goes to: `skills/previz/SKILL.md` and CLAUDE.md previz mode (already landed in commit 65c8e90).

### L5. Assembly: no black cards, no freeze frames, translucent overlay box, caption when speech starts
- Evidence: three rounds of notes on the internal cut ("the cuts make it last too long", "don't freeze
  the frame" four times, "have the card come up when the person is starting to talk").
- Goes to: CLAUDE.md previz mode (already landed). critical-patterns #9.

### L6. Lock a location by attaching the approved still of the same place
- Evidence: previz S04 kitchen matched S03 after the S03 still was attached. Launch 02b matched Jove's kitchen
  after the approved 04 frame was wired in.
- Goes to: critical-patterns #5 (seen twice, compounded).

### L7. Prop first: generate the object, then wire it in as a reference
- Evidence: the Polaroid was generated once, then referenced. It held across four hook frames on nano-banana-pro.
- Goes to: critical-patterns #6. Candidate for Films `skills/melius-cut-frames/SKILL.md` Lessons.

### L8. Inserts need the product state spelled out: worn, one hand, cord colour
- Evidence: v2 inserts F03 and F09 rendered the pendant HELD. The cord drifted to silver in about 1 in 3
  close-ups (v3 F01 v2, F09 v2, 02b v1). "No second hand" was ignored once.
- Goes to: `references/nano-banana-2.md` and Films `skills/melius-cut-frames/SKILL.md` Lessons (proposal).

### L9. Check a paid run against the target repo's known-failure list before firing
- Evidence: the v2 review flagged three failures the Films repo already documents: the "read as a gadget
  in hand" insert, "a puffer at an indoor dinner fails", and a face lock alone not holding a secondary
  character (Jove). All three were caught after the 3,760-credit run, not before.
- Cost: part of the 1,880-credit v3 redo.
- Goes to: critical-patterns #7 (compounded).

### L10. Ask for missing picks in the same message; do not default silently
- Evidence: the producer never named variations for F02, F03, F05, F06 or F10. The agent recorded v1 and
  flagged it afterwards. The flag was right, but the question belonged in the pick request.
- Goes to: critical-patterns #10.

### L11. The producer edits the Melius canvas between turns, so read it fresh
- Evidence: script v6 came from the producer's card edits. Two edits failed on stale node ids ("node does not
  exist on this canvas", "Node not found").
- Goes to: critical-patterns #8. Matches the CLAUDE.md "read it fresh" rule for shared files.

### L12. Session hygiene: start in the repo folder, one session per stage, one project per session
- Evidence: the session started in a scratch workspace, so three memories were saved under the scratch
  project folder and orphaned when the session moved. The current memory index linked to files that
  were not there. The context was compacted once in four days. The producer asked for "a prompt I can send
  to the other conversation" three times to carry context by hand.
- Goes to: `~/.claude/CLAUDE.md` Sessions section, critical-patterns #12. The orphaned memories were
  copied into the project memory on 2026-09-23.

### L13. Windows shell friction on this machine
- Evidence: three bash heredoc quoting failures ("unexpected EOF while looking for matching"), one bash
  heredoc sent to PowerShell, and a `UnicodeEncodeError: 'cp949'` when Python printed an em dash. The console
  code page is Korean. ffmpeg and PIL were missing on day one.
- Goes to: `~/.claude/CLAUDE.md` "This machine" section, critical-patterns #11.

### L14. Film work done here did not compound back into the Films repo
- Evidence: Films AGENTS.md says a frame pass's "lessons from each pass go into that skill, not only the
  journal". L7, L8 and the Jove-lock finding live only in this repo's review files and memory.
- Goes to: the routing rule in `~/.claude/CLAUDE.md` and CLAUDE.md "Where work lands". Films proposals below.

## What worked (keep doing)
- Spend table in every report, with the running total against the budget.
- A review `.md` per run with Held / Flags / recommended pick. The producer accepts recommendations readily.
- One-sentence characters in previz prompts (the producer's own rule).
- For cheap stills, "go all" one-pass chains beat two-stage checkpoints. The producer said so.
- Melius FINAL column read top to bottom, with old drafts off to the side. The producer asked for this layout.
- Script of record synced to the canvas card, the column header and `script.md` in one pass.

## Rule proposals
- [ ] P1 `CLAUDE.md` Generation defaults: Kling, Higgsfield Soul and the Higgsfield CLI fan-out were never
  used. The rails that actually ran were Nano Banana Pro (Higgsfield MCP and Melius), MiniMax H3 Max
  and Melius bulk runs. Rewrite the defaults to match, or mark them "production, untested".
- [ ] P2 `CLAUDE.md` Tools: `<!-- TODO(producer): set default editor -->` is still open.
- [ ] P3 `CLAUDE.md` Stages table: the launch project used `brief.md`, `cut-map-*.md`, `selects.json` and
  spend in `brief.md`, with no `shotlist.json` or `spend.json`. Either the table allows the Films P0-P6
  shape, or Films-lane projects live in the Films repo (see P4).
- [ ] P4 Decide where `projects/moonshot-launch/` lives from now on. Under the routing rule it is Films work.

## For other repos
- Films `skills/melius-cut-frames/SKILL.md` "Lessons": L7 prop-first chaining. L8 cord colour stated in
  every insert, and "ONE hand only, his right, the left hand out of frame". A face lock alone does not hold a
  secondary character across variations, so build a sheet. Open as a branch and PR in the Films repo when approved.

## Next session starts here
```
Launch preview: script v6 is of record (projects/moonshot-launch/script.md, Melius canvas c53d2818).
START set approved, 02b v2 recommended. Open: line 10 speaks the price against Dylan's
no-price rule (producer's call); Jove sheet; jacket-off wardrobe state; real-place photos.
No video yet. Higgsfield connector needs re-auth before any video.
```
