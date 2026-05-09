---
type: concept
title: Bronze-Silver-Gold Architecture
created: 2026-05-07
updated: 2026-05-07
tags: [data-lake, data-lakehouse, elt, data-refinement, medallion-architecture]
related: [elt-pattern, data-lakehouse, minio, apache-iceberg, dbt, dremio, data-quality-certification-vs-usability-certification]
sources: ["Sintesi Architettura (Claude).md"]
---
# Bronze-Silver-Gold Architecture

The Bronze-Silver-Gold architecture (also known as Medallion Architecture) is a progressive data refinement pattern used in the Regione Liguria Data Platform. Data flows through three layers of increasing quality and structure within the [[data-lakehouse]].

## Layers

### Bronze (RAW)
- **Purpose**: Raw data ingestion, immutable copy of source data
- **Storage**: [[minio]] object storage with [[apache-iceberg]] table format
- **Characteristics**: Full fidelity to source, no transformations, append-only
- **Use cases**: Audit trail, reprocessing, data recovery

### Silver
- **Purpose**: Cleaned, validated, and enriched data
- **Processing**: [[dbt]] transformations via [[dremio]]
- **Characteristics**: Deduplicated, standardized schemas, quality checks applied
- **Use cases**: Cross-domain analysis, data science, reporting

### Gold
- **Purpose**: Business-ready, aggregated, curated data products
- **Processing**: [[dbt]] transformations via [[dremio]]
- **Characteristics**: Domain-specific aggregations, business logic applied, performance-optimized
- **Use cases**: BI dashboards ([[apache-superset]], Power BI), open data publication ([[ckan-portal]]), API endpoints ([[wso2-api-gateway]])

## Relationship to ELT

The Bronze-Silver-Gold pattern is the concrete implementation of the [[elt-pattern]] in the platform. Raw data is extracted and loaded into Bronze, then transformed progressively through Silver to Gold using dbt and Dremio.

## Related Concepts

- [[data-quality-certification-vs-usability-certification]]: Distinction between data quality and data readiness across layers
- [[data-lakehouse]]: The architectural foundation enabling this pattern