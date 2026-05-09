---
type: concept
title: dbt Source Freshness
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, observability, monitoring]
related: [dbt, data-observability]
sources: ["10 Game-Changing dbt Tips I Wish I Knew Before My First Production Model 1.md"]
---
# dbt Source Freshness

**dbt Source Freshness** is a monitoring mechanism used to track the latency of incoming data. It allows data engineers to detect when source tables have become stale, indicating a failure or delay in the upstream ingestion pipeline.

## Configuration

Freshness parameters are defined in the `sources.yml` file. Engineers can set thresholds for warnings and errors based on a specific time period.

```yaml
sources:
  - name: my_source
    tables:
      - name: orders
        loaded_at_field: LAST_PROMSESSED_UTC
        freshness:
          warn_after: { count: 3, period: hour }
          error_after: { count: 6, period: hour }
```

## Importance

- **Pipeline Health**: Acts as an early warning system for upstream ingestion issues.
- **Data Reliability**: Ensures that downstream models are not being built on outdated information.
- **Automated Alerting**: Integrates with orchestration tools to trigger alerts when thresholds are breached.
