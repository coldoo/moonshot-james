# Moonshot — Present / Future Previz

**Mode:** previz, stills only. The agent generates keyframes with Nano Banana 2. The producer
picks, animates them by hand, and drops clips into `clips/`. The agent then handles
transitions and assembly.

## Product

Moonshot, a pendant worn on a necklace. It captures life in the moment (video and audio) and
retains context, so it can help later with what it remembers. Reference images in `assets/`.

## Concept

Present versus future. Each scenario is shown twice: the moment Moonshot captures something,
then a later moment where that captured context comes back and helps.

The rhythm is: present, future, cut. Present, future, cut. Present, future, cut. Then a final
scenario that is not a pair but the payoff of everything: pattern recognition over months.

## Scenarios

**1. Relationships.** Present: two friends talking, wearer says "yeah, I can help you move
Saturday." Future: Friday. Moonshot nudges: you told them you'd help tomorrow, want to send
a text? Practical. It understands the person in front of you and your relationship to them.

**2. Cooking (comedic).** Present: wearer cooking a steak, asks how much longer. Future: five
months later, same kitchen, asks "how do I avoid overcooking this again?" Moonshot knows
exactly what went wrong last time.

**3. Memory.** Present: grandma at the piano, playing something for the wearer. Moonshot
recognizes this is a moment and captures it. Future: years later, wearer looking at a photo
from that day, asks "what happened right after this photo?" Moonshot recalls it.

**4. Pattern recognition (finale, not a pair).** Months of life, captured. Wearer asks
"what should I do more of?" or "how do I best manage my time?" Moonshot answers from
months of real context. The questions people ask themselves but can't answer alone.

## Visual convention for "Moonshot working"

The pendant glows softly. That is the only visual cue generated. Any notification text,
answer text or UI is added as an overlay in assembly, never generated into the image.

## Rules for this project

- People, faces and quality do not matter. The action must read, the pendant must be visible.
- Product must look like the reference in `assets/`. That is the one thing to get right.
- Stills only. No video generation by the agent on this project.
- Small batches. Show prompts, wait for go, five at a time maximum.

## Deliverables

1. `stills/` one or more Nano Banana 2 keyframes per shot, contact sheet for review
2. Producer animates selected stills by hand, drops MP4s in `clips/<shot-id>.mp4`
3. `previz/previz.mp4` assembled by the agent in shotlist order with transitions and overlays

## Unknowns

- VO or on-screen text for the Moonshot responses. Assumed overlay text for now.
- Aspect ratio. Assumed 16:9.
- Whether the "present" halves need a visible time marker (day, date) or the cut carries it.
