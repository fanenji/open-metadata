---
type: concept
title: PyIceberg Usage Patterns for Geospatial ETL
created: 2026-04-29
updated: 2026-04-29
tags: [iceberg, python, pyiceberg, etl, geospatial]
related: [geospatial-etl-pipeline-iceberg, crs-transformation-strategies, apache-sedona, nessie-catalog-versioning, iceberg-table-versioning]
sources: ["ETL VETTORIALI.md"]
---
# PyIceberg Usage Patterns for Geospatial ETL

This concept page documents the usage patterns and considerations for using PyIceberg (the Python Iceberg client) in the geospatial vector ETL pipeline. While PyIceberg is technically feasible, the [[ETL VETTORIALI]] analysis recommends against its use for production workloads in favor of Spark's native Iceberg connector.

## When to Consider PyIceberg

- **Small datasets** where single-node processing is sufficient.
- **Prototyping and PoCs** where rapid iteration is more important than production robustness.
- **Python-only environments** where Spark is not available or desired.

## Core Pattern

The typical PyIceberg workflow for geospatial ETL involves:

1. **Write GeoParquet** to S3/MinIO using GeoPandas or DuckDB.
2. **Load the Iceberg table** from the Nessie catalog.
3. **Create a DataFile** object describing the Parquet file (path, format, row count, column stats).
4. **Append or overwrite** the Iceberg table with the new data file.
5. **Commit** the transaction to create a new snapshot.

## Example (Conceptual)

```python
from pyiceberg.catalog import load_catalog
from pyiceberg.types import DataFile, DataFileContent

catalog = load_catalog('nessie', uri='http://nessie_host:19120/api/v1')
table = catalog.load_table('namespace.table_name')

data_file = DataFile(
    file_path="s3a://bucket/path/to/file.parquet",
    file_format="PARQUET",
    content=DataFileContent.DATA,
    # Add row count, column stats, partition data
)

with table.transaction() as tx:
    tx.append_data_file(data_file)
    tx.commit()
```

## Critical Considerations

### 1. Complexity
Manual management of Iceberg metadata (manifest files, manifest lists, snapshots) is significantly more complex than using Spark's Iceberg connector. Errors can leave the table in an inconsistent state.

### 2. Error Handling and Rollback
Implementing robust error handling and rollback mechanisms is challenging. If the script fails after uploading the Parquet file but before committing to Iceberg, orphaned files remain on S3.

### 3. Performance
PyIceberg operations are single-node. For large datasets, the overhead of reading, writing, and committing can be substantial.

### 4. Feature Parity
PyIceberg may not support all Iceberg features available through the Spark connector (e.g., advanced partitioning, compaction, and maintenance operations).

## Recommendation

**Avoid PyIceberg for production geospatial ETL workloads.** Use Spark with the `spark-iceberg` connector instead. PyIceberg is acceptable for:
- Small-scale experiments and PoCs.
- Administrative tasks (e.g., inspecting table metadata, running maintenance operations).
- Environments where Spark is not available and data volumes are small.

## Related
- [[geospatial-etl-pipeline-iceberg]] — The overall ETL pipeline pattern.
- [[apache-sedona]] — The recommended Spark-based approach for geospatial Iceberg ingestion.
- [[nessie-catalog-versioning]] — The catalog versioning system used with Iceberg.