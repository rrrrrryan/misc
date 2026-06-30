# misc

Portable repo-understanding toolkit for quickly orienting in unfamiliar or fast-moving codebases.

## Contents

- `research/repo-understanding-tools.md`
  - Curated tool roundup with direct links.
- `research/repo-understanding-playbook.md`
  - Low-stakes and high-stakes workflows for getting oriented safely.
- `prompts/repo-understanding-prompt.md`
  - Copy-paste prompts for Codex or Claude.
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

A better default is:

1. map the structure
2. identify boundaries and entrypoints
3. trace one concrete flow
4. check blast radius and invariants
5. read only the critical code
