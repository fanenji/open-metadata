---
type: entity
title: OpenMetadata Database Connectors
created: 2026-04-04
updated: 2026-04-04
tags: [openmetadata, connectors, data-quality]
related: [openmetadata-data-quality, openmetadata-profiler, openmetadata, custom-connector-openmetadata]
sources: ["OpenMetadata Data Quality Management Guide.md"]
---
# OpenMetadata Database Connectors

OpenMetadata provides a set of built-in database connectors that enable metadata ingestion, profiling, and data quality testing across a wide range of data sources. The Data Quality module supports all of these connectors, meaning that native tests can be run on any database service that OpenMetadata can connect to.

Connectors are responsible for establishing the connection to the source database, extracting schema metadata, running profiler workflows, and executing data quality tests. The connector architecture is extensible, allowing users to build custom connectors for unsupported data sources via the [[custom-connector-openmetadata]] pattern.

## Supported Connectors (Partial List)

- Snowflake
- BigQuery
- Redshift
- Postgres
- MySQL
- Dremio (via [[openmetadata-dremio-connector]])
- Athena
- Databricks
- ClickHouse
- SingleStore
- Trino
- Presto

## Data Quality Implications

- All connectors support table-level and column-level native tests.
- Profiler workflows are available for all connectors, though performance characteristics vary.
- Connector-specific limitations (e.g., Dremio's single field size limit) may affect test execution on certain data types.
- Custom connectors require implementing the profiler and test execution interfaces to support data quality features.

## Connections

- Enables [[openmetadata-data-quality]] tests across diverse data sources.
- Supports [[openmetadata-profiler]] workflows for all connected databases.
- Custom connector pattern documented in [[custom-connector-openmetadata]].