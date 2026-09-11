# VLT-1: Taxonomy, Ontology, and Metadata Crosswalk

## Catalog taxonomy

Four base categories. Every asset belongs to exactly one primary category; an
entity can appear twice under distinct asset ids when it plays two roles (the
Thuum.org dictionary is a Category A dataset; Thuum.org the institution is a
Category B host).

| Code | Category | What belongs here |
|---|---|---|
| A | Datasets & Benchmarks | Lexicons, corpora, dictionaries, glossed-dialogue datasets, word-count censuses, NLP benchmarks |
| B | Distribution & Hosting | Publishers, learning platforms, app stores, wikis, reference hubs, fan institutions acting as data services |
| C | Visualizations & Schematics | Script charts, writing systems, language family trees, canonical diagrams |
| D | Technology & Tools | Construction software, sound-change appliers, dictionary software, learning apps, MT and NLP projects |

## Ontology

### Classes

| Class | Definition | Examples |
|---|---|---|
| Asset | A catalogued dataset, service, visualization, or tool | The Klingon Dictionary; Eldamo; SCA2 |
| Owner/Creator | The person or entity holding authorship or IP | Marc Okrand; Bethesda; David J. Peterson |
| Institution | An organization that curates, guards, or teaches | KLI; LCS; LearnNavi.org |
| Language | A constructed language the assets concern | Klingon; Quenya; Dovahzul |
| Tool | Software operating on conlang data | PolyGlot; Lexurgy; boQwI' |
| Visualization | A canonical visual artifact | Tengwar chart; Chakobsa abugida |

### Relations

| Relation | Domain to range | Reading |
|---|---|---|
| owns | Owner/Creator to Language or Asset | holds IP or authorship |
| documents | Asset or Institution to Language | records the language's content |
| hosts | Institution to Asset | serves the asset to the public |
| teaches | Institution or Tool to Language | delivers instruction |
| derived_from | Asset to Asset | built on another asset's data |
| guards_canon_of | Institution to Language | adjudicates what counts as canonical |
| cites | Asset to Asset | formal citation relationship |

Edges are serialized in `data/catalog.json` under each asset's `edges` array and
exported flat to `data/ecosystem-edges.csv`.

## Metadata crosswalk

Every VAULT catalog field maps to all three target standards. This table is the
normative mapping; the JSON-LD `@context` in `data/catalog.json` implements it.

| VAULT field | DCAT v3 | schema.org/Dataset | Croissant |
|---|---|---|---|
| asset_name | dcterms:title | name | name |
| asset_url | dcat:landingPage | url | url |
| description | dcterms:description | description | description |
| category | dcat:theme | about | (keyword) |
| tags | dcat:keyword | keywords | keywords |
| provenance.owner | dcterms:publisher | publisher | publisher |
| provenance.author | dcterms:creator | creator | creator |
| provenance.published_date | dcterms:issued | datePublished | datePublished |
| provenance.identifier | dcterms:identifier | identifier | citeAs |
| license | dcterms:license | license | license |
| distribution | dcat:distribution | distribution | distribution/fileObject |
| temporal_coverage | dcterms:temporal | temporalCoverage | (not mapped) |
| related_assets | dcterms:relation | isRelatedTo | (not mapped) |
| metrics[] | dqv:QualityMeasurement | variableMeasured | recordSet/field |
| last_updated | dcterms:modified | dateModified | (not mapped) |

Croissant has no native slot for temporal coverage or free relations; those
fields round-trip through schema.org properties, which Croissant permits as a
schema.org superset.

## Identifier scheme

- Asset ids: `vault:conlang-<category letter><ordinal>` (example: `vault:conlang-a03`
  is Eldamo). Ids are stable; deletions leave gaps rather than renumbering.
- The `vault:` prefix resolves against the BHIL VAULT schema namespace declared
  in the JSON-LD `@context`.

## Why this matters

No conlang dataset in the wild exposes DCAT, schema.org, or Croissant metadata.
This crosswalk is the reusable piece: any institution in the catalog (Eldamo is
the readiest candidate) can adopt the schema in `data/schema/` and become
discoverable to dataset search engines and ML tooling without changing its data.
