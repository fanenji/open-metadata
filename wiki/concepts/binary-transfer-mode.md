---
type: concept
title: Binary Transfer Mode
created: 2026-04-04
updated: 2026-04-04
tags: [postgresql, protocol, performance, duckdb]
related: [duckdb-postgres-scanner, duckdb-postgres-scanner-implementation]
sources: ["Querying Postgres Tables Directly from DuckDB.md"]
---

# Binary Transfer Mode

Binary Transfer Mode is a feature of the PostgreSQL client-server protocol that transfers data in native binary format rather than the default text format. This avoids expensive to-string and from-string conversions, significantly improving data transfer performance for analytical workloads.

## Usage in DuckDB Postgres Scanner

The DuckDB Postgres Scanner uses binary transfer mode to read PostgreSQL tables. Internally, it issues a query like:

```sql
COPY (SELECT * FROM lineitem) TO STDOUT (FORMAT binary);
```

This allows DuckDB to efficiently transform and use the data directly, with minimal conversion overhead. For example, reading an `int32` from the protocol message only requires a byte order swap (`ntohl`).

## Benefits

- Avoids string serialization/deserialization overhead.
- Data is transferred in a format close to PostgreSQL's on-disk representation.
- Enables efficient analytical queries on live transactional data.

## Limitations

- Rarely used in standard PostgreSQL clients, so may have less tooling support.
- Requires the scanner to handle binary format parsing correctly.