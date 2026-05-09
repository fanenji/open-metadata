---
type: concept
title: Iceberg Retention Policies
created: 2026-05-07
updated: 2026-05-07
tags: [iceberg, governance, configuration, best-practices]
related: [iceberg-table-maintenance, iceberg-snapshot-tags, data-lake-control-plane, iceberg-table-versioning]
sources: ["Why Every Data Lake Needs a Control Plane Lessons from Apache Iceberg.md"]
---
# Iceberg Retention Policies

Table-level configuration properties in Apache Iceberg that control how long snapshots, branches, and tags are retained. These properties act as "seatbelts" to prevent uncontrolled metadata and storage growth.

## Key Properties

| Property | Default | Recommended | Description |
|----------|---------|-------------|-------------|
| `history.expire.max-snapshot-age-ms` | 5 days | 14 days | Maximum age of snapshots to retain |
| `history.expire.min-snapshots-to-keep` | 1 | 10 | Minimum number of snapshots to always keep |
| `history.expire.max-ref-age-ms` | Forever | 90 days | Maximum age for branch/tag references |

## Setting Policies

**Spark SQL**:
```sql
ALTER TABLE prod.events SET TBLPROPERTIES (
  'history.expire.max-snapshot-age-ms'='1209600000',   -- 14 days
  'history.expire.min-snapshots-to-keep'='10',
  'history.expire.max-ref-age-ms'='7776000000'         -- 90 days
);
```

## Governance Challenge

Without a [[data-lake-control-plane]], these defaults diverge across teams and engines. One team sets retention to 7 days, another leaves it at "forever." Spark jobs expire snapshots, but Athena's tables keep old versions. A control plane enforces a single policy across all tables while allowing per-table customizations.