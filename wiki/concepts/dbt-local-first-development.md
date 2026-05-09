---
type: concept
title: dbt Local-First Development
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, duckdb, local-development, paradigm, cost-optimization]
related: [dbt-duckdb-adapter, duckdb, dbt-core, dbt-project-structure, elt-pattern]
sources: ["Report dettagliato su dbt software.md"]
---
# dbt Local-First Development

The combination of the dbt-duckdb adapter with S3 access creates a "serverless, local-first lakehouse" paradigm that fundamentally changes the economics and accessibility of analytics engineering.

## The Paradigm Shift

Traditional dbt workflows required a connection to a cloud data warehouse (Snowflake, BigQuery, etc.), incurring compute costs for every `dbt run`. The dbt-duckdb adapter, combined with the httpfs extension, allows dbt to use a free, local, extremely fast engine (DuckDB) to read and write directly to low-cost storage (S3).

This means:
- **Entire ELT pipelines can be developed, tested, and run on a developer's laptop**
- **Cloud interaction is limited to storage I/O, not compute**
- **Development costs are drastically reduced**
- **The development workflow is decoupled from expensive, always-on cloud compute**

## How It Works

1. **Define S3 sources** in `sources.yml` using `read_parquet()` to read Parquet files directly from S3.
2. **Develop and test models** locally with DuckDB, running `dbt run` against the local engine.
3. **Materialize to S3** using post-hooks or custom materializations to write transformed data back as Parquet files.
4. **Switch to production** by changing the target in `profiles.yml` to use Dremio (or another production engine) for large-scale execution.

## Implications

- **Cost savings:** No cloud compute costs during development; only storage costs for S3 I/O.
- **Accessibility:** Developers can work offline or with limited connectivity.
- **Portability:** The same dbt project can run locally (DuckDB) or in production (Dremio) by changing the target profile.
- **Reproducibility:** Local development environments are fully self-contained and versionable.

## Limitations

- Developers must manage S3 credentials locally.
- DuckDB is single-machine; it cannot scale horizontally like Dremio or Snowflake.
- Performance on very large datasets may be limited by local hardware.
- The dual-engine architecture requires maintaining two configurations.