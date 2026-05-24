---
description: Web research on a topic with multi-query, synthesis, and wiki cross-references
---

Invoca la skill `deep-research` per fare ricerca web su un topic e integrarlo nella wiki.

Topic: $ARGUMENTS

Se vuoto, chiedi all'utente quale topic ricercare.

Segui la procedura completa di `.claude/skills/deep-research/SKILL.md`:
1. Multi-query expansion (3-5 query da topic)
2. Web search (Tavily → DuckDuckGo fallback)
3. (Opzionale) Fetch contenuto pagine via skill `defuddle` o WebFetch
4. Cross-reference QMD su wiki esistente
5. Sintesi LLM con `[[wikilink]]` cross-ref
6. Save in `wiki/queries/research-<slug>-<date>.md`
7. `qmd embed --update`
8. (Default ON, salvo l'utente lo neghi) Auto-ingest del risultato chiamando wiki-ingest

Default: auto-ingest = sì. Per saltarlo, l'utente passa `--no-ingest`.
