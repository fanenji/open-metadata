---
type: concept
title: dbt-Dremio Adapter
created: 2026-04-29
updated: 2026-05-07
tags: [dbt, dremio, adapter, elt, data-lakehouse, lakehouse, configuration]
related: [dbt-dremio, dremio, dbt-cloud, data-lakehouse, self-serve-data-platform, dbt-mesh, dbt-core, dbt-project-structure, dremio-system-configuration, dremio-geospatial-limitations]
sources: ["INTEGRAZIONI.md", "Report dettagliato su dbt software.md"]
---
# dbt-Dremio Adapter

The dbt-Dremio adapter is a connector that enables [[dbt]] to transform and test data directly within [[Dremio]], the data lakehouse query engine. It allows dbt Core to use Dremio as its execution engine for production lakehouse workloads. Dremio provides a high-performance SQL query engine that queries data directly where it resides (Parquet/Iceberg on AWS S3) without copying or moving data. Data teams can use dbt's modeling, testing, and documentation capabilities on top of Dremio's virtualized data layer.

## Key Features

- Enables dbt-based ELT workflows on Dremio
- Allows management of the Dremio Semantic Layer through dbt
- Supports dbt's testing and documentation features for Dremio-managed data
- Provides materialization strategies: tables, views, and incremental models
- Synchronizes dbt documentation and tags with the Dremio data catalog for enhanced data discovery and governance

## Configuration

The adapter requires specific configuration in `profiles.yml`. The following table summarizes the key parameters.

| Parameter                 | Required | Description                                                       | Example (Cloud)                  | Example (Software)              |
|---------------------------|----------|-------------------------------------------------------------------|----------------------------------|---------------------------------|
| `type`                    | Yes      | Adapter type                                                      | `dremio`                         | `dremio`                        |
| `threads`                 | Yes      | Parallel threads for dbt execution                                | `4`                              | `4`                             |
| `user`                    | Yes      | Email (Cloud) or username (Software)                              | `user@example.com`               | `dremio_user`                   |
| `pat`                     | Yes (Cloud) | Personal Access Token                                          | `{{ env_var('DREMIO_PAT') }}`    | `{{ env_var('DREMIO_PAT') }}`   |
| `password`                | Yes (Software, no PAT) | Password for username auth                            | N/A                              | `{{ env_var('DREMIO_PASSWORD') }}` |
| `cloud_host`              | Yes (Cloud) | Dremio Cloud API endpoint                                       | `api.dremio.cloud`               | N/A                             |
| `cloud_project_id`        | Yes (Cloud) | Dremio Cloud project ID                                         | `1ab23-c456-78d9-e01f-234g`      | N/A                             |
| `software_host`           | Yes (Software) | Coordinator node hostname/IP                                  | N/A                              | `192.168.1.100`                 |
| `port`                    | Yes (Software) | API port (default: 9047)                                       | N/A                              | `9047`                          |
| `use_ssl`                 | Yes      | Use TLS                                                           | `true`                           | `true`                          |
| `object_storage_source`   | No       | Dremio source for table materialization                           | `MyS3Source`                     | `MyS3Source`                    |
| `dremio_space`            | No       | Dremio Space for view creation                                    | `analytics_space`                | `analytics_space`               |
| `dremio_space_folder`     | No       | Subfolder within Space for views                                  | `gold_layer`                     | `gold_layer`                    |

## Materialization Strategies

- **`materialized='table'`**: creates physical tables (Parquet/Iceberg files) in the specified object storage source.
- **`materialized='view'`**: creates logical views within a Dremio Space.
- **`materialized='incremental'`**: updates physical tables incrementally.

## Documentation Synchronization

Dremio can synchronize dbt documentation and tags directly with its data catalog, enriching data discovery and governance by making model and column descriptions visible in the Dremio interface.

## Integration Details

The adapter is maintained on GitHub by [[fabrice-etanchaud]] at [dbt-dremio](https://github.com/fabrice-etanchaud/dbt-dremio). Dremio has an official partnership with [[dbt Labs]], and the adapter is documented through blog posts and video tutorials.

## Related Concepts

- [[dbt-cloud]] — dbt Labs' managed platform for deploying dbt projects
- [[data-lakehouse]] — The architectural pattern Dremio implements
- [[self-serve-data-platform]] — Enabled by managing the Dremio Semantic Layer via dbt
- [[dbt-mesh]] — Cross-project dependency management that can leverage Dremio as a query engine
- [[dbt-core]] — Open-source core of dbt
- [[dbt-project-structure]] — Standard layout for dbt projects
- [[dremio-system-configuration]]
- [[dremio-geospatial-limitations]]