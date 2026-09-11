#!/usr/bin/env python3
"""Validate data/catalog.json against the VAULT asset schema and house rules.

Stdlib only. Implements the checks the JSON Schema expresses plus rules a
schema cannot express (STATED quarantine hints, id uniqueness, relation
targets). Exit 0 on pass, 1 on any failure.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "data" / "catalog.json"

ID_RE = re.compile(r"^vault:conlang-[abcd][0-9]{2}$")
DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
METRIC_NAME_RE = re.compile(r"^[a-z0-9_]+$")
TIERS = {"V", "C", "S", "U", "I"}
RIGHTS = {"franchise-ip", "creator-owned", "open-license", "fair-use-community"}
CATEGORIES = {
    "A-Datasets-Benchmarks",
    "B-Distribution-Hosting",
    "C-Visualizations-Schematics",
    "D-Technology-Tools",
}
RELATIONS = {"owns", "documents", "hosts", "teaches", "derived_from", "guards_canon_of", "cites"}
ASSET_TYPES = {
    "schema:Dataset", "schema:Service", "schema:CreativeWork",
    "schema:SoftwareApplication", "schema:Book", "schema:LearningResource",
}
REQUIRED = [
    "asset_id", "asset_name", "asset_url", "asset_type", "category",
    "description", "provenance", "evidence_tier", "rights_flag", "last_updated",
]
SELF_REPORT_MARKERS = ("self-report", "self report", "vendor", "listing", "store description", "abstract self-report", "pricing page")


def fail(errors, msg):
    errors.append(msg)


def validate_asset(a, ids, errors):
    aid = a.get("asset_id", "<missing id>")
    for field in REQUIRED:
        if field not in a:
            fail(errors, f"{aid}: missing required field '{field}'")
    if not ID_RE.match(a.get("asset_id", "")):
        fail(errors, f"{aid}: asset_id does not match id pattern")
    if a.get("asset_id") in ids:
        fail(errors, f"{aid}: duplicate asset_id")
    ids.add(a.get("asset_id"))
    if not str(a.get("asset_url", "")).startswith(("http://", "https://")):
        fail(errors, f"{aid}: asset_url must be an absolute http(s) URL")
    if a.get("asset_type") not in ASSET_TYPES:
        fail(errors, f"{aid}: asset_type '{a.get('asset_type')}' not in allowed set")
    if a.get("category") not in CATEGORIES:
        fail(errors, f"{aid}: category '{a.get('category')}' not in allowed set")
    if len(a.get("description", "")) < 20:
        fail(errors, f"{aid}: description under 20 characters")
    if a.get("evidence_tier") not in TIERS:
        fail(errors, f"{aid}: evidence_tier '{a.get('evidence_tier')}' invalid")
    if a.get("rights_flag") not in RIGHTS:
        fail(errors, f"{aid}: rights_flag '{a.get('rights_flag')}' invalid")
    if not DATE_RE.match(a.get("last_updated", "")):
        fail(errors, f"{aid}: last_updated must be YYYY-MM-DD")
    prov = a.get("provenance", {})
    for pf in ("owner", "author", "published_date", "identifier"):
        if not prov.get(pf):
            fail(errors, f"{aid}: provenance.{pf} missing or empty")
    for rid in a.get("related_assets", []):
        if not ID_RE.match(rid):
            fail(errors, f"{aid}: related asset id '{rid}' malformed")
    for m in a.get("metrics", []):
        for mf in ("name", "value", "as_of", "evidence_tier", "source"):
            if mf not in m:
                fail(errors, f"{aid}: metric missing '{mf}'")
        if not METRIC_NAME_RE.match(str(m.get("name", ""))):
            fail(errors, f"{aid}: metric name '{m.get('name')}' must be snake_case")
        if m.get("evidence_tier") not in TIERS:
            fail(errors, f"{aid}: metric '{m.get('name')}' has invalid tier")
        src = str(m.get("source", "")).lower()
        if m.get("evidence_tier") in ("V", "C") and any(k in src for k in SELF_REPORT_MARKERS):
            fail(errors, f"{aid}: metric '{m.get('name')}' cites a self-report but is tiered {m.get('evidence_tier')}; STATED quarantine violated")
    for e in a.get("edges", []):
        if e.get("relation") not in RELATIONS:
            fail(errors, f"{aid}: edge relation '{e.get('relation')}' not in ontology")
        if not e.get("target"):
            fail(errors, f"{aid}: edge missing target")


def main():
    doc = json.loads(CATALOG.read_text(encoding="utf-8"))
    assets = doc.get("assets", [])
    errors, ids = [], set()
    if not assets:
        errors.append("catalog contains no assets")
    for a in assets:
        validate_asset(a, ids, errors)
    # Cross-record: every related_assets id must exist in the catalog
    for a in assets:
        for rid in a.get("related_assets", []):
            if rid not in ids:
                errors.append(f"{a['asset_id']}: related asset '{rid}' not present in catalog")
    # Inference ceiling: asset-level INFERENCE under 40 percent
    inf = sum(1 for a in assets if a.get("evidence_tier") == "I")
    if assets and inf / len(assets) >= 0.40:
        errors.append(f"INFERENCE ceiling breached: {inf}/{len(assets)} assets")
    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for e in errors:
            print("  -", e)
        return 1
    print(f"PASS: {len(assets)} assets valid; INFERENCE share {inf}/{len(assets)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
