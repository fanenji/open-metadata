---
type: concept
title: dbt-duckdb Adapter
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, duckdb, adapter, local-development, s3]
related: [duckdb, dbt-core, dbt-local-first-development, dbt-project-structure, duckdb-iceberg-extension]
sources: ["Report dettagliato su dbt software.md"]
---
# dbt-duckdb Adapter

The dbt-duckdb adapter enables dbt Core to use DuckDB as its execution engine. Combined with S3 access via the httpfs extension, this creates a "serverless, local-first lakehouse" paradigm that disconnects development workflow from expensive cloud compute.

## Key Configuration Parameters

| Parameter | Level | Description | Example Value |
|-----------|-------|-------------|---------------|
| `type` | Output | Adapter type | `duckdb` |
| `path` | Output | Local DuckDB database file path | `dbt_local.duckdb` |
| `extensions` | Output | DuckDB extensions to load | `['httpfs', 'parquet']` |
| `settings` | Output | DuckDB configuration options | (see below) |
| `s3_region` | settings | AWS region of the S3 bucket | `eu-west-1` |
| `s3_access_key_id` | settings | AWS access key ID | `{{ env_var('AWS_ACCESS_KEY_ID') }}` |
| `s3_secret_access_key` | settings | AWS secret access key | `{{ env_var('AWS_SECRET_ACCESS_KEY') }}` |

## Example profiles.yml Configuration

```yaml
local_lakehouse:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: jaffle_shop.duckdb
      extensions:
        - httpfs
        - parquet
      settings:
        s3_region: 'us-east-1'
        s3_access_key_id: "{{ env_var('S3_ACCESS_KEY_ID') }}"
        s3_secret_access_key: "{{ env_var('S3_SECRET_ACCESS_KEY') }}"
```

## Use Cases

- **Local-first development:** Run entire lakehouse pipelines on a laptop, interacting with cloud only for storage I/O.
- **Direct S3 queries:** Define sources that read Parquet files directly from S3 using `read_parquet()`.
- **Materialization to S3:** Write transformed data back to S3 as Parquet files using post-hooks or custom materializations.
- **MotherDuck integration:** Connect to MotherDuck (serverless cloud DuckDB) by modifying the `path` parameter.

## Paradigm Shift

This adapter changes the economics of analytics engineering. Traditional dbt workflows required a connection to a cloud data warehouse with compute costs per run. With dbt-duckdb + S3, developers use a free, local, fast engine (DuckDB) to read/write directly to low-cost storage (S3), paying only for storage I/O during development.