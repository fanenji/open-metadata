---
type: concept
title: Stored Procedure Lineage
created: 2026-05-14
updated: 2026-05-14
tags: [postgresql, lineage, stored-procedures, configuration]
related: [postgresql-connector, pg-stat-statements, data-lineage]
sources: ["PostgreSQL Connector  OpenMetadata Database Integration.md"]
---
# Stored Procedure Lineage

When executing stored procedures in PostgreSQL, lineage extraction relies on capturing the SQL queries executed within the procedure. However, by default, PostgreSQL does not track the internal queries of a stored procedure in [[pg-stat-statements|pg_stat_statements]].

## Enabling Query Tracking for Lineage

To ensure OpenMetadata captures lineage from stored procedures via the [[postgresql-connector]], two configuration changes are required in `postgresql.conf`:

1. **Enable Logging for All Statements**: Set `log_statement = 'all'` to log all executed SQL statements, including those inside stored procedures.
2. **Configure `pg_stat_statements` to Track Nested Queries**: Set `pg_stat_statements.track = 'all'` to ensure statements executed within procedures are recorded, not just top-level procedure calls.

Without both settings, lineage from stored procedures will be incomplete or entirely missing.