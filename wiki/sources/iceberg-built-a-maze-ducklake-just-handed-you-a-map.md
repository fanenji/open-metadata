type: source
title: "Iceberg Built a Maze. DuckLake Just Handed You a Map."
created: 2026-04-29
updated: 2026-04-29
tags: [open-table-formats, ducklake, iceberg, delta-lake, metadata-architecture]
related: [ducklake, duckdb, apache-iceberg, delta-lake, data-lakehouse, data-lakehouse-versioning-strategies, iceberg-query-engine-comparison, ducklake-small-write-inlining, ducklake-snapshot-model]
sources: ["iceberg-built-a-maze-ducklake-just-handed-you-a-map.md"]
authors: [amin-siddique]
year: 2026
url: "https://reliable-data-engineering.netlify.app/posts/article_ducklake_open_table_format/#where-ducklake-genuinely-changes-the-game"
venue: "Reliable Data Engineering Blog"
---
# Iceberg Built a Maze. DuckLake Just Handed You a Map.

An independent editorial analysis of the DuckLake open table format, published by Amin Siddique in April 2026. The article examines the DuckDB team's new open table format that replaces the file-based metadata architecture of Iceberg and Delta Lake with a SQL database approach.

## Summary

The article argues that Iceberg and Delta Lake's file-based metadata architecture imposes a "quiet tax" on query performance, requiring 4-10+ HTTP round trips to resolve table state. DuckLake eliminates this by storing all metadata in a SQL database, requiring a single SQL query. The article covers DuckLake's architecture, setup, and three game-changing properties: snapshots without compaction tax, small write inlining, and native encryption. It provides a comparison table across Iceberg, Delta Lake, and DuckLake, and identifies four team profiles for whom DuckLake is immediately relevant.

## Key Claims

- DuckLake reduces metadata round trips from 6-10+ (Iceberg) to 1 SQL query
- Supports millions of snapshots without proactive compaction
- Small writes can be inlined into the catalog database, bypassing Parquet writes
- Multi-table ACID transactions are supported natively
- Data files are Iceberg-compatible Parquet, enabling metadata-only migrations
- Encryption is a first-class format feature with keys managed by the catalog

## Limitations Noted

- DuckDB-only engine support (v0.1)
- Catalog database becomes critical infrastructure
- No production war stories or enterprise-scale stress testing
- Ecosystem has not yet formed