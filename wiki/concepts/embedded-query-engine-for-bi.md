---
type: concept
title: Embedded Query Engine for BI
created: 2025-02-10
updated: 2025-02-10
tags: [bi, query-engine, duckdb, architecture, future-trend]
related: [duckdb, duckdb-iceberg-sufficiency, rill, medium-scale-data-architecture]
sources: ["Quando duckdb e iceberg sono sufficienti?.md"]
---
# Embedded Query Engine for BI

The architectural pattern where Business Intelligence (BI) tools embed a lightweight query engine (like [[duckdb]]) directly in the client application, rather than querying a remote data warehouse.

## How It Works

- The BI tool (e.g., [[Rill]], PowerBI, Tableau) ships with an embedded DuckDB instance.
- Data is stored in open formats ([[iceberg]], Delta, Parquet) on object storage (S3, GCS).
- The BI tool reads data directly from object storage using the embedded engine, bypassing the need for a dedicated warehouse.
- Queries execute locally on the client machine, reducing latency and eliminating warehouse compute costs.

## Advantages

- **No warehouse needed:** For most organizations, a dedicated warehouse becomes unnecessary.
- **Lower cost:** No per-query or per-compute pricing. Only storage costs remain.
- **Simpler architecture:** Fewer moving parts, easier to manage.
- **Offline capability:** BI dashboards can work without network connectivity to a warehouse.

## Current Status

- [[Rill]] is the first BI tool to adopt this pattern, using DuckDB as its embedded engine.
- Commenters in the DuckDB-Iceberg discussion predict this will become mainstream: "If PowerBI, Tableau, or Looker simply ran DuckDB on the client, most organizations wouldn't need Snowflake."

## Limitations

- **Data volume:** The client machine must have enough RAM to process the query. Very large datasets (>2-3 TB) may not fit.
- **Concurrency:** Each user runs their own DuckDB instance. There is no shared cache or result reuse.
- **Security:** Access control must be handled at the storage layer (IAM), not within the BI tool.
- **Complex queries:** Very complex joins or aggregations may be slower than a dedicated warehouse.

## Future Outlook

If major BI vendors adopt this pattern, it could fundamentally change the data architecture landscape. The warehouse would become optional for most organizations, reserved only for the largest datasets or most demanding workloads.

## Related Concepts

- [[duckdb-iceberg-sufficiency]] — The broader architecture that enables this pattern.
- [[medium-scale-data-architecture]] — The category of architectures where this pattern is most relevant.