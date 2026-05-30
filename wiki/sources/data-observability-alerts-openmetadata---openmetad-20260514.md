---
type: source
title: "Data Observability Alerts Openmetadata   Openmetad 20260514"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
authors: []
year: 2026
url: ""
venue: ""
---

type: source
title: "Data Observability Alerts | OpenMetadata"
created: 2026-05-14
updated: 2026-05-14
tags: [data-observability, alerts, notifications, openmetadata]
related: [data-observability-alerts, data-quality, data-profiling, data-lineage, change-events-system, teams-and-users, data-asset-ownership, bot-authentication]
sources: ["data-observability-alerts-openmetadata---openmetad-20260514.md"]
---

# Data Observability Alerts | OpenMetadata

**Source:** Official OpenMetadata documentation (v1.12.x) for the Data Observability Alerts feature.

## Summary

This source provides a detailed procedural guide for configuring data observability alerts in OpenMetadata. It covers the complete workflow: opening the Alerts page, naming the alert, selecting a source entity (Container, Ingestion Pipeline, Pipeline, Table, Test Case, Test Suite, Topic), configuring optional filters (Entity Specific Name, Owner Name, Domain, Updater Is Bot) with Include/Exclude logic, selecting trigger conditions (Schema Changes, Test Case Status, Pipeline Status, Metric Updates), and choosing internal (Admins, Followers, Owners, Teams, Users) or external (Email, Slack, MS Teams, Google Chat, Generic Webhooks) destinations.

## Key Contributions

- **Detailed procedural steps** for creating alerts, filling gaps in the existing wiki stub.
- **Filter configuration** with Include/Exclude toggle and specific filter criteria (Entity Specific Name, Owner Name, Domain, Updater Is Bot).
- **Trigger conditions** enumeration: Schema Changes, Test Case Status, Pipeline Status, Metric Updates.
- **Test Suite grouping** as a best practice to reduce notification fatigue.
- **Internal vs. external destination** distinction.

## Connections

- Strengthens [[data-observability-alerts]] with concrete procedural content.
- Extends [[data-quality]], [[data-profiling]], [[data-lineage]] by documenting the alerting consumption mechanism.
- Related to [[change-events-system]] (alerts are likely powered by change events).
- Related to [[teams-and-users]], [[data-asset-ownership]], [[bot-authentication]] (destinations and filters reference these entities).