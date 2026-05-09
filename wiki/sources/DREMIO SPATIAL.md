---
type: source
title: DREMIO SPATIAL
created: 2026-01-15
updated: 2026-01-15
tags: [dremio, spatial, gis, udf, geospatial]
related: [dremio, dremio-geospatial-limitations, dremio-udf-gis, dati-geo-con-dremio-e-nessie, iceberg-geospatial-support]
sources: ["DREMIO SPATIAL.md"]
---
# DREMIO SPATIAL

A curated collection of links and notes documenting the use of the `sheinbergon/dremio-udf-gis` plugin to extend Dremio with geospatial capabilities. The source confirms Dremio's limited native GEO support and provides a concrete implementation path via a community-maintained UDF plugin that implements OGC-standard SQL functions compatible with PostGIS conventions.

## Key Links

- [Dremio Geospatial SQL Functions Documentation](https://docs.dremio.com/current/reference/sql/sql-functions/GEOSPATIAL/)
- [Dremio Geo Spatial Extensions - Community Announcement](https://community.dremio.com/t/dremio-geo-spatial-extensions-announcements/10280)
- [sheinbergon/dremio-udf-gis on GitHub](https://github.com/sheinbergon/dremio-udf-gis)

## Summary

The plugin provides a widespread OGC SQL implementation adhering to PostGIS standards. It supports WKT, WKB (HEX or BINARY) input formats and WKT, WKB, and GeoJSON output formats. Installation is straightforward: download the shaded JAR artifact from Maven Central or GitHub, place it in `$DREMIO_HOME/jars/3rdparty`, and restart the Dremio server(s). The plugin is built on up-to-date Proj4J and JTS geometry libraries and is released for each Dremio Community Edition version.

## Caveats

- The plugin is community-maintained, not an official Dremio product.
- Compatibility with Iceberg tables and performance characteristics are not documented in this source.