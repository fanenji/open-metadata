---
type: source
title: Observability within dbt
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, observability, artifacts, alerting, performance]
related: [dbt-observability-implementation, dbt-artifacts, dbt-jinja-variables, on-run-end-hook, dbt-slim-ci, dbt-cloud, dbt-artifact-query-history-join, dbt-domain-alerting-pattern]
sources: ["Observability within dbt.md"]
authors: [Daniel Poppy, Kevin Chan, Jonathan Talmi]
year: 2021
url: "https://www.getdbt.com/blog/observability-within-dbt"
venue: "Coalesce 2021"
---
# Observability within dbt

This source is a transcript of a talk presented at Coalesce 2021 by Kevin Chan and Jonathan Talmi of Snapcommerce. It describes a lightweight, artifact-based observability system built entirely with the modern data stack (dbt, Airflow, Snowflake, Looker, Slack). The core insight is that dbt artifacts (run_results.json, manifest.json) contain sufficient metadata to build a comprehensive monitoring and alerting system without external observability tools.

The talk covers five architectural components: orchestration (Airflow with KubernetesPodOperator), artifact loading (a dbt macro using PUT/COPY/REMOVE), modeling (dbt models parsing JSON artifacts and joining with Snowflake query history), reporting (Looker dashboards for run status, test results, and performance), and alerting (Slack user groups triggered by domain-specific model tags).

A key novel contribution is joining dbt artifacts with Snowflake query history to surface deeper performance insights such as credit usage, spillage to disk, and warehouse sizing per model. The talk also presents pipeline bottleneck visualizations (thread-number vs. time Gantt charts) and time-series performance views for individual models.

The source acknowledges that dbt Cloud now has a robust metadata API and built-in visualizations, positioning this DIY approach as a pre-existing alternative. It recommends the dbt_artifacts package for easier artifact modeling.