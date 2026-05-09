---
type: source
title: VulcanSQL
created: 2026-04-04
updated: 2026-04-04
tags: [data-api, framework, sql, templating]
related: [vulcansql, data-api-framework, duckdb, reverse-etl-pattern, dbt-macros]
sources: ["VulcanSQL.md"]
authors: []
year: 2026
url: "https://vulcansql.com/?s=09"
venue: ""
---
# VulcanSQL

VulcanSQL is a Data API Framework for AI Agents and Data Apps. It provides a dbt-like development experience using templated SQL to generate REST API endpoints. The framework follows a four-stage workflow: Build (templated SQL with variables), Accelerate (DuckDB caching layer), Deploy (Docker or CLI), and Share (OpenAPI documentation, SQL-free data extraction). It is hosted on GitHub under the Canner organization.

## Key Features

- **Templated SQL API Framework**: Insert variables into SQL templates; VulcanSQL accepts API inputs and generates SQL statements dynamically.
- **DuckDB Caching Layer**: Uses DuckDB as an intermediate cache to accelerate query speed and API response time.
- **Flexible Deployment**: Supports Docker and command-based deployment via a `package` command.
- **Auto-generated API Documentation**: OpenAPI-based documentation built from SQL template definitions.
- **Data Sharing**: Extract data from APIs without SQL knowledge; integrate into familiar applications.

## Connections

- [[vulcansql]] — Entity page for the framework.
- [[data-api-framework]] — Concept page for templated SQL API frameworks.
- [[duckdb]] — DuckDB serves as the caching layer.
- [[reverse-etl-pattern]] — VulcanSQL serves processed data to operational systems.
- [[dbt-macros]] — Similar templating approach but for API serving rather than transformation.