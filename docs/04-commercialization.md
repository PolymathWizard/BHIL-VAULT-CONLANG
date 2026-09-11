# VLT-9: Commercialization Notes and Product Composition

## VAULT SKU mapping

| SKU | Scope | Conlang-domain form | Buyer |
|---|---|---|---|
| VAULT-A (Audit) | One-language rapid inventory plus evidence-graded scorecard | A "Klingon data audit" for a studio evaluating a language-learning tie-in; catalog-card format for one franchise, rights-flagged | Studio, licensor, agency |
| VAULT-S (Standard) | Full four-category catalog for a franchise or cluster | The Peterson/HBO cluster or the Tolkien cluster, with the metadata crosswalk applied and a canon-versus-reconstruction labeling pass | Publisher, streamer, franchise team |
| VAULT-X (Strategic) | Cross-franchise knowledge base, ecosystem map, white-space analysis, plus a Croissant-serialized pilot dataset | This repository, extended: a foundational AI knowledge base usable as a training, evaluation, or RAG substrate | Platforms, AI labs, large studios |
| VAULT-R (Retainer) | Ongoing maintenance | Tracking canon expansions (qep'a' word reveals, naviteri.org updates, new film releases), metric refreshes, new academic corpora | Any of the above |

The retainer is justified by the domain's living-canon nature: Klingon adds
words annually at qep'a', Na'vi grows with each Avatar release, and High
Valyrian expanded for House of the Dragon.

## Composition with the BHIL product line

```
VAULT (this repo)        the asset-catalog substrate: what exists, who owns it,
                         how good the evidence is, what it connects to
        |
BABEL (Skills Master)    the phrase and culture layer: canon-verified
                         translations, phonetics, cultural deep dives
        |
GamingToolset            the product layer: The Traveler's Phrasebook and
                         future supplements, built on the two layers below
```

VAULT answers "what data can we responsibly build on"; BABEL answers "what do
the languages say and mean"; GamingToolset answers "what does the customer
hold in their hands."

## Buyer map

| Buyer | Job to be done | Entry SKU |
|---|---|---|
| Game studios and TTRPG publishers | In-world language flavor, localization planning, canon-safe supplements | VAULT-A, then BABEL |
| Publishers and streamers | Fan-engagement campaigns tied to releases (the Duolingo x HBO pattern) | VAULT-S |
| Fan-engagement and franchise marketing teams | Canon-accurate, rights-flagged language content without embarrassment risk | VAULT-A |
| AI labs and platforms | Low-resource-language evaluation sets, RAG substrates, metadata pilots | VAULT-X |
| Convention and event programmers | Programming content and speaker sourcing via the creator/institution register | Resources tier |

## Rights posture

Per-asset rights flags in the catalog take one of four values:

- `franchise-ip`: language and canon owned by a franchise holder; any
  commercial use of the language content requires rights review
- `creator-owned`: rights sit with an individual creator; approachable directly
- `open-license`: explicit open license on the asset (Eldamo CC-BY, PolyGlot
  MIT, SCA2 freely provided); safe to build on immediately
- `fair-use-community`: fan-maintained material operating under fair-use
  disclaimers; describable and citable, not licensable through the community

Nothing in this repository constitutes a rights clearance. The flags are
navigation aids for the legal review that any commercialization requires.

## Recommendations carried from the run

1. Pilot the Croissant/DCAT wrapper on Eldamo first (CC-BY, already XML,
   stable identifiers). Lowest-friction proof of concept.
2. Ship a canon-versus-reconstruction labeling standard as a standalone
   deliverable, seeded from Thuum.org's canonicity model and Eldamo's period
   stratification.
3. Build the cross-institution join key (language by creator by canon source),
   starting with Klingon as the hardest test case.
4. Re-verify all vendor metrics quarterly under VAULT-R, with the Duolingo
   freeze and preprint arXiv items at the top of the queue.
5. Attach per-asset rights flags before any licensing conversation (done in
   v1.0.0; maintain on every addition).
