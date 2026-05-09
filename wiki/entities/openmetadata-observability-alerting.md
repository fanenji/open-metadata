---
type: entity
title: OpenMetadata Observability and Alerting
created: 2026-04-05
updated: 2026-04-05
tags: [openmetadata, observability, alerting, anomaly-detection, incident-management]
related: [openmetadata, openmetadata-data-quality, openmetadata-data-quality-tests, data-observability-definition, data-incident-management, data-quality-resolution-workflow]
sources: ["OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md"]
---
# OpenMetadata Observability and Alerting

OpenMetadata provides built-in observability features including profiling, anomaly detection, alerts, and incident management.

## Data Profiler

Computes and tracks metrics over time for every table:
- Row count (with historical trend)
- Null counts per column
- Unique value counts
- Min, max, mean, standard deviation
- Value distributions

Provides a baseline and enables anomaly detection.

## Anomaly Detection

Uses profiler history to automatically detect:
- Unexpected row count changes
- Sudden increases in null values
- Schema drift (new or removed columns)
- Data freshness violations

## Alerts and Notifications

Configure alerts that fire when:
- A test fails
- An asset is updated or deleted
- A quality metric crosses a threshold
- A pipeline fails

**Destinations:** Slack, Teams, Email, Webhook.

**Example Alert Config:**
```yaml
name: "Quality Alert"
alertType: Observability
filteringRules:
  resources:
    - "table"
  filters:
    - name: "TestResult"
      effect: include
      condition: "FAILED"
destinations:
  - type: Slack
    config:
      webhookUrl: "${SLACK_WEBHOOK_URL}"
```

## Incident Management

When data quality degrades, OpenMetadata tracks it as an incident:
- Incident created when test fails
- Assigned to an owner
- Status tracked: Open → In Progress → Resolved
- Timeline of when issue appeared and was fixed
- Linked to affected downstream assets