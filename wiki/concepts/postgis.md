---
type: concept
title: PostGIS
created: 2026-04-04
updated: 2026-04-04
tags: [geospatial, postgresql, spatial-database, gis]
related: [duckdb, geoparquet, geospatial-analytics-with-dbt, cloud-native-geospatial-workflow, legacy-geospatial-etl-pipeline]
sources: ["Modern Gis Workshop.md"]
---
# PostGIS

PostGIS is a spatial database extension for PostgreSQL that adds support for geographic objects, spatial queries, and geospatial analysis functions. It is a foundational component of traditional GIS workflows and remains relevant in modern geospatial data stacks.

## Role in Modern GIS

While cloud-native formats like [[GeoParquet]] and engines like [[DuckDB]] represent the cutting edge of geospatial analytics, PostGIS continues to serve as a robust spatial processing layer. The [[Modern Gis Workshop]] demonstrates a hybrid approach where PostGIS is used alongside modern tools for spatial queries and transformations.

## Integration with Modern Stack

- **DuckDB**: DuckDB can query PostGIS tables via the [[duckdb-postgres-scanner]] extension, enabling lightweight analytical queries against spatial data stored in PostgreSQL.
- **dbt**: dbt can transform and test geospatial data stored in PostGIS, integrating spatial validation into data pipeline workflows.
- **GeoParquet**: PostGIS data can be exported to GeoParquet format for cloud-native storage and analysis.

## Related Concepts

- [[legacy-geospatial-etl-pipeline]] — Traditional ETL patterns that rely on PostGIS as a transformation layer.
- [[geospatial-analytics-with-dbt]] — Using dbt for geospatial data transformation, including PostGIS integration.
- [[cloud-native-geospatial-workflow]] — Modern geospatial patterns that complement PostGIS with cloud-native tools.