---
type: entity
title: Google Chat Webhook
created: 2026-05-14
updated: 2026-05-14
tags: [google-chat, webhook, integration, alerts]
related: [google-chat-alerts-configuration, data-observability-alerts, system-governance-notifications, webhook-based-alert-delivery]
sources: ["google-chat-alerts-configuration-openmetadata---op-20260514.md"]
---
# Google Chat Webhook

A Google Chat Webhook is an integration mechanism that allows external services, such as OpenMetadata, to send messages directly into a Google Chat Space. The webhook is configured with a unique URL that acts as the endpoint for message delivery.

## Configuration

1. **Create a Webhook**: In Google Chat, navigate to Space Settings > Apps & Integrations > Add Webhooks. Provide a name and optional avatar.
2. **Copy the Webhook URL**: The URL follows the format `https://chat.googleapis.com/v1/spaces/XXXXXXXXXXXXXXX/messages?key=...&token=...`.
3. **Configure in OpenMetadata**: Paste the webhook URL into the Google Chat Webhook URL field when adding a destination for [[data-observability-alerts]] or [[system-governance-notifications]].

## Best Practices

- **Dedicated Spaces**: Create separate Google Chat Spaces for different alert types (e.g., "Data Quality Alerts", "Pipeline Failures", "Governance Events").
- **Space Members**: Ensure all relevant team members are added to the Google Chat Space.
- **Multiple Webhooks**: Configure multiple webhooks to send different alert types to different Spaces.
- **Notifications**: Enable notifications for the Space so team members don't miss important alerts.

## Related

- [[google-chat-alerts-configuration]] — Step-by-step guide for setting up Google Chat alerts in OpenMetadata.
- [[webhook-based-alert-delivery]] — The broader concept of delivering alerts via webhooks.
- [[data-observability-alerts]] — Alert type for data quality and pipeline monitoring.
- [[system-governance-notifications]] — Alert type for metadata and governance events.