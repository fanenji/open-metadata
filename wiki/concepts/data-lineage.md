---
sources: [sources.md, Announcing OpenMetadata 1.12 1.md]
tags: [openmetadata, data-lineage, data-governance, lineage, visualization]
related: [openmetadata, ingestion-framework, column-level-lineage, lineage-layers, lineage-parser, metric-lineage, dashboard-lineage, stored-procedure-lineage, openlineage-integration, sqlglot, python-sdk]
type: concept
title: Data Lineage
created: 2024-05-24
updated: 2026-07-07
---
# Data Lineage

Data lineage in OpenMetadata tracks the flow of data from source to destination across the entire data stack — databases, pipelines, warehouses, dashboards, APIs, and ML models. It provides a visual representation of how data flows, enabling impact analysis and governance. Lineage is critical for understanding data dependencies, troubleshooting issues, and ensuring compliance with data governance policies.

## How It Works

Lineage information is captured by the [[ingestion-framework|Ingestion Framework]] during metadata extraction and is stored and visualized in the [[openmetadata|OpenMetadata]] UI.

## Lineage Types

| Type | Description |
|------|-------------|
| [[column-level-lineage|Column-Level]] | Tracks data flow at the column granularity |
| Table-Level | Tracks which tables feed into which tables |
| [[dashboard-lineage|Dashboard Lineage]] | Links dashboards to underlying datasets |
| [[metric-lineage|Metric Lineage]] | Tracks metric definitions to source data |
| [[stored-procedure-lineage|Stored Procedure Lineage]] | Lineage through stored procedures (new in 1.12) |

## 1.12 Lineage Improvements

OpenMetadata 1.12 introduced significant usability and performance enhancements:

- **Column-Only Filtering**: View lineage for specific columns, filtering out unrelated paths for cleaner visualization
- **Edge Highlighting**: Hover over nodes to highlight connected edges; selecting a node highlights the complete path from source to destination
- **Stored Procedure Support**: Edit mode now supports stored procedures in lineage graphs
- **Column Pagination**: Efficient navigation through schemas with hundreds of columns
- **SQLglot Integration**: Dramatically faster SQL query parsing for complex lineages with thousands of nodes — replacing the previous parser

## OpenLineage Integration

As of 1.12, OpenMetadata natively ingests lineage from [[openlineage-integration|OpenLineage]]-compliant producers (Flink, Spark, Airflow, dbt). This enables organizations with existing OpenLineage implementations to adopt OpenMetadata without rewriting integrations.

## Manual Lineage

Lineage can also be manually curated through the UI or [[python-sdk|Python SDK]]. See [[how-to-manually-add-or-edit-lineage---openmetadata-20260514]].

## See Also

- [[column-level-lineage]] — Column-granularity lineage details
- [[openlineage-integration]] — OpenLineage standard support
- [[lineage-layers]] — Layered lineage visualization
- [[lineage-parser]] — SQL parsing for lineage extraction
- [[explore-the-lineage-view-official-documentation----20260514]] — UI guide for lineage exploration
