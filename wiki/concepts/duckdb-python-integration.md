---
type: concept
title: DuckDB Python Integration
created: 2026-04-04
updated: 2026-04-04
tags: [duckdb, python, api, dataframe]
related: [duckdb, duckdb-execution-model, duckdb-spatial-extension, duckdb-spatial-workflow]
sources: ["DuckDB Spatial Supercharged Geospatial SQL - Summary.md"]
---
# DuckDB Python Integration

DuckDB provides three Python APIs for interacting with the database, along with zero-copy dataframe interoperability.

## Three Python APIs

| API | Style | Notes |
|---|---|---|
| **Standard DB API** | Connections, cursors | Familiar if you've used any Python database driver |
| **PySpark-compatible API** | Spark-like | Drop-in replacement for PySpark code |
| **Relational API** | Chainable, lazy | Recommended — composable like a dataframe, but fully optimized |

## Relational API (Recommended)

The relational API is **completely lazy**: operators are chained in Python but nothing executes until a terminating call (`.show()`, `.to_table()`, `.fetchall()`). This lets DuckDB see the **entire query plan at once** and apply all optimizations before execution.

### Expression Builder

The relational API provides an expression builder for composing queries programmatically without raw SQL strings:

```python
from duckdb import FunctionExpression, ColumnExpression, ConstantExpression

def make_point(lat_col, lon_col):
    return FunctionExpression("ST_Point",
        ColumnExpression(lon_col),
        ColumnExpression(lat_col)
    )

def transform(geom_expr, src_crs, dst_crs):
    return FunctionExpression("ST_Transform",
        geom_expr,
        ConstantExpression(src_crs),
        ConstantExpression(dst_crs)
    )

rides = rides.select(
    "*",
    transform(make_point("pickup_latitude", "pickup_longitude"),
              "EPSG:4326", "EPSG:102718").alias("pickup_geom"),
    transform(make_point("dropoff_latitude", "dropoff_longitude"),
              "EPSG:4326", "EPSG:102718").alias("dropoff_geom")
)
```

## Zero-Copy Dataframe Interoperability

Because DuckDB is in-process and shares the same address space as Python, it can read dataframes **directly from memory** without copying:

```python
import duckdb
import pandas as pd

df = pd.DataFrame(...)
result = duckdb.sql("SELECT * FROM df WHERE value > 100")  # reads df directly
```

Supported formats: **Pandas, Polars, NumPy, PyArrow** — scan them in SQL queries directly.

Results can also be exported back to any of these formats for downstream processing (e.g., plotting with GeoPandas).

## Typical Workflow

1. Load data (Parquet, CSV, shapefile) using DuckDB's native readers or `ST_Read()`
2. Transform and clean using the relational API or SQL
3. Export results to Pandas/Polars for visualization or further processing
4. Optionally write results back to Parquet or database
