# critical-patterns.md

Compounded learnings from `docs/sessions/`. A learning lands here when it has shown up in two or more
sessions, or when missing it cost a paid run or a producer "no". Each entry names its sources. `/closeout`
adds entries and sharpens existing ones. Promotion to a CLAUDE.md rule needs the producer's yes.
Same shape as the Films repo's `docs/solutions/patterns/critical-patterns.md`, so entries can move between repos.

1. **Confirm the deliverable's form before building it.** If a stage output could be read two ways, say
   which one you are building in one line and wait. Examples: stills slideshow or video, black cards or
   overlay box. Source: 2026-09-18 L1, L5.
2. **One job on a new model or new prompt pattern, then look.** Probe the schema or constraints first, for free
   where the tool allows. Two parallel first jobs on MiniMax H3 Max both hit the same 422. Source: 2026-09-18 L2;
   Films critical-patterns 1 ("probe before plan").
3. **Propose the cheapest rail that shows the idea, with the credit comparison beside it.** Previz is never on
   the premium model by default. Source: 2026-09-18 L3.
4. **If a model refuses a start frame mixed with references, send everything as references and label each
   image in the prompt.** Source: 2026-09-18 L4; `skills/previz/SKILL.md`.
5. **Lock a location by attaching the approved still of the same place as a reference.** Worked in the previz
   kitchen and in the launch preview's 02b. Source: 2026-09-18 L6 (two projects).
6. **Prop first.** Generate the object once, then wire it in as a reference for every frame it appears in.
   Source: 2026-09-18 L7.
7. **Before a paid run, check each prompt against the target repo's known-failure list.** For Films that is the
   `melius-cut-frames` prompt blocks and lessons, wardrobe world-logic, and sheets for recurring characters.
   Catching a known failure in review costs a redo. Source: 2026-09-18 L8, L9.
8. **Read shared state fresh before editing it.** The producer edits the Melius canvas and files between turns,
   and stale node ids fail. Source: 2026-09-18 L11; CLAUDE.md "Parallel work".
9. **Assembly defaults:** clean cuts, no black cards, no freeze frames, overlays in a translucent box, a caption
   appears when the line starts. Source: 2026-09-18 L5 (four rounds of notes).
10. **Ask for every missing pick in the pick request itself.** Never record a default pick silently. Source: 2026-09-18 L10.
11. **Windows on this machine:** the console is cp949, so run Python with `PYTHONIOENCODING=utf-8` (or `-X utf8`).
    Write multi-line scripts to a scratch file instead of long inline heredocs, and use the Bash tool for POSIX
    syntax, never PowerShell. Source: 2026-09-18 L13; hit again on 2026-09-23.
12. **Session hygiene.** Start in the repo folder, never a scratch workspace. Use one session per stage or
    checkpoint. `/closeout` writes the handoff so context never travels by copy-paste. Source: 2026-09-18 L12;
    2026-09-23 Wispr L1.
13. **Work lands in the repo whose rules govern it, and so do its lessons.** Film work goes to Films and copy work
    goes to Content (routing in `~/.claude/CLAUDE.md`). Source: 2026-09-18 L14; 2026-09-23 access L2.
