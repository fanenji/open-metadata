---
type: entity
title: Iceberg Cherry-Pick Snapshot
created: 2026-05-07
updated: 2026-05-07
tags: [iceberg, data-quality, table-versioning]
related: [write-audit-publish-pattern, iceberg-table-versioning, WAP Pattern]
sources: ["WAP Pattern.md"]
---
# Iceberg Cherry-Pick Snapshot

An Apache Iceberg procedure that creates a new snapshot from an existing snapshot without altering or removing the original. This is the key mechanism that enables the [[write-audit-publish-pattern|WAP pattern]] on Iceberg tables: after staging changes on a branch and validating them, the cherry-pick procedure atomically publishes the validated snapshot to the main branch.

## Usage

The procedure is invoked via Spark SQL:
```sql
CALL catalog.system.cherrypick_snapshot('table_name', 'snapshot_id')
```

## Role in WAP

In the [[write-audit-publish-pattern|WAP pattern]]:
1. A new branch is created from the main Iceberg table
2. ETL changes are written to the branch
3. Data quality validations are performed on the branch
4. If validations pass, `cherrypick_snapshot` publishes the branch's snapshot to the main branch
5. If validations fail, the branch is dropped with no impact on the main table

## Related

- [[iceberg-table-versioning]] — Iceberg's broader branching and tagging capabilities
- [[write-audit-publish-pattern]] — The design pattern that uses cherry-pick as its publish mechanism
- [[WAP Pattern]] — The source document describing the pattern