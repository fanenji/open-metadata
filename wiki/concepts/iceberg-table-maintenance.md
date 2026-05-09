---
type: concept
title: Iceberg Table Maintenance
created: 2026-05-07
updated: 2026-05-07
tags: [iceberg, maintenance, performance, governance]
related: [data-lake-control-plane, iceberg-retention-policies, iceberg-snapshot-tags, iceberg-table-versioning, write-audit-publish-pattern, data-lakehouse]
sources: ["Why Every Data Lake Needs a Control Plane Lessons from Apache Iceberg.md"]
---
# Iceberg Table Maintenance

The set of operational procedures required to keep Apache Iceberg tables performant, cost-efficient, and compliant. Without regular maintenance, Iceberg tables suffer from metadata bloat, storage creep, and degraded query planning.

## Maintenance Procedures

### Snapshot Expiration
Deletes old snapshots and their referenced data files that exceed retention policies. Reclaims storage and shrinks metadata. Should be run daily.

### Compaction (Rewrite Data Files)
Consolidates small files into larger ones and merges delete files into base data files. Critical for Merge-on-Read (MOR) tables to physically apply deletes and reduce query overhead. Must run before snapshot expiration for GDPR compliance.

### Manifest Rewriting
Optimizes manifest lists and manifest files by consolidating metadata, reducing planning time and lowering query latency.

### Orphan File Removal
Deletes stray files left behind by failed jobs or mislocated writers. Prevents "dark storage" costs.

### Puffin File Maintenance
Refreshes auxiliary files storing column-level statistics and advanced indexes (min/max values, bloom filters, histograms). Puffin files can drift out of sync as data evolves.

## Recommended Default Policy

| Property | Value | Description |
|----------|-------|-------------|
| `max-snapshot-age-ms` | 14 days | Maximum age of snapshots to retain |
| `min-snapshots-to-keep` | 10 | Minimum number of snapshots to always keep |
| `max-ref-age-ms` | 90 days | Maximum age for branch/tag references |

## Coordination Requirements

For GDPR hard deletes, the correct sequence is:
1. Run compaction to physically apply deletes
2. Expire older snapshots
3. Remove orphan files

A [[data-lake-control-plane]] orchestrates this sequence across all tables and engines.