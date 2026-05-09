---
type: concept
title: DuckDB GeoParquet Limitations
created: 2026-04-04
updated: 2026-05-07
tags:
  - duckdb
  - geoparquet
  - limitations
  - geospatial
  - spatial
  - srs
related:
  - duckdb
  - cloud-native-geospatial-workflow
  - geoparquet-vs-iceberg-metadata
  - duckdb-geoparquet-workflow
  - duckdb-spatial-extension-usage
sources:
  - duckdb geoparquet tutorials.md
  - duckdb-geoparquet-tutorials.md
---
# DuckDB GeoParquet Limitations

Known limitations when using [[DuckDB]] with GeoParquet data, documented from practical experience, along with documented workarounds. These limitations are noted in the [[cloud-native-geospatial-workflow]] tutorial.

## Limitations

### No Native GeoParquet Output
DuckDB cannot natively write valid GeoParquet files. When exporting Parquet with geometry columns, the geometry is written as WKB (Well‑Known Binary) rather than the GeoParquet specification’s structured geometry encoding. This is a notable gap compared to engines like Spark that support native GeoParquet writing.

**Workaround**: Use the external `gpq` tool (by Planet Labs) to convert WKB Parquet to valid GeoParquet:
```bash
gpq convert input.parquet output-geo.parquet
```

### Missing Spatial Reference System (SRS)
When DuckDB writes geospatial formats via GDAL (e.g., FlatGeobuf), the output does not consistently set the spatial reference system. Exported files may lack coordinate system metadata.

**Workaround**: Use `ogr2ogr` to assign the correct projection:
```bash
ogr2ogr -a_srs EPSG:4326 output.fgb input.fgb
```

### Inaccurate Progress Reporting
DuckDB’s progress updates during remote file operations (e.g., S3 streaming) are not accurate, making it difficult to estimate completion time for large downloads.

### Performance Dependency
Querying large remote files requires a fast network connection. Large regions (hundreds of MB to GB) may be impractical on slower connections without first persisting data locally.

## Impact
These limitations mean that [[DuckDB]] is best suited for ad‑hoc analysis and intermediate processing, with final production‑ready output requiring post‑processing with external tools (`gpq`, GDAL/`ogr2ogr`).

## Future Improvements
The documentation notes that native GeoParquet output and consistent SRS handling are hoped‑for improvements in future DuckDB versions.