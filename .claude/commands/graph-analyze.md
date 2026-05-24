---
description: Analyze the wiki as a graph and save metrics to _notes/
---

Invoca la skill `graph-analyze` per fare l'analisi del grafo della wiki.

Argomenti dall'utente: $ARGUMENTS

Flag riconosciuti:
- `--console-only` → stampa riepilogo ma non scrive il file in `_notes/`

Segui la procedura completa di `.claude/skills/graph-analyze/SKILL.md`: lo script `scripts/graph-analyze.py` calcola tutte le metriche (nodi, edge, degree, densità, orfani, sink, top hub) e scrive `_notes/graph-analysis-<YYYY-MM-DD>.md`. Riporta all'utente il riepilogo console + 1-2 osservazioni qualitative dalla sezione "Lettura dei risultati".
