---
type: source
title: "Modern data warehouse modeling and ensuring data quality with dbt and OpenMetadata"
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, openmetadata, duckdb, data-modeling, data-quality, airflow, great-expectations]
related: [hybrid-dimensional-obt-modeling, luatnc87, fal-tool, custom-connector-openmetadata, dbt-dag-generator, dbt-expectations, duckdb, openmetadata-data-quality]
sources: ["Modern data warehouse modeling and ensuring data quality with dbt and OpenMetadata.md"]
authors: [luatnc87]
year: 2024
url: "https://github.com/luatnc87/modern-data-warehouse-modeling-and-data-quality-with-dbt-openmetadata"
venue: "GitHub Repository"
---
# Modern data warehouse modeling and ensuring data quality with dbt and OpenMetadata

A comprehensive guide to building a modern data warehouse using an open-source stack: DuckDB, dbt, OpenMetadata, and Apache Airflow. The repository demonstrates a [[hybrid-dimensional-obt-modeling]] approach combining a dimensional star schema base layer with a One Big Table (OBT) mart layer, along with data quality testing via dbt and [[dbt-expectations]], metadata ingestion into OpenMetadata via a [[custom-connector-openmetadata|custom DuckDB connector]], and job automation with Airflow using a [[dbt-dag-generator]] that parses `manifest.json`.

## Key Contributions

- **Hybrid Modeling Pattern**: Documents a two-layer architecture — a dimensional model (star schema) for power users and a denormalized OBT for business users.
- **Custom DuckDB Connector for OpenMetadata**: Provides a working implementation of a custom connector for ingesting DuckDB metadata into OpenMetadata, since DuckDB is not natively supported.
- **dbt DAG Generation from manifest.json**: Demonstrates programmatic creation of Airflow tasks by parsing dbt's `manifest.json` to preserve lineage.
- **End-to-End Integration**: Shows a complete, runnable pipeline from data modeling through testing, metadata governance, and orchestration using Docker Compose.

## Caveats

- DuckDB is an in-memory, single-machine database suitable for development/small-scale analytics but not production-grade for large-scale, multi-user workloads.
- The custom DuckDB connector is version-specific (OpenMetadata v1.1.2) and may require maintenance for newer versions.
- The guide is a tutorial/demonstration, not a rigorous comparative study.

## Related Wiki Pages

- [[hybrid-dimensional-obt-modeling]] — The core modeling pattern documented in this guide.
- [[luatnc87]] — Author and maintainer of the repository.
- [[fal-tool]] — Tool used for running Python scripts (Slack bot) within dbt.
- [[custom-connector-openmetadata]] — Pattern for building custom connectors, with this DuckDB connector as a concrete example.
- [[dbt-dag-generator]] — The manifest.json parsing pattern demonstrated here.
- [[dbt-expectations]] — Package used for enhanced Great Expectations-style tests.
- [[duckdb]] — The analytical database used as the warehouse engine.
- [[openmetadata-data-quality]] — OpenMetadata's data quality module, complementary to dbt testing.