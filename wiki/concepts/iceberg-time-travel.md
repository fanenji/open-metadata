---
type: concept
title: Iceberg Time Travel
created: 2026-04-29
updated: 2026-04-29
tags: [iceberg, querying, versioning]
related: [iceberg-table-versioning, iceberg-rollback, iceberg-metadata-tables]
sources: ["ICEBERG.md"]
---
# Iceberg Time Travel

Time travel in Apache Iceberg allows querying a table as it existed at a specific point in time or at a specific snapshot. This is enabled by Iceberg's immutable snapshot model, where each write operation creates a new snapshot without modifying previous ones.

## Time Travel Methods

- **By timestamp**: Query the table as of a specific timestamp (e.g., `SELECT * FROM table FOR SYSTEM_TIME AS OF '2024-01-01 00:00:00'`).
- **By snapshot ID**: Query the table at a specific snapshot (e.g., `SELECT * FROM table FOR SYSTEM_VERSION AS OF 123456789`).

## Use Cases

- **Auditing**: Reproduce the state of data at a past point in time for compliance.
- **Debugging**: Investigate what data looked like before a problematic transformation.
- **Reproducibility**: Ensure consistent results across repeated queries on historical data.
- **Comparison**: Compare current data with historical snapshots to detect changes.

## Snapshot Retention

- Snapshots are retained based on configurable retention policies (age and count).
- Expired snapshots are removed by Iceberg's `expireSnapshots` action.
- Time travel is only possible to snapshots that have not been expired.

## Related Wiki Pages

- [[iceberg-table-versioning]] — Iceberg's native table-level branching and tagging.
- [[iceberg-rollback]] — Rollback mechanics and incident recovery.
- [[iceberg-metadata-tables]] — Hidden system tables for debugging and governance.