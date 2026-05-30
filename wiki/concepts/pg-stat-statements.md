---
type: concept
title: pg_stat_statements
created: 2026-05-14
updated: 2026-05-15
tags:
  - postgresql
  - lineage
  - usage
  - statistics
  - ingestion
  - limitations
  - extension
  - query-statistics
related:
  - postgresql-connector
  - data-lineage
  - ingestion-scheduling
  - soft-deletion
  - stored-procedure-lineage
  - oracle-schema-select-limitation
  - postgresql-connector-troubleshooting
sources:
  - "PostgreSQL Connector  OpenMetadata Database Integration.md"
  - "postgresql-connector-troubleshooting---openmetadat-20260514.md"
---

# pg_stat_statements

`pg_stat_statements` is a PostgreSQL extension that collects execution statistics of SQL statements executed by a server. OpenMetadata relies on this extension for usage and lineage workflows when ingesting metadata from PostgreSQL databases via the [[postgresql-connector]].

## Critical Limitation: Not a Query Log

`pg_stat_statements` is **not a query log** – it is a fixed-size, in-memory statistics collector. This has important consequences for lineage and usage completeness:

### Entry Eviction

Entries are stored in a hash table controlled by `pg_stat_statements.max` (default: **5000**). When the table is full, the least-executed entries are silently evicted. Queries can disappear before OpenMetadata reads them, causing gaps in lineage and usage data.

### Query Normalization

Queries are deduplicated by shape — literal values are replaced with placeholders (e.g., `SELECT * FROM users WHERE id = $1`). Individual executions are not stored; only aggregated statistics are available.

### No Timestamps

There is no time data associated with entries. Only cumulative `calls` count and `total_exec_time` since the last reset are tracked. The **query log duration** setting in OpenMetadata has no impact — only the **query limit** matters.

### Non-Persistence and Resets

The extension is non-persistent: entries are held in memory only. A server restart or `pg_stat_statements_reset()` wipes all entries. Any queries not yet ingested are permanently lost.

## Common Errors

### Relation Does Not Exist

**Error**: `(psycopg2.errors.UndefinedTable) relation "pg_stat_statements" does not exist`

**Cause**: The extension is not enabled.

**Solution**: Run `CREATE EXTENSION IF NOT EXISTS pg_stat_statements;` and set `shared_preload_libraries = 'pg_stat_statements'` in `postgresql.conf`.

### Incomplete Lineage/Usage Data

**Cause**: Eviction of entries from the fixed-size hash table, or data loss due to resets.

**Solution**: Increase `pg_stat_statements.max`, run ingestion more frequently, or use a custom query source (see below).

## Mitigation Strategies

To maximize lineage and usage completeness:

1. **Increase `pg_stat_statements.max`** to at least **10000** (or higher) in `postgresql.conf` to reduce entry eviction.
2. **Set `pg_stat_statements.track = 'all'`** to capture queries inside functions and procedures. For [[stored-procedure-lineage]] to work, this setting along with `log_statement = 'all'` is required.
3. **Schedule frequent ingestion runs** (e.g., every 1–2 hours) to capture queries before they are evicted. See [[ingestion-scheduling]].
4. **Avoid calling `pg_stat_statements_reset()`** before ingestion. If periodic resets are needed, schedule them after ingestion completes.
5. **Use a custom query source** — periodically snapshot `pg_stat_statements` into a persistent table and configure OpenMetadata to read from it using the `queryStatementSource` connection property. This provides a more stable, query-log-like interface.

### Custom Query Source Alternative

Organizations with restricted access to `pg_stat_statements` or needing more control over query retention can configure a custom view or table via the **Query Statement Source** connection property. The custom source must expose columns matching the expected schema: `userid` (oid), `dbid` (oid), `query` (text), and either `total_exec_time` (double precision, PostgreSQL 13+) or `total_time` (double precision, PostgreSQL < 13). By periodically copying `pg_stat_statements` content into such a persistent table, you create a more reliable source for lineage and usage.

## Interaction with Soft Deletion

A potential operational concern: if queries are evicted from `pg_stat_statements` between ingestion runs, OpenMetadata may interpret the absence of previously seen queries as deleted lineage. This interaction with [[soft-deletion]] warrants careful scheduling and monitoring.

## Comparison with Other Connectors

Similar statistics-collector limitations may exist in other database connectors. The [[oracle-connector]] has a documented [[oracle-schema-select-limitation|schema-level SELECT limitation]] that affects Profiler and Data Quality workflows. Consistent documentation of such connector-specific constraints helps operators plan ingestion strategies.