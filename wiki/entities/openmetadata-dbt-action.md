---
type: entity
title: openmetadata-dbt-action
created: 2026-07-07
updated: 2026-07-07
tags: [dbt, github-action, ci-cd, ingestion, automation, openmetadata]
related: [dbt, dbt-integration, ingestion-framework, metadata-cli]
sources: ["research-how-to-ingest-dbt-data-contracts-to-open-metadata-2026-07-07.md"]
---

# openmetadata-dbt-action

**openmetadata-dbt-action** è una GitHub Action ufficiale mantenuta dal progetto [[openmetadata|OpenMetadata]] che automatizza l'ingestione dei metadati [[dbt]] in OpenMetadata direttamente da una pipeline CI/CD.

Repository: [open-metadata/openmetadata-dbt-action](https://github.com/open-metadata/openmetadata-dbt-action)

## Scopo

L'action permette di triggerare l'ingestione dei metadati dbt (inclusi model contracts, lineage, test results) dopo ogni run di dbt in CI/CD, eliminando la necessità di configurare workflow separati in OpenMetadata.

## Utilizzo tipico

1. La pipeline CI/CD esegue `dbt run`, `dbt test`, `dbt docs generate`
2. La GitHub Action invoca `metadata ingest-dbt` (o equivalente) contro il server OpenMetadata
3. I metadati vengono automaticamente sincronizzati

## Related

- [[dbt-integration]] — Overview dell'integrazione
- [[dbt]] — Il tool di data transformation
- [[ingestion-framework]] — Framework di ingestione di OpenMetadata
- [[metadata-cli]] — La CLI `metadata` usata per l'ingestione