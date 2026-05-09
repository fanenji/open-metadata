---
type: concept
title: Friendly SQL
created: 2026-04-29
updated: 2026-04-29
tags: [duckdb, sql, user-experience]
related: [duckdb]
sources: ["DuckDB Spatial Supercharged Geospatial SQL.md"]
---
# Friendly SQL

Friendly SQL refers to [[DuckDB]]'s extended SQL dialect that provides syntax conveniences beyond standard SQL, making it more approachable for data scientists and analysts. DuckDB's SQL dialect is a superset of the PostgreSQL dialect.

## Features

- **GROUP BY ALL:** Automatically groups by all non-aggregated columns.
- **Dynamic column selections:** Select columns using patterns or expressions.
- **Nested types and lambda functions:** Support for working with nested data structures and inline functions.
- **List comprehensions:** Python-inspired syntax for list operations.
- **Unified function call syntax:** Functions can be called using method-style syntax (e.g., `column.function()` instead of `function(column)`).
- **FIRST syntax:** Ability to swap FROM and SELECT clauses.

## Related

- [[duckdb]] — The database engine implementing friendly SQL