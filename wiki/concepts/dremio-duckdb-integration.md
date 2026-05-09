---
type: concept
title: Dremio-DuckDB Integration
created: 2026-04-29
updated: 2026-04-29
tags: [dremio, duckdb, integration, data-lakehouse, query-engine]
related: [dremio, duckdb, data-lakehouse, duckdb-iceberg-extension]
sources: ["INTEGRAZIONI.md"]
---
# Dremio-DuckDB Integration

The Dremio-DuckDB integration enables using [[DuckDB]] as a lightweight, in-process query engine against data managed by [[Dremio]]'s data lakehouse. This pattern allows analysts and data scientists to query Dremio-managed data using DuckDB's fast, single-machine analytical engine.

## Use Cases

- Lightweight ad-hoc analytics on Dremio data lakehouse
- Cost-effective querying for smaller workloads
- Local development and exploration of Dremio-managed datasets

## Resources

The integration is documented through a blog post and video tutorial from Dremio:
- [Using DuckDB with Your Dremio Data Lakehouse](https://www.dremio.com/blog/using-duckdb-with-your-dremio-data-lakehouse/)
- [EP30 - Unlock the Potential of Data Analytics with Dremio and DuckDB](https://www.youtube.com/watch?v=M1DGI-QoQAk)

## Related Concepts

- [[duckdb-iceberg-extension]] — DuckDB's native Iceberg support, complementary to Dremio integration
- [[data-lakehouse]] — The shared architectural foundation
- [[dremio]] — The query engine being integrated with