---
type: entity
title: Microsoft Teams
created: 2026-05-14
updated: 2026-05-14
tags: [microsoft, collaboration, notifications, alerts]
related: [openmetadata, data-observability-alerts, workflow-webhooks, adaptive-cards, system-governance-notifications]
sources: ["microsoft-teams-alerts-configuration-openmetadata--20260514.md"]
---

# Microsoft Teams

Microsoft Teams is a collaboration platform that serves as a notification destination for [[openmetadata]] alerts. OpenMetadata integrates with Microsoft Teams using Workflow Webhooks to deliver alert messages directly to Teams channels, enabling real-time notifications for data quality, pipeline monitoring, and governance events.

## Integration with OpenMetadata

OpenMetadata v1.12.x sends alerts to Microsoft Teams via Workflow Webhooks using the [[adaptive-cards]] message format. The integration requires no code changes from the previous Office 365 Connector approach — only the webhook URL needs to be updated.

### Supported Alert Types

- [[data-observability-alerts]] — For data quality and pipeline monitoring events
- [[system-governance-notifications]] — For metadata and governance events

### Configuration

The configuration involves two main steps:
1. Creating a Workflow Webhook in Microsoft Teams using pre-configured templates
2. Adding Microsoft Teams as a destination in OpenMetadata's alert configuration

See [[microsoft-teams-alerts-configuration]] for the complete setup workflow.

## Migration from Office 365 Connector

Microsoft has deprecated the legacy Office 365 Connector in favor of Workflow Webhooks. Users with existing Office 365 Connector URLs must replace them with new Workflow Webhook URLs. No code changes are required in OpenMetadata.