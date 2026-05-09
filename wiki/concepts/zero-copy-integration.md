type: concept
title: Zero-Copy Integration
created: 2026-05-07
updated: 2026-05-07
tags: [duckdb, pandas, pyarrow, performance, integration]
related: [duckdb, duckdb-production-deployment, duckdb-performance-benchmarks]
sources: ["why-duckdb-crushed-our-500gb-data-pipeline-and-how-itll-crush-yours-too.md"]
---
# Zero-Copy Integration

Zero-copy integration is a technique where DuckDB can query in-memory data structures (Pandas DataFrames, Apache Arrow tables) directly without copying the data into the database. This eliminates the data movement overhead that typically dominates query time in traditional database workflows.

## How It Works

- DuckDB's in-memory query engine can directly access the memory buffers of Pandas DataFrames and Arrow tables
- No serialization, deserialization, or data copying is required
- The data stays in its original format; DuckDB reads it in place

## Examples

### Pandas Integration
```python
import duckdb
import pandas as pd

df = pd.DataFrame({'user_id': range(1000000), 'revenue': [100*i for i in range(1000000)]})

# Query the DataFrame directly — no copy to database!
result = duckdb.sql("""
    SELECT SUM(revenue), AVG(revenue), COUNT(*)
    FROM df
    GROUP BY country
""").fetchdf()
```

### Arrow Integration
```python
# Execute query and get Arrow table (zero-copy)
arrow_table = conn.execute("""
    SELECT * FROM user_sessions
    WHERE duration_seconds > 60
""").fetch_arrow_table()
```

## Benefits

- Eliminates data transfer bottleneck between data science tools and database
- Enables interactive analysis on large in-memory datasets
- Reduces memory usage (no duplicate data)
- Simplifies workflows (no need to load data into database first)

## Limitations

- Data must fit in memory (or be processed in chunks)
- Only works with supported formats (Pandas, Arrow, NumPy)
- Not applicable for persistent storage scenarios

## Relevance

Zero-copy integration is a key differentiator for DuckDB in data science and analytics workflows. It allows analysts to work with their existing Pandas/Arrow data while leveraging DuckDB's optimized analytical query engine.