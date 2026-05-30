---
type: source
title: "Slack Alerts Configuration Openmetadata   Openmeta 20260514"
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
title: Slack Alerts Configuration | OpenMetadata
created: 2026-05-14
updated: 2026-05-14
tags: [alerts, notifications, slack, webhooks, data-observability]
related: [data-observability-alerts, alert-destinations, slack-alerts-configuration, system-governance-notifications]
sources: ["slack-alerts-configuration-openmetadata---openmeta-20260514.md"]
---

# Slack Alerts Configuration | OpenMetadata

**Source**: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/alerts-notifications/slack-alerts-configuration

This official OpenMetadata v1.12.x documentation page provides a step-by-step guide for configuring Slack alerts using Incoming Webhooks. It covers the two-phase setup process: creating a Slack webhook via the Slack API, and configuring the webhook as an alert destination within OpenMetadata. The guide includes best practices for channel management and multiple webhook configurations.

## Key Content

- **Slack Webhook Setup**: Steps to create a Slack app, enable Incoming Webhooks, and obtain the webhook URL.
- **OpenMetadata Configuration**: How to add Slack as a destination for [[data-observability-alerts]] or [[system-governance-notifications]].
- **Test Connection**: Verification step that sends a test message to validate the webhook.
- **Best Practices**: Dedicated channels, channel permissions, multiple webhooks for different alert types.

## Connections

- Extends [[data-observability-alerts]] with a concrete destination implementation.
- Related to [[alert-destinations]] as one of several supported notification targets.
- Complements [[system-governance-notifications]] for metadata and governance event alerts.