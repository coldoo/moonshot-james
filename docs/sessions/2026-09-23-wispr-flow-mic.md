---
date: 2026-09-23
session: 3b00745d-edf7-4325-ba9c-f77823414750
title: Wispr Flow microphone troubleshooting
repo: none (machine support, run from C:\moonshot-pipeline)
pr: none
spend: {}
tags: [dictation, input-quality, session-hygiene]
written_by: backfill, 2026-09-23
---

# Wispr Flow: why dictations fail

## What happened
Nothing was broken. 181 of the last 218 dictations worked. The failures were: no text box focused (51),
the push-to-talk key (Right Alt) tapped instead of held (28), "press enter" not said as the final words, and
the mic auto-switching between devices (9). Nothing was changed on the machine.

## Learnings

### L1. Most of the producer's messages to agents are dictated, so proper nouns arrive misheard
- Evidence, from the 2026-09-18 session: "Mushan" for Moonshot, "Joke" for Jove, "Milios" and "Amelia" for
  Melius, "code off" for coat off, "stick" for steak, "seedabce" for Seedance, "Frank" at the start of a
  pasted reply. The agent read them right, but every one is a chance to act on the wrong word.
- Fix: add Moonshot, Melius, Jove, Dylan, Higgsfield, Seedance, MiniMax, Nano Banana and Polaroid to
  Wispr Flow's dictionary.
- Goes to: `~/.claude/CLAUDE.md` Sessions note: read dictated input for sound-alikes of project names, and
  confirm when a misheard word would change a paid action.

### L2. A dictation that "didn't work" is usually on the clipboard
- Evidence: 51 of the failures showed "Select a text box first", and the text was copied to the clipboard.
- Fix: Ctrl+V before re-dictating.
