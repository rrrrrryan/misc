# LLM Output Digestion Playbook

This is the sibling of the repo-understanding playbook.

The problem here is not an unfamiliar repository. It is a familiar modern failure mode:

- the model produced too much
- the output is not obviously trustworthy
- the raw transcript is the wrong first surface

## Core Principle

Do not start with the full output if a better representation can be generated first.

Start by asking:
- what am I trying to understand?
- what representation would make that easiest to inspect?
- what evidence do I need before I trust it?

## When To Use This

Use this when:
- a model produced a very long answer
- a coding agent produced a large plan, diff, or trace
- the output feels impressive but slippery
- you need to review quickly without becoming careless
- you want a talkable artifact instead of a giant transcript

## The Representation Ladder

Move down this ladder only as needed.

1. headline or thesis
2. structured summary
3. visual overview
4. invariants or constraints
5. concrete path or worked example
6. raw transcript, raw diff, or raw trace

Raw output is often the last thing you should inspect, not the first.

## Best First Surfaces

### For generated code

Ask for:
- architecture recap
- subsystem boundaries
- wiring diagram
- blast-radius note
- one concrete request path

### For generated reasoning

Ask for:
- claim list
- evidence list
- uncertainty list
- reasoning tree of revisions and pivots
- shortest path to the conclusion

### For generated workflows

Ask for:
- state machine
- sequence diagram
- invariants
- error paths
- handoff points between agents or tools

### For generated prose

Ask for:
- reader-safe final version
- no-breadcrumbs rewrite
- list of claims that need evidence
- list of assumptions that were smuggled in

## Good Default Workflow

1. Get the headline.
   - what is this output trying to do?
   - what is the strongest claim?

2. Ask for the best representation.
   - diagram
   - state machine
   - reasoning tree
   - claims/evidence/uncertainty list
   - blast-radius map

3. Ask for invariants and risks.
   - what must remain true?
   - what could silently be wrong?
   - where is confidence low?

4. Force one concrete path.
   - one request path
   - one worked example
   - one before/after flow
   - one step-by-step execution path

5. Only then inspect the raw output.
   - read the critical sections
   - spot-check against the artifact
   - look for contradictions

## When To Inspect Traces

Inspect traces when:
- the model changed course repeatedly
- the final output looks too clean to trust
- the review target is process quality, not just final correctness
- you are comparing how different models think, not just what they answered

Do not inspect the whole trace by default.

Ask for:
- pivot points
- abandoned branches
- revised assumptions
- where confidence changed

## When To Ask For Compression vs Evidence

Ask for compression when:
- the output is too long to hold in working memory
- you need orientation
- you are trying to find the real complexity

Ask for evidence when:
- the summary sounds persuasive but vague
- the claim matters operationally
- the model is flattening uncertainty
- you are about to repeat the claim in public

## Final Artifact Hygiene

Do not let reader-facing artifacts inherit invisible process residue.

Bad:
- "this replaces the previous version"
- "unlike the earlier draft"
- "as mentioned above" when there is no visible above

Good:
- describe what is true now
- keep revision process in separate notes
- keep final artifacts readable without backstage context

## Good Enough Test

You are done when you can answer:
- what this output is trying to say
- what representation makes it easiest to inspect
- what must be true for it to be useful
- where uncertainty remains
- what part of the raw output is still worth reading

## Bottom Line

The bottleneck is not just model verbosity.

It is choosing the wrong first representation.

If you inspect the right artifact first, raw output becomes something you verify selectively instead of something you drown in.
