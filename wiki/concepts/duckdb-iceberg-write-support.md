---
type: concept
title: DuckDB Iceberg Write Support
created: 2025-02-10
updated: 2026-05-07
tags: [duckdb, iceberg, write-support, limitation, lakehouse]
related: ["duckdb", "iceberg", "duckdb-iceberg-limitations", "pyiceberg", "duckdb-iceberg-extension", "local-iceberg-development-stack", "data-lakehouse", "iceburg-query-engine-comparison", "dwicky-feri", "dlthub", "duckdb-iceberg-sufficiency"]
sources:
  - "Quando duckdb e iceberg sono sufficienti?.md"
  - "Writing Iceberg Tables with DuckDB 1.4.0 A Practical Starter Guide.md"
---
# DuckDB Iceberg Write Support

## Overview

DuckDB Iceberg Write Support refers to the ability of [[duckdb]] to write data directly to [[iceberg]] tables. Initially, as of early 2025, DuckDB lacked native write support and could only read Iceberg tables with limitations. With the release of version 1.4.0, DuckDB introduced the ability to write Apache Iceberg tables directly, enabling local, lightweight authoring of production‑grade open table formats without requiring heavy infrastructure like Spark or Flink. This write capability operates via the `iceberg` extension and an Iceberg REST catalog connection.

## Historical Context (Pre‑1.4.0)

Before version 1.4.0, DuckDB's Iceberg support was limited:

- **Read‑only:** DuckDB could only read Iceberg tables (with limitations) and could not write to them.
- **Intermediate formats required:** Transformations had to output to formats like Parquet, Arrow, or CSV.
- **Separate tooling needed:** Writing to Iceberg required dedicated tools such as [[PyIceberg]], Apache Spark, or Apache Flink.
- **No ACID writes:** DuckDB could not participate in Iceberg's optimistic concurrency for writes, limiting its use in transactional pipelines.
- **Limited automation:** Automated pipelines that write to Iceberg could not use DuckDB as the sole engine.

**Workarounds (still useful for some scenarios):**
- Use DuckDB for in‑memory transformations, write results to Parquet files, and then commit the Parquet files as a new Iceberg snapshot using [[PyIceberg]].
- Use DuckDB's `COPY` statement to Parquet, followed by a separate process (e.g., Python with PyIceberg) to append to Iceberg.
- Use [[dlthub]] for ingestion into Iceberg, with DuckDB as an intermediate transformation step.

## Current State (Version 1.4.0+)

DuckDB 1.4.0 introduced native write support for Iceberg tables. The following subsections describe configuration, capabilities, and current limitations.

### Configuration

Writing Iceberg tables requires the `iceberg` extension and an Iceberg REST catalog. A typical setup uses the `ATTACH` statement:

```sql
INSTALL iceberg;
LOAD iceberg;

CREATE OR REPLACE SECRET iceberg_rest (
  TYPE ICEBERG,
  TOKEN 'dummy'
);

ATTACH 'icelake' AS icelake (
  TYPE ICEBERG,
  ENDPOINT 'http://<catalog>:8181/catalog/',
  SECRET iceberg_rest
);
```

> **Note:** The example uses a dummy token and is not production‑ready. For production use, configure appropriate credentials and secure endpoints.

### Capabilities

- Create schemas and tables in an Iceberg catalog.
- Insert rows into Iceberg tables.
- Query Iceberg tables via DuckDB.
- Works with any Iceberg REST catalog (e.g., Lakekeeper).
- Enables local prototyping of Iceberg workflows before scaling to distributed engines.

### Limitations

Despite the new write support, several limitations remain:

- **Production authentication:** The documented setup uses a dummy token; proper secret management is required for production.
- **Performance benchmarking:** Large‑write performance has not yet been benchmarked; users should test with their data volumes.
- **Partitioning and schema evolution:** The write interface does not yet expose all Iceberg table maintenance operations (e.g., partition transformations, schema evolution) – these are not covered and may require external tools.
- **Concurrent writes:** Iceberg's optimistic concurrency for concurrent writes is not addressed; DuckDB's behavior under concurrent write attempts is not specified.
- **No ACID guarantees from DuckDB:** While Iceberg itself provides ACID properties at the table format level, DuckDB’s writer does not yet participate in multi‑table transactions or offer its own ACID guarantees over the write process.

These limitations are expected to diminish as the feature matures (see [[iceberg-query-engine-comparison]] for context on how DuckDB fits among other query engines).

## Significance and Future Outlook

The addition of Iceberg write support in DuckDB 1.4.0 fulfills a long‑standing community request and significantly lowers the barrier to entry for working with open table formats. Data engineers and analysts can now prototype Iceberg workflows locally and iterate using familiar SQL, then scale to distributed engines when needed. DuckDB is now a viable Iceberg writer, complementing its existing read capabilities.

However, the feature is still in its early stages. Future developments are expected to fill the gaps in partitioning, schema evolution, concurrent write support, and performance optimisation. As of mid‑2025 and beyond, DuckDB’s Iceberg write support is a rapidly evolving area.

## Related Concepts

- [[duckdb-iceberg-limitations]] — Broader context of DuckDB's Iceberg limitations (including read capabilities)
- [[duckdb-iceberg-sufficiency]] — Architectural discussion where write limitations may be a constraint
- [[PyIceberg]] — Python library for Iceberg operations
- [[dlthub]] — Data ingestion framework that works with DuckDB and Iceberg
- [[local-iceberg-development-stack]] — Docker‑based stacks that pair with DuckDB’s REST catalog support
- [[iceberg-query-engine-comparison]] — Comparative analysis of query engines for Iceberg
- [[data-lakehouse]] — Lakehouse architecture context
- [[dwicky-feri]] — (possible reference to related project/tutorial)