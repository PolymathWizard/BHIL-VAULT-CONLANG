#!/usr/bin/env python3
"""House style gate: no em dashes or en dashes anywhere in tracked prose or data.

Scans raw bytes (UTF-8 sequences for U+2014 and U+2013), not parsed values,
so encoded and embedded occurrences are caught too. Exit 1 on any hit.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EM = "\u2014".encode("utf-8")
EN = "\u2013".encode("utf-8")
EXTS = {".md", ".json", ".csv", ".py", ".yml", ".yaml", ".cff", ".txt"}
SKIP_DIRS = {".git", "__pycache__", "engagements", "site"}


def main():
    hits = []
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or p.suffix not in EXTS:
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        raw = p.read_bytes()
        for label, needle in (("em dash", EM), ("en dash", EN)):
            idx = raw.find(needle)
            if idx != -1:
                line = raw[:idx].count(b"\n") + 1
                hits.append(f"{p.relative_to(ROOT)}:{line}: {label}")
    if hits:
        print(f"FAIL: {len(hits)} dash violation(s)")
        for h in hits:
            print("  -", h)
        return 1
    print("PASS: no em or en dashes in tracked files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
