---
name: graph-analyze
description: Analyze the wiki as a directed graph (pages = nodes, [[wikilinks]] = edges). Computes node/edge counts, degree, density, orphans, sinks, broken links, top hubs. Saves a structured report in _notes/graph-analysis-YYYY-MM-DD.md. Use when the user asks for wiki graph metrics, link analysis, or structural health overview.
---

# graph-analyze

Analisi del grafo orientato della wiki: ogni `.md` in `wiki/` è un nodo, ogni `[[wikilink]]` è un arco diretto. Calcola metriche di degree distribution, densità, broken links, hub principali. Output: riepilogo console + report markdown in `_notes/`.

## Quando usarla

- L'utente chiede "quanto è interconnessa la wiki?", "quali pagine sono hub?", "ci sono molti orfani?"
- Periodicamente (es. settimanale) per monitorare l'evoluzione del grafo
- Pre / post grandi ingest, per misurare l'impatto strutturale

## Procedura

```bash
python .claude/skills/graph-analyze/scripts/graph-analyze.py [--console-only]
```

Lo script:
1. Cammina ricorsivamente `wiki/` raccogliendo i nodi (file .md, indicizzati per stem lowercase)
2. Estrae i `[[wikilink]]` dai body
3. Distingue link interni validi (target esiste) da broken
4. Calcola: N, L_internal, L_broken, ⟨K_out⟩, ⟨K_in⟩, densità, orfani, sink, top-10 hub in/out
5. Stampa riepilogo console
6. (Salvo `--console-only`) scrive `_notes/graph-analysis-<YYYY-MM-DD>.md` con il report completo

**Output console (sempre)**:
```
Graph Analysis — 2026-05-24
N = 142  |  L = 387  |  L_broken = 12
<K_out> = 2.81  |  <K_in> = 2.73  |  d = 0.019345 (1.935%)
Orphans: 8  |  Sinks: 15
Output: /vault/_notes/graph-analysis-2026-05-24.md
```

**Output file** (solo senza `--console-only`):
- Frontmatter `type: analysis`, tag `[analysis, graph, metrics]`
- Tabella "Metriche di base"
- Tabella "Hub principali" (top-10 per in-degree)
- Tabella "Pagine più connesse in uscita" (top-10 per out-degree)
- Sezione "Lettura dei risultati" con interpretazione qualitativa di densità, orfani, broken link

## Flag

- `--console-only` — stampa riepilogo ma non scrive il file
- `--vault PATH` — usa un vault diverso da quello auto-detected

## Interazione con altre skill

- Dopo `wiki-ingest` su molti file: usa `graph-analyze` per misurare l'impatto sul grafo
- Per fix puntuali sui broken link: passa al follow-up con `wiki-lint --check structural`
- Il report `_notes/graph-analysis-*.md` finisce nella personal area, non è parte della wiki — non viene letto da `wiki-query`/`qmd embed`

## Note

- **Case-insensitive**: i nomi pagina sono normalizzati lowercase, coerente con il resto delle skill.
- **Exclude orphan list**: `index`, `log`, `overview`, `glossary`, `lint-report`, `meetings-index` sono esclusi dagli "orfani" perché auto-gestiti / strutturali.
- **Dipendenze**: zero — solo stdlib Python.
- **Performance**: O(N) sui file. Vault da 1000 pagine processata in <1s.

## Esempio d'uso

**Utente**: "Fai un'analisi del grafo della wiki"

**Skill flow**:
```bash
python .claude/skills/graph-analyze/scripts/graph-analyze.py
```

Output console + file `_notes/graph-analysis-2026-05-24.md` creato.

Riporta all'utente il riepilogo + path del file generato + 1-2 osservazioni qualitative dalla sezione "Lettura dei risultati".
