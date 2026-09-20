# MiniMax H3 Max — image-to-video notes

First used 2026-09-20 on the Moonshot previz. 768p, 16:9, native audio, 20 credits per
8 s, 15 per 6 s. `batch_size` up to 4 makes sibling jobs from one prompt; only the first
job id comes back from the call, the rest appear in generation history with the same
prompt and thumbnail.

## Hard constraint
Rejects `start_image` mixed with `image_references` (422). Workaround that worked: pass
the start frame as the FIRST `image_references` entry and label all images in the prompt:
"Image 1 is the STARTING FRAME ... Image 2 is THE MAN ... Image 3 is THE PRODUCT". The
model honoured the labels: first frame matched the still, hero matched the sheet, pendant
matched the product image, across 21 of 21 takes.

## Higgsfield preset nudge
Prompts describing dim or evening scenes get intercepted with a suggestion to use the
"IN THE DARK" preset. Nothing runs until it is declined with `declined_preset_id`.

## Prompt shape that worked
REFERENCES (labelled images) → SUMMARY → TIMESTAMPS (2–4 beats with inline sound and any
spoken line in quotes) → GENERAL RULES (identity lock, style, no music, no text) → SETTING.

## Observed failure modes (Moonshot previz, 21 takes)
- **Cut to the product reference.** One take of a quiet hallway scene cut away to a
  beauty shot of two pendants on a table, straight from the product reference image, then
  to the man in a different doorway. Add to negatives: "never show the product reference
  image itself, no product beauty shot, no cutaway".
- **Looking into the lens.** When the prompt has him speak and does not fix the eyeline,
  roughly half the takes have him deliver the line to camera. Fix the eyeline explicitly
  in the beat: "eyes stay on the steak", "eyes on nothing, never toward the camera".
- **Cut continuity.** When a prompt asks for a CUT to a new angle, one in three takes
  changed the room. Add "same room, same window, same counter" to the cut beat.
- **Invented light effects.** One take added glowing particles around a framed photo,
  presumably reading "what happened right after this" as a magical reveal. Add "no visual
  effects, no glow, no particles" to negatives on any scene where the device is addressed.
- **Front-door walk-in.** With a start frame of him already inside, only one of three takes
  actually staged the entrance. If the walk-in matters, the start frame should show him
  in the doorway.
