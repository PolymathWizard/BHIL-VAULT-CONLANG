#!/usr/bin/env python3
"""Regenerate all derived artifacts from the canonical data/catalog.json.

Outputs:
  data/catalog.csv          one row per asset
  data/metrics.csv          one row per metric
  data/ecosystem-edges.csv  one row per ontology edge
  data/checksums.sha256     SHA-256 drift manifest for the three CSVs

Derived files are never hand-edited. Stdlib only.
"""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CATALOG = DATA / "catalog.json"

DERIVED = ["catalog.csv", "metrics.csv", "ecosystem-edges.csv"]


def build():
    doc = json.loads(CATALOG.read_text(encoding="utf-8"))
    assets = doc["assets"]

    with (DATA / "catalog.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([
            "asset_id", "asset_name", "category", "asset_type", "evidence_tier",
            "rights_flag", "asset_url", "owner", "author", "published_date",
            "identifier", "license", "distribution", "temporal_coverage",
            "tags", "related_assets", "description", "strategic_value",
            "notes", "last_updated",
        ])
        for a in assets:
            p = a["provenance"]
            w.writerow([
                a["asset_id"], a["asset_name"], a["category"], a["asset_type"],
                a["evidence_tier"], a["rights_flag"], a["asset_url"],
                p["owner"], p["author"], p["published_date"], p["identifier"],
                a.get("license", ""), a.get("distribution", ""),
                a.get("temporal_coverage", ""),
                "; ".join(a.get("tags", [])),
                "; ".join(a.get("related_assets", [])),
                a["description"], a.get("strategic_value", ""),
                a.get("notes", ""), a["last_updated"],
            ])

    with (DATA / "metrics.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["asset_id", "asset_name", "metric_name", "value", "as_of", "evidence_tier", "source"])
        for a in assets:
            for m in a.get("metrics", []):
                w.writerow([a["asset_id"], a["asset_name"], m["name"], m["value"], m["as_of"], m["evidence_tier"], m["source"]])

    with (DATA / "ecosystem-edges.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["source_asset_id", "source_asset_name", "relation", "target"])
        for a in assets:
            for e in a.get("edges", []):
                w.writerow([a["asset_id"], a["asset_name"], e["relation"], e["target"]])

    lines = []
    for name in DERIVED:
        digest = hashlib.sha256((DATA / name).read_bytes()).hexdigest()
        lines.append(f"{digest}  {name}")
    (DATA / "checksums.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")

    n_metrics = sum(len(a.get("metrics", [])) for a in assets)
    n_edges = sum(len(a.get("edges", [])) for a in assets)
    print(f"built: {len(assets)} assets, {n_metrics} metrics, {n_edges} edges; checksums written")


if __name__ == "__main__":
    build()
