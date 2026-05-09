---
type: entity
title: dremio-simple-query
created: 2026-04-08
updated: 2026-04-08
tags: [dremio, python, library, arrow-flight]
related: [dremio, duckdb, apache-arrow-flight, alex-merced, dremio-duckdb-integration]
sources: ["Using DuckDB with Your Dremio Data Lakehouse.md"]
---
# dremio-simple-query

`dremio-simple-query` is a Python library created by [[Alex Merced]] that simplifies querying [[dremio]] via [[apache-arrow-flight]] and converting results to [[duckdb]] relations or Arrow tables. It is available on PyPI.

The library provides a `DremioConnection` class with two primary methods:
- `toDuckDB()`: Executes a query against Dremio and returns a DuckDB relation directly.
- `toArrow()`: Executes a query and returns an Arrow `FlightStreamReader` for manual conversion.

This library is part of the [[dremio-duckdb-integration-pattern]] described in the article "Using DuckDB with Your Dremio Data Lakehouse."

**Note**: The maintenance status and compatibility with current Dremio versions should be verified before production use.