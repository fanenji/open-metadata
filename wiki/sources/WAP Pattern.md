---
type: source
title: WAP Pattern
created: 2026-05-07
updated: 2026-05-07
tags: [data-quality, design-pattern, iceberg, data-engineering]
related: [write-audit-publish-pattern, iceberg-table-versioning, iceberg-cherry-pick-snapshot, shift-left-data-quality, data-quality-certification-vs-usability-certification]
sources: ["WAP Pattern.md"]
---
# WAP Pattern

A concise definition of the Write-Audit-Publish (WAP) design pattern for data quality and integrity, with specific implementation guidance using Apache Iceberg branching and cherry-pick snapshots.

## Summary

The WAP pattern operates in three stages:
1. **Write** — data is written to a non-production environment (e.g., an Iceberg branch)
2. **Audit** — data is validated and quality issues are identified and rectified
3. **Publish** — validated data is promoted to production

The document highlights Iceberg's branching mechanism as an implementation vehicle: a new branch is created from the existing table, changes are staged to that branch, validations are performed, and if checks pass, the data is published to the main branch via the `cherry-pick` snapshot procedure. If checks fail, the branch can simply be dropped.

## Key References

- [Write-Audit-Publish in data pipelines | Dagster Blog](https://dagster.io/blog/python-write-audit-publish)
- [Streamlining Data Quality in Apache Iceberg with write-audit-publish & branching | Dremio Blog](https://www.dremio.com/blog/streamlining-data-quality-in-apache-iceberg-with-write-audit-publish-branching/)
- [Iceberg Cherry-Pick Snapshot Procedure](https://iceberg.apache.org/docs/latest/spark-procedures/cherrypick_snapshot)

## Connections

- [[write-audit-publish-pattern]] — The existing wiki page on this pattern, now enriched with Iceberg implementation details
- [[iceberg-table-versioning]] — Iceberg's native branching and tagging capabilities enable WAP
- [[iceberg-cherry-pick-snapshot]] — The specific Iceberg procedure that makes atomic publishing possible
- [[shift-left-data-quality]] — WAP is a practical implementation of moving quality checks earlier in the pipeline
- [[data-quality-certification-vs-usability-certification]] — WAP provides a mechanism for certification before production exposure