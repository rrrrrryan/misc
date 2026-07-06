# misc

Portable toolkit for understanding unfamiliar codebases and digesting high-volume LLM output through better intermediate representations.

## Contents

- `research/repo-understanding-tools.md`
  - Curated tool roundup with direct links.
- `research/repo-understanding-playbook.md`
  - Low-stakes and high-stakes workflows for getting oriented safely.
- `research/llm-output-digestion-playbook.md`
  - Practical guide for understanding model output when the raw transcript, trace, or diff is the wrong first surface.
- `research/representation-ladder.md`
  - Short reference for choosing the right representation before reading raw output.
- `prompts/repo-understanding-prompt.md`
  - Copy-paste prompts for Codex or Claude.
- `prompts/artifact-first-digestion-prompt.md`
  - Copy-paste prompts for converting raw model output into inspectable artifacts.
- `scripts/repo_map.py`
  - Lightweight local CLI that generates a first-pass markdown repo map.
- `design.md`
  - UI and product design rules that are useful as a reusable reference.

## Quick Usage

Generate a repo map:

```bash
python3 scripts/repo_map.py /path/to/repo
```

Save a markdown snapshot:

```bash
python3 scripts/repo_map.py /path/to/repo --output repo-map.md
```

## Why This Exists

Large and AI-generated repositories are hard to understand if the first move is reading raw code linearly.

Likewise, long model outputs are hard to trust if the first move is reading the whole transcript as-is.

A better default is:

1. map the structure
2. identify boundaries and entrypoints
3. trace one concrete flow
4. check blast radius and invariants
5. inspect a better artifact first
6. read only the critical raw output
