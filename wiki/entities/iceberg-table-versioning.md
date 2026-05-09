---
type: entity
title: Apache Iceberg Table Versioning
created: 2026-05-07
updated: 2026-05-07
tags: [versioning, data-lakehouse, apache-iceberg, table-format]
related: [nessie-catalog-versioning, lakefs-file-versioning, data-lakehouse-versioning-strategies, write-audit-publish-pattern, data-lakehouse]
sources: ["data-lakehouse-versioning-nessie-vs-iceberg-vs-lakefs.md"]
---
# Apache Iceberg Table Versioning

Apache Iceberg provides versioning at the **table metadata level** through a snapshot log. Each snapshot captures a particular state of the table, enabling time travel queries, reader isolation, and branching/tagging per table.

## Key Features

- **Snapshot Log:** Historical record of all changes applied to a table.
- **Branches:** Independent lines of snapshot history for parallel development and experimentation.
- **Tags:** Named references to specific snapshots for compliance or historical reference.
- **Retention Policies:** Configurable rules for how long branches, tags, and snapshots are retained.
- **Write-Audit-Publish (WAP):** Pattern for validating writes on an audit branch before fast-forwarding to main.

## Use Cases

- **Historical Tags:** Retain weekly/monthly/annual snapshots for auditing.
- **Temporary Testing Branches:** Short-lived branches for safe experimentation.
- **Audit Branches:** Validate write workflows independently before integration.

## Pros and Cons

**Pros:** Catalog-agnostic, no additional service required, cloud/storage agnostic, supports complex transactions.  
**Cons:** Single-table focus (no cross-table transactions), exclusive to Iceberg format.

## Example (SparkSQL)

```sql
-- Create tags for snapshot retention
ALTER TABLE prod.db.table CREATE TAG `EOW-01` AS OF VERSION 7 RETAIN 7 DAYS;
ALTER TABLE prod.db.table CREATE TAG `EOY-2023` AS OF VERSION 365;

-- Create a temporary test branch
ALTER TABLE prod.db.table CREATE BRANCH `test-branch` RETAIN 7 DAYS WITH SNAPSHOT RETENTION 2 SNAPSHOTS;

-- Enable WAP and create audit branch
ALTER TABLE prod.db.table SET TBLPROPERTIES ('write.wap.enabled'='true');
ALTER TABLE prod.db.table CREATE BRANCH `audit-branch` AS OF VERSION 3 RETAIN 7 DAYS;

-- Fast forward main to audit branch after validation
CALL catalog_name.system.fast_forward('prod.db.table', 'main', 'audit-branch');
```

## Related

- [[nessie-catalog-versioning]] — Catalog-level versioning alternative
- [[lakefs-file-versioning]] — File-level versioning alternative
- [[write-audit-publish-pattern]] — WAP pattern details
- [[data-lakehouse-versioning-strategies]] — Comparative framework
- [[data-lakehouse]] — Core architecture