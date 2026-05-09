---
type: concept
title: Iceberg Planning Internals
created: 2026-04-29
updated: 2026-04-29
tags: [iceberg, query-planning, performance]
related: [iceberg-metadata-tables, iceberg-compaction, iceberg-table-versioning]
sources: ["ICEBERG.md"]
---
# Iceberg Planning Internals

Iceberg's query planning is the process by which the engine determines which files to scan for a given query. Efficient planning is critical for performance, especially on large tables with many files.

## How Planning Works

1. **Snapshot resolution**: The planner identifies the target snapshot (current or time-travel).
2. **Manifest list scan**: The planner reads the manifest list to identify relevant manifest files.
3. **Metadata filtering**: Using partition statistics and column-level min/max values stored in manifests, the planner prunes files that cannot contain matching data.
4. **File skipping**: Files that pass metadata filtering are included in the scan plan.

## Key Optimizations

- **Partition pruning**: Queries with partition filters skip entire partitions.
- **Column statistics**: Min/max values in manifests enable skipping files based on filter predicates.
- **Manifest caching**: Frequently accessed manifests can be cached to reduce planning overhead.

## Factors Affecting Planning Performance

- **Number of files**: More files increase manifest size and planning time.
- **Partition granularity**: Fine-grained partitions improve pruning but increase metadata overhead.
- **Manifest size**: Large manifests slow down scanning; compaction helps reduce manifest count.

## Related Wiki Pages

- [[iceberg-metadata-tables]] — Hidden system tables for debugging and governance.
- [[iceberg-compaction]] — Compaction strategies and file size tuning.
- [[iceberg-table-versioning]] — Iceberg's native table-level branching and tagging.