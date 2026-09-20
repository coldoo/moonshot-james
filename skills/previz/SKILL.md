---
name: previz
description: Build a scrappy video previz of a product concept from a scene list. One hero character, stills as start frames, cheap image-to-video with native audio, assembled with captions. Use when the producer asks for a previz, concept pass, or "just show the use cases".
---

# Previz

Proven on the Moonshot previz, 2026-09-19/20: 7 scenes, 665 credits, about a day of
producer attention. Every step below is what actually worked, including the failures.

## Inputs from the producer

- Scene list: one paragraph per scene with what we see, what he does with his hands, and
  the spoken line if any. Ask for it scene by scene; do not invent scenes.
- Product reference images, into `projects/<name>/assets/`.
- Answers to: aspect ratio, product finish, whether the device answers on screen.

## Stage 1 · Shotlist

Write `shotlist.json` with one entry per scene: id, action, camera, ask, label. Present it
in plain words and stop. The producer edits it in conversation; write the edits back.

## Stage 2 · Hero character (2 credits × 4)

One still of the hero in a neutral doorway wearing the product, `nano_banana_pro`, 16:9,
4 variants, product image attached as `image_references`. One-sentence character, no face
detail. Producer picks one. That job id is now `@character` for everything else.

## Stage 3 · Scene stills (2 credits each)

One prompt per scene, 4 variants, references = hero job id + product media id. Template:
`templates/still-prompt.template.md`. Batches of 12 through `generate_image_batch`.
Download every result, build a contact sheet per scene with `scripts/contact_sheet.py`,
send the sheets, stop. Producer picks.

Redo rules that worked:
- Same location across two scenes: attach the approved still of the first scene as a third
  reference and say "the exact same kitchen as the attached kitchen reference".
- Night version of a day scene: same prompt plus "late at night, desk lamp on, window dark
  with the room reflected".
- A photo-in-photo must show the device's point of view, not a third-person still. Ask the
  producer what the device would have seen before generating it.

## Stage 4 · Video (20 credits per 8 s, 15 per 6 s)

Model `minimax_h3_max`, 768p, 16:9, `batch_size: 3`. It rejects `start_image` mixed with
`image_references`. Pass three `image_references` in this order and label them in the prompt:

```
REFERENCES: Image 1 is the STARTING FRAME: <what it shows>; the first frame of the video
matches it and the scene continues from it. Image 2 is THE MAN, for consistency: <one
line>. Image 3 is THE PRODUCT, for consistency: <one line>, never redesigned.
SUMMARY: <two sentences on what happens>
TIMESTAMPS:
0-2.5s: ...  (2 to 4 beats; spoken lines in quotes; sound inline)
GENERAL RULES: identity lock, casual phone footage, no music, no on-screen text, never
show the product reference image itself, no cutaway, no visual effects.
SETTING: <room and light>, exactly as in image 1.
```

Higgsfield will try to redirect evening scenes to the "IN THE DARK" preset; pass
`declined_preset_id` and resubmit. Only the first job id comes back; find the other takes in
`show_generations` by matching prompt and thumbnail.

Run the first two scenes, stop, let the producer pick, then run the rest. Build a review
grid per scene (rows = takes, columns = 0/2/4/6 s). Report what you can see; say plainly
that you cannot hear the line reads.

Known failure modes and the fix for each: `references/minimax-h3-max.md`.

## Stage 5 · Assembly (0 credits)

`python scripts/assemble.py projects/<name> --labels --overlays --trim-head 0.5 --trim-tail 0.5`

- Clean cuts. No slates, no black cards, no freeze frames unless asked.
- Label tag: translucent box top-left for the first 2.2 s of each clip, from `label`.
- Reply captions: `reply` and `reply_at` per scene; time them to when he starts speaking.
- Lines the producer supplies for captions must match what the footage actually shows.
- Producer notes come as film timecodes; map them to scenes before editing.

## Credit discipline that held

Show every prompt and the credit count, wait for go, batch, review, then redo only the
scenes that need it. Coverage of 3 takes per scene gave one usable take per scene with
one redo round for about half the scenes.
