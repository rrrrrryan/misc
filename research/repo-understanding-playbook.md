# Repo Understanding Playbook

This is the practical version of the tool roundup: what to do when a repo lands in front of you and the code is arriving faster than you can comfortably read it.

## Core Principle

Do not start by reading raw code linearly.

Start by building a map:
- structure
- boundaries
- flows
- invariants
- blast radius

Then only read the code that matters.

## Low-Stakes Repo Workflow

Use this when:
- the repo is exploratory
- mistakes are cheap
- you mostly need orientation
- you want a fast mental model in 10 to 30 minutes

### Goal

Get a decent map fast without pretending to fully understand every subsystem.

### Steps

1. Find the entry surface.
   - README
   - package manifest or build file
   - top-level directories
   - main app entrypoints

2. Generate or request a structure map.
   - Use GitNexus or DevilDev if available.
   - If not, ask the agent for:
     - top-level module map
     - request or data flow
     - major dependencies
     - likely entrypoints

3. Ask for one visual artifact.
   - preferred: architecture diagram
   - fallback: wiring diagram
   - fallback: ASCII diagram if that is fastest

4. Find the 3 to 7 important modules.
   - auth
   - data layer
   - request handlers
   - background jobs
   - state management
   - domain core

5. Ask for a subsystem walkthrough.
   - "Explain this repo as if you were onboarding a senior engineer in 10 minutes."
   - "Which files are central vs incidental?"
   - "If I only read five files, which ones and why?"

6. Force one path through the system.
   - pick a concrete flow:
     - user login
     - API request
     - data write
     - background task
   - ask for the exact hop-by-hop path

7. Use state machine diagrams where logic feels slippery.
   - UI state
   - workflows
   - retries
   - async jobs
   - approval flows

### Output You Want

- one architecture sketch
- one concrete request or data path
- one shortlist of files worth reading
- one paragraph on where complexity actually lives

### Good Enough Test

You should be able to answer:
- what this repo does
- where requests start
- where business logic lives
- where data enters and leaves
- which files you would open next if something broke

## High-Stakes Repo Workflow

Use this when:
- production risk is real
- the code is security-sensitive
- a bad refactor could break hidden dependencies
- you are making changes, not just touring
- generated code volume is high enough that line-by-line review is not realistic

### Goal

Reduce the chance of missing a dangerous dependency or violating an architectural invariant.

### Steps

1. Identify the control surfaces first.
   - ADRs
   - spec docs
   - contracts
   - API schemas
   - tests that encode invariants
   - deployment or CI constraints

2. Review contracts before implementations.
   - interfaces
   - return shapes
   - data models
   - event schemas
   - cross-service assumptions

3. Generate a dependency or blast-radius map.
   - best fit: GitNexus
   - strong fit: Code Review Graph
   - ask specifically for:
     - callers of target functions
     - imports and reverse imports
     - execution flow from entrypoint
     - what breaks if this interface changes

4. Create visual artifacts for risky areas.
   - architecture diagram for subsystem boundaries
   - state machine diagram for logic-heavy components
   - sequence diagram for multi-step flows
   - schema or interface diff for proposed changes

5. Ask for invariants explicitly.
   - "What must remain true after this change?"
   - "What assumptions are other modules making?"
   - "What hidden coupling exists here?"

6. Use a visual recap before trusting the result.
   - Visual Explainer
   - Builder-style visual recap
   - or a manual architecture diff or subsystem recap

7. Dogfood or simulate the real path.
   - follow a concrete user flow
   - run E2E or integration tests
   - compare expected path vs actual path

8. Preserve what you learned.
   - write or update ADRs
   - keep diagrams near the project
   - save review artifacts if they explain important boundaries

### Output You Want

- dependency or blast-radius view
- explicit invariants list
- contract-level understanding
- visual recap of what changed
- test-backed confidence on the risky path

### Good Enough Test

You should be able to answer:
- what boundary this change crosses
- who depends on the touched interfaces
- what invariant could silently break
- what artifact proves the architecture still makes sense

## Fastest Useful Prompts

### For any repo

- "Give me a top-level architecture map of this repo. Show central modules, entrypoints, and data flow."
- "If I only had 15 minutes to understand this repo, which files would I read and in what order?"
- "Trace one real request through this system from entrypoint to persistence."

### For slippery logic

- "Make a state machine diagram of this component, including error paths and retries."
- "Turn this pipeline into a wiring diagram so I can see the typed flow between steps."

### For risky changes

- "Show me the blast radius if this interface changes."
- "List the invariants this subsystem relies on."
- "Give me a visual recap of what changed architecturally, not just line-by-line code diff."

## Best Tool Fits

### For direct repo graphing
- GitNexus
- Code Review Graph
- Project Orchestrator
- DevilDev

### For visual review surfaces
- Visual Explainer
- Builder visual plan / visual recap
- Excalidraw Diagram Skill

### For thought structure
- ADRs
- contract review
- state machine diagrams
- wiring diagrams

## Bottom Line

The real bottleneck is not just that there is too much code to read.

It is that raw code is often the wrong first representation when code is being generated this quickly.

The better move is:
- inspect the map
- inspect the boundaries
- inspect the flow
- inspect the blast radius
- then read the critical code
