---
type: analysis
title: "Graph Analysis — 2026-10-21"
tags: [analysis, graph, metrics]
created: 2026-10-21
updated: 2026-10-21
---

# Graph Analysis — 2026-10-21

## Metriche di base

| Metrica | Valore |
|---|---|
| **N** (nodi / file .md) | 621 |
| **L** (link interni validi) | 3695 |
| **L rotti** (→ pagine mancanti) | 89 |
| **⟨K_out⟩** grado uscente medio | 6.09 |
| **⟨K_in⟩** grado entrante medio | 5.95 |
| **Densità** `d = L / N(N-1)` | 0.009597 (0.960%) |
| Nodi orfani (in-degree = 0) | 0 |
| Nodi sink (out-degree = 0) | 106 |

## Hub principali (top 10 per in-degree)

| Pagina | In-degree |
|---|---|
| [[classification-tags]] | 96 |
| [[data-quality]] | 88 |
| [[openmetadata]] | 81 |
| [[glossary-terms]] | 70 |
| [[dbt-integration]] | 58 |
| [[data-observability-alerts]] | 55 |
| [[data-profiling]] | 53 |
| [[data-lineage]] | 51 |
| [[unified-metadata-graph]] | 50 |
| [[roles-and-policies]] | 46 |

## Pagine più connesse in uscita (top 10 per out-degree)

| Pagina | Out-degree |
|---|---|
| [[index]] | 640 |
| [[log]] | 199 |
| [[overview]] | 69 |
| [[openmetadata]] | 38 |
| [[powerbi-connector]] | 36 |
| [[autenticazione-autorizzazione-bot-ingestion-2026-06-15]] | 30 |
| [[glossary-terms]] | 29 |
| [[overview-api-openmetadata-metadati-tabella-2026-06-24]] | 25 |
| [[data-product-openmetadata-gestione-2026-06-29]] | 25 |
| [[classification-tags]] | 22 |

## Lettura dei risultati

- **Densità**: sparse — typical for a focused research wiki with deep but narrow cross-referencing
- **Hub dominanti**: [[classification-tags]], [[data-quality]], [[openmetadata]] — these act as anchor pages that concentrate inbound references
- **Orfani**: none — all pages are linked from at least one other page
- **Link rotti**: high (89) — actionable; run /wiki-lint for detailed report
- **Struttura della rete**: hub-and-spoke pattern with core hubs ([[classification-tags]], [[data-quality]], [[openmetadata]]) acting as central reference points, consistent with a curated research wiki

## Componenti connesse

Grafo connesso: un'unica componente da 621 pagine.

## Community tematiche (Louvain)

12 community emergenti dalla topologia dei link (modularità Q = 0.505). Le pagine-chiave sono le più centrali (PageRank) di ciascun gruppo:

| Cluster | Pagine | Pagine-chiave |
|---|---|---|
| #0 | 102 | [[test-library]], [[order-of-precedence-storage-credentials]], [[openmetadata-storage-config]], [[dimensional-validation]] |
| #1 | 81 | [[unified-metadata-graph]], [[kubernetes-native-orchestrator]], [[omjob-operator]], [[openmetadata-connectors]] |
| #2 | 79 | [[data-quality]], [[ingestion-framework]], [[data-observability-alerts]], [[data-profiling]] |
| #3 | 78 | [[classification-tags]], [[change-events-system]], [[glossary-terms]], [[glossary-tags]] |
| #4 | 71 | [[data-lineage]], [[metadata-ingestion-workflow]], [[powerbi-connector]], [[postgresql-connector]] |
| #5 | 55 | [[openmetadata]], [[dbt-integration]], [[dbt-lineage-ingestion]], [[dbt-artifact-storage]] |
| #6 | 46 | [[hybrid-rbac-abac-model]], [[viewbasic-viewall-operations]], [[resource-attributes]], [[roles-and-policies]] |
| #7 | 38 | [[openmetadata-administration]], [[openmetadata-insights]], [[openmetadata-features]], [[custom-properties]] |
| #8 | 26 | [[bot-authentication]], [[cli-ingestion-with-basic-auth]], [[metadata-cli]], [[personal-access-token]] |
| #9 | 23 | [[lineage-layers]], [[column-level-lineage]], [[data-asset-ownership]], [[data-product-layer]] |
| #10 | 16 | [[activity-feed]], [[announcements]], [[conversation-threads]], [[tasks]] |
| #11 | 6 | [[data-discovery]], [[advanced-search]], [[usage-metrics]], [[keyword-search]] |

## Centralità — hub globali e pagine-ponte

**Hub globali (PageRank)** — importanza pesata anche dall'importanza di chi linka:

| Pagina | PageRank |
|---|---|
| [[hybrid-rbac-abac-model]] | 0.0446 |
| [[openmetadata]] | 0.0321 |
| [[data-quality]] | 0.0237 |
| [[viewbasic-viewall-operations]] | 0.0234 |
| [[resource-attributes]] | 0.0222 |
| [[classification-tags]] | 0.0191 |
| [[unified-metadata-graph]] | 0.0186 |
| [[kubernetes-native-orchestrator]] | 0.0183 |

**Pagine-ponte (betweenness)** — stanno sui cammini fra gruppi diversi; rimuoverle frammenterebbe la wiki. Candidate a link ridondanti:

| Pagina | Betweenness |
|---|---|
| [[index]] | 173011.47 |
| [[log]] | 3465.04 |
| [[openmetadata]] | 2115.53 |
| [[data-quality]] | 1293.92 |
| [[classification-tags]] | 1096.41 |
| [[overview]] | 774.18 |
| [[glossary-terms]] | 672.08 |
| [[data-lineage]] | 401.37 |

## Link suggeriti (deduzione strutturale — da verificare)

Coppie di pagine **non collegate** che condividono molti vicini: candidate a un wikilink. _Deduzione topologica, non un fatto wiki — valuta caso per caso._

| Pagina A | Pagina B | Vicini in comune | Score |
|---|---|---|---|
| [[classification-tags]] | [[data-asset-ownership]] | [[creating-data-contracts]], [[creating-data-contracts-openmetadata-data-contract-20260514]], [[data-asset-versioning]], [[data-asset-versioning-openmetadata-version-control-20260514]] (18) | 7.5487 |
| [[data-lineage]] | [[data-quality]] | [[data-asset-details-page]], [[data-contracts-openmetadata-data-contracts---openm-20260514]], [[data-lineage-openmetadata-lineage-how-to-guide---o-20260514]], [[data-observability-alerts-openmetadata---openmetad-20260514]] (18) | 6.9195 |
| [[glossary-terms]] | [[tiers]] | [[classification-best-practices]], [[classification-openmetadata-data-classification-gu-20260514]], [[classification-tags]], [[creating-data-contracts]] (14) | 5.3137 |
| [[data-quality]] | [[glossary-terms]] | [[creating-data-contracts]], [[creating-data-contracts-openmetadata-data-contract-20260514]], [[data-asset-details-page]], [[data-contracts]] (13) | 5.2912 |
| [[data-observability-alerts]] | [[openmetadata]] | [[announcements]], [[custom-metrics]], [[data-quality]], [[data-quality-as-code]] (12) | 5.1479 |
| [[classification-tags]] | [[data-quality]] | [[creating-data-contracts]], [[creating-data-contracts-openmetadata-data-contract-20260514]], [[data-asset-details-page]], [[data-contracts]] (13) | 5.0217 |
| [[metadata-ingestion-workflow]] | [[openmetadata-connectors]] | [[api-services-openmetadata-connector-integration-gu-20260514]], [[custom-connectors]], [[custom-connectors-build-extend-openmetadata-easily-20260514]], [[index]] (12) | 5.0039 |
| [[data-lineage]] | [[metadata-ingestion-workflow]] | [[autopilot]], [[data-lineage-openmetadata-lineage-how-to-guide---o-20260514]], [[how-to-deploy-a-lineage-workflow---openmetadata-do-20260514]], [[index]] (11) | 4.7297 |
| [[data-lineage]] | [[data-profiling]] | [[autopilot]], [[data-asset-details-page]], [[data-contracts-openmetadata-data-contracts---openm-20260514]], [[data-discovery]] (12) | 4.5688 |
| [[hybrid-rbac-abac-model]] | [[roles-and-policies]] | [[autenticazione-autorizzazione-bot-ingestion-2026-06-15]], [[authorization-rules]], [[data-governance-openmetadata-governance-guide---op-20260514]], [[index]] (12) | 4.5605 |
| [[ingestion-framework]] | [[personal-access-token]] | [[cli-ingestion-with-basic-auth]], [[data-quality-as-code---openmetadata-documentation-20260514]], [[getting-started-with-data-quality-as-code---openme-20260514]], [[index]] (11) | 4.3946 |
| [[dbt-artifacts]] | [[openmetadata]] | [[auto-ingest-dbt-core---openmetadata-documentation-20260514]], [[data-quality]], [[dbt]], [[dbt-artifact-storage-local]] (11) | 4.288 |
| [[oracle-connector]] | [[postgresql-connector]] | [[connector-permission-issues]], [[dashboard-connectors]], [[data-lineage]], [[data-profiling]] (13) | 4.0539 |
| [[ingestion-pipeline-troubleshooting]] | [[metadata-ingestion-workflow]] | [[debug-logging-ingestion]], [[index]], [[kubernetes-native-orchestrator]], [[powerbi-connector]] (9) | 3.961 |
| [[data-asset-ownership]] | [[data-quality]] | [[creating-data-contracts]], [[creating-data-contracts-openmetadata-data-contract-20260514]], [[data-contracts]], [[data-contracts-openmetadata-data-contracts---openm-20260514]] (9) | 3.9007 |
