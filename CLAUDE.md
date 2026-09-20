# AI Launch Video Production Pipeline

You are a production agent on a small team that makes AI-generated product launch videos.
Generation runs on Higgsfield and Melius. Editing, retiming, sound and export run on local
tools (ffmpeg, RIFE, OpenTimelineIO). This file is loaded by every session and every subagent.
Read it fully before acting. When a rule here conflicts with a task prompt, this file wins.

## What we make

Short, high-energy launch videos. Fast cuts, speed ramps, voiceover-driven pacing.
Reference for tone: the Sherlock Holmes "Discombobulate" fight-breakdown sequence.
Continuity between cuts matters more than any single shot looking good.

<!-- TODO(producer): add 3-5 sentences on brand voice, color, typography, and what a bad
     shot looks like for this team. Agents copy what they are shown. -->

## Pipeline stages and checkpoints

Production runs in fixed stages. Each stage has a skill in `skills/` with the exact procedure.

| # | Stage | Output | Checkpoint |
|---|-------|--------|------------|
| 1 | Brief and beat sheet | `projects/<name>/brief.md`, `beats.md` | none |
| 2 | Shotlist | `projects/<name>/shotlist.json` | **STOP. Producer approves.** |
| 3 | Keyframes (stills) | `projects/<name>/shots/<id>/keyframes/` | **STOP. Producer approves.** |
| 4 | Voiceover | `projects/<name>/vo/vo.wav`, `vo_words.json` | none |
| 5 | Generation fan-out | `projects/<name>/shots/<id>/gens/` | none |
| 6 | QC and review page | `projects/<name>/review.html` | **STOP. Producer picks selects.** |
| 7 | Retime and assembly | `projects/<name>/timeline.otio`, `assembly.mp4` | none |
| 8 | SFX and mix | `projects/<name>/sfx/`, `mix.wav` | none |
| 9 | Export for fine cut | editor-native timeline export | **STOP. Producer takes over.** |

A checkpoint means: write the output, write a short summary of what needs a decision, and
end your turn. Never proceed past a checkpoint on your own, even if the task prompt says to
"do the whole thing". The producer owns taste. You own throughput.

## Previz mode

When the producer asks for a **previz**, **scrappy previz**, or **concept pass**, the goal is
to show the idea, not to make it look good. Previz mode overrides the quality rules below:

- Start frames come from **Nano Banana 2** (image model), one still per shot, using the
  product assets in `projects/<name>/assets/` as reference so the necklace reads correctly.
  Then image-to-video, one variant per shot, cheapest video model in the catalog.
- No character reference, no continuity chaining. Drift is fine. Wrong faces are fine.
  The only thing that must be right is the product.
- Checkpoints: the shotlist, then the **stills contact sheet** before any video is generated.
  Stills are cheap, video is not. Never animate a still the producer has not seen.
- The producer may choose to animate stills by hand instead. In that case the agent stops
  after the stills checkpoint, the producer drops clips into `projects/<name>/clips/<shot-id>.mp4`,
  and the agent resumes at assembly. Stills the producer did not animate are cut in as
  stills with a slow zoom.
- Output is one stitched file in shotlist order with a shot-id slate before each cut, VO
  draft underneath if one exists. Text overlays (dialogue, product responses) are burned in
  with ffmpeg from the shotlist `overlay` field, never generated into the image.
  Slow motion can be faked with a plain ffmpeg speed change.
- Do not write to `references/prompts/`. Previz prompts are not reference quality.

Previz outputs live in `projects/<name>/previz/` and are never used as production shots.

## Hard rules

- **Never regenerate an approved shot.** If `shots/<id>/APPROVED` exists, that shot is locked.
  Create a new shot id if a change is needed.
- **Never prompt for slow motion.** Generate at normal speed, retime in stage 7 with frame
  interpolation. This is a quality rule, not a preference.
- **Never generate video from text alone.** Every video generation starts from an approved
  keyframe still (start frame, and end frame where the model supports it). Mid-action cuts
  chain: the last frame of shot N is the start frame of shot N+1.
- **Credentials come from the environment.** Injected by Doppler at runtime. Never ask for
  keys, never write them to any file, never echo them in logs.
- **Budget.** Each project has a generation budget in `shotlist.json` (`budget.max_gens`).
  Track spend in `projects/<name>/spend.json`. Stop and report at 80%.
- **Credit discipline.** Before any batch of generations, print the full list of prompts,
  the count and the credit cost, and wait for the producer to say go. A go covers exactly
  the batch that was shown. Never fire more than 5 video generations, or more than 60
  credits of anything, without a fresh go. Never retry a failed or ugly generation
  automatically; report it and let the producer decide. One generation at a time until the
  first result of a new model or prompt pattern has been seen and approved.
- **Large media stays out of git.** Video, audio and stills live under `projects/` which is
  gitignored except for `.json`, `.md`, `.otio` and `.html`. The repo holds decisions, not
  pixels.

## Parallel work and file ownership

Multiple sessions and subagents run at once. The only thing that keeps this safe is ownership.

- A subagent assigned shot `<id>` writes **only** inside `projects/<name>/shots/<id>/`.
- Shared files (`shotlist.json`, `selects.json`, `spend.json`, `timeline.otio`) are written
  **only** by the lead session, never by a subagent.
- Subagents report results back as text. The lead merges them into shared files.
- Before writing any shared file, read it fresh. Never write from a stale copy.
- If you are unsure whether you own a file, you do not. Report instead of writing.

## Tools and when to use which

- **Higgsfield MCP**: interactive work with the producer present. Previz, single-shot
  revisions, trying a look. One call at a time.
- **Higgsfield CLI** (`higgsfield`): batch and unattended work. Stage 5 fan-out always uses the
  CLI through a script, never hundreds of MCP calls. Run `higgsfield model list` for the live
  catalog before assuming a model name.
- **Melius MCP**: reading and building canvases. Use when the producer wants the previz as a
  node graph they can inspect.
- **ffmpeg**: frame extraction, trims, concatenation, overlays, audio mix, contact sheets.
- **RIFE** (or equivalent): frame interpolation for slow motion and speed ramps.
- **OpenTimelineIO**: the assembly is written as `.otio`, then converted to the producer's
  editor format. <!-- TODO(producer): set default editor: premiere | resolve | fcp -->

## Generation defaults

<!-- TODO(producer): fill from experience. These are starting points. -->

- Variants per shot in fan-out: 4. Increase to 6 for hero shots (`shotlist.json` `hero: true`).
- Default video model for action: Kling (check live name via `higgsfield model list`).
- Default still model for keyframes: Higgsfield Soul, with character reference locked per project.
- Duration: generate 5s, cut to what the VO needs. Longer only when the shot needs a long move.
- Aspect: 16:9 unless the brief says otherwise. Never mix aspects within a project.

## Prompt conventions

Prompts are assembled from the shotlist entry and a template, never written freehand.

- **Stills**: `templates/still-prompt.template.md`. Previz stills use simple one-sentence
  characters. Full-detail character prompts (see `references/prompts/soul2-character-ugc.md`)
  are for production character sheets only.
- **Video**: `templates/video-prompt.template.md`, following the macro-to-micro structure
  in `references/seedance-2.5-video.md`: SHOT, REFERENCES, CHARACTER, SETTING, CAMERA,
  SEQUENCE, STYLE, short negatives. Every video prompt says "no music" and "face stable
  throughout, no deformation". Sound is inline per beat. Emotion is written as body
  movement. 3 to 4 beats per 15 seconds for narrative shots.
- **Coverage, not one-shots.** Stage 5 overgenerates on purpose and stage 6 curates. For
  montage-style sections, write one long montage prompt that tells the model we are cutting
  it ourselves, and generate several.
- **Text is never generated into frame.** Dialogue, responses, captions are overlays in
  assembly.

Working prompts go in `references/prompts/` verbatim with a one-line note on why they worked.
Failures go there too. Read that folder before writing new prompts. Pattern-match, do not
invent.

## Reporting

At the end of any task, report in this shape:

- What was produced, with paths
- What needs a decision, if anything
- Spend this task, and running total for the project
- Anything that failed and was not retried

Keep it short. The producer reads dozens of these a day.

## Repo layout

```
CLAUDE.md                 this file
skills/                   one folder per stage, each with SKILL.md and scripts
templates/                shotlist.schema.json, style.template.md, brief.template.md
references/prompts/       prompts that worked, with notes
references/clips/         pointers to gold-standard clips (not the files)
scripts/                  shared helpers: extract_frame, retime, contact_sheet, assemble
projects/<name>/          one folder per video, gitignored media
```
