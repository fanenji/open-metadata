type: concept
title: GeoParquet
created: 2026-04-08
updated: 2026-04-08
tags: [geospatial, storage, big-data]
related: [duckdb, parquet]
sources: ["A Modern Geospatial Workflow PyEnv, Poetry, DuckDB, and JuPySQL.md"]
---
# GeoParquet

**GeoParquet** is an optimized, columnar storage format specifically designed for the efficient storage and processing of geospatial data in cloud-native environments.

### Advantages over Traditional Formats
- **Performance:** Significant compression reduces file size and network bandwidth requirements compared to Shapefiles or GeoPackages.
- **Cloud-Native:** Highly compatible with modern analytical engines like [[duckdb]] and distributed computing frameworks.
- **Metadata Preservation:** Maintains essential geospatial metadata, such as Coordinate Reference Systems (CRS) and geometry types, within the file structure.
- **Scalability:** Enables efficient querying of massive datasets by allowing engines to read only the necessary columns and partitions.
---END 
---FILE: wiki/concepts/sql-driven-data-science.md---
type: concept
title: SQL-Driven Data Science
created: 2026-04-08
updated: 2026-04-08
tags: [data-science, sql, workflow]
related: [jupysql, duckdb]
sources: ["A Modern Geospatial Workflow PyEnv, Poetry, DuckDB, and JuPySQL.md"]
---
# SQL-Driven Data Science

**SQL-Driven Data Science** is a paradigm shift where SQL is used as the primary interface for data manipulation, cleaning, and even visualization, rather than relying solely on complex Python-based transformation logic.

### Core Principles
- **Declarative Logic:** Using SQL to describe *what* data to retrieve rather than *how* to iterate through it.
- **Efficiency:** Leveraging highly optimized analytical engines like [[duckdb]] to perform complex aggregations and joins at high speeds.
- **Reduced Complexity:** Minimizing the amount of boilerplate Python code required for standard ETL (Extract, Transform, Load) tasks.
- **Integrated Visualization:** Using tools like [[jupysql]] to bridge the gap between SQL queries and graphical outputs (e.g., `%sqlplot`).