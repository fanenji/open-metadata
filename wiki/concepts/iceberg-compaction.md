---
type: concept
title: Iceberg Compaction
created: 2026-04-29
updated: 2026-04-29
tags: [iceberg, performance, maintenance]
related: [iceberg-table-versioning, iceberg-metadata-tables, data-lakehouse]
sources: ["ICEBERG.md"]
---
# Iceberg Compaction

Compaction in Apache Iceberg is the process of merging small data files into larger ones to improve query performance and reduce metadata overhead. Iceberg's snapshot isolation allows compaction to run as a background operation without affecting concurrent reads or writes.

## Why Compact

- **Reduce file count**: Too many small files degrade metadata operations and query planning.
- **Improve scan efficiency**: Larger files enable better compression and sequential I/O.
- **Lower metadata overhead**: Fewer manifest entries reduce planning time.

## Compaction Strategies

- **File size target**: Compact files to a target size (e.g., 128 MB or 256 MB) based on workload.
- **Rewrite data files**: Use Iceberg's `rewriteDataFiles` action to merge small files.
- **Rewrite manifests**: Use `rewriteManifests` to consolidate manifest files.
- **Scheduling**: Run compaction periodically (e.g., daily or after large batch writes) or trigger it based on file count thresholds.

## Considerations

- **Compaction is not free**: It consumes compute resources and creates new snapshots.
- **Snapshot retention**: Old snapshots must be expired to reclaim storage from compacted files.
- **Concurrent operations**: Compaction can run concurrently with writes, but care is needed to avoid conflicts with concurrent schema changes.

## Related Wiki Pages

- [[iceberg-table-versioning]] — Iceberg's native table-level branching and tagging.
- [[iceberg-metadata-tables]] — Hidden system tables for debugging and governance.
- [[data-lakehouse]] — Hybrid architecture combining data lake and warehouse features.