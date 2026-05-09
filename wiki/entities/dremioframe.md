---
type: entity
title: DremioFrame
created: 2026-04-29
updated: 2026-05-07
tags:
  - dremio
  - python
  - library
  - dataframe
  - alpha
related:
  - dremio
  - dremio-mcp-server
  - dremioframe-data-quality-framework
  - dremioframe-ai-agent
  - dremioframe-orchestration
  - dremioframe-iceberg-management
  - dremioframe-admin-governance
  - dremioframe-profile-config
  - developer-advocacy-dremio
  - dremioframe-f-api
  - dremioframe-data-quality
  - dremioframe-ingestion
  - dremio-reflections
  - dremio-duckdb-integration
  - dremio-udf-gis
  - fastapi
  - dbt-osmosis
  - dbt-expectations
  - data-ingestion-architectural-patterns
  - data-quality-dimensions
  - iceberg-table-versioning
sources:
  - DremioFrame - Dremio Dataframe Library.md
  - "Introducing dremioframe - A Pythonic DataFrame Interface for Dremio.md"
---

# DremioFrame

**DremioFrame** (package name `dremioframe`) is an unofficial Python library (currently in alpha) that provides a Pandas-like, method-chaining API for interacting with [[dremio|Dremio Cloud]] and Dremio Software. The library generates optimized SQL queries and pushes them down to Dremio's lakehouse engine. It is maintained by [[developer-advocacy-dremio]] and published on PyPI.

## Installation

```bash
pip install dremioframe
```

## Status

- **Alpha**: The library is in early development and not yet production-ready. Use with caution in production environments.
- **Support**: Issues and pull requests are handled via the [GitHub repository](https://github.com/developer-advocacy-dremio/dremio-cloud-dremioframe).

## Authentication

DremioFrame supports two authentication modes:

1. **Dremio Cloud** (recommended): Uses environment variables `DREMIO_PAT`, `DREMIO_PROJECT_ID`, and `DREMIO_PROJECT_NAME`.
2. **Dremio Community Edition / Software**: Uses `DREMIO_HOSTNAME`, `DREMIO_PORT`, `DREMIO_USERNAME`, `DREMIO_PASSWORD`, and `DREMIO_TLS`.

Additionally, connection details can be managed via a YAML-based profile configuration located at `~/.dremio/profiles.yaml`. This configuration supports both Dremio Cloud (using PAT + project ID) and Dremio Software (versions 25 and 26+).

## Clients

- **`DremioClient`** — Synchronous client for standard workflows.
- **`AsyncDremioClient`** — Asynchronous client for event-driven applications, such as those built with [[fastapi]].

## Core API

The library exposes a method-chaining DataFrame builder interface:

- `.query()` — Execute raw SQL.
- `.table()` — Reference a table for chainable operations.
- `.select()`, `.mutate()`, `.filter()`, `.join()`, `.union()`, `.group_by()`, `.order_by()`, `.limit()`, `.offset()` — Incremental query construction.
- `.collect()` or `.toPandas()` — Execute the query and return results as a Pandas DataFrame.

Programmatic expression construction is available through the F API ([[dremioframe-f-api]]) with functions like `F.col()`, `F.case()`, and `F.lit()`.

## Advanced Features

### Data Quality
[[dremioframe-data-quality-framework]] (also referred to as [[dremioframe-data-quality]]) provides built-in expectation testing for data validation.

### AI Agent
[[dremioframe-ai-agent]] enables code generation for SQL, scripts, and API calls.

### Orchestration
[[dremioframe-orchestration]] includes tasks, sensors, scheduling, and distributed execution capabilities.

### Ingestion
[[dremioframe-ingestion]] supports both REST API and Pandas DataFrame ingestion patterns.

### Reflections Management
[[dremio-reflections]] provides management of Dremio's acceleration layer for query performance.

### Iceberg Management
[[dremioframe-iceberg-management]] offers Iceberg time travel (via `.at_snapshot()`), schema evolution, and incremental processing. See also [[iceberg-table-versioning]].

### Administration & Governance
[[dremioframe-admin-governance]] covers catalog management, reflections, user-defined functions (UDFs), data masking, row access policies, tags, lineage, and privilege management.

### Visualization and Export
- `.chart()` — Inline plotting.
- `.to_csv()`, `.to_parquet()` — Export query results.

### MCP Server
The package includes an MCP server component; see [[dremio-mcp-server]].

### Integrations
Supports integration with Airflow, notebooks, dlt, Pydantic, and S3.

## Comparisons

- **[[dremio-duckdb-integration]]**: An alternative approach that uses DuckDB as a separate query engine rather than a dedicated library like DremioFrame.
- **[[dremio-mcp-server]]**: Another Dremio access tool, but designed for AI agents via the Model Context Protocol rather than Python developers.
- **[[dbt-osmosis]]**: Similar in spirit — both improve developer ergonomics around data transformation tools.
- **[[dbt-expectations]]**: Overlaps with DremioFrame's data quality expectations feature.

## Limitations

- Unofficial and Alpha — no long-term support guarantee.
- No benchmarks or performance comparisons against alternative Python–Dremio interfaces.
- It is unclear whether all Dremio SQL features (e.g., geospatial UDFs like [[dremio-udf-gis]]) are supported.
- Feature overlap with dbt testing patterns is not addressed.

## Related

- [[dremio]] — The data lakehouse engine DremioFrame interacts with.
- [[data-ingestion-architectural-patterns]] — DremioFrame supports API, database, and file system ingestion patterns.
- [[data-quality-dimensions]] — Details on the data quality framework.
- [[dremioframe-profile-config]] — Profile configuration details.
- [[dremio-udf-gis]] — Geospatial UDFs (if supported).