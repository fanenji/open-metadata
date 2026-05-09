type: concept
title: DuckLake Snapshot Model
created: 2026-04-29
updated: 2026-04-29
tags: [ducklake, snapshots, versioning, compaction]
related: [ducklake, data-lakehouse-versioning-strategies, apache-iceberg, delta-lake]
sources: ["iceberg-built-a-maze-ducklake-just-handed-you-a-map.md"]
---
# DuckLake Snapshot Model

DuckLake's approach to snapshot management, where snapshots are stored as rows in a SQL table rather than as files on blob storage. This eliminates the compaction tax inherent in Iceberg and Delta Lake architectures.

## How It Works

- Adding a snapshot is a SQL INSERT
- Expiring a snapshot is a SQL DELETE
- No manifest list to rewrite, no new root file to generate
- Snapshots can refer to portions of a Parquet file for fine-grained history without file count explosion

## Comparison with Iceberg and Delta Lake

| Format | Snapshot Storage | Compaction Required | Scalability |
|--------|-----------------|-------------------|-------------|
| Iceberg | Root metadata file grows with history | EXPIRE_SNAPSHOTS needed | Limited by file growth |
| Delta Lake | Transaction log entries accumulate | VACUUM needed | Limited by log growth |
| DuckLake | Rows in SQL table | No compaction needed | Millions of snapshots supported |

## Significance

The DuckLake manifesto explicitly states the format supports millions of snapshots without proactive pruning because the catalog database handles lookup efficiently regardless of snapshot count. This is a fundamentally different approach from Iceberg and Delta Lake, where snapshot accumulation is a known operational burden.