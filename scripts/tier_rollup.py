#!/usr/bin/env python3
"""Print the evidence tier roll-up from the canonical catalog. Stdlib only."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAMES = {"V": "VERIFIED", "C": "CORROBORATED", "S": "STATED", "U": "UNCORROBORATED", "I": "INFERENCE"}


def main():
    doc = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))
    assets = doc["assets"]
    n = len(assets)
    counts = Counter(a["evidence_tier"] for a in assets)
    print(f"Asset-level evidence tier roll-up ({n} assets)")
    print(f"{'Tier':<16}{'Count':>6}{'Share':>8}")
    for t in "VCSUI":
        c = counts.get(t, 0)
        print(f"{NAMES[t]:<16}{c:>6}{c / n:>8.0%}")
    strong = counts.get("V", 0) + counts.get("C", 0)
    print(f"Primary plus corroborated share: {strong / n:.0%}")
    mcounts = Counter(m["evidence_tier"] for a in assets for m in a.get("metrics", []))
    mn = sum(mcounts.values())
    if mn:
        print(f"\nMetric-level roll-up ({mn} metrics)")
        for t in "VCSUI":
            c = mcounts.get(t, 0)
            print(f"{NAMES[t]:<16}{c:>6}{c / mn:>8.0%}")
    cat = Counter(a["category"][0] for a in assets)
    print("\nCategory counts:", ", ".join(f"{k}={cat[k]}" for k in sorted(cat)))


if __name__ == "__main__":
    main()
