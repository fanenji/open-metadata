---
type: concept
title: dbt Deployment Tag System
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, tagging, orchestration, airflow]
related: [dbt-observability-implementation, dbt-domain-tag-alerting, dbt-artifact-upload-macro]
sources: ["How to add observability to your dbt deployment - Show and Tell.md"]
---
# dbt Deployment Tag System

A tagging convention used at Snapcommerce to assign every dbt model to exactly one pipeline: hourly, nightly, or external. This enables clear pipeline assignment and prevents duplication between scheduled and external pipelines.

## Tag Categories

- **tag:hourly** — Models that run every hour
- **tag:nightly** — Models that run once per night
- **tag:external** — Models managed by external pipelines (e.g., triggered by data loads from partners)

## Intersection Selectors

To avoid duplication between scheduled and external pipelines, intersection selectors are used. For example, an external pipeline runs models at the intersection of a source's downstream models and `tag:external`:
```
dbt run -s source.myreport+, tag:external
```

## Context

This system was part of the [[dbt-observability-implementation]] at Snapcommerce, orchestrated via Airflow with KubernetesPodOperator. It requires manual tagging discipline but provides clear pipeline ownership and prevents conflicts.