---
type: entity
title: Slack Alerts Configuration
created: 2026-05-14
updated: 2026-05-14
tags: [slack, alerts, notifications, webhooks, integration]
related: [data-observability-alerts, alert-destinations, system-governance-notifications, slack]
sources: ["slack-alerts-configuration-openmetadata---openmeta-20260514.md"]
---

# Slack Alerts Configuration

The Slack Alerts Configuration is the concrete implementation of [[alert-destinations]] for the Slack messaging platform. It enables OpenMetadata to send real-time notifications to Slack channels via Incoming Webhooks, covering both [[data-observability-alerts]] (data quality and pipeline monitoring) and [[system-governance-notifications]] (metadata and governance events).

## Setup Workflow

The configuration follows a two-phase setup pattern common to all webhook-based destinations:

1. **Slack-side setup**: Create a Slack app via the Slack API, enable Incoming Webhooks, and generate a webhook URL.
2. **OpenMetadata-side setup**: Navigate to Alerts & Notifications, add Slack as a destination, paste the webhook URL, test the connection, and save.

## Best Practices

- Use dedicated Slack channels for different alert types (e.g., `#data-quality-alerts`, `#pipeline-failures`).
- Ensure channel permissions allow access to all relevant team members.
- Configure multiple webhooks to route different alert types to different channels.
- Regularly monitor channels to verify alert delivery.

## Limitations

- No documented rate limits or retry logic for failed webhook deliveries.
- Webhook URL rotation or expiration handling is not covered.
- Test Connection verifies connectivity but does not guarantee long-term delivery.