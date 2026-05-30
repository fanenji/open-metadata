---
type: entity
title: dbt (Data Build Tool)
created: 2026-05-14
updated: 2026-05-15
tags:
  - dbt
  - data-transformation
  - analytics-engineering
  - metadata
  - metadata-ingestion
  - ingestion
related:
  - dbt-integration
  - dbt-artifacts
  - dbt-lineage-ingestion
  - openmetadata
  - data-lineage
  - data-quality
  - dbt-artifact-storage
  - dbt-glossary-ingestion
  - manifest-json
sources:
  - "dbt Workflow  OpenMetadata Data Build Tool Integration.md"
  - "dbt-workflow-openmetadata-data-build-tool-integrat-20260514.md"
  - "ingest-glossary-from-dbt-official-documentation----20260514.md"
---

# dbt (Data Build Tool)

dbt is a data transformation tool that enables analytics engineers to transform data in their warehouse by writing modular SQL `SELECT` statements. OpenMetadata integrates with both dbt Core and dbt Cloud to ingest metadata from dbt‑generated JSON artifact files, enriching the [[unified-metadata-graph]] with transformation lineage, documentation, data quality test results, glossary terms, and governance metadata.

## Deployment Models

### dbt Core
Self‑hosted dbt running within the user's infrastructure (Airflow, Kubernetes, GitHub Actions, or locally). Requires manual configuration of artifact storage (S3, GCS, Azure, HTTP, or Local filesystem) so that OpenMetadata can access the generated JSON files. See [[dbt-artifact-storage]].

### dbt Cloud
SaaS dbt platform integrated via API. OpenMetadata pulls metadata directly from dbt Cloud APIs, eliminating the need for external artifact storage. Requires an active dbt Cloud account, configured jobs, and a valid API token.

## Supported Versions

OpenMetadata supports dbt Core versions v1.2 through v1.9.

## Artifact Files

dbt generates JSON files in the `target/` directory. These files are essential for metadata ingestion. See [[dbt-artifacts]] for detailed reference.

- **[[manifest-json]]** (Required) — Model definitions, lineage, descriptions, tags, ownership, domains, test configurations, and glossary term FQNs (if configured via `meta.openmetadata.glossary` in `schema.yml` files).
- **catalog.json** (Recommended) — Column data types, database‑level ownership, column ordering.
- **run_results.json** (Recommended) — Test pass/fail/warn status, execution timestamps, error messages.

## Role in OpenMetadata

dbt serves as a **transformation metadata connector** — distinct from typical database/service connectors. Rather than connecting to a live data source, OpenMetadata reads pre‑generated static artifact files to extract metadata about data transformations. This makes dbt a unique category within the [[openmetadata-connectors]] ecosystem.

## Metadata Categories

OpenMetadata ingests ten categories of metadata from dbt. These include model definitions, lineage, descriptions, tags, ownership, domains, test configurations, column metadata, execution results, and glossary terms. See [[dbt-integration]] for the full list.

## Glossary Ingestion via dbt

dbt supports associating OpenMetadata glossary terms with models and columns through the `meta.openmetadata.glossary` configuration in `schema.yml` files. This configuration embeds glossary term Fully Qualified Names (FQNs) into the [[manifest-json]] artifact, which OpenMetadata ingests during the dbt workflow.

For detailed instructions, see [[dbt-glossary-ingestion]].

## Related

- [[dbt-integration]] — Overall integration overview.
- [[dbt-artifacts]] — Detailed artifact file reference.
- [[dbt-lineage-ingestion]] — Lineage extraction from dbt.
- [[dbt-artifact-storage]] — Storage configuration for dbt Core.
- [[dbt-glossary-ingestion]] — Glossary term ingestion via dbt.
- [[manifest-json]] — The primary artifact carrying glossary and other metadata.
- [[openmetadata]] — The metadata platform.