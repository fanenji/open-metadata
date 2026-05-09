---
type: concept
title: Iceberg Snapshot Tags
created: 2026-05-07
updated: 2026-05-07
tags: [iceberg, versioning, governance, compliance]
related: [iceberg-table-versioning, iceberg-table-maintenance, iceberg-retention-policies, data-lake-control-plane]
sources: ["Why Every Data Lake Needs a Control Plane Lessons from Apache Iceberg.md"]
---
# Iceberg Snapshot Tags

Named snapshot references in Apache Iceberg that can be retained with optional retention periods. Tags are a powerful but underused feature for disaster recovery, compliance audits, and release safety.

## Use Cases

- **Disaster Recovery**: Tag a snapshot before a risky migration. The tag protects the snapshot from expiration for the specified duration.
- **GDPR Compliance Audits**: Tag the table state before running GDPR purge jobs, providing a checkpoint to validate the effect.
- **Release Safety**: Engineering teams can tag the snapshot before a pipeline upgrade and roll back instantly if something breaks.

## Creating Tags

**Spark SQL**:
```sql
ALTER TABLE prod.events CREATE TAG dr_sept_2025 RETAIN 90 DAYS;
ALTER TABLE prod.events CREATE TAG pre_schema_update RETAIN 7 DAYS;
```

**Trino**:
```sql
ALTER TABLE prod.events
  ADD SNAPSHOT REFERENCE 'dr_sept_2025'
  AS OF SNAPSHOT 1234567890
  RETAIN 90 DAYS;
```

## Governance Risk

Tags have a default retention of "keep forever." Without a [[data-lake-control-plane]], tags can become "immortal" references that block snapshot expiration and prevent storage reclamation. A control plane enforces tag policies, tracks their lifecycle, and reports which tags are consuming storage.

## Expiration Behavior

When `expire_snapshots` runs, Iceberg skips any snapshot referenced by a tag until its retention period expires. This allows aggressive storage reclamation while preserving defined rollback points.