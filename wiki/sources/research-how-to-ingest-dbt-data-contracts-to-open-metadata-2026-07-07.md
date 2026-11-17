---
type: source
title: "Research: how to ingest dbt data contracts to open-metadata"
created: 2026-07-07
updated: 2026-07-07
tags: [dbt, data-contracts, ingestion, openmetadata, model-contracts, research]
related: [dbt-model-contracts, data-contracts, dbt-integration, dbt-lineage-ingestion, dbt-artifacts, dbt-troubleshooting, openmetadata-dbt-action]
sources: ["research-how-to-ingest-dbt-data-contracts-to-open-metadata-2026-07-07.md"]
source_path: "[[raw/sources/research-how-to-ingest-dbt-data-contracts-to-open-metadata-2026-07-07]]"
---
# Research: how to ingest dbt data contracts to open-metadata

Ricerca su come i dbt model contracts (feature nativa dbt 1.5+) vengono ingeriti in OpenMetadata e come si relazionano con gli OpenMetadata Data Contracts.

## Risultati principali

Il termine "data contracts" ha due significati distinti:

1. **dbt Model Contracts** — feature nativa dbt (Core 1.5+) che garantisce la struttura di un modello (colonne, data types, constraints) con `contract: {enforced: true}`. dbt esegue un preflight check a build-time.
2. **OpenMetadata Data Contracts** — entità nativa OpenMetadata (v1.12) per accordi formali producer-consumer su schema, semantica, qualità, SLA.

**Non esiste un bridge automatico** tra i due. I dbt model contracts vengono ingeriti come normali metadati di modello (colonne, constraints, test). Gli OpenMetadata Data Contracts vanno creati separatamente via UI.

## Metodi di ingestione

| Metodo | Descrizione |
|--------|-------------|
| Auto-ingest dbt Core | `metadata ingest-dbt` con variabili in `dbt_project.yml` |
| External Workflow | YAML con storage S3/GCS/Azure/Local |
| dbt Cloud | API diretta con token |
| GitHub Action | `openmetadata-dbt-action` per CI/CD |

## Bug noto

OpenMetadata < 1.12.4 ha il bug #27161: falsi version bump con modelli dbt che hanno column-level constraints.

## Riferimenti

- dbt Model Contracts: https://docs.getdbt.com/docs/mesh/govern/model-contracts
- OpenMetadata Data Contracts: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-contracts/spec
- Auto Ingest dbt-core: https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/auto-ingest-dbt-core