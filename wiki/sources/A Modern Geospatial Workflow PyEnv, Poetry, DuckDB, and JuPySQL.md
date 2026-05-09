type: source
title: "A Modern Geospatial Workflow: PyEnv, Poetry, DuckDB, and JuPySQL"
authors: [Jake Gearon]
year: 2023
url: "https://medium.com/@jake.gearon_34983/a-modern-geospatial-workflow-pyenv-poetry-duckdb-and-jupysql-7e7d355655f5"
venue: "Medium"
tags: [geospatial, duckdb, python, workflow]
created: 2026-04-08
updated: 2026-04-08
sources: ["A Modern Geospatial Workflow PyEnv, Poetry, DuckDB, and JuPySQL.md"]
---
# A Modern Geospatial Workflow: PyEnv, Poetry, DuckDB, and JuPySQL

An article by Jake Gearon detailing a transition from heavy, unstable Conda-based environments to a lightweight, modular Python stack for geospatial data science.

The author proposes using **PyEnv** for Python version management and **Poetry** for dependency and virtual environment management to avoid "dependency hell" (specifically regarding GDAL). The workflow leverages **DuckDB** as an in-process OLAP engine for high-performance analytical queries on large datasets, specifically demonstrating the use of **GeoParquet** for efficient storage. Additionally, the use of **JuPySQL** is highlighted for its ability to perform SQL-driven data science and visualization directly within Jupyter Notebooks.

The demonstration uses the **SWORD (SWOT River Database) v16** dataset, showing that over 10 million rows can be loaded in less than a second and complex plots can be generated in milliseconds.