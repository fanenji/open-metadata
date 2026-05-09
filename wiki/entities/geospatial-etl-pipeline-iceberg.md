---
type: entity
title: Geospatial ETL Pipeline for Iceberg
created: 2026-05-07
updated: 2026-05-07
tags: [geospatial, etl, iceberg, pipeline, gis]
related: [iceberg-geospatial-support, dremio-geospatial-limitations, geoparquet-vs-iceberg-metadata, data-ingestion-architectural-patterns, data-lakehouse]
sources: ["Dati Geo con Dremio e Nessie.md"]
---
# Geospatial ETL Pipeline for Iceberg

Ingesting geospatial data into an Iceberg-based data lakehouse requires a multi-step pipeline because common ETL tools (GDAL/OGR) are not natively Iceberg-aware.

## Typical Pipeline

1. **Extract:** Source spatial data (e.g., from PostGIS, Shapefiles, GeoJSON) using GDAL/OGR.
2. **Intermediate Format:** Convert to GeoParquet, which preserves spatial metadata (CRS, bounding box per row group).
3. **Spark Transformation:** Use Apache Spark (optionally with Sedona) to read the GeoParquet files and write them into an Iceberg table. This step registers the files, computes necessary statistics, and applies spatial partitioning/ordering.
4. **Query:** The Iceberg table is then queryable via Dremio (with UDFs for spatial functions) or other engines.

## Challenges

- **Complexity and Latency:** The Spark intermediary step adds complexity, latency, and potential failure points.
- **Metadata Coordination:** Ensuring consistency between GeoParquet's embedded metadata and Iceberg's manifest-level statistics requires careful design.
- **Tooling Gaps:** GDAL/OGR are not Iceberg-aware, limiting direct write capabilities.

## Related Pages

- [[geoparquet-vs-iceberg-metadata]] — Analysis of metadata overlap and coordination strategies.
- [[iceberg-geospatial-support]] — Iceberg's native geospatial capabilities.
- [[dremio-geospatial-limitations]] — Dremio's challenges with spatial data.
- [[data-ingestion-architectural-patterns]] — Broader ingestion pattern framework.
