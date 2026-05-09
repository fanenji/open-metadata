---
type: entity
title: Snapcommerce
created: 2026-04-29
updated: 2026-05-07
tags: [company, dbt, observability, data-platform]
related: [dbt-observability-implementation, dbt-artifact-upload-macro, dbt-query-comment-pattern, dbt-domain-tag-alerting, kevin-chan, jonathan-talmi, dbt-artifact-query-history-join]
sources: ["How to add observability to your dbt deployment - Show and Tell.md", "Observability within dbt.md"]
---
# Snapcommerce

Snapcommerce is a mobile commerce company that has driven nearly a billion dollars in sales through its platform, starting with hotel bookings and consumer goods. The platform is designed to maximize savings, benefits, and rewards for shoppers.

The company's data platform team, led by [[Jonathan Talmi]] and [[Kevin Chan]], built a pioneering artifact-based observability system for dbt, presented at Coalesce 2021. This system, also described in [[How to add observability to your dbt deployment - Show and Tell]], provides comprehensive observability into dbt pipelines without relying on external monitoring tools. It leverages dbt artifacts, Airflow orchestration, Snowflake query history, Looker dashboards, and Slack alerts to monitor model runs, tests, and performance, establishing a foundational approach for dbt observability within the company.