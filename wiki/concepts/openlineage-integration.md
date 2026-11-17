---
type: concept
title: "OpenLineage Integration"
created: 2026-07-07
updated: 2026-07-07
tags: [openmetadata, lineage, standards, openlineage, interoperability]
related: [data-lineage, column-level-lineage, odcs-open-data-contract-standard, dbt, openmetadata]
sources: ["Announcing OpenMetadata 1.12 1.md"]
---
# OpenLineage Integration

**OpenLineage** is an open standard for collecting and propagating data lineage metadata. Native API ingestion of OpenLineage-compliant lineage was introduced in OpenMetadata 1.12.

## Supported Producers

OpenMetadata 1.12 can ingest lineage from any tool that emits OpenLineage events:

| Producer | Type | Notes |
|----------|------|-------|
| Apache Flink | Stream processing | Real-time lineage |
| Apache Spark | Batch/stream processing | ETL pipeline lineage |
| Apache Airflow | Orchestrator | Workflow-level lineage |
| dbt | Transformation | Model-level column lineage |
| Other OpenLineage producers | Various | Any compliant emitter |

## OpenMetadata's Extended Lineage Model

OpenMetadata's lineage goes beyond the OpenLineage spec, covering:

- **APIs** — service-to-service data flows
- **OLTP Systems** — transactional database lineage
- **Data Warehouses** — warehouse table lineage
- **Dashboards** — dashboard-to-dataset lineage
- **Data Models** — dbt model lineage
- **S3 / Object Storage** — file-level lineage

## Why It Matters

OpenLineage integration enables organizations to adopt OpenMetadata without replacing existing lineage tooling. Teams already using Spark, Flink, or Airflow with OpenLineage can immediately ingest that lineage into OpenMetadata. Combined with [[odcs-open-data-contract-standard|ODCS support]], it's part of a broader open-standards strategy to prevent vendor lock-in.

## See Also

- [[data-lineage]] — Lineage in OpenMetadata
- [[column-level-lineage]] — Column-level lineage details
- [[odcs-open-data-contract-standard]] — Companion open standard for data contracts
- [[openmetadata]] — Platform overview