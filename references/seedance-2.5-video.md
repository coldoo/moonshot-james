# Seedance 2.5 — image-to-video prompting

Distilled from a third-party guide the producer supplied on 2026-09-19. Method only, in our
own words. Not yet tested by us. Confirm against our own results and update.

## The mental model: coverage, not one-shots

Do not try to get the finished video from one generation. Generate more than you need, pull
the best moments, cut them yourself. Treat each generation like a day of coverage on a real
shoot. Most extra shots are unusable. Occasionally the model invents a shot better than the
one you wrote. This is the workflow, not a side effect.

Cost is the reason for every rule below. Roughly $0.50 to $1.20 per 5 second clip at API
rates, and a full 30 second 4K run is 2,000+ credits on credit platforms. Spend on coverage,
never on re-running a broken prompt hoping it fixes itself.

## Two prompt types

**Narrative prompt.** One continuous shot or a tight sequence. Under 3,500 characters.
3 to 4 beats per 15 seconds, hard ceiling. More beats feel rushed.

**Montage prompt.** Take 2 to 5 seconds of script and expand it into a 15 to 30 second
fast-cut montage. Tell the model explicitly that you are cutting it yourself in the edit and
want extra shots and options. Many beats, deliberately. Generate around 10 and harvest.
15 to 30 seconds is the sweet spot for these.

## Prompt structure, macro to micro

```
SHOT: name it, one line on what happens
REFERENCES: what each @imageN is. Lock this before anything else
CHARACTER @image1: identical description every time, plus action and feeling for this shot. Clothing locked
SETTING @image2: the place, light, materials. Matched to the environment sheet
CAMERA: lens, distance, movement, framing, light
SEQUENCE: time-coded beats. This is where the video lives
STYLE: your look, pasted identically in every prompt. Ratio, duration, 24fps
negative: short, only problems actually seen
```

## Four things in every prompt

1. **No music.** Diegetic sound only, described per beat. Music is added in the edit.
2. **"Face stable throughout, no deformation."** Written every time.
3. **@image discipline.** Every reference has a named role, numbered by order of appearance.
   Never cite an image the model will not receive.
4. **Short negatives.** Only list problems that have shown up in your own generations.

## Writing beats

Each beat: time range, shot type, action, camera, sound. Four rules:

- **Emotion is body movement.** Not "he is angry." Write what the feeling does to the body.
- **Physics, not vibes.** Every action has trajectory, distance, impact, reaction.
- **Sound inline, per beat.** Never a sound list at the end.
- **Rhythm through contrast.** Wide against macro, fast against still, impact frames, a
  held freeze. The rhythm is written into the beats.

## Cutting a longer story into prompts

- One narrative block, one continuity. Same references, same environment descriptor, same
  light. Copy paste between prompts, do not rewrite.
- Split at 3 to 4 beats per 15 seconds.
- Bridge with sound. End prompt A and start prompt B on the same audio cue.
- Match the frame at the cut. Write the same framing and eye placement in both prompts.

## References

- **Character sheet**: three angles of the face. Tag that image every time the person is
  mentioned.
- **Environment sheet**: two or three angles of the location.
- 4 to 10 references for narrative continuity. Up to 50 slots are supported.
- **For montages, go light.** Fewer references means more invention. Give it the rough
  environment and the style prompt and it holds the look.

## Style prompt

One paragraph describing the look, reused identically in the image model prompt and the
video prompt. Build it by handing imagery you love to a model and having it extract the
concrete things that make the look, as keywords. One description enforced at every stage.

## Known behaviour

- Text in frame is broken. Captions and overlays are done in the edit. This matches our
  overlay convention.
- Native sound effects are good, especially mechanical. Keep them.
- Native dialogue is usable for talking heads but generally skip it.
- Phone-camera honesty sells realism: slight shake, autofocus hunting, no gimbal smoothing.
- Objects should enter frame through a visible hand action.
- Speech direction with real pauses and filler reads as real.

## How this maps to our pipeline

- Stage 5 fan-out is coverage. Overgenerate and let stage 6 curate.
- Our "never prompt slow motion" rule stands. Speed changes are written as rhythm in beats
  or done in retime, not requested as an effect.
- Our overlay convention already assumes text is never generated.
- Previz: the producer animates stills by hand. A single narrative prompt per still, one
  beat, 5 seconds, using the template in `templates/video-prompt.template.md`.
