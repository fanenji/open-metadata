---
type: concept
title: Data Observability Alerts and Notifications
created: 2026-05-14
updated: 2026-05-15
tags:
  - administration
  - observability
  - alerts
  - notifications
  - data-quality
  - schema-changes
  - pipeline-failures
  - data-observability
  - monitoring
related: ["openmetadata-administration", "data-quality", "data-lineage", "ingestion-framework", "data-profiling", "change-events-system", "teams-and-users", "data-asset-ownership", "bot-authentication", "data-observability-alerts-openmetadata---openmetad-20260514"]sources:
  - admin-guide-openmetadata-administration-documentat-20260514.md
  - data-observability-alerts-openmetadata---openmetad-20260514.md
---

# Data Observability Alerts and Notifications

Data Observability Alerts in OpenMetadata provide fine-grained, configurable notifications for monitoring the health of data systems. They cover pipeline failures, data quality issues, schema changes, and metric updates, keeping teams informed about important events in the data estate and enabling them to respond proactively to data incidents.

## Alert Configuration Workflow

The complete workflow for creating an alert is:

1. **Open the Alerts Page** — Navigate to Observability > Alerts and click Add Alert.
2. **Name the Alert** — Provide a unique, descriptive name and optional description.
3. **Select a Source** — Choose the operational entity to monitor (see [Sources](#sources) below).
4. **Configure Filters (Optional)** — Refine the alert scope using filter criteria with Include/Exclude logic.
5. **Select Trigger Conditions (Optional)** — Define specific events that fire the alert.
6. **Choose a Destination** — Select internal or external notification channels.

This workflow is part of the broader **Services and Notifications** administrative capability.

## Sources

The following operational entities can be monitored:

- **Container** — Schema changes for the container asset.
- **Ingestion Pipeline** — Status changes to OpenMetadata ingestion pipelines.
- **Pipeline** — Updates to ingested pipeline assets.
- **Table** — Schema changes and table metric updates.
- **Test Case** — Alerts for a specific test case.
- **Test Suite** — Alerts for any test case event linked to the test suite. Grouping alerts by Test Suite is recommended to reduce notification fatigue.
- **Topic** — Schema changes for the topic asset.

## Filters

Filters refine the alert scope to improve signal-to-noise ratio by narrowing events based on specific criteria. Available filter criteria:

- **Entity Specific Name** — Filter by the defined specific name of the entity.
- **Owner Name** — Filter events based on the designated owner of the asset.
- **Domain** — Filter events based on the Data Domain the entity belongs to.
- **Filter By Updater Is Bot** — Include or exclude changes made by automated ingestion or system processes.

Each filter uses an **Include/Exclude toggle**:

- **Include (Toggle ON)** — If the event meets the filter condition, the alert is sent.
- **Exclude (Toggle OFF)** — If the event meets the filter condition, the alert is silenced.

If no filters are set, the alert applies to all relevant events over the selected source entity type, which may lead to excessive notifications.

## Trigger Conditions

Define the specific events that trigger the alert:

- **Schema Changes** — Notifications when table or dataset schemas are modified (added, deleted, or updated columns).
- **Pipeline Status** — Alert when pipeline execution is Failed or Pending.
- **Test Case Status** — Notifications when [[data-quality|Data Quality]] tests fail or thresholds are breached (triggered when tests are Failed, Aborted, or Queued).
- **Metric Updates** — Notify when table metrics are updated.

Multiple trigger conditions can be selected for comprehensive monitoring coverage.

## Destinations

Alerts can be sent to internal or external notification channels.

**Internal Destinations:**
- **Admins** — Notify all platform administrators.
- **Followers** — Notify users following the asset.
- **Owners** — Alert the asset owners.
- **Teams or Specific Users** — Target specific teams or individuals.

**External Destinations:**
- **Email**
- **Chat** — Slack, MS Teams, Google Chat
- **Automation** — Generic Webhooks

## Best Practices

- Use **Test Suite** as the source to group alerts and reduce notification fatigue.
- Configure **filters** to narrow the alert scope and improve signal-to-noise ratio.
- Use the **Filter By Updater Is Bot** option to exclude automated changes from triggering alerts.
- Select **multiple trigger conditions** for comprehensive monitoring coverage.

## Open Questions

- How does the alerting system interact with the [[change-events-system]]? Is there a direct pipeline from change events to alert evaluation? This is not covered in the source.
- Is there support for alert severity levels and escalation policies? Not covered in the source.