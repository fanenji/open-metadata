---
type: concept
title: Data API Framework
created: 2026-04-04
updated: 2026-04-04
tags: [data-api, framework, sql, templating]
related: [vulcansql, dbt-macros, reverse-etl-pattern, duckdb, openapi]
sources: ["VulcanSQL.md"]
---
# Data API Framework

A Data API Framework is a pattern for exposing SQL transformations as REST APIs. It uses templated SQL with variables that accept API inputs and generate dynamic SQL statements. This approach provides a dbt-like development experience but focused on API endpoints rather than data models.

## Key Characteristics

- **Templated SQL**: SQL templates with placeholders for API parameters.
- **Dynamic SQL Generation**: The framework generates SQL statements at runtime based on API inputs.
- **Caching Layer**: Often includes a caching mechanism (e.g., [[duckdb]]) to accelerate query performance.
- **Auto-generated Documentation**: OpenAPI-based documentation derived from SQL template definitions.
- **Flexible Deployment**: Supports Docker and CLI deployment options.

## Examples

- [[vulcansql]] — A Data API Framework for AI Agents and Data Apps.

## Connections

- [[dbt-macros]] — Similar templating approach but for data transformation rather than API serving.
- [[reverse-etl-pattern]] — Data API frameworks can serve processed data to operational systems.
- [[duckdb]] — Used as a caching layer in some implementations.
- [[openapi]] — Standard for auto-generated API documentation.