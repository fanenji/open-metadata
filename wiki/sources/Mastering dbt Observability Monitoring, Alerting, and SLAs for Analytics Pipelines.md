---
type: source
title: "Source: Mastering dbt Observability Monitoring, Alerting, and SLAs for Analytics Pipelines.md"
created: 2026-05-07
updated: 2026-05-07
sources: ["Mastering dbt Observability Monitoring, Alerting, and SLAs for Analytics Pipelines.md"]
tags: []
related: []
---

# Source: Mastering dbt Observability Monitoring, Alerting, and SLAs for Analytics Pipelines.md

## Key Entities

- **[[abhishek-kumar-gupta]]** (Author) — Central. Already exists in wiki.
- **dbt Cloud** (Platform) — Central. Already exists in wiki.
- **Metaplane** (External Observability Tool) — Peripheral. Not in wiki.
- **Databand, Bigeye, Monte Carlo, Elastic Observability** (External Observability Tools) — Peripheral. Not in wiki.
- **Datadog, Prometheus, PagerDuty** (External Monitoring/Alerting Tools) — Peripheral. Not in wiki.
- **Looker, Tableau, Power BI** (BI Tools) — Peripheral. Not in wiki.
- **dbt Labs** (Organization) — Peripheral. Already exists in wiki.

## Key Concepts

- **[[dbt-observability-implementation]]** — Pattern for monitoring dbt runs, tests, and freshness using artifacts and structured models. Central to the source. Already exists in wiki.
- **[[dbt-artifacts]]** — JSON files (`run_results.json`, `manifest.json`, `sources.json`) produced by dbt runs, forming the foundation for custom observability. Central. Already exists in wiki.
- **[[data-contract-observability]]** — Dashboard patterns for tracking SLA/SLO compliance. Central. Already exists in wiki.
- **[[data-observability-definition]]** — The three core questions: Are jobs running? Is data correct and fresh? Can failures be seen and fixed fast? Central. Already exists in wiki.
- **[[dbt-cloud-webhooks]]** — Native dbt Cloud job notifications for success/failure/warnings. Peripheral. Already exists in wiki.
- **[[data-incident-management]]** — On-call playbook: alert → dashboard check → artifact inspection → impact assessment → communication → fix. Peripheral. Already exists in wiki.
- **[[dbt-source-freshness]]** — YAML-based freshness checks with `warn_after` and `error_after` thresholds. Central. Not explicitly in wiki as a standalone concept, but related to [[data-quality-dimensions]].
- **[[data-sla]]** — Service Level Agreements for data timeliness, success rate, and latency. Central. Not in wiki.
- **[[data-slo]]** — Measurable targets (e.g., "99% of runs succeed on time"). Central. Not in wiki.

## Main Arguments & Findings

- **Core Claim:** dbt observability transforms a collection of models into a reliable data product with measurable SLAs/SLOs.
- **Evidence:** The article provides a step-by-step pattern: capture artifacts → land in warehouse → model into structured tables → build dashboards → define SLAs → alert → respond.
- **Evidence Strength:** Medium. The article is a practical guide with conceptual SQL examples and architectural patterns, but no empirical data or case study results.

## Connections to Existing Wiki

- **Strengthens:** [[dbt-observability-implementation]], [[dbt-artifacts]], [[data-contract-observability]], [[data-observability-definition]], [[data-incident-management]].
- **Extends:** Introduces the SLA/SLO dimension explicitly, which is currently absent from the wiki. The article frames observability as a reliability engineering practice, not just monitoring.
- **Related but not in wiki:** The concept of "data product" wi
