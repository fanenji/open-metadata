---
type: source
title: DREMIO - NOTE.md
created: 2026-02-21
updated: 2026-04-29
tags: [dremio, geospatial, configuration, postgis]
related: [dremio-geospatial-limitations, dremio-system-configuration, geospatial-etl-pipeline-iceberg, dremio-mcp-server]
sources: ["DREMIO - NOTE.md"]
---
# DREMIO - NOTE.md

Internal project note documenting a critical Dremio configuration issue when importing large geospatial geometries from PostGIS. The note identifies that Dremio's default `limits.single_field_size_bytes` setting of 32,000 bytes is insufficient for complex PostGIS geometry fields and provides the `ALTER SYSTEM` command to increase it to 1,000,000 bytes. Also includes a trivial example of creating a Virtual Dataset (VDS) from a sample JSON file.

## Key Content

- **Problem:** Dremio truncates or fails on fields larger than 32,000 bytes (default limit).
- **Solution:** `ALTER SYSTEM SET limits.single_field_size_bytes = 1000000;`
- **Context:** Importing `wkb_geometry` from PostGIS table `ctemi_corine`.
- **Reference:** [Dremio Community discussion](https://community.dremio.com/t/how-to-handle-dremio-limit-32000-bytes-of-a-field/6315)

## Relevance

This is an operational workaround for one of Dremio's geospatial limitations documented in [[dremio-geospatial-limitations]]. It provides an alternative to the more complex GDAL → GeoParquet → Spark → Iceberg pipeline described in [[geospatial-etl-pipeline-iceberg]].