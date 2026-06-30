#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
from collections import Counter
from pathlib import Path


MAX_SCAN_FILES = 4000
MAX_TOP_FILES = 12
MAX_TOP_DIRS = 12
IGNORED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".next",
    ".nuxt",
    ".cache",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
    "coverage",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".turbo",
    ".idea",
    ".vscode",
}

LANGUAGE_BY_SUFFIX = {
    ".py": "Python",
    ".ts": "TypeScript",
    ".tsx": "TypeScript React",
    ".js": "JavaScript",
    ".jsx": "JavaScript React",
    ".go": "Go",
    ".rs": "Rust",
    ".java": "Java",
    ".kt": "Kotlin",
    ".swift": "Swift",
    ".rb": "Ruby",
    ".php": "PHP",
    ".c": "C",
    ".cc": "C++",
    ".cpp": "C++",
    ".h": "C/C++ Header",
    ".hpp": "C++ Header",
    ".cs": "C#",
    ".scala": "Scala",
    ".sh": "Shell",
    ".sql": "SQL",
}

MANIFEST_FILES = [
    "package.json",
    "pnpm-workspace.yaml",
    "turbo.json",
    "pyproject.toml",
    "requirements.txt",
    "Cargo.toml",
    "go.mod",
    "pom.xml",
    "build.gradle",
    "Gemfile",
    "composer.json",
    "docker-compose.yml",
    "Dockerfile",
]

CONTROL_FILES = [
    "README.md",
    "README",
    "AGENTS.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "ARCHITECTURE.md",
]

ENTRYPOINT_CANDIDATES = [
    "main.py",
    "app.py",
    "server.py",
    "manage.py",
    "main.ts",
    "main.tsx",
    "main.js",
    "index.ts",
    "index.tsx",
    "server.ts",
    "server.js",
    "app.ts",
    "app.js",
    "src/main.py",
    "src/main.ts",
    "src/main.tsx",
    "src/index.ts",
    "src/index.tsx",
    "src/app.ts",
    "src/app.js",
    "src/routes/+page.ts",
    "src/routes/+page.js",
    "src/routes/+layout.ts",
    "src/routes/+layout.js",
    "app/page.tsx",
    "app/page.jsx",
    "pages/index.tsx",
    "pages/index.jsx",
    "cmd",
]

DOC_CANDIDATES = [
    "docs",
    "adr",
    "docs/adr",
    "spec",
    "specs",
]

TEST_MARKERS = {"tests", "test", "__tests__", "spec"}
ENTRYPOINT_SUFFIXES = {".py", ".ts", ".tsx", ".js", ".jsx", ".go", ".rs", ".java", ".kt", ".swift", ".rb", ".php", ".sh"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a first-pass markdown repo map.")
    parser.add_argument("repo", help="Path to the repository")
    parser.add_argument("--output", help="Optional markdown output file")
    return parser.parse_args()


def relative_to(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def should_skip_dir(dirname: str) -> bool:
    return dirname in IGNORED_DIRS or dirname.startswith(".")


def walk_repo(root: Path) -> tuple[list[Path], Counter[str], Counter[str], list[tuple[str, int]]]:
    files: list[Path] = []
    language_counts: Counter[str] = Counter()
    top_level_counts: Counter[str] = Counter()
    sized_files: list[tuple[str, int]] = []

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not should_skip_dir(d)]
        current_dir = Path(dirpath)
        for filename in filenames:
            path = current_dir / filename
            if path.is_symlink():
                continue
            rel = relative_to(path, root)
            parts = Path(rel).parts
            if not parts:
                continue
            top_level = parts[0]
            top_level_counts[top_level] += 1
            suffix = path.suffix.lower()
            language = LANGUAGE_BY_SUFFIX.get(suffix)
            if language:
                language_counts[language] += 1
            try:
                size = path.stat().st_size
            except OSError:
                size = 0
            sized_files.append((rel, size))
            files.append(path)
            if len(files) >= MAX_SCAN_FILES:
                return files, language_counts, top_level_counts, sized_files
    return files, language_counts, top_level_counts, sized_files


def find_existing(root: Path, candidates: list[str]) -> list[str]:
    found: list[str] = []
    for candidate in candidates:
        path = root / candidate
        if path.exists():
            found.append(candidate)
    return found


def find_entrypoints(root: Path, files: list[Path]) -> list[str]:
    found = find_existing(root, ENTRYPOINT_CANDIDATES[:-1])
    cmd_root = root / "cmd"
    if cmd_root.is_dir():
        for child in sorted(cmd_root.iterdir()):
            main_go = child / "main.go"
            if main_go.exists():
                found.append(relative_to(main_go, root))
    if not found:
        for path in files:
            rel = relative_to(path, root)
            name = path.name.lower()
            parts = Path(rel).parts
            if path.suffix.lower() not in ENTRYPOINT_SUFFIXES:
                continue
            if name.endswith(".d.ts"):
                continue
            if len(parts) > 2 and parts[0] not in {"src", "app", "cmd"}:
                continue
            if name.startswith("index.") and len(parts) > 2:
                continue
            if name.startswith(("main.", "app.", "server.", "index.")):
                found.append(rel)
        found = sorted(dict.fromkeys(found))[:10]
    return found


def find_docs(root: Path) -> list[str]:
    found = find_existing(root, CONTROL_FILES)
    for candidate in DOC_CANDIDATES:
        path = root / candidate
        if path.exists():
            found.append(candidate)
    return found


def find_tests(files: list[Path], root: Path) -> list[str]:
    matches: list[str] = []
    for path in files:
        rel = relative_to(path, root)
        parts = Path(rel).parts
        if any(part.lower() in TEST_MARKERS for part in parts):
            matches.append(rel)
    return matches[:12]


def suggest_read_first(root: Path, manifests: list[str], docs: list[str], entrypoints: list[str], files: list[Path]) -> list[str]:
    picks: list[str] = []
    picks.extend(docs)
    picks.extend(manifests)
    picks.extend(entrypoints)

    router_keywords = {"router", "routes", "route", "api", "server", "app", "main"}
    for path in files:
        rel = relative_to(path, root)
        basename = path.stem.lower()
        parent_names = {part.lower() for part in Path(rel).parts[:-1]}
        if path.suffix.lower() not in ENTRYPOINT_SUFFIXES:
            continue
        if basename in router_keywords or parent_names.intersection(router_keywords):
            picks.append(rel)

    deduped: list[str] = []
    seen: set[str] = set()
    for item in picks:
        if item in seen:
            continue
        seen.add(item)
        deduped.append(item)
    return deduped[:10]


def render_markdown(root: Path, files: list[Path], language_counts: Counter[str], top_level_counts: Counter[str], sized_files: list[tuple[str, int]]) -> str:
    manifests = find_existing(root, MANIFEST_FILES)
    docs = find_docs(root)
    entrypoints = find_entrypoints(root, files)
    tests = find_tests(files, root)
    read_first = suggest_read_first(root, manifests, docs, entrypoints, files)
    top_dirs = top_level_counts.most_common(MAX_TOP_DIRS)
    biggest_files = sorted(sized_files, key=lambda item: item[1], reverse=True)[:MAX_TOP_FILES]

    lines: list[str] = []
    lines.append(f"# Repo Map: {root.name}")
    lines.append("")
    lines.append(f"- Path: `{root}`")
    lines.append(f"- Files scanned: `{len(files)}`")
    lines.append("")

    lines.append("## Likely Stack")
    if language_counts:
        for language, count in language_counts.most_common(8):
            lines.append(f"- {language}: `{count}` files")
    else:
        lines.append("- No common source files detected from the lightweight scan.")
    lines.append("")

    lines.append("## Manifests And Build Files")
    if manifests:
        for item in manifests:
            lines.append(f"- `{item}`")
    else:
        lines.append("- None of the common manifest files were found.")
    lines.append("")

    lines.append("## Docs And Decision Surfaces")
    if docs:
        for item in docs:
            lines.append(f"- `{item}`")
    else:
        lines.append("- No obvious docs/ADR/spec folders found.")
    lines.append("")

    lines.append("## Likely Entrypoints")
    if entrypoints:
        for item in entrypoints:
            lines.append(f"- `{item}`")
    else:
        lines.append("- No strong entrypoint candidates found from filename heuristics.")
    lines.append("")

    lines.append("## Top-Level Areas")
    if top_dirs:
        for dirname, count in top_dirs:
            lines.append(f"- `{dirname}`: `{count}` files")
    else:
        lines.append("- No top-level areas found.")
    lines.append("")

    lines.append("## Read These First")
    if read_first:
        for item in read_first:
            lines.append(f"- `{item}`")
    else:
        lines.append("- No clear first-pass files found.")
    lines.append("")

    lines.append("## Test Surface")
    if tests:
        for item in tests[:10]:
            lines.append(f"- `{item}`")
    else:
        lines.append("- No obvious test files or test directories found.")
    lines.append("")

    lines.append("## Largest Files")
    if biggest_files:
        for rel, size in biggest_files:
            lines.append(f"- `{rel}` ({size:,} bytes)")
    else:
        lines.append("- No large files found.")
    lines.append("")

    lines.append("## Next Questions")
    lines.append("- Which entrypoint actually handles the most important production path?")
    lines.append("- Are there ADRs, specs, or schemas that define invariants outside the code?")
    lines.append("- Which subsystem would be riskiest to change without a blast-radius check?")
    lines.append("- Which single request or workflow should be traced end-to-end next?")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(args.repo).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Repository path not found or not a directory: {root}")

    files, language_counts, top_level_counts, sized_files = walk_repo(root)
    markdown = render_markdown(root, files, language_counts, top_level_counts, sized_files)

    if args.output:
        output_path = Path(args.output).expanduser().resolve()
        output_path.write_text(markdown + "\n", encoding="utf-8")
    else:
        print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
