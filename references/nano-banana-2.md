# Nano Banana 2 — prompts and patterns

Status 2026-09-19: no Nano Banana 2 generations exist yet. The Moonshot previz is the first
run. Everything below the note is a hypothesis to be tested, not a pattern that is known
to work. Fill the sections as results come in, verbatim prompts only.

## Model note
On Higgsfield the catalog id is `nano_banana_pro`; the job runs as `nano_banana_2`. It
accepts multiple reference images under the role `image_references`, 16:9, 2 credits per
image at 1k or 2k. First run 2026-09-20.

## Successful prompts

### H00 hero + product validation (2026-09-20, 4 of 4 usable)
Reference attached: product macro image (both finishes). Result: pendant shape, wave
texture, lens position, gold finish and braided cord all accurate in every variant. Face
was near-identical across all four variants from one prompt, which is useful for a hero
character. Hair came out darker than "brown" suggests. Two variants rendered the t-shirt
as heather grey rather than dark.

"A photorealistic iPhone photo of an ordinary white man in his early 30s, short brown hair,
average build, in a plain dark crew-neck t-shirt, standing in a plain interior doorway,
relaxed, hands at his sides, looking just off camera. He wears a small rectangular pendant
with rounded corners at upper chest, metallic gold finish, flowing wave texture across its
lower front, a small camera lens at the top left, hanging on a thin black braided cord,
matching the attached product reference exactly. Medium shot, chest up, straight on at eye
level, 16:9. Neutral painted wall, a door frame, soft daylight from a window to one side.
Casual unpolished phone snapshot, natural skin, no beauty filter, not cinematic, not glossy,
no dramatic color grading, no text, no graphic overlays."

Why it worked: short, one-sentence person, product clause describes the physical object
in plain terms and points at the reference. The simplified template held up.

### Scene batch S01–S05, S07 (2026-09-20, 24 of 24 usable)
Two references attached to every prompt: the approved hero still (by job id) and the
product macro. Opening phrase "the man from the attached character reference, same face
and short dark brown hair, in his heather grey crew-neck t-shirt". Results: hero identity
held in all 24 stills across six different settings with no visible drift. Pendant accurate
in all 24. Secondary people (friend, grandmother) vary per variant as expected. Two
references via `image_references` role works; the model reads which is the person and
which is the product without explicit role labels. Prompts are in
`projects/moonshot-previz/stills/prompts.md`.

Observed: the model adds sensible environmental detail beyond the prompt (steam, kitchen
clutter, real-looking neighbourhoods). Screens and paper show plausible gibberish text,
fine for previz, never for production.

## Failed prompts
UNKNOWN: ask producer.

## Prompt structure pattern
UNKNOWN: ask producer.

## Known failure modes
UNKNOWN: ask producer.

## Note
The only image prompt in our history is a character-reference prompt for a
female actor, written for a different project. Structure used, verbatim:

"A photorealistic iPhone photo of a white woman in her late 30s standing in a
small lived-in bathroom, captured as a casual static UGC phone shot. She has
long thick dark brown hair with soft layers and wispy bangs, pale natural
skin, minimal makeup, and a calm neutral expression while looking directly at
the camera. She wears a loose faded blue graphic T-shirt with an open
oversized grey cardigan over it, a simple ring on one hand, and a black hair
tie around her wrist. Her arms hang naturally at her sides, hands relaxed and
visible, no props.

The framing is vertical 9:16 portrait, medium chest-up shot, captured straight
on from approximately countertop height with slight everyday asymmetry. Her
upper body fills most of the frame while part of the bathroom counter remains
visible along the bottom edge. The setting is an ordinary residential bathroom
with warm off-white walls, a white paneled door behind her, a round smoke
detector above the door, a brass wall light fixture partially visible in the
upper left, a black adjustable towel hook on the left wall, and a patterned
white hand towel with small blue floral details hanging beside her. A few
normal bathroom items are partially visible on the countertop in the
foreground.

Lighting is believable warm-neutral bathroom lighting mixed with soft ambient
indoor light, creating natural shadows and realistic skin tones without
dramatic contrast. Everything should have crisp natural iPhone realism with
visible individual hair strands, realistic skin texture, natural eye
reflections, true-to-life fabric and bathroom materials, and slight
phone-camera imperfection. The image should feel like an authentic unfiltered
creator snapshot, not a polished commercial image, not cinematic, not glossy,
no dramatic color grading, no beauty-filter skin, no fake lens effects, and no
added text or graphic overlays."

Observed structure: subject and setting, then physical description, then
clothing, then pose, then framing and camera position, then environment
detail, then lighting, then realism instructions, then a negative list.

Whether this structure works in Nano Banana 2 is untested.
