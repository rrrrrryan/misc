# Repo Understanding Tools

This is a compact roundup of tools and approaches that make repositories easier to understand quickly, especially when code is being generated faster than it can be reviewed line by line.

## Direct Repo Visualization And Code Graph Tools

### GitNexus
- Link: <https://github.com/abhigyanpatwari/GitNexus>
- What it does: turns a repo into an interactive knowledge graph with AST-based dependency and call-graph analysis.
- Why it matters: one of the strongest direct matches for "show me the repo structure fast."

### Code Review Graph
- Link: <https://github.com/tirth8205/code-review-graph>
- What it does: local knowledge graph for Claude Code that maps the codebase so the model reads only what matters.
- Why it matters: more structural compression than visual polish, but highly relevant for review and daily coding.

### Project Orchestrator
- Link: <https://github.com/this-rs/project-orchestrator>
- What it does: Rust + Neo4j + Tree-sitter system that stores code structure, plans, and decisions in a shared graph.
- Why it matters: useful when the problem is not just "see the repo once" but "preserve understanding across multiple agent runs."

### DevilDev
- Link: <https://github.com/lak7/devildev>
- What it does: generates software architecture from specs or an existing repo.
- Why it matters: direct repo-to-architecture tooling.

## Visual Review, Plan, And Recap Surfaces

### Visual Explainer
- Link: <https://github.com/nicobailon/visual-explainer>
- What it does: rich HTML diagrams, visual diffs, plan reviews, project recaps, and fact checks against code.
- Why it matters: strong option for making code review and architecture review inspectable instead of text-heavy.
- Strong idea worth borrowing: commit visual artifacts as an architectural audit trail.

### Builder Visual Plan / Visual Recap
- Link: <https://github.com/BuilderIO/skills>
- What it does: plans and recaps rendered as MDX with diagrams, schema diffs, wireframes, and annotated code.
- Why it matters: shifts review from "read the wall of markdown" to "inspect the plan as an intermediate representation."

### Excalidraw Diagram Skill
- Link: <https://github.com/coleam00/excalidraw-diagram-skill>
- What it does: coding-agent skill for generating Excalidraw diagrams with visual validation.
- Why it matters: useful when a subsystem needs to be explained visually rather than described in prose.

## Structure And Documentation That Make Repos Easier To Read

### ADRs
- What they do: explain how to think about the codebase, not just what files exist.
- Why they matter: especially valuable in large or AI-generated codebases where architectural intent is otherwise easy to lose.

### Contract Review
- What it means: review subsystem boundaries, interfaces, invariants, and tests before reading implementation details.
- Why it matters: helps shift attention from line-by-line code reading to the actual control surfaces.

### State Machine Diagrams
- What they do: force explicit path enumeration, retries, and error states.
- Why they matter: excellent for logic that is easy to hand-wave in prose.

### Wiring Diagrams
- What they do: show typed flow between components or pipeline stages.
- Why they matter: useful for understanding data-heavy or transformation-heavy systems quickly.

## Search And Navigation

### Sourcegraph
- Link: <https://sourcegraph.com/>
- What it does: search across codebases, trace references, analyze refactor impact, and inspect dependency surfaces.
- Why it matters: not a visualizer first, but a strong repo-understanding multiplier.

## Most Actionable Things To Try

1. Try GitNexus or Code Review Graph on one real repo you currently find slow to parse.
2. Use Visual Explainer or Builder-style visual recaps for PR review and project recap.
3. Ask for state machine diagrams and wiring diagrams for any subsystem with tricky control flow.
4. Create or refresh ADRs for the parts of the codebase that keep confusing people.
5. Shift some review effort from line-by-line code reading to contract, interface, and invariant review.

## Bottom Line

The strongest pattern is not that one perfect repo visualizer exists.

It is:
1. precompute or externalize structure
2. turn that structure into a graph or diagram
3. review the artifact instead of rereading raw code every time
4. preserve decisions so future understanding starts from a map instead of a blank page
