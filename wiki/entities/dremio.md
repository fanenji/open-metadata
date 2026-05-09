---
type: entity
title: Dremio
created: 2026-05-22
updated: 2026-05-07
tags: 
  - "data-virtualization"
  - "query-engine"
  - "semantic-layer"
  - "analytics"
  - "dremio"
  - "data-lakehouse"
  - "dremio-udf-gis"
  - "dremio-semantic-layer"
  - "dremio-acceleration-engine"
  - "nessie-catalog-versioning"
  - "iceberg-table-versioning"
  - "dremio-arctic"
  - "dremio-sonar"
related:
  - "data-virtualization-layer"
  - "apache-iceberg"
  - "project-nessie"
  - "minio"
  - "data-storage-layer"
  - "nessie-versioning-strategy"
  - "dremio-geospatial-limitations"
  - "dremio-system-configuration"
  - "dremio-mcp-server"
  - "dremio-nessie-branch-workaround"
  - "geospatial-etl-pipeline-iceberg"
  - "dremio-udf-gis"
  - "dremio-semantic-layer"
  - "dremio-acceleration-engine"
  - "nessie-catalog-versioning"
  - "iceberg-table-versioning"
  - "data-lakehouse"
  - "dremio-arctic"
  - "dremio-sonar"
sources:
  - "Analisi Architettura Data Platform Regionale_ .md"
  - "AMBIENTI.md"
  - "DREMIO - NOTE.md"
  - "Dremio.md"
---
# Dremio

**Dremio** is a data virtualization and access layer that provides a semantic layer for the platform. As a central component of the Data Platform, it serves as a data lakehouse query engine, enabling high-performance SQL analytics directly on data lake storage (e.g., Apache Iceberg, Parquet, JSON) and external sources (e.g., PostGIS). It combines a query engine with a semantic layer, distinguishing it from pure query engines like Trino/Presto. Dremio enables the creation of Virtual Datasets (VDS) from Physical Datasets (PDS) and offers a unified SQL interface across heterogeneous sources.

## Architecture

Dremio's architecture consists of several key components:

- **Dremio Sonar** — The core query engine component that executes SQL queries against data lake storage.
- **Dremio Arctic** — A managed service offering that integrates Dremio with Nessie catalog versioning for Git-like data management.
- **Semantic Layer** — An abstraction layer providing business-friendly views of underlying data through Virtual Datasets (VDS) and Physical Datasets (PDS). Dremio "Spaces" organize project-specific queries and business logic across environments (e.g., `dev`, `sandbox`, `staging`, `prod`).
- **Acceleration Engine** — A caching and optimization layer that uses Data Reflections (materialized views + indexes) to accelerate query performance.

### Environment Isolation

To ensure high availability and prevent resource contention, Dremio is deployed in two distinct instances:

1. **Development Instance**: Supports the `DEV` and `SANDBOX` environments.
2. **Production Instance**: Supports the `STAGING` and `PROD` environments.

Separating environments guarantees that heavy analytical queries or pipeline runs in the staging/development environment cannot compromise the performance or stability of the production instance.

## Key Features

- **Virtual Datasets (VDS)** — Dremio's term for views and transformations that provide semantic abstractions over physical data.
- **Physical Datasets (PDS)** — Dremio's term for source tables directly referencing underlying storage.
- **Data Reflections** — Performance optimization artifacts that function as materialized views and indexes, automatically maintained by Dremio.
- **Nessie Integration** — Native support for Nessie catalog-level versioning, enabling branching, tagging, and time-travel queries. Note that some branch operations may require a macro workaround (see [[dremio-nessie-branch-workaround]]).
- **Iceberg Support** — Full support for Apache Iceberg table format, including schema evolution, partitioning, and snapshot isolation.
- **Security** — Implements granular row- and column-level access control.
- **Geospatial Support** — Provides limited native support for Iceberg GEO types; complex operations require User-Defined Functions (UDFs) (see [[dremio-geospatial-limitations]] and [[dremio-udf-gis]]).
- **System Configuration** — Exposes tunable parameters such as `limits.single_field_size_bytes` for performance tuning (see [[dremio-system-configuration]]).

## Deployment Options

- **Self-hosted** — Deployed on-premises or in private cloud infrastructure.
- **Dremio Cloud** — Fully managed cloud service.
- **Dremio Arctic** — Managed service with integrated Nessie versioning.

## Integration Patterns

- **With dbt** — dbt-dremio adapter enables dbt transformations on Dremio-managed data.
- **With OpenMetadata** — Custom OpenMetadata connector for metadata ingestion (see [[Dremio Connector]]).
- **With MCP** — [[dremio-mcp-server]] enables AI agent interaction with Dremio data.
- **With Geospatial Tools** — [[dremio-udf-gis]] extends Dremio with OGC-standard geospatial functions.

## Configuration Notes

- The default `limits.single_field_size_bytes` is 32,000 bytes; must be increased for large PostGIS geometry fields (see [[dremio-system-configuration]]).
- Nessie branch support may require a macro workaround (see [[dremio-nessie-branch-workaround]]).
- A self-hosted MCP server is available for AI-driven agent interaction (see [[dremio-mcp-server]]).

## Known Limitations

- **Geospatial Limitations**: Limited native support for Iceberg GEO types, requiring UDF dependency (see [[dremio-geospatial-limitations]]).
- **Field Size Limitation**: Single field size limit (default 32,000 bytes) affects large geometries.
- **Nessie Branch Workaround**: Branch support may require a macro workaround (see [[dremio-nessie-branch-workaround]]).

## Critical Considerations

- **Resource Consumption**: Requires significant CPU and RAM (e.g., 128 GB RAM per executor node).
- **Criticality**: Acts as a single point of failure for the platform's usability.

## Related Pages

- [[data-virtualization-layer]]
- [[apache-iceberg]]
- [[project-nessie]]
- [[minio]]
- [[data-storage-layer]]
- [[nessie-versioning-strategy]]
- [[dremio-geospatial-limitations]]
- [[dremio-system-configuration]]
- [[dremio-mcp-server]]
- [[dremio-nessie-branch-workaround]]
- [[geospatial-etl-pipeline-iceberg]]
- [[dremio-udf-gis]]
- [[dremio-semantic-layer]]
- [[dremio-acceleration-engine]]
- [[nessie-catalog-versioning]]
- [[iceberg-table-versioning]]
- [[data-lakehouse]]
- [[dremio-arctic]]
- [[dremio-sonar]]