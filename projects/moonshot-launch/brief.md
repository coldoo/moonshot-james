# Moonshot Launch Video Preview: P0 brief

Format follows `references/external/moonshot-films/workflow/PRODUCTION-STAGES.md` P0. Provenance
tags per that repo's rule. Stage reported: **P0 closed 2026-09-22 (decisions below); P1 routed; P2 cast: Dylan lock exists, reuse; P3 pendant sheet v3 silver exists, reuse; P4 plates: not started, [NEED: real-place photos]; P5, P6 not started.**

```
PIECE          one launch video preview, presenter to camera, general audience. 35 to 45 s spoken
               (the producer's script reads at that length). 16:9 master, 9:16 cutdown later.
GOAL           you wear it, it pays attention, later you ask and it already has the moment. One swipe
               on, one swipe off.
AUDIENCE       public preview (waitlist, X, TikTok). Not the internal explainer.
REFERENCE      Dollar Shave Club launch ad (walk-and-talk, gags in the environment). The repo already
               holds a DSC treatment (R/12-script-v6-dsc.md, world/TREATMENT-01-dsc.md) and the
               Pocket cut map (R/09-pocket-15-cut-map.md) with camera moves by library name.
QUALITY BAR    identity held on the presenter across every cut; the pendant exact; realism of staging
               (people stand, move, varied expressions, nobody grinning at the lens).
MUST NOT       [canon, moonshot-films brand-context.md STOP block] no price in copy; no "assistant";
               no memory-as-the-pitch (the verb stays on the day, not the product); never end on a
               logo card; no ages or children; no phone calls or money features implied.
REGISTER       live-action photoreal, founder voice, deadpan. [OPEN: register] the moonshot-films
               lane is painted 2D; photoreal is the moonshot-launch-video lane. Recommend: photoreal,
               since the previz assets and the DSC treatment are photoreal. Dylan to confirm lane.
CAST           the presenter (proves the product is worn and forgotten); one friend or grandma
               (proves a moment was captured without him doing anything). [OPEN: presenter identity].
WORLD          his house: hallway, kitchen, the wall with the framed photo, the desk. Plates from
               real-place photos per AGENTS.md. Previz stills exist for each but are generated, not
               real-place; usable as composition reference only.
OBJECT         the Moonshot pendant. [OPEN: product truth] the registry flipped 2026-09-21 from the
               gold/blue wave tag (preorder site, the images the producer gave me 09-19) to a
               silver/black boxy body with a button-closed hatch. Recommend: whichever the current
               preorder page shows; do not build a sheet until confirmed.
CONSTRAINTS    Melius for stills, frames and consistency; Seedance 2.5 START-to-END for motion per
               the repo (MODEL-ROUTING.md). Budget ceiling per film in the repo: 3,000 Higgsfield
               credits. Melius credits: [OPEN: Melius plan and balance].
OPEN           presenter identity; use case A/B pick; product truth; register/lane; price line;
               "already has the moment" wording; Melius connected; Higgsfield re-authorised.
```

## P1 router (recommended, applied and named)
register live-action photoreal · reference origin: real-place photos for plates, real camera frame
for the presenter (AGENTS.md identity rule 2026-09-22) · who is in it: one person, a second in one
cut · length: one film cut from START-to-END shots · object: a real object we own, prop sheet from
the product page · rails: Melius for sheets, plates and frames; Seedance 2.5 for video.

## Decisions 2026-09-22 [DYLAN via producer]
- Presenter: Dylan, via face lock v3.1 A (Melius V6 canvas node 20c54436, APPROVED 09-21) and SHEET v3 Dylan + silver pendant (node 65930b52). Start with these; a real-camera pass can replace frames later.
- Lane: photoreal.
- Product truth: any of the four finishes is fine. Using SILVER (PRODUCT SHEET v3, node 9962e55d) because the Dylan sheet already carries it.
- Price line: a pop-up on screen only, not narrative. Still subject to the no-price-in-copy canon; kept as [OPEN: price line] on the card.
- Use case A: something simple, instantly recognisable, that uses the VIDEO layer (the camera). Use case B: a later ask that recalls what Moonshot snapshotted; the recall is the image or the context behind it. Exact pick: [OPEN], three options in the cut map.
- Melius credits: unknown, assumed sufficient. Nano Banana Pro is 188 Melius credits per image; Seedance 2.5 on Melius is 170 to 284 per second, so video stays on Higgsfield Seedance 2.5 per the repo's routing.

## Presenter identity [CLOSED: Dylan]
The repo rules (AGENTS.md, 2026-09-22): realistic human imagery needs a traceable real camera frame
and an original human identity source; a generated face lock is an aid, not a substitute. The
previz hero is a generated face with no real source. Options:
A. Dylan, via his approved face lock `@char_MS_founder_dylan_v3` and the real-reference method the
   repo already runs. Matches the V6 DSC script where he is the presenter. Recommend.
B. A new real person cast from their own photos, with their say-so.
C. The previz hero, accepted as a review-cut-only presenter, labelled as such, never shipped.

## Use case A / B [OPEN, blocking the cut list]
A must be a moment captured live with nothing asked; B must recall that exact moment.
1. Steak: A = flip question over the pan; B = weeks later, "what did I do wrong last time".
   Fast, funny, proves the mic. Weak on the camera.
2. Grandma at the piano: A = the moment, nothing asked; B = the framed photo, "what happened
   right after". Warm, proves the camera (the photo IS what it saw). Recommend for a public preview:
   it is the only pair that shows the product's visual capture, which is the 09-18 canon ruling.
3. Both, if the runtime allows: steak as A/B quick, then piano as the emotional close before the
   swipe-off. Adds about 10 s.

## Melius (created 2026-09-22)
- Project: "Moonshot Launch Preview - One Swipe (DSC shape)", id 12802868-c952-46c2-96b9-8b0df9e63a3d
- Canvas 1: c53d2818-f07f-4b0b-8acf-4c938b8be449
- Nodes: brief, script, use-case options, 11 cut cards, 3 locks copied from the V6 canvas (Dylan
  face lock v3.1 A, Dylan SHEET v3 silver, PRODUCT SHEET v3 silver), 11 START-frame image nodes on
  nano-banana-pro image-to-image wired from the locks and their cards. Nothing has been run.
- Layout: cards x 1080..2160, locks x 2160..2700, frames x 3180..4540; rows 665 px apart.
- Rule from the repo honoured: the frame prompts on the canvas are DRAFT composition notes; the
  director skill rewrites them before any paid run.

## Status 2026-09-22 (evening): v2 START frames run
- Script v2 (10 cuts) replaced the v0 piano/steak map. v2 column on the canvas: cards c01..c10,
  START-frame nodes F01..F10, 2 variations each, nano-banana-pro image-to-image. Bulk run
  c0e54635, 20 of 20 finished, no failures. Video NOT generated, by producer instruction.
- Spend: 3,760 Melius credits (20 x 188). Higgsfield: 0 this stage. Running Melius total for
  this project: 3,760.
- Agent review in `frames-v2-review.md`. Producer picks and redos pending (F03, F09 pendant held
  not worn; F04 Jove drift; puffer indoors).

## Status 2026-09-22 (night): v3 redo of five frames
- Producer notes on v2 applied: F01 chest close-up with fingers on the worn pendant, F04 Jove identity,
  F07/F08 tee only on the edge of the bed at 2 am with the new habits line, F09 putting it away.
- Bulk run d7b2743a, 10 of 10 finished. Spend 1,880 Melius credits. Project Melius total: 5,640.
- Review in `frames-v3-review.md`. Recommended picks: F01 v2 (cord fix), F04 either, F07 v2, F08 v1, F09 v1.

## Status 2026-09-23: hook frames run
- Script v4 adds hook cuts H01, H02 ahead of cut 01 (Polaroid on the fridge, nostalgic look, turn to
  camera). Phone dropped; answer as a card. Chain run a93ca883: P01 prop x1, H01 x2, H02 x2, no failures.
- Spend 940 Melius credits. Project Melius total: 6,580 of 221,000.
- Review in `frames-hook-review.md`. Recommended picks: P01 v1, H01 v1, H02 v2.
- START set now complete pending these picks: H01, H02, F01..F10. No END frames, no video generated.

## APPROVED 2026-09-23 [PRODUCER]: START set
H01 v1, H02 v2, P01 v1 (prop), F01 v2 (cord fix in edit), F04 v1, F07 v2, F08 v1, F09 v1; F02, F03, F05,
F06, F10 from v2 (variation not stated, v1 recorded, swap on request). Recorded in `selects.json`.
Locked: no regeneration of these frames; a change means a new frame id. Next stage (END frames or video)
not requested.

## Canvas reorganised 2026-09-23 [producer request]
FINAL column at the far left of canvas c53d2818 (prop x -2300, cards x -1700, frames x -1240), read top
to bottom: H01, H02, 01..10, with the Polaroid prop beside H01. The approved frame nodes were moved there
and each shows its approved variation. Draft columns stay to the right as history. Node ids and rows in
`selects.json`. F05, F06, F10 recorded as v2 (the displayed variation) since no pick was stated.

## Status 2026-09-23: cut 01 removed, 02b run
- Script v5. Film order H01, H02, 02b, 03..10. 01 and old 02 left the film (frames kept as history).
- 02b run a9100c7f, 2 variations, no failures. Spend 376. Project Melius total: 6,956 of 221,000.
- Review in `frames-v5-review.md`. Recommend v2 (black cord). Pick pending.

## Status 2026-09-23 (afternoon): script v7, six new frames run
- Script v7: hook, 02b, 03, NEW 03b, 04, 05, 06, NEW 06b, desk ending 07b to 10b (replaces bed and doorway).
  Blocking notes per cut in `cut-map-v7.md` for the live shoot that follows.
- One-pass chain run 1dc575fc: 07b once as the desk plate, five frames x 2. 11 renders, 2,068 credits,
  no failures. Project Melius total: 9,024 of 221,000.
- Review in `frames-v7-review.md`. Recommended: 03b v2, 06b v1, 07b (single), 08b v2, 09b v1, 10b v1.
- Routing: this is Moonshot video work and belongs in dylanpakd-cyber/moonshot-films-private on a
  james/ branch per ~/.claude/CLAUDE.md. No Films clone on this machine yet; producer to decide.
- 2026-09-23 later: 09c (pendant close-up) and 03c (empty background) run, 752 credits. Project Melius total: 9,776.

## Shot list 2026-09-23
- Google Doc (Claude Docs) "Moonshot Launch Preview, Shot List v7":
  https://claude.ai/code/artifact/2728eec8-717c-4cb0-bb97-76fc42d5a0a5
  Sections: how to use and running order (13 cuts, about 43 s), prep (cast, wardrobe states A/B/C, props,
  locations), the shot list with the approved frame per cut plus line, frame, camera, Dylan, movement, cut in
  and out, edit notes (three phone answers, one price block, no logo card), shoot order by location.
- Frames embedded as 1280 px JPEGs uploaded to the doc's asset store (14, including the Polaroid prop).
- 2026-09-23 evening: 02c (front door entry) run, 376 credits. Project Melius total: 10,152. Shot list trimmed to line/frame/movement.
- 2026-09-23 night: script v9 (claim, proof, name). H01 hook + two phone-close inserts run, 1,128 credits. Project Melius total: 11,280. v9 FINAL column built at x -3500; v7 column kept as history. Angles and cuts in cut-map-v9.md.

