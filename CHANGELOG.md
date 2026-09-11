# Changelog

All notable changes to BHIL-VAULT-CONLANG are documented here. The format
follows Keep a Changelog; versions follow semantic versioning.

## [1.0.0] - 2026-09-11

### Added
- Initial public release of the full VAULT run on fictional constructed languages
- Canonical JSON-LD catalog of 31 assets across four categories (data/catalog.json)
- JSON Schema for the VAULT asset record (data/schema/vault-asset.schema.json)
- Derived exports: catalog.csv, metrics.csv, ecosystem-edges.csv, with SHA-256 drift manifest
- Four category deep-dive documents in catalog/
- Documentation set: scope lock, taxonomy and ontology with DCAT/schema.org/Croissant
  crosswalk, evidence tier rules and roll-up, strategic landscape, commercialization,
  and methodology
- Stdlib-only tooling: validate_catalog.py, build_derived.py, tier_rollup.py,
  dash_gate.py, drift_gate.py
- Resource registers: creators, institutions, reading list
- Launch collateral: GitHub description options and LinkedIn variants
- CI quality gate workflow (validation, dash gate, drift gate)

### Known limitations
- Duolingo learner counters frozen since 2025-06-23; metrics decayed one tier
- Two academic sources carry future-dated arXiv identifiers pending verification
- Thuum.org largely unmaintained since 2019; metrics decayed one tier
