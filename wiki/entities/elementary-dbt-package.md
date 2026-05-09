---
type: entity
title: Elementary dbt Package
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, observability, monitoring, open-source]
related: [dbt-observability-implementation, or-avidov, dbt-artifacts, data-observability-definition]
sources: ["dbt observability 101 How to monitor dbt run and test results.md"]
---
# Elementary dbt Package

An open-source dbt package developed by [[Or Avidov]] that provides comprehensive dbt observability. It extends the basic Jinja-based logging pattern with richer metadata collection, dashboards for flaky tests and execution results, and Slack alerts. Supports Snowflake, BigQuery, Redshift, and Databricks.

## Features

- Collects all dbt artifact metadata (models, sources, tests, exposures, metrics) into simple warehouse tables.
- Tracks flaky tests by monitoring test success rates over time.
- Provides dashboards for execution results and performance trends.
- Sends Slack alerts on test failures and anomalies.
- Updates metadata tables on every PR or dbt command invocation.

## Relationship to the Jinja-based Approach

The article presents the Jinja-based macro pattern as a lightweight starting point, while Elementary is positioned as the production-ready, feature-rich solution. There is an internal tension: the article criticizes processing dbt artifacts as complex, but Elementary itself processes those same artifacts for richer metadata.

## Related

- [[dbt-observability-implementation]] — The basic pattern that Elementary extends.
- [[dbt-artifacts]] — The JSON files that Elementary processes.
- [[data-observability-definition]] — The broader framework that dbt observability contributes to.