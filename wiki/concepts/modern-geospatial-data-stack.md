---
type: concept
title: Modern Geospatial Data Stack
created: 2026-05-07
updated: 2026-05-07
tags: [modern-data-stack, geospatial, architecture, postgis, duckdb, dbt]
related: [postgis-as-central-hub, postgis, duckdb, dbt, h3-geospatial-indexing, cloud-native-geospatial-workflow, data-lakehouse]
sources: ["spatial-sql-the-modern-data-stack-and-postgis.md"]
---
# Modern Geospatial Data Stack

The adaptation of the Modern Data Stack (MDS) concept to geospatial data workflows. The MDS promises a simpler approach to data infrastructure: one tool for one specific thing, all working nicely together via SQL.

## Core Principles

1. **SQL as lingua franca**: All tools (dbt, DuckDB, BI) converge on SQL, making spatial SQL the natural language for geospatial analytics
2. **Specialized tools**: Each tool handles what it does best (DuckDB for bulk CSV, PostGIS for spatial analysis, dbt for orchestration)
3. **Interconnectivity**: Tools connect through SQL interfaces and foreign data wrappers

## Architecture Components

From [[Matt Forrest]]'s talk:

| Layer | Tools | Role |
|-------|-------|------|
| Data Sources | NOAA FTP, FEMA Esri JSON, Copernicus STAC, AWS Open Data | Raw geospatial data |
| Ingestion | Airbyte, GDAL/OGR | Load data into storage |
| Storage | PostGIS (central), DuckDB (bulk processing) | Store and analyze data |
| Transformation | dbt, H3 | Automate pipelines, spatial indexing |
| Output | QGIS, GeoPandas, Leafmap | Visualization and analysis |

## Comparison with Lakehouse Architecture

The modern geospatial data stack (PostGIS-centric) differs from lakehouse approaches (Iceberg + Dremio/Spark):
- **Storage**: PostGIS (relational database) vs. object storage (S3/MinIO)
- **Spatial engine**: PostGIS (mature, feature-rich) vs. Dremio/Spark (limited native GEO support)
- **Orchestration**: dbt (SQL-native) vs. Spark jobs
- **Scale**: PostGIS for moderate scale; lakehouse for massive scale

## Related

- [[postgis-as-central-hub]] — The thesis that PostGIS is the interconnectivity layer
- [[cloud-native-geospatial-workflow]] — Complementary DuckDB + GeoParquet pattern
- [[data-lakehouse]] — Alternative architecture for large-scale data