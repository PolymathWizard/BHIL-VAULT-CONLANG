# Contributing to BHIL-VAULT-CONLANG

Corrections, new assets, and metric refreshes are welcome. This catalog runs on evidence discipline; the rules below are what keep it citable.

## The non-negotiables

1. **Every claim carries a tier.** VERIFIED, CORROBORATED, STATED, UNCORROBORATED, or INFERENCE. An untagged claim is a blocked PR, not a small nit.
2. **STATED is a quarantine, not an insult.** A vendor's own learner count, a fan site's self-reported database size, a publisher's blurb: all STATED, no matter how plausible. If a second independent non-owner source confirms it, upgrade to CORROBORATED and cite both.
3. **Default to the lowest defensible tier.** When in doubt between two tiers, take the lower one.
4. **No invention, no lexicon reproduction.** This catalog describes and cites assets. It never reproduces dictionary content, and it never fills a gap with a made-up figure. A missing value is a finding; record it as such.
5. **Recency decay.** Non-specification metrics older than 18 months drop one tier and get an `as_of` date. Frozen or unmaintained sources are flagged in the asset notes.
6. **Canonical source only.** Edit `data/catalog.json`, run `python3 scripts/build_derived.py`, and commit the regenerated CSVs and checksums together. Hand edits to derived files fail the drift gate.
7. **House style.** No em dashes or en dashes anywhere in prose or data. `scripts/dash_gate.py` enforces this on raw bytes and CI runs it on every push.

## Adding a new asset

1. Pick the category (A, B, C, or D) and the next free asset id in that series
   (pattern: `vault:conlang-a12`, `vault:conlang-b11`, etc.).
2. Add the record to `data/catalog.json` following `data/schema/vault-asset.schema.json`.
   Required fields: `asset_id`, `asset_name`, `asset_url`, `category`, `description`,
   `provenance`, `evidence_tier`, `rights_flag`, `last_updated`.
3. Every metric goes in the `metrics` array with `name`, `value`, `as_of`,
   `evidence_tier`, and `source`.
4. Add relations to the `related_assets` array and, where applicable, edges in the
   `edges` array using the ontology relations: `owns`, `documents`, `hosts`,
   `teaches`, `derived_from`, `guards_canon_of`, `cites`.
5. Add a matching asset card to the relevant file in `catalog/`.
6. Run the full gate locally:

```bash
python3 scripts/validate_catalog.py && \
python3 scripts/build_derived.py && \
python3 scripts/tier_rollup.py && \
python3 scripts/dash_gate.py && \
python3 scripts/drift_gate.py
```

7. Commit with a conventional commit scoped to the framework:
   `feat(vault): add <asset> to category <X>` or `fix(vault): correct <metric> tier`.

## Correcting an existing entry

Open an issue titled `C-NNN: <short description>` describing the claim, the current
tier, the correction, and the source. Corrections are tracked as numbered tickets
and resolved in the CHANGELOG. Silent corrections are not accepted; the ledger is
part of the product.

## Sufficiency and scope

New assets must fit the scope lock in `docs/00-scope-lock.md`. Out of scope: natural
languages, auxiliary languages beyond boundary mentions, conlang-creation-for-hire
services, and phrase-level translation content (that belongs to BABEL). If an asset
is real but too thin to catalog responsibly, it belongs in the resources reading
list with a note, not in the catalog.

## Code contributions

- Python 3 standard library only. A PR that adds a pip dependency will be asked to
  remove it.
- Regression tests name their bugs: every regression test carries a docstring naming
  the specific bug it prevents.
