---
type: source
title: Google Chat Alerts Configuration | OpenMetadata
created: 2026-05-14
updated: 2026-05-14
tags: [alerts, notifications, google-chat, webhook, configuration]
related: [data-observability-alerts, system-governance-notifications, google-chat-webhook, webhook-based-alert-delivery]
sources: ["google-chat-alerts-configuration-openmetadata---op-20260514.md"]
authors: []
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/alerts-notifications/google-chat-alerts-configuration"
venue: "OpenMetadata Documentation"
---
# Google Chat Alerts Configuration | OpenMetadata

This official OpenMetadata documentation page (v1.12.x) provides a step-by-step guide for configuring Google Chat webhook alerts. It covers creating a webhook in a Google Chat Space, configuring the webhook URL in OpenMetadata, testing the connection, and saving the alert configuration. The guide also includes best practices for dedicated Spaces, team member inclusion, and multiple webhook usage.

## Key Content

- **Webhook Creation**: Steps to create a webhook in a Google Chat Space via Space Settings > Apps & Integrations.
- **OpenMetadata Configuration**: Adding Google Chat as a destination for Data Observability Alerts or System & Governance Notifications.
- **Test Connection**: A verification mechanism that sends a test message to the Google Chat Space to confirm the configuration works before saving.
- **Best Practices**: Dedicated Spaces for different alert types, adding relevant team members, enabling notifications, and regular monitoring.

## Connections

- Extends [[data-observability-alerts]] with a specific destination configuration.
- Complements [[system-governance-notifications]] as a delivery channel.
- References the [[google-chat-webhook]] integration mechanism.
- Relates to the broader [[webhook-based-alert-delivery]] concept.