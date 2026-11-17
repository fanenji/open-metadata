---
type: analysis
title: "Graph Analysis — 2026-06-16"
tags: [analysis, graph, metrics]
created: 2026-06-16
updated: 2026-06-16
---

# Graph Analysis — 2026-06-16

## Metriche di base

| Metrica | Valore |
|---|---|
| **N** (nodi / file .md) | 585 |
| **L** (link interni validi) | 2994 |
| **L rotti** (→ pagine mancanti) | 87 |
| **⟨K_out⟩** grado uscente medio | 5.27 |
| **⟨K_in⟩** grado entrante medio | 5.12 |
| **Densità** `d = L / N(N-1)` | 0.008764 (0.876%) |
| Nodi orfani (in-degree = 0) | 197 |
| Nodi sink (out-degree = 0) | 104 |

## Hub principali (top 10 per in-degree)

| Pagina | In-degree |
|---|---|
| [[classification-tags]] | 94 |
| [[data-quality]] | 83 |
| [[glossary-terms]] | 69 |
| [[openmetadata]] | 66 |
| [[dbt-integration]] | 53 |
| [[data-profiling]] | 53 |
| [[data-observability-alerts]] | 53 |
| [[data-lineage]] | 49 |
| [[roles-and-policies]] | 46 |
| [[ingestion-framework]] | 40 |

## Pagine più connesse in uscita (top 10 per out-degree)

| Pagina | Out-degree |
|---|---|
| [[index]] | 198 |
| [[log]] | 197 |
| [[_notes/02.notes/Overview]] | 54 |
| [[data-quality-as-code]] | 40 |
| [[powerbi-connector]] | 36 |
| [[autenticazione-autorizzazione-bot-ingestion-2026-06-15]] | 30 |
| [[glossary-terms]] | 29 |
| [[classification-tags]] | 22 |
| [[workflow-deployment-error]] | 21 |
| [[auto-classification]] | 20 |

## Lettura dei risultati

- **Densità**: sparse — typical for a focused research wiki with deep but narrow cross-referencing
- **Hub dominanti**: [[classification-tags]], [[data-quality]], [[glossary-terms]] — these act as anchor pages that concentrate inbound references
- **Orfani**: significant (197) — many unlinked pages; consider cross-linking or pruning
- **Link rotti**: high (87) — actionable; run /wiki-lint for detailed report
- **Struttura della rete**: hub-and-spoke pattern with core hubs ([[classification-tags]], [[data-quality]], [[glossary-terms]]) acting as central reference points, consistent with a curated research wiki

## Componenti connesse

56 componenti — la principale ha 526 pagine; 55 isole scollegate:

- isola da 3: [[custom-sql-test-definitions]], [[test-library]], [[test-platforms]]
- isola da 2: [[dbt-artifact-storage-s3]], [[iam-policy-separation]]
- isola da 2: [[glossary-apis]], [[glossary-fqn]]
- isola da 1: [[add-complex-queries-using-advanced-search---openme-20260514]]
- isola da 1: [[advanced-usage---openmetadata-documentation-20260514]]
- isola da 1: [[airflow-dag-pattern-dbt-s3]]
- isola da 1: [[auto-classification-in-openmetadata---openmetadata-20260514]]
- isola da 1: [[auto-pii-tagging-guide-official-documentation---op-20260514]]
- isola da 1: [[best-practices-for-glossary-official-documentation-20260514]]
- isola da 1: [[bulk-import-data-assets-via-csv-in-openmetadata----20260514]]
- isola da 1: [[bulk-import-data-assets-via-csv-in-openmetadata----20260514-2]]
- isola da 1: [[chrome-extension]]
- isola da 1: [[comparisons]]
- isola da 1: [[concepts]]
- isola da 1: [[configure-data-quality-official-documentation---op-20260514]]
- isola da 1: [[creating-data-contracts-openmetadata-data-contract-20260514-2]]
- isola da 1: [[csv-import-fields-reference]]
- isola da 1: [[data-discovery-openmetadata-how-to-guide---openmet-20260514]]
- isola da 1: [[data-governance-glossary-troubleshooting-openmetad-20260514]]
- isola da 1: [[detailed-view-of-the-data-assets---openmetadata-do-20260514]]
- isola da 1: [[domains-data-products-official-documentation---ope-20260514]]
- isola da 1: [[entities]]
- isola da 1: [[external-auto-classification-workflow---openmetada-20260514]]
- isola da 1: [[external-profiler-workflow-official-documentation--20260514]]
- isola da 1: [[glossary-openmetadata-data-glossary-guide---openme-20260514]]
- isola da 1: [[glossary-styling-openmetadata-glossary-customizati-20260514]]
- isola da 1: [[how-to-discover-assets-of-interest---openmetadata--20260514]]
- isola da 1: [[how-to-invite-users-to-openmetadata---openmetadata-20260514]]
- isola da 1: [[how-to-use-data-products-official-documentation----20260514]]
- isola da 1: [[how-to-use-domains-openmetadata-governance-guide---20260514]]
- isola da 1: [[how-to-work-with-the-incident-manager-official-doc-20260514]]
- isola da 1: [[incident-status-workflow]]
- isola da 1: [[ingest-descriptions-from-dbt-official-documentatio-20260514]]
- isola da 1: [[ingest-lineage-from-dbt-official-documentation---o-20260514]]
- isola da 1: [[lineage-from-pbit-files---openmetadata-documentati-20260514]]
- isola da 1: [[metrics-for-openmetadata---openmetadata-documentat-20260514]]
- isola da 1: [[metrics-openmetadata-profiler-metrics-guide---open-20260514]]
- isola da 1: [[mini-webinar on custom connectors dataintegration connectors ingestion datacatalog metadata]]
- isola da 1: [[openmetadata community meeting oct 2023 release 1 2 0 datamesh openmetadata]]
- isola da 1: [[oracle-connector-openmetadata-enterprise-database--20260514]]
- isola da 1: [[overview-of-classification-official-documentation--20260514]]
- isola da 1: [[overview-of-data-assets-official-documentation---o-20260514]]
- isola da 1: [[postgresql-connector-troubleshooting---openmetadat-20260514]]
- isola da 1: [[powerbi-connector-openmetadata-integration-documen-20260514]]
- isola da 1: [[publishing-results-best-practices---openmetadata-d-20260514]]
- isola da 1: [[queries]]
- isola da 1: [[research-capture-referenced-design-page-2026-05-15]]
- isola da 1: [[service-insights-overview-official-documentation---20260514]]
- isola da 1: [[superset-connector-openmetadata-dashboard-integrat-20260514]]
- isola da 1: [[synthesis]]
- isola da 1: [[system-governance-notifications-openmetadata---ope-20260514]]
- isola da 1: [[test-library-custom-sql-based-data-quality-tests---20260514]]
- isola da 1: [[testrunner---running-table-level-tests---openmetad-20260514]]
- isola da 1: [[thinkwe-need-to-answer-the-question-explain-in-det-2026-05-22-061312]]
- isola da 1: [[troubleshooting-for-import-export-issue---openmeta-20260514]]

## Community tematiche (Louvain)

14 community emergenti dalla topologia dei link (+52 pagine isolate) (modularità Q = 0.578). Le pagine-chiave sono le più centrali (PageRank) di ciascun gruppo:

| Cluster | Pagine | Pagine-chiave |
|---|---|---|
| #0 | 91 | [[ingestion-framework]], [[openmetadata-connectors]], [[bot-authentication]], [[metadata-agent]] |
| #1 | 87 | [[unified-metadata-graph]], [[kubernetes-native-orchestrator]], [[omjob-operator]], [[pipeline-service-client]] |
| #2 | 68 | [[glossary-tags]], [[classification-tags]], [[glossary-terms]], [[tag-based-access-control]] |
| #3 | 61 | [[data-quality]], [[data-observability-alerts]], [[data-profiling]], [[data-quality-as-code]] |
| #4 | 48 | [[hybrid-rbac-abac-model]], [[viewbasic-viewall-operations]], [[resource-attributes]], [[roles-and-policies]] |
| #5 | 44 | [[dbt-integration]], [[dbt-lineage-ingestion]], [[dbt-artifact-storage]], [[dbt-artifacts]] |
| #6 | 40 | [[openmetadata-collaboration]], [[change-events-system]], [[tag-request-workflow]], [[conversations-around-classification]] |
| #7 | 38 | [[data-lineage]], [[openmetadata-features]], [[openmetadata-administration]], [[lineage-layers]] |
| #8 | 24 | [[openmetadata-insights]], [[data-insights-application-troubleshooting]], [[application-framework]], [[service-insights]] |
| #9 | 17 | [[openmetadata]], [[dimensional-validation]], [[data-products]], [[domains]] |
| #10 | 8 | [[test-case]], [[test-definition]], [[test-case-result]], [[test-suite]] |
| #11 | 3 | [[test-library]], [[custom-sql-test-definitions]], [[test-platforms]] |
| #12 | 2 | [[dbt-artifact-storage-s3]], [[iam-policy-separation]] |
| #13 | 2 | [[glossary-apis]], [[glossary-fqn]] |

## Centralità — hub globali e pagine-ponte

**Hub globali (PageRank)** — importanza pesata anche dall'importanza di chi linka:

| Pagina | PageRank |
|---|---|
| [[openmetadata]] | 0.0855 |
| [[hybrid-rbac-abac-model]] | 0.0419 |
| [[unified-metadata-graph]] | 0.0345 |
| [[data-quality]] | 0.0303 |
| [[data-lineage]] | 0.0253 |
| [[ingestion-framework]] | 0.0237 |
| [[viewbasic-viewall-operations]] | 0.0223 |
| [[resource-attributes]] | 0.0211 |

**Pagine-ponte (betweenness)** — stanno sui cammini fra gruppi diversi; rimuoverle frammenterebbe la wiki. Candidate a link ridondanti:

| Pagina | Betweenness |
|---|---|
| [[index]] | 54877.16 |
| [[log]] | 17828.71 |
| [[data-quality]] | 14400.18 |
| [[openmetadata]] | 13716.02 |
| [[data-observability-alerts]] | 9130.39 |
| [[classification-tags]] | 8968.29 |
| [[powerbi-connector]] | 7006.88 |
| [[glossary-terms]] | 6945.01 |

## Link suggeriti (deduzione strutturale — da verificare)

Coppie di pagine **non collegate** che condividono molti vicini: candidate a un wikilink. _Deduzione topologica, non un fatto wiki — valuta caso per caso._

| Pagina A | Pagina B | Vicini in comune | Score |
|---|---|---|---|
| [[data-profiling]] | [[data-quality]] | [[column-level-tests]], [[custom-metrics]], [[custom-metrics---openmetadata-documentation-20260514]], [[data-asset-details-page]] (31) | 15.9632 |
| [[classification-tags]] | [[openmetadata]] | [[apis-openmetadata-metadata-standard-apis---openmet-20260514]], [[classification-best-practices]], [[data-governance-openmetadata-governance-guide---op-20260514]], [[data-products]] (19) | 9.5295 |
| [[classification-tags]] | [[data-asset-ownership]] | [[creating-data-contracts]], [[creating-data-contracts-openmetadata-data-contract-20260514]], [[data-asset-versioning]], [[data-asset-versioning-openmetadata-version-control-20260514]] (18) | 8.1541 |
| [[data-lineage]] | [[data-quality]] | [[data-asset-details-page]], [[data-contracts-openmetadata-data-contracts---openm-20260514]], [[data-lineage-openmetadata-lineage-how-to-guide---o-20260514]], [[data-observability-alerts-openmetadata---openmetad-20260514]] (17) | 7.0212 |
| [[data-quality]] | [[ingestion-framework]] | [[admin-guide-openmetadata-administration-documentat-20260514]], [[custom-tests]], [[custom-tests-openmetadata-quality-testing-guide----20260514]], [[data-quality-as-code]] (15) | 6.9003 |
| [[glossary-terms]] | [[openmetadata]] | [[classification-best-practices]], [[data-governance-openmetadata-governance-guide---op-20260514]], [[data-products]], [[domains]] (14) | 6.3904 |
| [[glossary-terms]] | [[tiers]] | [[classification-best-practices]], [[classification-openmetadata-data-classification-gu-20260514]], [[classification-tags]], [[creating-data-contracts]] (14) | 5.7504 |
| [[data-quality]] | [[glossary-terms]] | [[creating-data-contracts]], [[creating-data-contracts-openmetadata-data-contract-20260514]], [[data-asset-details-page]], [[data-contracts]] (12) | 5.518 |
| [[metadata-ingestion-workflow]] | [[openmetadata-connectors]] | [[api-services-openmetadata-connector-integration-gu-20260514]], [[custom-connectors]], [[custom-connectors-build-extend-openmetadata-easily-20260514]], [[index]] (12) | 5.3459 |
| [[data-lineage]] | [[metadata-ingestion-workflow]] | [[autopilot]], [[data-lineage-openmetadata-lineage-how-to-guide---o-20260514]], [[how-to-deploy-a-lineage-workflow---openmetadata-do-20260514]], [[index]] (11) | 5.2286 |
| [[classification-tags]] | [[data-quality]] | [[creating-data-contracts]], [[creating-data-contracts-openmetadata-data-contract-20260514]], [[data-asset-details-page]], [[data-contracts]] (12) | 5.1879 |
| [[ingestion-framework]] | [[personal-access-token]] | [[cli-ingestion-with-basic-auth]], [[data-quality-as-code]], [[data-quality-as-code---openmetadata-documentation-20260514]], [[getting-started-with-data-quality-as-code---openme-20260514]] (12) | 5.0628 |
| [[data-lineage]] | [[data-profiling]] | [[autopilot]], [[data-asset-details-page]], [[data-contracts-openmetadata-data-contracts---openm-20260514]], [[data-discovery]] (12) | 4.8288 |
| [[data-quality]] | [[test-runner]] | [[advanced-usage-patterns]], [[data-quality-as-code]], [[dataframe-chunk-based-validation]], [[dataframe-validator]] (8) | 4.7903 |
| [[hybrid-rbac-abac-model]] | [[roles-and-policies]] | [[autenticazione-autorizzazione-bot-ingestion-2026-06-15]], [[authorization-rules]], [[data-governance-openmetadata-governance-guide---op-20260514]], [[index]] (12) | 4.7339 |
