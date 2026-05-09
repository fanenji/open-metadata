---
type: source
title: "How to add observability to your dbt deployment - Show and Tell"
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, observability, artifacts, snowflake, airflow, snapcommerce]
related: [dbt-artifact-upload-macro, dbt-query-comment-pattern, dbt-domain-tag-alerting, dbt-observability-implementation, dbt-artifacts, data-observability-definition, data-incident-management, dbt-artifact-publishing, dbt-jinja-variables, elementary-dbt-package]
sources: ["How to add observability to your dbt deployment - Show and Tell.md"]
---
# How to add observability to your dbt deployment - Show and Tell

**Source:** [dbt Community Forum](https://discourse.getdbt.com/t/how-to-add-observability-to-your-dbt-deployment/3451)  
**Authors:** @kevinc (Kevin C.) and @jt_st (JT) at Snapcommerce  
**Published:** 2021-12-06  
**Updated:** April 2023 (with link to newer blog post)

## Summary

This post describes a production system built at Snapcommerce to add observability to a dbt deployment using existing stack components: Airflow, Snowflake, Looker, and dbt artifacts. The system answers common analytics engineer questions about model freshness, runtime, test status, and performance bottlenecks.

## Key Contributions

1. **Failure-resilient artifact upload** — A macro that uploads dbt artifacts (run_results.json, manifest.json) to Snowflake even when the dbt pipeline fails, using a shell `ret=$?` pattern.
2. **Query comment integration** — A macro that injects `node_id` and `invocation_id` into every SQL query, enabling joins between dbt artifacts and Snowflake query history for cost and performance analysis.
3. **Domain-tagged alerting** — Every model tagged with a single domain (finance, growth, product) enables targeted Slack alerts to the right owners via Looker alerts.
4. **Model performance triage** — Three action items from performance data: materialization change, clustering key optimization, warehouse resize.

## Architecture

The system has four parts:
1. **Orchestration** — Airflow with KubernetesPodOperator runs dbt commands by deployment tag (hourly, nightly, external)
2. **Metadata** — Artifacts loaded to Snowflake stage via PUT/COPY/REMOVE macro
3. **Modelling** — Artifacts modelled in dbt and joined to Snowflake query history
4. **Reporting and Alerting** — Looker dashboards and alerts with Slack notifications

## Limitations

- Snowflake-specific (query history, stage operations, cost calculation)
- Airflow-specific (KubernetesPodOperator pattern)
- Requires manual tagging (deployment tags, domain tags)
- Dated (2021); the April 2023 update directs readers to a newer blog post