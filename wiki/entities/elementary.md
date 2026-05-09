---
type: entity
title: Elementary
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, observability, tool]
related: ["dbt", "data-observability", "dbt-lifecycle", "metadata-mart", "anomaly-detection", "slack"]
sources: ["Are You Using Elementary for DBT?.md", "Are You Using Elementary for DBT?-20260506.md"]
---
# Elementary

[[elementary]] is a dbt package and command-line interface (CLI) designed for data observability, metadata management, and automated alerting. It acts as an "infrastructure-in-a-box" for dbt users, significantly reducing the manual effort required to implement monitoring.

## Core Features

### 1. Metadata Mart
At the heart of [[elementary]] is a structured [[metadata-mart]] within the data warehouse. It automatically ingests and maintains dimension tables for various dbt artifacts, including:
- `dbt_run_results`
- `dbt_models`
- `dbt_tests`
- `dbt_sources`
- `dbt_exposures`
- `dbt_metrics`
- `dbt_snapshots`

This architecture allows engineers to perform complex analytical queries (e.g., detecting performance regressions via standard deviation of execution times) directly using SQL.

### 2. Observability & Dashboards
[[elementary]] provides built-in dashboards that offer a faceted view of the dbt project. These dashboards are useful for monitoring:
- Latest test results (including the failing SQL query and specific failing rows).
- Test results over time for specific models.
- End-to-end pipeline visibility.

Reports can be generated and shared via the `edr report` command to platforms like [[azure]], [[s3]], or [[slack]].

### 3. Automated Alerting
The tool provides highly configurable, test-level alerting, primarily through [[slack]]. Alerts can be tailored to specific channels (e.g., notifying a Customer Success team when source data fails a quality check) and can include rich context like links to the dashboard and the actual failing data rows.

## Summary of Capabilities
- **Anomaly Detection**: Built-in tests for detecting unexpected changes in data patterns.
- **Schema Testing**: Advanced schema-level validation.

- **Lineage Tracking**: Visualizing test lineage and impact.
- **Multi-platform support**: Integration with [[airflow]], [[github-actions]], [[looker]], and [[tableau]].