# Repo Understanding Prompt

Use this when a repo is too large, too fresh, or too AI-generated to read linearly.

The goal is to force a map first and only then read the critical code.

## Low-Stakes Repo Prompt

Best for:
- exploratory repos
- fast onboarding
- cheap mistakes
- quick orientation

```markdown
You are helping me understand an unfamiliar code repository quickly.

Do not start with a long line-by-line code summary.
Start by building a map of the repository.

Your job:
1. Identify the top-level structure of the repo.
2. Tell me what the system appears to do.
3. Find the likely entrypoints, core modules, and boundaries.
4. Trace one concrete request or data flow through the system.
5. Recommend the 5 to 10 files I should read first, in order.
6. Call out where the real complexity probably lives.

Output format:
- Short repo summary
- Top-level module map
- Likely architecture or data-flow explanation
- One concrete end-to-end flow through the system
- "Read these first" file list
- "What I would ignore for now"

If the repo structure is ambiguous, say so clearly.
If useful, include a simple architecture diagram, wiring diagram, or ASCII map.
Optimize for speed and orientation, not completeness.
```

## High-Stakes Repo Prompt

Best for:
- production systems
- risky changes
- security-sensitive code
- generated code where reading everything is unrealistic

```markdown
You are helping me understand a high-stakes code repository before I trust a change.

Do not begin with a broad prose summary.
Begin by identifying the control surfaces, boundaries, and blast radius.

Your job:
1. Identify the top-level structure and likely system purpose.
2. Find ADRs, spec docs, contracts, schemas, tests, and other files that define invariants.
3. Identify likely entrypoints and subsystem boundaries.
4. Trace the execution flow for the area most likely to matter operationally.
5. List the interfaces, assumptions, and invariants that other parts of the repo depend on.
6. Show the likely blast radius of touching the relevant modules.
7. Recommend the minimum set of files I must read before making or approving changes.
8. Tell me where hidden coupling or architectural risk probably exists.

Output format:
- System purpose
- Top-level module map
- Control surfaces and invariant files
- Critical execution flow
- Blast radius or dependency notes
- "Read these first" file list
- Risks and unknowns

If useful, include:
- subsystem architecture diagram
- state machine diagram for tricky logic
- wiring diagram for pipelines

Be explicit about uncertainty.
Do not claim understanding you have not earned from the code.
Optimize for safe understanding, not verbal confidence.
```

## Fast Follow-Up Prompts

- `Trace one real request through this system from entrypoint to persistence.`
- `Make a state machine diagram of this component, including error paths and retries.`
- `Show me the blast radius if this interface changes.`
- `List the invariants this subsystem relies on.`
- `Give me a visual recap of what changed architecturally, not just the line-by-line diff.`

## Pair It With The Local Script

```bash
python3 scripts/repo_map.py /path/to/repo
python3 scripts/repo_map.py /path/to/repo --output repo-map.md
```
