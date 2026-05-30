---
type: source
title: "Microsoft Teams Alerts Configuration Openmetadata  20260514"
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
title: Microsoft Teams Alerts Configuration | OpenMetadata
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, microsoft-teams, alerts, notifications, webhooks]
related: [microsoft-teams-alerts-configuration, data-observability-alerts, system-governance-notifications, adaptive-cards, workflow-webhooks]
sources: ["microsoft-teams-alerts-configuration-openmetadata--20260514.md"]
---

# Microsoft Teams Alerts Configuration | OpenMetadata

This source is the official OpenMetadata v1.12.x documentation for configuring Microsoft Teams as a destination for alerts and notifications. It covers the complete setup workflow, including creating a Workflow Webhook in Microsoft Teams, configuring the destination in OpenMetadata, testing the connection, and migrating from the deprecated Office 365 Connector.

## Key Content

- **Migration Notice**: Microsoft has deprecated the Office 365 Connector in favor of Workflow Webhooks. OpenMetadata v1.12.x requires no code changes, but existing Office 365 Connector URLs must be replaced.
- **Workflow Webhook Setup**: Step-by-step instructions for creating an incoming webhook in Microsoft Teams using pre-configured templates.
- **OpenMetadata Configuration**: Steps to add Microsoft Teams as a destination for [[data-observability-alerts]] and [[system-governance-notifications]], including URL pasting, display naming, and connection testing.
- **Adaptive Cards**: OpenMetadata sends alert messages in Adaptive Cards format, which is the native format for Teams Workflow Webhooks.
- **Best Practices**: Dedicated channels for different alert types, testing in non-production channels, and enabling notifications.
- **Migration Guide**: Procedure for transitioning from Office 365 Connector to Workflow Webhook URLs.

## Relevance

This source provides the concrete implementation details for one of the supported destinations in the [[data-observability-alerts]] system. It fills a gap in the wiki by documenting the Microsoft Teams-specific configuration, complementing the existing generic alert destination documentation.