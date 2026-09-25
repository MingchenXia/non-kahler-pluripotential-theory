#!/usr/bin/env python3
"""Check the active manuscript's book-only citation policy outside history."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "book"
HISTORY = BOOK / "author/chapter_history.tex"
# Classification follows the nature of each work, not its BibTeX entry type.
BOOK_KEYS = {"SGPT", "DemAM11", "DemCADG", "GZ17", "OV24LCK", "HuyK3", "GT01"}
CITE = re.compile(r"\\(?:cite|citep|citet|autocite|parencite|textcite|nocite)\*?(?:\[[^\]]*\])*\{([^}]+)\}")
INPUT = re.compile(r"\\(?:input|include)\{([^}]+)\}")


def active_sources():
    seen = set()
    pending = [BOOK / "book.tex"]
    while pending:
        path = pending.pop()
        if path in seen:
            continue
        seen.add(path)
        source = re.sub(r"(?<!\\)%[^\n]*", "", path.read_text())
        yield path, source
        for name in INPUT.findall(source):
            child = BOOK / (name + ".tex")
            if child.exists():
                pending.append(child)


def main():
    errors = []
    active = list(active_sources())
    if HISTORY not in {path for path, _ in active}:
        errors.append("Historical chapter is not included in the manuscript.")
    for path, source in active:
        if path == HISTORY:
            continue
        for match in CITE.finditer(source):
            papers = set(map(str.strip, match[1].split(","))) - BOOK_KEYS
            if papers:
                line = source.count("\n", 0, match.start()) + 1
                errors.append(f"{path.relative_to(ROOT)}:{line}: non-book citation: {', '.join(sorted(papers))}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Citation placement: all non-book citations are confined to the historical chapter.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
