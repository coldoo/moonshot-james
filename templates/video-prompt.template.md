# Video prompt template — image-to-video from an approved still

Follows the Seedance 2.5 structure in `references/seedance-2.5-video.md`. Works as a
starting shape for Kling and others too; adjust once we have results per model.

For previz: one beat, 5 seconds, the still is @image1, product reference is @image2.
Keep it short. The still already carries the look.

```
SHOT: <shot id> — <one line from shotlist.action>
REFERENCES: @image1 is the approved still for this shot, locked framing, person, setting and pendant. @image2 is the Moonshot pendant, locked design.
CHARACTER @image1: the person as shown. <clothing from the still>. Face stable throughout, no deformation.
SETTING @image1: as shown. Same light, same objects.
CAMERA: <from shotlist.camera>. <from shotlist.animate_hint>.
SEQUENCE:
0–5s: <the action as physical movement, one beat>. <camera move>. <diegetic sound only>.
STYLE: <project style prefix from style.md>. 16:9, 5 seconds, 24fps. No music.
negative: no face morph, no pendant redesign, no added text
```

## Rules

- Emotion as body movement. Write what the body does, not what the person feels.
- One sound per beat, inline. Room tone counts.
- Never request slow motion. Retime after.
- Never request on-screen text. Overlays come from the shotlist in assembly.
- Negatives only for problems actually seen. Start with the three above and grow the list
  from results.

## Example, S04 (steak, future)

```
SHOT: S04 — months later, wearer holds the pan up toward the pendant with mock suspicion
REFERENCES: @image1 is the approved still for S04, locked framing, person, kitchen and pendant. @image2 is the Moonshot pendant, locked design.
CHARACTER @image1: the man as shown, dark t-shirt. Face stable throughout, no deformation.
SETTING @image1: as shown. Same kitchen, same evening light.
CAMERA: medium, eye level, static. Small handheld drift only.
SEQUENCE:
0–5s: He lifts the pan a few inches toward the pendant on his chest, one eyebrow rises, head tilts a fraction, then he holds still and waits. Faint sizzle from the pan, kitchen hum.
STYLE: casual unpolished phone footage, natural skin, not cinematic, not glossy, no dramatic color grading. 16:9, 5 seconds, 24fps. No music.
negative: no face morph, no pendant redesign, no added text
```
