---
type: concept
title: PostGIS Performance Tuning for ETL Workloads
created: 2026-04-29
updated: 2026-04-29
tags: [postgis, performance, etl, tuning, geospatial]
related: [crs-transformation-strategies, geospatial-etl-pipeline-iceberg, legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl]
sources: ["ETL VETTORIALI.md"]
---
# PostGIS Performance Tuning for ETL Workloads

This concept page documents strategies for mitigating performance bottlenecks on PostGIS (`viscarto`) when it is used as a staging and transformation layer for the geospatial vector ETL pipeline.

## The Bottleneck

When Spark reads from PostGIS using a JDBC query that includes `ST_Transform(geometry, target_srid)`, the transformation is executed on-the-fly by PostGIS for every row. This can impose significant CPU load on the PostGIS server, potentially becoming the bottleneck of the entire ingestion pipeline.

## Mitigation Strategies

### 1. Server Resource Optimization
- **CPU**: Ensure adequate CPU cores for parallel query execution.
- **RAM**: Sufficient shared buffers and work memory for large transformations.
- **I/O**: Fast storage (SSD) for database files and temporary files.

### 2. PostgreSQL Configuration Tuning
- **`shared_buffers`**: Increase for better caching.
- **`work_mem`**: Increase for sort and hash operations.
- **`maintenance_work_mem`**: Increase for VACUUM and ANALYZE.
- **`effective_cache_size`**: Set to reflect available OS cache.
- **`max_parallel_workers_per_gather`**: Enable parallel query execution.

### 3. Spatial Indexes
Ensure spatial indexes exist on the geometry column being transformed. While `ST_Transform` itself doesn't use the index, the underlying table scan can be optimized with proper indexing on filter columns.

### 4. Table Maintenance
- Run `VACUUM ANALYZE` regularly on tables involved in ETL reads.
- Consider `VACUUM FREEZE` for tables with high update rates.

### 5. Spark JDBC Parallelization
Use Spark's JDBC partitioning options (`partitionColumn`, `lowerBound`, `upperBound`, `numPartitions`) to distribute the read load across multiple connections. This distributes the `ST_Transform` workload across PostGIS processes but does not reduce total CPU load.

### 6. Materialized Views (Recommended)
Create a Materialized View in PostGIS with pre-transformed geometries:

```sql
CREATE MATERIALIZED VIEW schema.tabella_trasformata AS
SELECT colonna1, colonna2, ST_Transform(geometria, 7791) AS geom_epsg7791
FROM schema.tabella_sorgente;
```

Refresh the view periodically after the Oracle → PostGIS load phase:

```sql
REFRESH MATERIALIZED VIEW schema.tabella_trasformata;
```

**Pros:**
- Eliminates `ST_Transform` overhead during Spark reads
- Transformed data is pre-computed and indexed
- Significantly faster reads

**Cons:**
- Additional storage on PostGIS
- Requires scheduled refresh management
- Adds complexity to the PostGIS maintenance workflow

## Monitoring

Monitor the following metrics during ETL reads:
- **CPU utilization** on PostGIS server
- **Query execution time** for JDBC reads
- **Connection pool usage** (Spark parallel connections)
- **Disk I/O** for temporary files during large transformations

## Related
- [[crs-transformation-strategies]] — Decision framework for where to perform CRS transformations.
- [[geospatial-etl-pipeline-iceberg]] — The overall ETL pipeline that uses PostGIS as a staging layer.
- [[legacy-geospatial-etl-pipeline]] — The legacy pipeline context.