# Artifact-First Digestion Prompts

Use these when the model output is too long, too slippery, or too risky to trust as raw text.

The goal is to force a better intermediate representation before reading the full output.

## Architecture Recap Prompt

```markdown
Do not summarize this output as a wall of prose.

Turn it into an architecture recap:
- top-level components
- responsibilities
- boundaries
- one concrete end-to-end flow
- likely risks or hidden coupling

If helpful, include a simple diagram or ASCII map.
Optimize for inspection, not completeness.
```

## Reasoning Tree Prompt

```markdown
Turn this reasoning trace into a tree of pivots.

Show:
- initial approach
- where the model changed its mind
- abandoned branches
- revised assumptions
- final path that survived

Do not restate the whole trace.
Compress it into a structure I can inspect quickly.
```

## Claims / Evidence / Uncertainty Prompt

```markdown
Rewrite this output into three sections:
1. claims
2. evidence
3. uncertainty

For each claim, say whether the evidence is explicit, inferred, or missing.
Call out any leap that sounds confident without enough support.
```

## State Machine Prompt

```markdown
Turn this workflow into a state machine.

Include:
- states
- transitions
- retries
- failure paths
- exit conditions

If useful, render it as Mermaid or simple text.
```

## Wiring Diagram Prompt

```markdown
Turn this system explanation into a wiring diagram.

Show:
- inputs
- outputs
- transformations
- external dependencies
- storage or persistence hops

Keep the focus on flow, not prose.
```

## Final-Reader Hygiene Prompt

```markdown
Rewrite this for a final reader.

Rules:
- no breadcrumbs
- do not mention invisible prior drafts
- do not refer to what used to be true
- do not narrate the editing process
- only describe what is true now

If there is process history worth preserving, put it in a separate notes section.
```

## Blast Radius Prompt

```markdown
I do not want a line-by-line explanation.

Tell me:
- what boundary this output crosses
- what depends on it
- what invariant could silently break
- which 3 to 7 raw sections I should actually inspect
```

## Best Representation Prompt

```markdown
What is the best representation for understanding this output quickly and safely?

Choose one primary representation:
- architecture recap
- wiring diagram
- state machine
- reasoning tree
- claims/evidence/uncertainty list
- blast-radius map

Explain why that representation is the right first surface, then produce it.
```
