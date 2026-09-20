# Still prompt template — previz, Nano Banana 2

Previz rule: **simple characters.** One sentence on the person. No face anatomy, no skin
detail, no hair strands. Nobody will look at their face. The action and the pendant are the
shot. The full-detail Soul 2 structure in `references/prompts/soul2-character-ugc.md` is for
production character sheets, not for this.

Keep the ordering from the producer's Soul 2 prompt, but each block is one sentence.
Target: under 700 characters per prompt. Untested on Nano Banana 2; revise after S00.

## Blocks, in order

1. **Opener**: "A photorealistic iPhone photo of" + who, one sentence. Age range, one
   clothing item. Nothing about the face.
2. **Action**: from `shot.action`. What they are doing, where the hands are.
3. **Pendant**: verbatim `shotlist.product_clause` + "matching the attached reference image".
   Attach the reference every time.
4. **Framing**: from `shot.camera`. Height, distance, angle. Aspect stated.
5. **Setting**: the place plus two or three ordinary objects.
6. **Light**: source and quality, one clause.
7. **Realism + negatives**: one fixed sentence, identical every prompt:
   "Casual unpolished phone snapshot, natural skin, no beauty filter, not cinematic, not
   glossy, no dramatic color grading, no text, no graphic overlays."

## Rules

- All prompts written to `projects/<name>/stills/prompts.md` and shown before generating.
- S00 first and alone. Wait for approval of the pendant.
- Then batches of five maximum, fresh go each time.
- Save results as `stills/<shot-id>_v<n>.png` with the prompt beside it as `.txt`.
- Working and failing prompts get copied verbatim into `references/nano-banana-2.md` after
  the run, with a one-line note.

## Hero character shortcut (previz only)

When one character carries every scene, generate them first in a neutral setting wearing
the product (H00). That image validates the product and becomes the character reference.
Every scene prompt then opens with "the man from the attached character reference" and
attaches H00 plus the product reference. This is a previz shortcut, not the production
method, which uses proper character sheets.

## Worked examples

See `projects/moonshot-previz/stills/prompts.md` for the full set of eight built from this
template, including the H00 hero validation shot.
