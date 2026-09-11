# Category A: Datasets & Benchmarks

Eleven assets. Lexicons, corpora, dictionaries, glossed-dialogue datasets, and NLP benchmarks. Machine-readable form: `data/catalog.json` (ids `vault:conlang-a01` through `a11`).

---

## a01. The Klingon Dictionary (TKD) `[V]`

- **URL:** https://www.simonandschuster.com/books/The-Klingon-Dictionary
- **Owner/Creator:** Marc Okrand; Pocket Books / Simon & Schuster. IP: Paramount/CBS.
- **Published:** 1st ed. 1985; 2nd ed. 1992 (ISBN 0-671-74559-X)
- **Description:** The foundational creator-published lexicon and grammar of tlhIngan Hol. The canonical anchor for all Klingon data and the model every screen conlang has followed since.
- **Metrics:** 1,586 words in the 1985 first edition `[S]`; 1,889 after the 1992 addendum (+219 words) `[S]`; "about 3,000" in modern popular usage `[U]`; 4,221 entries in maintainer De'vID's aggregated lexicon as of 2018-09 `[S]`.
- **Rights flag:** franchise-ip
- **Relations:** documents Klingon; cited by a02, d06, d07; companion volumes The Klingon Way (1996), Klingon for the Galactic Traveler (1997).

## a02. KLI "New Klingon Words" List `[V]`

- **URL:** https://www.kli.org/about-klingon/new-klingon-words/
- **Owner/Creator:** Klingon Language Institute; volunteer curation team.
- **Description:** Post-TKD canonical additions from confirmed Okrand sources, each entry source-cited with an abbreviation key. A living census of canon expansion, refreshed after each annual qep'a'.
- **Metrics:** Acceptance rule: confirmed Okrand sources only `[V]`.
- **Rights flag:** fair-use-community (content cites franchise-ip canon)
- **Relations:** derived_from a01; guarded by b02; feeds d06.
- **Why it matters:** The canonical-labeling exemplar. Every entry carries provenance, which is exactly the discipline VAULT recommends domain-wide.

## a03. Eldamo: An Elvish Lexicon / Elvish Data Model `[V]`

- **URL:** https://eldamo.org/ (data: https://github.com/pfstrack/eldamo)
- **Owner/Creator:** Paul Strack. Launched 2008; v0.8.13 generated 2026-05-31. License: CC-BY.
- **Description:** XML-backed lexicon of all Tolkien's invented languages, stratified by period (Early 1910-30, Middle 1930-50, Late 1950-73), with etymological relations and stable per-reference identifiers (example: LotR/0305.0604).
- **Metrics:** "Tens of thousands" of lexical entries per third-party encyclopedic description `[S]`; covers Quenya, Sindarin, Noldorin, Telerin, Khuzdul, Valarin, Adunaic, Westron, and more `[C]`; no new Tolkien words added since v0.8.6 (2023-05) `[V]`.
- **Rights flag:** open-license
- **Relations:** documents Tolkien languages; feeds a04; parallels d08.
- **Why it matters:** The only conlang dataset already built on a formal data model with an open license and stable identifiers. The natural pilot for a DCAT/Croissant wrapper.

## a04. Parf Edhellen / Elfdict `[C]`

- **URL:** https://www.elfdict.com/
- **Owner/Creator:** Open-source collaborative project, roughly 15 years running.
- **Description:** Aggregated Elvish dictionary importing multiple quality sources (Eldamo, Hiswelokë, Fauskanger's Quettaparma Quenyallo), searchable by sense and conjugation.
- **Metrics:** 136,992 words; 49,436 active glosses; 72 phrases `[S]` (site self-report).
- **Rights flag:** fair-use-community
- **Relations:** derived_from a03 and d08.
- **Data-quality note:** Demonstrates the aggregation-versus-canon tension; imported glosses can drift from source.

## a05. Na'vi-English Dictionary (LearnNavi.org) `[C]`

- **URL:** https://files.learnnavi.org/dicts/NaviDictionary.pdf
- **Owner/Creator:** Community-compiled (Tìtstewan / Roland R.S.; previously Mark Miller); canon authority Dr. Paul Frommer.
- **Description:** The most comprehensive fan-maintained Na'vi lexicon, source-tagged per word, seeded from roughly 500 Frommer words in 2010-03 and grown through the Lexical Expansion Project.
- **Metrics:** ~2,656 words per the Wikibooks print version `[S]`; "2,000+ attested as of 2026" per secondary sources `[U]`; new canon flows from naviteri.org `[V]`.
- **Rights flag:** fair-use-community (canon: franchise-ip, Disney/Fox)
- **Relations:** hosted by b04; canon derived_from Paul Frommer.

## a06. Dothraki Dictionary (languageinvention.com wiki) `[C]`

- **URL:** https://wiki.languageinvention.com/index.php?title=Dothraki_Dictionary
- **Owner/Creator:** David J. Peterson (creator-hosted wiki). Franchise: HBO.
- **Description:** Creator-hosted Dothraki lexicon with IPA, part of speech, and glossed example sentences.
- **Metrics:** 3,163 words as of 2011-09 per Wired, cited on Wikipedia `[C]`; "over 3,000" commonly cited `[C]`; Martin's novels contained roughly 30 Dothraki words; Peterson delivered 1,700+ before initial shooting `[C]`.
- **Rights flag:** franchise-ip (creator-hosted documentation)
- **Relations:** documents Dothraki; companion product d09.

## a07. Dragon Language (Dovahzul) Dictionary, Thuum.org `[V]`

- **URL:** https://www.thuum.org/
- **Owner/Creator:** Community-organized (paarthurnax et al.). Language IP: Bethesda Softworks.
- **Description:** Dictionary of Dovahzul from The Elder Scrolls V: Skyrim, distinguishing canonical from fan-made entries by an explicit canonicity field. Dual role: this record covers both the dataset and the hosting institution.
- **Metrics:** 647 words attested in the canonical language, per the Fifth Edition print dictionary `[V]`; Third Edition carried over 4,000 Dovahzul words including fan coinage, labeled by canonicity `[S]`; roughly 40 shout words officially translated in-game `[U]`. Site largely unmaintained since early 2019; expanded metrics decayed.
- **Rights flag:** fair-use-community (canon: franchise-ip, Bethesda)
- **Relations:** guards_canon_of Dovahzul; visualized in c03; exports CSV/Excel.
- **Why it matters:** The clearest canon-versus-reconstruction case study in the domain.

## a08. Belter Creole Dictionary (lang belta) `[C]`

- **URL:** https://archive.org/details/BelterCreoleDictionaryVersion1.1
- **Owner/Creator:** Language by Nick Farmer for The Expanse; e-reader "Fictionary" compiled by TheKreig.
- **Description:** English-based creole with Romance, Germanic, Slavic, Japanese, Chinese, Arabic, Hebrew, and Zulu lexical influence; Ceres dialect used on screen. Distinct novel and TV versions exist.
- **Metrics:** Over 1,000 words created by Farmer, growing on producer and fan request, per Ars Technica cited on Wikipedia `[C]`.
- **Rights flag:** creator-owned (franchise context: Alcon/Amazon)
- **Relations:** documents Belter Creole; primer hosted by SYFY.

## a09. Chakobsa / Neo-Chakobsa (Dune films) `[C]`

- **URL:** https://www.omniglot.com/conscripts/chakobsa.htm and https://dune.fandom.com/
- **Owner/Creator:** David J. Peterson and Jessie Peterson, expanding Frank Herbert's base. Franchise: Legendary.
- **Description:** The expanded Fremen language of the 2021/2024 films, with full grammar, lexicon, and a custom abugida script; noun cases marked by stress pattern. Full dialogue with glosses published at dedalvs.com.
- **Metrics:** Herbert's base of roughly 123 marked Fremen words `[U]`; full grammar, lexicon, and script by the Petersons `[C]`.
- **Rights flag:** franchise-ip
- **Relations:** script visualized in c04; creator documentation at dedalvs.com.

## a10. ConlangBench (conlang NLP benchmark) `[U]`

- **URL:** https://arxiv.org/abs/2608.03505
- **Owner/Creator:** Academic preprint.
- **Description:** Claimed first large-scale conlang NLP benchmark spanning 21 constructed languages with parallel corpora and vocabulary sets.
- **Metrics (all self-reported in abstract):** 21 conlangs; 21M+ conlang-English parallel sentence pairs (430K across the 20 non-Esperanto conlangs); 321K vocabulary entries `[S]`.
- **Verification flag:** future-dated arXiv identifier at run time; preprint pending verification. Treat with tongs.
- **Rights flag:** open-license (claimed)
- **Why it matters:** If genuine and openly licensed, this partially closes white-space item 1 and changes the build plan (see thresholds in `docs/03`).

## a11. Emergent Translation in Multi-Agent Communication (Klingon MT dataset) `[V]`

- **URL:** https://arxiv.org/pdf/1710.06922
- **Owner/Creator:** Academic paper (archived).
- **Description:** Used 15,000 English captions machine-translated into Klingon pIqaD via Bing Translator to test translation learning from monolingual captions.
- **Metrics:** 15k Klingon pIqaD captions; words occurring fewer than 5 times discarded `[V]`.
- **Rights flag:** open-license (paper); pipeline derived_from d07
- **Why it matters:** Concrete precedent for conlangs as low-resource MT testbeds.
