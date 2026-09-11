# VLT-7: Evidence Grading Rules and Roll-up

## The five tiers

| Tag | Tier | Definition | Conlang-domain examples |
|---|---|---|---|
| `[V]` | VERIFIED | Authoritative primary source: creator-published dictionary, official specification, peer-reviewed or archived paper | Okrand's TKD; Thuum.org's statement of 647 canonical words; the SCA2 spec by its author |
| `[C]` | CORROBORATED | Two or more independent non-owner sources agree | Dothraki word counts confirmed by Wired plus Wikipedia; Belter Creole size per Ars Technica plus Wikipedia |
| `[S]` | STATED | Owner or vendor self-description or self-reported metric; quarantined regardless of plausibility | Duolingo learner counts; Elfdict's own 136,992-word figure; Omniglot's script counts; app store downloads |
| `[U]` | UNCORROBORATED | Single non-owner source, unconfirmed elsewhere | The popular "about 3,000 Klingon words" figure; Herbert's Fremen word census |
| `[I]` | INFERENCE | Analytical conclusion; must publish its reasoning chain | The white-space findings in the strategic landscape |

## Operating rules

1. **Default to the lowest defensible tier.** Ambiguity resolves downward.
2. **STATED is a hard quarantine.** Self-reported numbers never inherit the
   parent asset's tier. A VERIFIED asset can carry STATED metrics, and most do.
3. **Recency decay.** Non-specification findings older than 18 months drop one
   tier and must carry an `as_of` date. Frozen sources are flagged in notes.
4. **INFERENCE ceiling.** Asset-level INFERENCE must stay under 40% of the
   catalog. This run holds it at 0%; inference is confined to the strategic
   landscape analysis, where each finding publishes its reasoning chain.
5. **No silent correction.** Tier changes and metric corrections are tracked as
   numbered tickets (C-NNN) and land in the CHANGELOG.
6. **A missing value is a finding.** Gaps are recorded as absences with an
   explanation, never filled by estimate or invention.

## Asset-level roll-up (v1.0.0)

| Tier | Count | Share |
|---|---|---|
| VERIFIED | 19 | 53% |
| CORROBORATED | 12 | 33% |
| STATED | 2 | 6% |
| UNCORROBORATED | 3 | 8% |
| INFERENCE | 0 | 0% |
| **Total** | **36** | **100%** |

Primary-plus-corroborated share: 86%. At the metric level (45 metrics), 60%
sit in STATED quarantine, 13% VERIFIED, 16% CORROBORATED, 11% UNCORROBORATED.
The gap between asset-level and metric-level quality is itself a finding:
the domain's assets are solid, but its numbers are mostly self-reported. Regenerate this table at any time with:

```bash
python3 scripts/tier_rollup.py
```

The script reads `data/catalog.json` (the canonical source) and prints the
roll-up; the table above is a derived artifact and is refreshed on release.

## Decayed and flagged items in v1.0.0

| Item | Flag | Reason |
|---|---|---|
| Duolingo learner counts | STATED, decayed | Public counters frozen since 2025-06-23 |
| Thuum.org expanded dictionary metrics | STATED, decayed | Site largely unmaintained since early 2019 |
| ConlangBench (arXiv 2608.03505) | UNCORROBORATED, verification pending | Future-dated arXiv identifier at run time; preprint |
| Conlang probing paper (arXiv 2510.07591) | UNCORROBORATED, verification pending | Same class of flag |

## Definitional caveat on vocabulary counts

Word-count spreads in this domain are real definitional disagreements, not just
sourcing noise. Counts differ on whether they include affixes, proper names,
fan-coined vocabulary, and course-exclusive words. Klingon illustrates the full
spread: 1,586 words in the 1985 first edition, 1,889 after the 1992 addendum,
"about 3,000" in popular usage, and 4,221 entries in one maintainer's aggregated
lexicon. The catalog records each figure with its own tier and source rather
than picking a winner.
