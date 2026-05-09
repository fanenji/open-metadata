---
type: concept
title: Iceberg Metadata Tables
created: 2026-04-29
updated: 2026-04-29
tags: [iceberg, metadata, governance, debugging]
related: [iceberg-table-versioning, iceberg-planning-internals, data-lakehouse]
sources: ["ICEBERG.md"]
---
# Iceberg Metadata Tables

Apache Iceberg exposes hidden system tables that provide access to the table's internal metadata. These tables are invaluable for governance, debugging, performance analysis, and data discovery.

## Key Metadata Tables

- **snapshots** — Lists all snapshots of the table, including timestamps, operation types, and manifest lists.
- **manifests** — Details about manifest files, including partition summaries and file counts.
- **files** — Information about all data files in the current snapshot, including file paths, partition values, record counts, and column statistics.
- **history** — Historical record of snapshot creation events.
- **partitions** — Partition metadata for the table.
- **refs** — References (branches and tags) pointing to specific snapshots.

## Use Cases

- **Governance**: Audit snapshot history to verify data lineage and compliance.
- **Debugging**: Identify which files were added or removed in a specific snapshot.
- **Performance Analysis**: Examine file sizes and partition statistics to optimize compaction and partitioning strategies.
- **Data Discovery**: Explore table structure and partition layout without scanning data files.

## Related Wiki Pages

- [[iceberg-table-versioning]] — Iceberg's native table-level branching and tagging.
- [[iceberg-planning-internals]] — How Iceberg plans queries using metadata.
- [[data-lakehouse]] — Hybrid architecture combining data lake and warehouse features.