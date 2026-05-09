---
type: entity
title: Dremio UDF GIS
created: 2026-01-15
updated: 2026-01-15
tags: [dremio, gis, udf, geospatial, plugin]
related: [dremio, dremio-geospatial-limitations, dati-geo-con-dremio-e-nessie, iceberg-geospatial-support]
sources: ["DREMIO SPATIAL.md"]
---
# Dremio UDF GIS

The `sheinbergon/dremio-udf-gis` plugin is a community-maintained user-defined function package that extends Dremio with geospatial capabilities. It implements a widespread OGC SQL standard adhering to PostGIS conventions, enabling spatial queries on data stored in Dremio.

## Installation

1. Download the shaded JAR artifact for the desired Dremio CE version from Maven Central or GitHub.
2. Place the JAR file in `$DREMIO_HOME/jars/3rdparty`.
3. Restart the Dremio server(s).

## Supported Formats

- **Input**: WKT (Well-Known Text), WKB (Well-Known Binary, HEX or BINARY)
- **Output**: WKT, WKB, GeoJSON

## Dependencies

- Built on up-to-date [[Proj4J]] for coordinate transformations and [[JTS (Java Topology Suite)]] for geometry operations.

## Compatibility

- Released for each Dremio Community Edition version.
- Community-maintained — not an official Dremio product. Support and compatibility guarantees may vary.

## Usage

The plugin provides OGC-standard SQL functions that can be used directly in Dremio SQL queries. Refer to the [GitHub repository](https://github.com/sheinbergon/dremio-udf-gis) for the full list of supported functions.

## See Also

- [[dremio-geospatial-limitations]] — Dremio's limited native GEO support and the UDF dependency.
- [[dati-geo-con-dremio-e-nessie]] — Geospatial challenges with the Iceberg, Nessie, and Dremio stack.
- [[iceberg-geospatial-support]] — Apache Iceberg's native geospatial types.