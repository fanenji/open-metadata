---
description: Analyze the wiki as a graph and save metrics to _notes/
---

Analyze the wiki knowledge base as a directed graph where each `.md` file in `wiki/` is a node and each `[[wikilink]]` is a directed edge. Save the results to `_notes/graph-analysis-YYYY-MM-DD.md`.

Run:

```bash
python3 _system/scripts/graph-analyze.py [--console-only]
```

Optional flag in $ARGUMENTS:
- `--console-only` — print results to console only, do not write the output file

The script collects all `.md` nodes under `wiki/`, extracts `[[wikilink]]` edges (normalizing targets), and computes: node/edge counts, average in/out degree, graph density, orphan pages, sink pages, broken links, and top-10 hubs by in-degree and out-degree.

Output file `_notes/graph-analysis-YYYY-MM-DD.md` uses this structure:

```markdown
---
type: analysis
title: "Graph Analysis — YYYY-MM-DD"
tags: [analysis, graph, metrics]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Graph Analysis — YYYY-MM-DD

## Metriche di base

| Metrica | Valore |
|---|---|
| **N** (nodi / file .md) | N |
| **L** (link interni validi) | L_internal |
| **L rotti** (→ pagine mancanti) | L_broken |
| **⟨K_out⟩** grado uscente medio | K_out |
| **⟨K_in⟩** grado entrante medio | K_in |
| **Densità** `d = L / N(N-1)` | d (d*100%) |
| Nodi orfani (in-degree = 0) | N_orphans |
| Nodi sink (out-degree = 0) | N_sinks |

## Hub principali (top 10 per in-degree)
...

## Pagine più connesse in uscita (top 10 per out-degree)
...

## Lettura dei risultati
...
```

Console summary is always printed regardless of `--console-only`.

---

## Context

- Wiki root: `wiki/`
- Output directory: `_notes/`
- Script: `_system/scripts/graph-analyze.py`
- Do NOT modify any file in `wiki/` or `raw/`
- Today's date: available from system context
