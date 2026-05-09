---
type: concept
title: Dremio UDF GIS Plugin
created: 2026-01-15
updated: 2026-01-15
tags: [dremio, gis, udf, geospatial, plugin, ogc]
related: [dremio, dremio-udf-gis, dremio-geospatial-limitations, dati-geo-con-dremio-e-nessie, iceberg-geospatial-support]
sources: ["DREMIO SPATIAL.md"]
---
# Dremio UDF GIS Plugin

The Dremio UDF GIS plugin is a community-maintained extension that adds geospatial query capabilities to Dremio by implementing OGC-standard SQL functions compatible with PostGIS conventions. It serves as a mitigation strategy for Dremio's limited native support for geospatial data types and operations.

## Key Characteristics

- **OGC SQL Implementation**: Adheres to the Open Geospatial Consortium standard for geospatial SQL functions, ensuring interoperability with PostGIS conventions.
- **Format Support**: Accepts WKT and WKB (HEX or BINARY) as input; outputs WKT, WKB, or GeoJSON.
- **Installation**: Simple file-drop deployment — place a shaded JAR in the Dremio 3rd-party libraries directory and restart.
- **Dependency**: Built on Proj4J (coordinate transformations) and JTS (geometry operations).

## Role in the Architecture

The plugin fills a critical gap in the Dremio + Iceberg + Nessie stack for geospatial workloads. While [[iceberg-geospatial-support]] provides native GEO types at the storage layer, Dremio's query engine does not fully support these types natively. The UDF plugin provides a workaround by implementing geospatial functions as user-defined functions, enabling spatial queries on data stored in Dremio.

## Limitations

- Community-maintained — no official support from Dremio.
- Performance characteristics relative to native geospatial engines (e.g., PostGIS, Snowflake GEO) are not documented.
- Compatibility with Iceberg tables and Arrow Flight/ODBC/JDBC interfaces is not confirmed.
- Maintenance status depends on community contributions.

## See Also

- [[dremio-geospatial-limitations]] — Detailed analysis of Dremio's geospatial constraints.
- [[dati-geo-con-dremio-e-nessie]] — Geospatial challenges in the Iceberg/Nessie/Dremio stack.
- [[dremio-udf-gis]] — Entity page for the specific GitHub project.