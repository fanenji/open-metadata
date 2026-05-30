---
type: concept
title: Webhook-based Alert Delivery
created: 2026-05-14
updated: 2026-05-14
tags: [alerts, notifications, webhook, integration]
related: [google-chat-webhook, google-chat-alerts-configuration, data-observability-alerts, system-governance-notifications]
sources: ["google-chat-alerts-configuration-openmetadata---op-20260514.md"]
---
# Webhook-based Alert Delivery

Webhook-based alert delivery is a method by which OpenMetadata sends real-time notifications to external messaging platforms, such as Google Chat, Slack, or Microsoft Teams, by posting messages to a configured webhook URL. This approach enables teams to receive alerts directly in their collaboration tools without requiring custom integrations or polling.

## How It Works

1. A webhook URL is created in the target platform (e.g., Google Chat Space).
2. The URL is configured as a destination in OpenMetadata's alert system.
3. When an alert is triggered (e.g., a data quality test fails, a pipeline errors, a governance event occurs), OpenMetadata sends an HTTP POST request to the webhook URL with the alert payload.
4. The target platform receives the request and displays the message in the designated space or channel.

## Key Features

- **Real-time Delivery**: Alerts are delivered immediately upon trigger.
- **Test Connection**: OpenMetadata provides a test connection mechanism that sends a test message to verify the webhook configuration works before saving.
- **Multiple Destinations**: Multiple webhooks can be configured for different alert types, sending notifications to different spaces or channels.

## Supported Platforms

- Google Chat (via [[google-chat-webhook]])
- Slack
- Microsoft Teams
- Generic Webhook

## Best Practices

- Use dedicated spaces/channels for different alert types to reduce noise.
- Ensure all relevant team members have access to the notification space.
- Regularly monitor alert delivery to confirm the webhook is functioning.
- Enable notifications for the space so team members are alerted.

## Related

- [[google-chat-alerts-configuration]] — Step-by-step guide for Google Chat webhook setup.
- [[data-observability-alerts]] — Alert type for data quality and pipeline monitoring.
- [[system-governance-notifications]] — Alert type for metadata and governance events.