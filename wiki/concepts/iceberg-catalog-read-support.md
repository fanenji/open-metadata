---
type: concept
title: Iceberg Catalog Read Support
created: 2025-02-10
updated: 2025-02-10
tags: [iceberg, catalog, duckdb, integration]
related: [iceberg, duckdb, duckdb-iceberg-limitations, pyiceberg]
sources: ["Quando duckdb e iceberg sono sufficienti?.md"]
---
# Iceberg Catalog Read Support

The ability of a query engine to read and interact with an [[iceberg]] Catalog — the metadata layer that tracks table versions, schemas, partitions, and snapshots.

## DuckDB's Current Limitation

[[duckdb]] cannot read Iceberg Catalogs natively. This means:

- DuckDB cannot discover Iceberg tables through a catalog interface.
- It cannot resolve table names to their current snapshot.
- It cannot leverage catalog-level features like branching, tagging, or time travel.
- Users must manually specify the path to Iceberg metadata files.

## Why It Matters

Without catalog read support, DuckDB cannot integrate seamlessly into an Iceberg-based data lakehouse. Users must use workarounds ([[PyIceberg]]) to handle catalog operations, adding complexity and an additional dependency.

## Workarounds

- Use [[PyIceberg]] to read the catalog and pass data to DuckDB via [[PyArrow]].
- Use [[PyArrow]] datasets to read Iceberg tables directly.
- Store table metadata in a separate system (e.g., a simple file registry) that DuckDB can read.

## Future Outlook

The DuckDB community has an open issue for catalog support, but it is not a high priority. Each vendor is building their own catalog implementation despite the Iceberg REST Catalog specification, making it harder for DuckDB to support all variants.

## Related Concepts

- [[duckdb-iceberg-limitations]] — Broader context of DuckDB's Iceberg limitations.
- [[duckdb-iceberg-sufficiency]] — The architecture where this limitation is a key constraint.