---
type: source
title: "Source: DuckDB PostGIS e GeoParquet.md"
created: 2026-05-07
updated: 2026-05-07
sources: ["DuckDB PostGIS e GeoParquet.md"]
tags: []
related: []
---

# Source: DuckDB PostGIS e GeoParquet.md

## Key Entities

- **DuckDB** — Open-source analytical query engine. Central role: the tool used to query PostGIS and export to GeoParquet. Likely already exists in wiki.
- **PostGIS** — Spatial extension for PostgreSQL. Central role: the source database being queried. Likely already exists in wiki.
- **GeoParquet** — Open format for storing geospatial data in Parquet files. Central role: the target output format. Likely already exists in wiki.
- **PostgreSQL** — Relational database system. Peripheral role: underlying database for PostGIS. Likely already exists in wiki.

## Key Concepts

- **postgres_scanner** — DuckDB extension/connector for reading PostgreSQL tables. Why it matters: enables direct querying of PostGIS without data movement. Likely does not exist as a dedicated wiki page.
- **DuckDB spatial extension** — DuckDB extension providing limited spatial functions. Why it matters: defines the boundary of what spatial operations can be performed in DuckDB vs. PostGIS. Likely does not exist as a dedicated wiki page.
- **GeoParquet export via COPY** — DuckDB's `COPY ... TO` syntax for writing GeoParquet files. Why it matters: provides a direct pipeline from PostGIS to GeoParquet. Likely does not exist as a dedicated wiki page.

## Main Arguments & Findings

- **Core claim**: DuckDB can query PostGIS tables and export results to GeoParquet, but with important limitations.
- **Evidence**: Step-by-step SQL workflow provided (install postgres_scanner, attach database, query, COPY to GeoParquet).
- **Strength**: Moderate — based on documented DuckDB features, but no actual test results or performance data.

## Connections to Existing Wiki

- **Related pages**: [[duckdb]], [[duckdb-geoparquet-limitations]], [[cloud-native-geospatial-workflow]], [[geoparquet-vs-iceberg-metadata]]
- **Strengthens**: The existing DuckDB geospatial workflow pattern by adding PostGIS as a data source.
- **Extends**: The cloud-native geospatial workflow by showing a PostGIS-to-GeoParquet pipeline, not just remote GeoParquet querying.

## Contradictions & Tensions

- **Internal tension**: The source claims DuckDB syntax is "very similar" to PostgreSQL but warns about incompatibility for advanced PostGIS functions — this creates a practical gap for users needing spatial transformations.
- **Caveat**: PostGIS spatial functions (ST_Transform, ST_Intersection) are not available in DuckDB; users must either pre-process in PostGIS or use DuckDB's limited spatial extension.

## Recommendations

- **Create new wiki page**: [[duckdb-postgres-scanner]] — Document the connector, syntax, and limitations for PostGIS integration.
- **Update existing page**: [[duckdb-geoparquet-limitations]] — Add the PostGIS-to-GeoParquet pipeline as a use case, noting the spatial function limitation.
- **Emphasize**: The practical workflow (attach → query → COPY) is the key takeaway; the spatial function gap is the critical caveat.
- **De-emphasize**: The Python/geopandas example offer (not provided
