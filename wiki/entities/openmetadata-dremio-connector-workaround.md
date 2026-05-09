---
type: entity
title: OpenMetadata Dremio Connector Workaround
created: 2026-02-13
updated: 2026-02-13
tags: [openmetadata, dremio, connector, trino, jdbc, workaround]
related: [openmetadata, dremio, trino, openmetadata-dremio-connector, data-catalog-tool-comparison]
sources: ["OpenMetadata for data quality.md"]
---
# OpenMetadata Dremio Connector Workaround

OpenMetadata does **not** have a dedicated Dremio connector in its main release. This page documents the workarounds for connecting OpenMetadata to Dremio.

## Workaround Options

### 1. Connect via Trino (Recommended)

If Trino is available in the stack and can query the same Iceberg/Parquet data that Dremio serves, connect OpenMetadata to **Trino** instead. This is the most production-grade and plug-and-play approach.

- **Pros:** Native Trino connector in OpenMetadata, full profiling and test execution support.
- **Cons:** Requires Trino to be deployed and configured to access the same data sources.

### 2. Connect via JDBC

Use the OpenMetadata **Database Service (JDBC)** connector with Dremio's JDBC driver.

- **Pros:** Direct connection to Dremio, no intermediate engine needed.
- **Cons:** Less plug-and-play than native connectors; may have limited profiling or test execution capabilities.

### 3. Connect via DuckDB

If DuckDB is used as a lightweight query engine against Iceberg tables (via the [[duckdb-iceberg-extension]]), OpenMetadata can connect to DuckDB.

- **Pros:** DuckDB has a native OpenMetadata connector.
- **Cons:** DuckDB may not have the same performance or feature set as Dremio for large-scale queries.

## Impact on Data Quality

The workaround does not affect OpenMetadata's ability to suggest or run data quality tests. The local LLM integration (via Ollama) works independently of the query engine connection. Tests are pushed to the connected engine for execution.

## Related

- [[openmetadata]] — The main OpenMetadata entity.
- [[openmetadata-dremio-connector]] — The custom connector maintained by TIKI-Institut.
- [[data-catalog-tool-comparison]] — Comparison of data catalog tools including connector support.