type: source
title: "Geospatial Tables in the Open Lakehouse: A New Era for Iceberg & Parquet"
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, iceberg, geoparquet, parquet, lakehouse, open-format]
related: [iceberg-geospatial-support, geoparquet-vs-iceberg-metadata, iceberggo-v3-spec, geospatial-vendor-lock-in-avoidance, iceberggo-vs-delta-lake-geospatial, wherobots, jia-yu, chris-holmes, szehon-ho, vikram-gundeti, planet-labs, foursquare, databricks, havasi]
sources: ["Geospatial Tables in the Open Lakehouse A New Era for Iceberg & Parquet.md"]
---
# Geospatial Tables in the Open Lakehouse: A New Era for Iceberg & Parquet

A livestream hosted by [[Wherobots]] featuring [[Jia Yu]] (Co-Founder/CTO, Wherobots), [[Chris Holmes]] (Creator of GeoParquet, Planet Fellow at Planet Labs), [[Szehon Ho]] (Iceberg PMC Member, Software Engineer at Databricks), and [[Vikram Gundeti]] (CTO, Foursquare). The discussion covers the introduction of native geospatial data types (GEO) into Apache Iceberg (v3) and Apache Parquet, marking a paradigm shift for geospatial data management in the open lakehouse.

## Key Topics

- **GeoParquet Origin Story**: Chris Holmes describes how GeoParquet started as an OGC effort for interoperability between cloud data warehouses (BigQuery, Snowflake, Redshift) and merged with the GeoArrow community to standardize geospatial metadata in Parquet files.
- **Iceberg GEO v3 Specification**: Szehon Ho details the technical debates around CRS (Coordinate Reference System), edge interpolation, and anti-meridian bounding boxes. The spec settled on two parameters (CRS and edge interpolation) to balance simplicity with correctness.
- **Performance Optimizations**: Native bounding box statistics at the Parquet row group level (not just file level) enable finer-grained spatial predicate pushdown, improving query performance.
- **Vendor Lock-in Avoidance**: Storage-compute separation via Iceberg allows data to be stored once and queried by any engine (Snowflake, BigQuery, DuckDB, Spark), eliminating the need for data migration.
- **Industry Adoption**: Foursquare's experience migrating from custom folder structures and JSON formats to Iceberg tables, enabling flexible querying, schema evolution, and GDPR compliance.
- **Implementation Timeline**: The Iceberg v3 spec is near finalization (minor additions pending). Parquet logical type release is a dependency. Wherobots' Havasu engine already implements the spec.
- **Iceberg vs. Delta Lake**: Szehon Ho characterizes Iceberg as read-optimized (slower writes, faster reads) and Delta Lake as write-optimized (faster writes, slower reads), noting the tension between open standards and vendor proprietary formats.

## Speakers

- **Jia Yu** — Co-Founder and CTO at Wherobots
- **Chris Holmes** — Creator of GeoParquet, Planet Fellow at Planet Labs
- **Szehon Ho** — Iceberg PMC Member, Software Engineer at Databricks
- **Vikram Gundeti** — CTO at Foursquare

## Key Quotes

> "Iceberg was breaking open data silos... having geo in iceberg is really spreading that iceberg moment to the geo as well." — Szehon Ho

> "The core of it really is this separation of compute from storage... the fact that iceberg makes it possible where you can just find the best query engine for your given job." — Chris Holmes

> "The standardization of the storage layer opens up the doors for a lot more things... it gives control back to the provider." — Vikram Gundeti

## References

- Apache Iceberg GEO v3 Specification
- GeoParquet Standard
- Apache Parquet GEO Logical Type
- Wherobots Havasu Engine