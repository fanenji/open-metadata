---
type: concept
title: dbt Domain Alerting Pattern
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, alerting, observability, slack]
related: [dbt-observability-implementation, dbt-artifact-query-history-join, dbt-artifacts]
sources: ["Observability within dbt.md"]
---
# dbt Domain Alerting Pattern

The dbt Domain Alerting Pattern is a method for sending targeted notifications to model owners based on domain-specific tags, rather than alerting the entire data team or company.

## Implementation

1. **Domain Tagging**: Every dbt model is assigned exactly one domain tag (e.g., `growth`, `finance`, `catalog`).
2. **Dashboard Filtering**: Looker dashboards are filtered by domain tag to show only relevant model and test results.
3. **Slack User Groups**: Slack user groups are created per domain (e.g., `@growth-team`, `@finance-team`).
4. **Alert Trigger**: When a model's status changes to "failed" within a 15-minute window, a Slack alert is sent tagging the relevant user group.

## Benefits

- Reduces alert fatigue by notifying only the responsible team.
- Enables domain ownership of data quality.
- Scales with organizational growth — new domains simply add new tags and user groups.
- Works with any BI tool that supports alerting (Looker, Metabase, etc.).

## Relationship to Other Patterns

This pattern was developed as part of the [[dbt-observability-implementation]] at [[Snapcommerce]] and relies on the [[dbt-artifact-query-history-join]] for the underlying data. It is a practical application of [[data-domain-governance]] principles at the alerting level.