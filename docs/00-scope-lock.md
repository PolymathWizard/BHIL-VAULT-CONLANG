# VLT-0: Scope Lock Sheet

**Topic:** Constructed languages from fiction (film, TV, literature, games), catalogued as data assets.

**Run date:** 2026-09-11. **Framework:** BHIL VAULT. **Layer:** asset catalog, sitting beneath BABEL (phrase and culture layer) and the GamingToolset Traveler's Phrasebook (product layer).

## Inclusions

| Class | Examples |
|---|---|
| Creator-published lexicons, dictionaries, grammars | The Klingon Dictionary; Living Language Dothraki; Frommer's Na'vi corpus; Peterson's wikis |
| Digital corpora and datasets | Eldamo XML; glossed-dialogue sets; word-count censuses; NLP benchmarks |
| Fan-scholarship institutions and their databases | kli.org, Thuum.org, Elfdict/Parf Edhellen, Ardalambion, RealElvish.net, LearnNavi.org, dedalvs.com, mandoa.org, korsaya.org, Dothraki.org |
| Conlang construction and documentation tools | PolyGlot, Vulgar, ConWorkShop, SCA2, Lexurgy, word generators |
| Learning platforms carrying conlangs | Duolingo High Valyrian and Klingon, Memrise courses, Living Language Dothraki |
| Canonical visualizations and scripts | Tengwar/Cirth charts, Klingon pIqaD, Dovahzul runes, Chakobsa abugida, Tolkien's language family trees |
| Marketplaces and distribution | Publisher channels, Duolingo, app stores, Omniglot, fan wikis |
| Academic and NLP resources | Conlang-NLP papers, Klingon MT datasets, the Language Creation Society, Fiat Lingua |

## Exclusions

- Natural languages (out of domain by definition)
- Esperanto-class auxiliary languages, except as boundary references where they
  anchor NLP resources no fiction conlang has (a UD treebank, benchmark presence)
- Original conlang creation services (a different engagement; MYTHOS FORGE territory)
- Phrase-level translation and cultural analysis content (BABEL's domain)

## Recency policy

- Reference works (dictionaries, grammars, scripts): timeless, no decay
- Tool and platform metrics: 18-month decay, one tier per lapse, `as_of` dated
- Known frozen sources at run time: Duolingo public counters (frozen 2025-06-23),
  Thuum.org (largely unmaintained since early 2019). Both decayed accordingly.

## Boundary note

Esperanto appears in this catalog only where it defines the frontier that fiction
conlangs have not reached: it is the sole conlang with a Universal Dependencies
treebank and a standing presence in NLP benchmarks. That absence for Klingon,
Na'vi, and the rest is itself a catalogued finding.

## Target size and result

Target was 24 to 35 assets; the research run rolled up 31, normalized to 36 distinct catalog records for this repository (grouped entries split, role duplicates merged). The full roster and cards live
in `catalog/`; the machine-readable form is `data/catalog.json`.
