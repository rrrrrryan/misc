# Representation Ladder

When an LLM gives you too much information, do not ask first:

- "how do I read all of this?"

Ask:

- "what representation would make this easiest to understand?"

## The Ladder

Move from top to bottom only as needed.

1. **Headline**
   - one sentence
   - what is the main claim or purpose?

2. **Structured summary**
   - a few bullets
   - central claims
   - risks
   - unknowns

3. **Visual overview**
   - architecture diagram
   - wiring diagram
   - state machine
   - reasoning tree
   - sequence diagram

4. **Invariants and constraints**
   - what must remain true?
   - what assumptions are load-bearing?
   - what contracts or boundaries matter?

5. **Concrete path**
   - one worked example
   - one request path
   - one end-to-end flow
   - one failure path

6. **Raw output**
   - full transcript
   - raw diff
   - raw trace
   - source code

## Heuristic

If the thing is:

- **structural** -> ask for a diagram
- **logic-heavy** -> ask for a state machine
- **argumentative** -> ask for claims / evidence / uncertainty
- **process-heavy** -> ask for a trace tree or sequence diagram
- **risky** -> ask for invariants and blast radius

## Common Mistake

People often jump directly from:

- "the model said a lot"

to:

- "I guess I need to read the whole thing"

Usually that is wrong.

The right move is often:

- summarize
- externalize structure
- inspect a visual or structured artifact
- then read only the critical raw sections

## Good Default Question

Ask:

> What is the best representation for understanding this output quickly and safely?

## Bottom Line

The right representation reduces both:

- time to comprehension
- chance of false confidence

Raw output is not the gold-standard first surface.
It is often the fallback.
