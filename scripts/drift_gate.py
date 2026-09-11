#!/usr/bin/env python3
"""Drift gate: derived CSVs must match data/checksums.sha256 exactly.

Catches hand edits to derived artifacts and stale builds after canonical
edits. Regenerate with scripts/build_derived.py. Exit 1 on drift.
"""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def main():
    manifest = (DATA / "checksums.sha256").read_text(encoding="utf-8").strip().splitlines()
    drift = []
    for line in manifest:
        digest, name = line.split(None, 1)
        actual = hashlib.sha256((DATA / name.strip()).read_bytes()).hexdigest()
        if actual != digest:
            drift.append(name.strip())
    if drift:
        print("FAIL: drift detected in derived artifacts:", ", ".join(drift))
        print("Regenerate with: python3 scripts/build_derived.py")
        return 1
    print(f"PASS: {len(manifest)} derived artifact(s) match manifest")
    return 0


if __name__ == "__main__":
    sys.exit(main())
