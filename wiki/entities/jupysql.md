type: entity
title: JuPySQL
created: 2026-04-08
updated: 2026-04-08
tags: [sql, jupyter, data-science]
related: [duckdb, sql-driven-data-science]
sources: ["A Modern Geospatial Workflow PyEV, Poetry, DuckDB, and JuPySQL.md"]
---
# JuPySQL

**JuPySQL** is a SQL magic extension for Jupyter Notebooks, developed by the Ploomber organization. It allows users to execute SQL queries directly within notebook cells and integrate the results with Python-based data science tools.

### Key Capabilities
- **SQL Magic:** Enables seamless execution of SQL statements within Jupyter.
- **Interoperability:** Works effectively with engines like [[duckdb]] and integrates with libraries like Matplotlib and Pandas.
- **`%sqlplot`:** A specialized magic function that allows for quick, SQL-driven visualization (e.g., generating histograms directly from query results).
- **Data Pipeline Integration:** Supports saving query results to variables for downstream use in Python.