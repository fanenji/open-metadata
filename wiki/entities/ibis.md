---
type: entity
title: Ibis
created: 2026-04-29
updated: 2026-04-29
tags: [database, dataframe, python, api]
related: [duckdb, duckdb-spatial-architecture]
sources: ["DuckDB Spatial Supercharged Geospatial SQL.md"]
---
# Ibis

Ibis is a universal interface to databases and dataframes, developed by Voltron Data. It provides a dataframe-like API that can target multiple backends, including [[DuckDB]]. Community contributor Nic Clementi has added support for [[DuckDB Spatial]] expressions in Ibis, exposing DuckDB Spatial's GDAL integration through a dataframe-style interface.

## Related

- [[duckdb]] — One of the supported backends
- [[duckdb-spatial-architecture]] — Spatial extension exposed through Ibis