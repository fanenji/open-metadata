---
type: concept
title: System & Governance Notifications
created: 2026-05-14
updated: 2026-05-14
tags: ["notifications", "governance", "alerts", "metadata", "events", "system-events", "openmetadata"]
related: ["data-observability-alerts", "data-asset-ownership", "teams-and-users", "announcements", "glossary-terms", "classification-tags", "hybrid-rbac-abac-model", "alert-destinations", "slack-alerts-configuration", "microsoft-teams", "workflow-webhooks", "microsoft-teams-alerts-configuration", "google-chat-alerts-configuration", "webhook-based-alert-delivery", "google-chat-webhook"]
sources: ["system-governance-notifications-openmetadata---ope-20260514.md", "slack-alerts-configuration-openmetadata---openmeta-20260514.md", "microsoft-teams-alerts-configuration-openmetadata--20260514.md", "google-chat-alerts-configuration-openmetadata---op-20260514.md"]
---
# System & Governance Notifications

System & Governance Notifications are an alert type in OpenMetadata that notify users about metadata and governance events. These notifications complement [[data-observability-alerts]] by covering platform-level and governance-related changes rather than data quality or pipeline monitoring.

## Event Types

System & Governance Notifications typically cover events such as:

- **Metadata Changes**: Additions, updates, or deletions of data assets (tables, topics, pipelines, etc.).
- **Governance Events**: Changes to glossary terms, classification tags, ownership, or team structure.
- **Schema Changes**: Alterations to table schemas or column definitions.
- **Policy and Role Changes**: Modifications to access control policies or user roles.

## Configuration

System & Governance Notifications can be configured to deliver alerts to various destinations, including:

- Email
- Slack
- Microsoft Teams
- [[google-chat-webhook|Google Chat Webhook]]
- Generic Webhook

The configuration process follows the same pattern as [[data-observability-alerts]]: select the alert type, add a destination, configure the webhook URL, test the connection, and save.

## Related

- [[data-observability-alerts]] — The companion alert type for data quality and pipeline monitoring.
- [[google-chat-alerts-configuration]] — Step-by-step guide for configuring Google Chat as a destination.
- [[webhook-based-alert-delivery]] — The delivery mechanism used for webhook destinations.