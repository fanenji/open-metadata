---
type: entity
title: VulcanSQL
created: 2026-04-04
updated: 2026-04-04
tags: [data-api, framework, sql, templating]
related: [data-api-framework, duckdb, reverse-etl-pattern, dbt-macros, openapi]
sources: ["VulcanSQL.md"]
---
# VulcanSQL

VulcanSQL is a Data API Framework for AI Agents and Data Apps. It offers a development experience similar to [[dbt-macros]], using templated SQL with variables that accept API inputs and generate SQL statements dynamically. The framework is designed to bridge the gap between data transformation and data serving.

## Architecture

VulcanSQL follows a four-stage workflow:

1. **Build**: Write templated SQL with variables. VulcanSQL accepts API input and generates SQL on the fly.
2. **Accelerate**: Uses [[duckdb]] as a caching layer to boost query speed and API response time, reducing strain on data sources.
3. **Deploy**: Flexible deployment via Docker or command-based setups. A `package` command bundles assets for smooth transition from development to production.
4. **Share**: Auto-generated OpenAPI documentation; data extraction without SQL knowledge; seamless integration into familiar applications.

## Connections

- [[data-api-framework]] — Concept page for templated SQL API frameworks.
- [[duckdb]] — DuckDB serves as the caching layer for query acceleration.
- [[reverse-etl-pattern]] — VulcanSQL can serve processed data to operational systems.
- [[dbt-macros]] — Similar templating approach but focused on API endpoints rather than data models.
- [[openapi]] — Auto-generated API documentation is based on the OpenAPI standard.

## Caveats

- Source is a marketing page with no benchmarks, case studies, or technical depth.
- Production readiness, scalability limits, and enterprise features are not documented.
- Authentication, rate limiting, and API security are not addressed in the source.