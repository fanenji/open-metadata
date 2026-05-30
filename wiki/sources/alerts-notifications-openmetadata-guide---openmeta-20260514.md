---
type: source
title: "Source: alerts-notifications-openmetadata-guide---openmeta-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["alerts-notifications-openmetadata-guide---openmeta-20260514.md"]
tags: []
related: []
---

# Source: alerts-notifications-openmetadata-guide---openmeta-20260514.md

## Analysis of: Alerts & Notifications | OpenMetadata Guide

### Key Entities

- **EventSubscription entity** — Central entity for configuring alerts; requires `Create` permission. Likely already exists in wiki implicitly but not as a dedicated page.
- **OpenMetadata (platform)** — The system providing the alerting framework. Already exists in wiki.
- **Slack, Microsoft Teams, Google Chat, Email, Generic Webhook** — External notification destinations. Not yet documented as dedicated pages in the wiki.

### Key Concepts

- **Data Observability Alerts** — Alerts for monitoring data system health (pipeline failures, data quality, schema changes). Not yet a dedicated wiki page.
- **System & Governance Notifications** — Alerts for metadata changes and collaboration events (glossary terms, tags, ownership). Not yet a dedicated wiki page.
- **Unified Event Subscription Framework** — The underlying architecture that supports both observability and governance alerts with a similar configuration workflow. Not yet documented.
- **Fine-grained alerting** — Ability to filter by Test Suite, Pipeline Status, Ingestion Pipeline, and Metadata Change types. Not yet documented.

### Main Arguments & Findings

- **Core claim:** OpenMetadata provides a revamped (since v1.3) unified alerting framework for both data observability and governance notifications.
- **Evidence:** Official documentation describing two main alert categories, required permissions, and external destination support.
- **Strength:** Official documentation from the project; high reliability.

### Connections to Existing Wiki

- **Directly related to:** [[data-observability-alerts]] — This source provides the broader context and framework that the existing page covers partially.
- **Related to:** [[announcements]] — Alerts can send announcements via email/Slack/Teams.
- **Related to:** [[openmetadata-administration]] — Alert configuration is an administrative capability.
- **Related to:** [[activity-feed]] — Mentions in tasks/activity feed trigger alerts.

### Contradictions & Tensions

- **No contradictions** with existing wiki content. The existing [[data-observability-alerts]] page is a brief overview; this source provides more structured detail.
- **Internal tension:** The documentation distinguishes between "Data Observability Alerts" and "System & Governance Notifications" but notes they share the same configuration workflow — this could cause confusion about when to use which.

### Recommendations

**Pages to create:**
1. **[[event-subscription-framework]]** — Document the unified Event Subscription framework, the two alert categories, and the shared configuration workflow.
2. **[[system-governance-notifications]]** — Document the second alert category (metadata changes, governance events) which is currently missing from the wiki.
3. **[[alert-destinations]]** — Consolidate configuration guides for all five external destinations (Email, Slack, Teams, Google Chat, Generic Webhook) into a sing
