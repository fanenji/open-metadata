---
type: concept
title: Data Lakehouse
created: 2026-02-13
updated: 2026-05-07
tags: [architecture, storage, data-architecture, data-lake, data-warehouse, data-engineering, lakehouse]
related: [minio, apache-iceberg, project-nessie, data-mesh, monolithic-data-lake, data-ingestion-architectural-patterns, medallion-architecture, data-quality-certification-vs-usability-certification, network-shuffle, iceberg-query-engine-comparison]
sources: ["Analisi Architettura Data Platform Regionale_ .md", "DATA MESH.md", "if-you-understand-these-5-data-engineering-terms-youre-ahead-of-90-of-the.md"]
---
# Data Lakehouse

A data lakehouse is a hybrid data architecture that combines the flexibility and low-cost storage of a data lake with the ACID transaction support, schema enforcement, and performance optimization of a data warehouse. The Data Lakehouse architecture implemented in this platform specifically combines the low-cost, scalable storage of a Data Lake with the ACID transactions and management capabilities of a Data Warehouse.

## Key Characteristics
- Single platform for BI, analytics, and machine learning
- ACID transactions on data lake storage
- Schema enforcement and evolution
- Direct access to raw data alongside structured tables
- Open formats (e.g., Apache Iceberg, Delta Lake, Parquet)

## Core Components (Platform Implementation)
- **Storage**: [[minio]] (S3-compatible object storage).
- **Table Format**: [[apache-iceberg]] (enables schema evolution and time travel).
- **Catalog/Versioning**: [[project-nessie]] (provides Git-like branching and merging for data).

## Medallion Architecture as a Lakehouse Pattern

The most common organizational pattern for data lakehouses is the [[medallion-architecture]], which structures data into three quality tiers:

- **Bronze:** Raw ingested data, preserved for replay and audit.
- **Silver:** Cleaned, typed, and validated data.
- **Gold:** Business-ready aggregations and star schemas.

This pattern brings governance and auditability to the lakehouse, turning a potential data swamp into a managed supply chain. It also enables efficient debugging: when a metric is wrong, engineers can trace the issue through the tiers rather than untangling complex SQL.

## Relationship to Data Mesh
The data lakehouse is an architectural pattern that can serve as the storage and compute foundation for a [[data-mesh]] implementation. However, it does not address the organizational and ownership principles of mesh — it is a technology enabler, not a governance paradigm. It is mentioned in the TDWI survey as a related trend to data mesh.

## Relationship to Monolithic Data Lake
The lakehouse addresses some technical limitations of the [[monolithic-data-lake]] (e.g., performance, ACID guarantees) but does not solve the ownership and scalability problems that data mesh targets.