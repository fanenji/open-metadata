---
type: concept
title: DremioFrame Iceberg Management
created: 2026-04-29
updated: 2026-04-29
tags: [dremio, iceberg, table-management, time-travel, schema-evolution, python]
related: [dremioframe, iceberg-table-versioning, data-lakehouse, dremioframe-orchestration]
sources: ["DremioFrame - Dremio Dataframe Library.md"]
---
# DremioFrame Iceberg Management

DremioFrame Iceberg Management provides specialized capabilities for managing Apache Iceberg tables within the [[dremioframe|DremioFrame]] library. It covers the full lifecycle of Iceberg table management including time travel, schema evolution, and incremental processing.

## Key Features

- **Iceberg Tables**: Create, read, update, and delete Iceberg tables
- **Time Travel**: Query table snapshots at specific points in time (`.at_snapshot("snapshot_id")`)
- **Schema Evolution**: Manage schema changes over time
- **Incremental Processing**: Process only new or changed data
- **Iceberg Lakehouse Management**: Comprehensive management of Iceberg-based lakehouses
- **Iceberg Tasks**: Specialized orchestration tasks for Iceberg operations (see [[dremioframe-orchestration]])

## Related

- [[dremioframe]] — The parent library
- [[iceberg-table-versioning]] — Iceberg's native table-level branching and tagging
- [[data-lakehouse]] — The lakehouse architecture DremioFrame operates within
- [[dremioframe-orchestration]] — Orchestration integration for Iceberg tasks