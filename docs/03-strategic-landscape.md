# VLT-8: Strategic Landscape Analysis

## 1. Key data hubs

Five gravity wells hold most of the domain's high-quality data:

| Hub | Language(s) | Why it matters |
|---|---|---|
| kli.org (Klingon Language Institute) | Klingon | Canon guardian; source-cited new-word ledger; Duolingo and Microsoft partner |
| Eldamo + Elfdict + Ardalambion cluster | Tolkien's languages | The deepest and most scholarly corpus; the only one treated like a real dead language, with period stratification and sourced references |
| LearnNavi.org | Na'vi | Creator-community co-development model; source-tagged dictionary; live canon feed from naviteri.org |
| Thuum.org | Dovahzul | The cleanest canon-versus-fan labeling model in the domain (647 canonical words, thousands fan-coined, labeled) |
| David J. Peterson's ecosystem | Dothraki, High Valyrian, Chakobsa, Sangheili | The professional screen-conlang pipeline: creator wiki, licensed courses, film documentation |

Two cross-cutting hubs sit above them: Omniglot (scripts, all franchises) and
the Language Creation Society with Fiat Lingua (the profession and its
scholarly record).

## 2. Dominant technologies and platforms

- **Distribution:** Duolingo is the dominant learner-acquisition funnel; app
  stores and publisher channels carry the rest.
- **Construction:** PolyGlot (open desktop) and Vulgar (commercial generator)
  lead creation; SCA2 and Lexurgy own diachronic derivation; ConWorkShop adds
  the community and typological-analytics layer (CALS).
- **NLP frontier:** Microsoft's Bing Klingon MT (2013) remains the only
  commercial conlang MT engine. Academic work (emergent-translation MT
  experiments, ConlangCrafter, the ConlangBench preprint) is nascent and
  centers on Klingon and Esperanto.

## 3. White space (all findings tiered INFERENCE, reasoning chains included)

1. **No standardized machine-readable conlang corpus format.**
   Reasoning: across all 31 assets, every institution rolls its own format
   (Eldamo bespoke XML, Thuum CSV exports, Elfdict imports, PDF dictionaries).
   No shared schema surfaced anywhere in the sweep. Highest-value intervention.
2. **Zero DCAT, schema.org, or Croissant metadata on any conlang dataset.**
   Reasoning: none of the catalogued assets exposes discovery metadata; even
   the open-licensed Eldamo ships raw XML. The crosswalk in this repo is the
   direct response.
3. **Fragmentation of fan institutions.**
   Reasoning: a single language splits across incompatible sources with
   different counts (Klingon across kli.org, boQwI'/GitHub, Klingonska,
   Duolingo). No canonical join key exists.
4. **Canon-versus-reconstruction labeling is an unsolved data-quality problem.**
   Reasoning: Dovahzul's 647 canonical versus 4,000-plus fan words,
   Neo-Sindarin and Neo-Quenya, and Neo-Chakobsa all mix authorial and fan
   material; only Thuum.org and Eldamo label systematically. A labeling
   standard is a sellable deliverable.
5. **Commercial licensing ambiguity around franchise-owned languages.**
   Reasoning: the most popular languages are IP-encumbered (Paramount/CBS,
   Disney, HBO, Bethesda); the fan databases survive on fair-use disclaimers.
   Any licensable knowledge base must carry per-asset rights flags, which
   this catalog does.
6. **Na'vi is a genuine academic-data gap.**
   Reasoning: a null result is a finding. No dedicated Na'vi NLP or MT corpus
   surfaced, and only Esperanto has a Universal Dependencies treebank among
   conlangs. Conlang NLP remains Klingon- and Esperanto-centric.

## 4. Ecosystem map

Nodes are owners, institutions, and assets; edges use the ontology relations.
The machine-readable edge list is `data/ecosystem-edges.csv`. Summary:

```
Marc Okrand        --owns/documents-->    Klingon
KLI                --guards_canon_of-->   Klingon
Duolingo           --teaches-->           Klingon, High Valyrian
Microsoft Bing MT  --derived_from-->      KLI corpus
J.R.R. Tolkien     --owns-->              Quenya, Sindarin, Khuzdul, ...
Ardalambion        --documents-->         Tolkien languages
Eldamo             --documents-->         Tolkien languages
Elfdict            --derived_from-->      Eldamo, Ardalambion
David J. Peterson  --owns/documents-->    Dothraki, High Valyrian, Chakobsa, Sangheili
LCS                --hosts-->             the profession (Fiat Lingua, LCC)
Paul Frommer       --owns-->              Na'vi
LearnNavi.org      --hosts/teaches-->     Na'vi
Bethesda           --owns-->              Dovahzul
Thuum.org          --guards_canon_of-->   Dovahzul
Nick Farmer        --owns-->              Belter Creole
Omniglot           --hosts-->             scripts (cross-franchise)
Fiat Lingua        --cites-->             the field's scholarship
```

## Thresholds that change the plan

- If ConlangBench (or a comparable standardized multi-conlang corpus) is
  confirmed genuine and openly licensed, de-prioritize building a new corpus
  and wrap or extend it instead; white space item 1 partially closes.
- If a franchise owner signals licensing willingness, flip the flagship pilot
  from Eldamo to that franchise's catalog, because licensed data commands
  higher margin.
- If Duolingo resumes public metric refreshes, upgrade its metrics from decayed
  STATED toward CORROBORATED where an independent tracker agrees.
