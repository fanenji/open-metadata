---
type: entity
title: Apache Sedona
created: 2026-04-04
updated: 2026-05-07
tags:
  - spark
  - geospatial
  - library
  - sedona
  - big-data
  - spatial
  - computing
  - gis
  - distributed-computing
  - spatial-computing
  - flink
  - snowflake
related: ["spark", "geospatial-data-stack", "spatial-sql", "analyzing-real-estate-data-with-apache-concordia", "proj4j", "spatial-rdd-and-spatial-dataframe", "spatial-pre-processing-pattern", "geospatial-etl-pipeline-iceberg", "crs-transformation-strategies", "legacy-geospatial-etl-pipeline", "dremio-geospatial-limitations", "duckdb", "apache-spark", "iceberg-geospatial-support", "gdal-ogr", "geoparquet-vs-iceberg-metadata", "sedona-st-transform-limitations", "geotools", "postgis", "grid-shift-transformations"]sources:
  - "Analyzing Real Estate Data With Apache Sedona.md"
  - "Apache Sedona Coordinate Transform.md"
  - "Apache Sedona Coordinate Transform-20260506.md"
  - "ETL VETTORIALI.md"
  - "Ingestione dati cartografici_ analisi alternative.md"
  - "Sedona e file grigliati GSB.md"
---
# Apache Sedona

**Apache Sedona** (formerly GeoSpark) is an open‑source distributed computing framework that extends Apache Spark, Apache Flink, and Snowflake with native geospatial capabilities. It provides specialized data structures (Spatial RDDs, Spatial DataFrames), high‑performance spatial SQL functions, user‑defined types (UDTs) for geometries, and native support for reading and writing GeoParquet, Shapefile, GeoJSON, and GeoPackage formats. Designed for large‑scale spatial data processing and analytics, Sedona is the recommended tool for handling geospatial data within Spark‑based ETL pipelines in the Data Platform and serves as a key alternative to GDAL‑based approaches in a data lakehouse architecture.

## Architecture

Sedona relies on the **GeoTools** Java geospatial library for coordinate transformation operations. The `geotools-wrapper` dependency version is typically tied to the GeoTools version it encapsulates (e.g., Sedona 1.7.1 uses GeoTools 28.5). This means Sedona inherits the capabilities and limitations of the underlying GeoTools library, which in turn may use Proj4j (a lightweight PROJ implementation) or the full PROJ library for CRS transformations.

## Core Capabilities

- **Spatial RDDs and Spatial DataFrames**: Extend Spark's distributed data structures with spatial indexing (R‑Tree, Quad‑Tree) and partitioning for efficient geometric operations.
- **Spatial SQL**: Provides a rich set of SQL spatial functions with the `ST_` prefix, similar to PostGIS. Includes core functions like `ST_Centroid`, `ST_Intersects`, `ST_Distance`, `ST_Transform`, `ST_GeomFromWKB`, `ST_GeomFromEWKT`, as well as advanced geodetic functions such as `ST_BestSRID`, `ST_DistanceSpheroid`, `ST_AreaSpheroid`, `ST_FlipCoordinates`.
- **Geometry UDT**: A native geometry type within Spark DataFrames, enabling first‑class geospatial support.
- **GeoParquet Support**: Automatically writes GeoParquet with correct geo‑metadata (CRS, geometry column, encoding, bounding box) via integration with Spark's Parquet writer. Also reads GeoParquet files.
- **Multi‑Format Support**: In addition to GeoParquet, Sedona can read and write Shapefile, GeoJSON, and GeoPackage.
- **Iceberg and Delta Lake Integration**: Works with the Spark‑Iceberg connector to write GeoParquet data into Iceberg tables, and also integrates with Delta Lake. Sedona was one of the first query engines to support native GEO types introduced in Iceberg V3.
- **CRS Handling**: Can infer the Coordinate Reference System from EWKT strings or set it explicitly on geometries.
- **Multi‑Language API**: Supports Scala, Java, Python (PySpark), and R.
- **JDBC Connectivity**: Can read from PostGIS and Oracle Spatial databases. For Oracle, geometry conversion via `ST_AsBinary`/`ST_GeomFromWKB` may be required.
- **Platform Support**: Beyond Apache Spark, Sedona also extends Apache Flink and Snowflake, providing distributed spatial operations across these environments. The **SedonaSnow Native App** for Snowflake offers enhanced transformation capabilities.

## Role in Vector ETL

In the context of the [[ETL VETTORIALI]] analysis, Apache Sedona is the primary tool for parsing WKB/WKT geometries from JDBC reads, writing GeoParquet with correct metadata, and applying spatial functions within Spark DataFrames for validation and transformation. It represents a key alternative to the legacy GDAL‑based pipeline, potentially unifying the entire geospatial ETL process within a single Spark‑based framework and simplifying the architecture compared to heterogeneous tool orchestration. Sedona is central to the [[geospatial-etl-pipeline-iceberg]] pattern.

## CRS Transformation and Grid File Support

A critical technical constraint in Sedona’s architecture is its handling of Coordinate Reference System transformations requiring grid‑based methods.

**Limitations:**
- `ST_Transform` does not directly support GSB (grid shift binary) files, `+nadgrids` directives, or complete PROJ strings in the Spark/Flink SQL and DataFrame API.
- Users cannot specify a specific transformation method (e.g., EPSG code 1612) when transforming between datums (see [GitHub issue #1397](https://github.com/apache/incubator-sedona/issues/1397)).
- This is a **library‑interface gap**: the underlying GeoTools library does support grid‑based transformations, but Sedona’s API does not expose the necessary parameters to use them.

**Snowflake Exception:** The SedonaSnow Native App for Snowflake does support grid‑based transformations, proving the underlying engine capability exists but is not universally exposed across all platforms.

### Workarounds

For workflows that need high‑accuracy CRS transformations involving grid files, the following approaches are recommended:

1. **Delegation to PostGIS**: Perform the transformation inside the JDBC source query using `ST_Transform` before the data reaches the Sedona cluster. This is the preferred approach for transformations requiring grid‑based methods (e.g., EPSG:7791).
2. **Pre‑processing with GDAL (ogr2ogr)**: Transform geometries outside Sedona using GDAL’s `ogr2ogr` as a separate step before loading into Sedona. This can be done by invoking GDAL from Spark or by pre‑processing files.
3. **Custom UDF (GDAL/PROJ)**: Write a custom Spark UDF that uses GDAL or PROJ bindings to perform the transformation with full grid support.
4. **Spark UDF with pyproj**: For Python users, a PySpark UDF can encapsulate `pyproj`, distributing GSB files to worker nodes and configuring the `PROJ_LIB` environment variable.
5. **Configure PROJ Environment**: If Sedona/GeoTools uses PROJ underneath, configuring the underlying PROJ environment may enable grid support, but this requires careful setup and testing.
6. **SedonaSnow Native App**: For Snowflake users, this approach supports grid‑based transformations directly.

See [[crs-transformation-strategies]] for a decision framework on where to apply transformations, and [[sedona-st-transform-limitations]] for more details on the GSB limitation.

## Usage Pattern

The following code snippet demonstrates the typical pattern for reading geospatial data from PostGIS, transforming it (if needed), and writing GeoParquet, avoiding Sedona’s grid‑file limitations by letting PostGIS handle the transformation:

```python
from sedona.register import SedonaRegistrator
from sedona.utils import SedonaKryoRegistrator, KryoSerializer

spark = SparkSession.builder \
    .config("spark.serializer", KryoSerializer.getName) \
    .config("spark.kryo.registrator", SedonaKryoRegistrator.getName) \
    .getOrCreate()

SedonaRegistrator.registerAll(spark)

# Read from PostGIS with ST_Transform applied before retrieval
df = spark.read.format("jdbc") \
    .option("query", "SELECT ST_AsBinary(ST_Transform(geom, 7791)) AS geom_wkb FROM table") \
    .load()

# Convert WKB to Sedona geometry
df.createOrReplaceTempView("data")
geometry_df = spark.sql("SELECT ST_GeomFromWKB(geom_wkb) AS geometry FROM data")

# Write GeoParquet
geometry_df.write.format("parquet").save("path")
```

For Oracle Spatial, replace the query with `SELECT ST_AsBinary(ST_Transform(geom, target_srid)) AS geom_wkb FROM table`, but note that Oracle uses `SDO_GEOMETRY`; the conversion function may vary.

This pattern is a core part of the [[legacy-geospatial-etl-pipeline]] replacement.

## Performance Considerations

Apache Sedona requires significant CPU and memory resources for the driver and executors. Careful configuration and tuning are essential for optimal performance, especially when dealing with large‑scale spatial joins or transformations. However, Sedona’s ability to unify the entire geospatial ETL pipeline within a single framework can simplify architecture and reduce overhead compared to orchestrating multiple heterogeneous tools.

## Use Cases

Apache Sedona is particularly effective for performing spatial joins between massive datasets, such as joining point‑in‑polygon datasets (e.g., property locations) with administrative boundaries (e.g., county shapefiles). When combined with its spatial indexing and partitioning capabilities, it enables scalable geospatial analytics and ETL processing directly within Spark.

## Related

- [[apache-spark]]
- [[analyzing-real-estate-data-with-apache-concordia]]
- [[crs-transformation-strategies]]
- [[dremio-geospatial-limitations]]
- [[duckdb]]
- [[gdal-ogr]]
- [[geospatial-data-stack]]
- [[geospatial-etl-pipeline-iceberg]]
- [[geoparquet-vs-iceberg-metadata]]
- [[geotools]]
- [[grid-shift-transformations]]
- [[iceberg-geospatial-support]]
- [[legacy-geospatial-etl-pipeline]]
- [[postgis]]
- [[proj4j]]
- [[sedona-st-transform-limitations]]
- [[spatial-pre-processing-pattern]]
- [[spatial-rdd-and-spatial-dataframe]]
- [[spatial-sql]]
- [[spark]]