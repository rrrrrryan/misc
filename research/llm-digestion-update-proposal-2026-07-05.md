# LLM Digestion Update Proposal — 2026-07-05

This repo is currently tight and coherent: it is mostly a **repo-understanding toolkit**.

The highest-signal update since the last push is not "add more random links." It is to expand the repo one notch outward:

- from **understanding unfamiliar codebases**
- to **digesting high-volume LLM output through better intermediate representations**

That is the common thread running through a lot of the recent captures.

## Recommendation

Do **not** turn `misc` into a generic AI-thoughts dump.

Do:
- keep the repo focused on **how to digest generated information safely and quickly**
- add one new adjacent cluster around **artifact-first LLM digestion**
- update the existing repo-understanding docs with a few new ideas that clearly belong there

## Best Additions

### 1. Add `research/llm-output-digestion-playbook.md`

Purpose:
- practical guide for understanding LLM outputs when the raw transcript or raw diff is the wrong first surface

Core thesis:
- do not start with the full output
- start with a better representation

Suggested sections:
- when to use artifact-first digestion
- representation ladder:
  - summary paragraph
  - architecture or wiring diagram
  - state machine
  - reasoning tree
  - invariant list
  - blast-radius map
  - exact raw output
- when to inspect traces vs outputs
- when to ask for compression vs when to ask for evidence
- "good enough" tests for understanding

Why it belongs here:
- it is the same family of problem as repo understanding
- generated code, generated plans, generated reasoning, and generated research all become easier to trust when you inspect an intermediate artifact first

### 2. Add `prompts/artifact-first-digestion-prompt.md`

Purpose:
- copy-paste prompts for forcing models to transform raw outputs into inspectable artifacts

Prompt families to include:
- "turn this diff into an architecture recap"
- "turn this reasoning trace into a tree of revisions and pivots"
- "turn this long answer into claims / evidence / uncertainty"
- "turn this workflow into a state machine"
- "turn this system explanation into a wiring diagram"
- "turn this generated doc into final-reader-safe prose with no revision breadcrumbs"

This should be short and practical, closer to `repo-understanding-prompt.md` than to an essay.

### 3. Update `research/repo-understanding-playbook.md`

Keep the repo-understanding focus, but add three small ideas that now seem important:

1. **Agent traces are a first-class review surface**
   - not just code diffs
   - not just final summaries
   - sometimes the best review target is the plan, trace, or recap artifact

2. **Visual recaps beat prose walls**
   - architecture-first review
   - diagrams before line-by-line trust
   - state and flow surfaces for slippery logic

3. **Final artifact hygiene matters**
   - generated docs or code explanations should not mention invisible prior drafts
   - if the reader did not see the earlier state, the final artifact should not act like they did

These belong in the existing playbook rather than a separate philosophical note.

### 4. Add `research/representation-ladder.md`

Purpose:
- compact reference for choosing the right representation for the thing you are trying to understand

Example ladder:

1. headline / thesis
2. structured summary
3. visual overview
4. invariants / constraints
5. concrete path or example
6. raw transcript / raw code / raw trace

The point:
- raw output is often the **last** thing you should inspect, not the first

This would work well as a standalone reusable reference.

### 5. Add `research/cognitive-load-and-review-rhythm.md`

This is the most optional file, but I think it is worth adding if you want the repo to support a talk.

Core idea:
- stronger models can increase output while worsening day-to-day cognitive load
- so digestion is not just an information problem, it is also an ergonomic one

Suggested content:
- productive-but-drained paradox
- heavy review early, lighter exploratory work later
- physical resets and rhythm design
- choosing representations that reduce cognitive drag
- when to stop asking for more output and ask for a better artifact instead

This file is the bridge between "tooling" and "human factors."

## Best Source Material Since Last Push

These are the strongest recent sources to seed the above updates.

### Artifact-first review and digestion

- Matt Pocock — code review is a scale, not a binary; agent traces belong on the review surface  
  `https://x.com/mattpocockuk/status/2073711736838918436?s=12`

- Ole Lehmann — good prompting is really extracting missing context before execution  
  `https://x.com/itsolelehmann/status/2073740677175996453?s=12`

- stevibe — render LLM self-corrections as branching trees  
  `https://x.com/stevibe/status/2073784489856450916?s=12`

- Viem — image-led conceptual diagram for centered vs centerless attention  
  `https://x.com/viemccoy/status/2073859679772684728?s=12`

### Final artifact hygiene

- Drew Breunig — models leaking revision-history framing into final docs  
  `https://x.com/dbreunig/status/2073811538553741552?s=12`

- dex — "no breadcrumbs" as the practical rule for final docs and code  
  `https://x.com/dexhorthy/status/2073855036279402660?s=12`

### Representation and interface design

- Maxime Rivest — "Tom Riddle's diary" framing; interface translation matters  
  `https://x.com/maximerivest/status/2073544461473169432?s=12`

- Omar / elvis — Fable for world generation + realtime model for interaction  
  `https://x.com/omarsar0/status/2073865696253980735?s=12`

- Séb Krier — MJ 8.1 game-art moodboard; coherent worlds > isolated pretty images  
  `https://x.com/sebkrier/status/2073918367866458159?s=12`

### Ergonomics and cognitive load

- David Sholz — people feel more productive and more drained with coding models  
  `https://x.com/davidsholz/status/2073923496821002533?s=12`

- Minh Nhat Nguyen — split heavy focused vibecoding earlier and lighter/funner work later  
  paired in vault with the David note

## What I Would Not Add

To keep this repo useful, I would **not** add:

- broad speculation about model weirdness unless it cashes out as workflow guidance
- generic frontier-model hype
- every AI-taste post
- market or macro notes unless they directly inform digestion / review / representation

Examples that are interesting but probably out of scope here:
- AI labor-market competition arguments
- Taiwan receipt-lottery mechanism design
- general alpha or market-information notes

## Suggested Repo Shape After Update

```text
misc/
  README.md
  design.md
  prompts/
    repo-understanding-prompt.md
    artifact-first-digestion-prompt.md
  research/
    repo-understanding-playbook.md
    repo-understanding-tools.md
    llm-output-digestion-playbook.md
    representation-ladder.md
    cognitive-load-and-review-rhythm.md
    llm-digestion-update-proposal-2026-07-05.md
  scripts/
    repo_map.py
```

## My Actual Recommendation

If you want the smallest high-value update, do only this:

1. add `research/llm-output-digestion-playbook.md`
2. add `prompts/artifact-first-digestion-prompt.md`
3. patch `research/repo-understanding-playbook.md` with:
   - trace review
   - visual recap
   - no-breadcrumbs hygiene

That gets you a coherent expansion of the repo without diluting what it already does well.
