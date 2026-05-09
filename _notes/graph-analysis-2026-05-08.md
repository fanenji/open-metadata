---
type: analysis
title: "Graph Analysis — 2026-05-08"
tags: [analysis, graph, metrics]
created: 2026-05-08
updated: 2026-05-08
---

# Graph Analysis — 2026-05-08

## Metriche di base

| Metrica | Valore |
|---|---|
| **N** (nodi / file .md) | 1759 |
| **L** (link interni validi) | 5926 |
| **L rotti** (→ pagine mancanti) | 800 |
| **⟨K_out⟩** grado uscente medio | 3.82 |
| **⟨K_in⟩** grado entrante medio | 3.37 |
| **Densità** `d = L / N(N-1)` | 0.001916 (0.192%) |
| Nodi orfani (in-degree = 0) | 786 |
| Nodi sink (out-degree = 0) | 505 |

## Hub principali (top 10 per in-degree)

| Pagina | In-degree |
|---|---|
| [[duckdb]] | 133 |
| [[openmetadata]] | 123 |
| [[model-context-protocol]] | 104 |
| [[dremio]] | 98 |
| [[data-lakehouse]] | 86 |
| [[dbt]] | 68 |
| [[data-mesh]] | 65 |
| [[dbt-testing-patterns]] | 64 |
| [[kestra]] | 60 |
| [[elt-pattern]] | 55 |

## Pagine più connesse in uscita (top 10 per out-degree)

| Pagina | Out-degree |
|---|---|
| [[log]] | 483 |
| [[index]] | 246 |
| [[service-account-authentication]] | 184 |
| [[pull-based-ingestion]] | 142 |
| [[semantic-contracts]] | 81 |
| [[openmetadata]] | 45 |
| [[modern-data-stack-overview]] | 44 |
| [[ollama]] | 40 |
| [[understanding-the-modern-data-stack]] | 36 |
| [[dremio]] | 31 |

## Lettura dei risultati

- **Densità**: sparse — typical for a focused research wiki with deep but narrow cross-referencing
- **Hub dominanti**: [[duckdb]] , [[openmetadata]] , [[model-context-protocol]] — these act as anchor pages that concentrate inbound references, suggesting they cover foundational topics
- **Orfani**: significant (786) — many unlinked pages; consider cross-linking or pruning
- **Link rotti**: high (800) — actionable; run /wiki-lint for detailed report
- **Struttura della rete**: hub-and-spoke pattern with core hubs ([[duckdb]], [[openmetadata]], [[model-context-protocol]]) acting as central reference points, consistent with a curated research wiki
