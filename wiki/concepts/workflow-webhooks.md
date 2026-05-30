---
type: concept
title: Workflow Webhooks
created: 2026-05-14
updated: 2026-05-14
tags: [microsoft-teams, webhooks, notifications, alerts]
related: [microsoft-teams, microsoft-teams-alerts-configuration, adaptive-cards, data-observability-alerts, system-governance-notifications]
sources: ["microsoft-teams-alerts-configuration-openmetadata--20260514.md"]
---

# Workflow Webhooks

Workflow Webhooks are the current Microsoft mechanism for receiving external alerts into Microsoft Teams channels. They replace the deprecated Office 365 Connector and are the required configuration path for OpenMetadata v1.12.x.

## Overview

Workflow Webhooks use pre-configured templates provided by Microsoft to create incoming webhooks that can receive HTTP POST requests from external systems like [[openmetadata]]. OpenMetadata sends alert messages in [[adaptive-cards]] format, which is natively supported by Teams Workflow Webhooks.

## Setup Process

1. Access the Workflows app from a Teams channel or chat
2. Select the "Send webhook alerts to a channel" pre-configured template
3. Name and configure the workflow
4. Select the destination (Team, Channel, or Chat)
5. Copy the generated HTTP POST URL

## Key Characteristics

- **No code changes required**: OpenMetadata v1.12.x already sends the correct Adaptive Cards format
- **URL-based configuration**: The webhook URL is the only configuration needed in OpenMetadata
- **Testable**: The test connection feature in OpenMetadata verifies the webhook is working
- **Retrievable**: Webhook URLs can be retrieved later from the Workflows app

## Migration from Office 365 Connector

Microsoft has deprecated the Office 365 Connector. Users must:
1. Create a new Workflow Webhook
2. Copy the new webhook URL
3. Update OpenMetadata with the new URL
4. Test the configuration
5. Delete the old Office 365 Connector

## Related Concepts

- [[microsoft-teams-alerts-configuration]] — Complete configuration workflow
- [[adaptive-cards]] — Message format used by OpenMetadata
- [[data-observability-alerts]] — Alert type that can use Workflow Webhooks