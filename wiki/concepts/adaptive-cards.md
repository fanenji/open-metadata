---
type: concept
title: Adaptive Cards
created: 2026-05-14
updated: 2026-05-14
tags: [microsoft-teams, message-format, notifications, alerts]
related: [microsoft-teams, workflow-webhooks, microsoft-teams-alerts-configuration, data-observability-alerts]
sources: ["microsoft-teams-alerts-configuration-openmetadata--20260514.md"]
---

# Adaptive Cards

Adaptive Cards are the message format that OpenMetadata uses for Microsoft Teams notifications. They are a platform-agnostic card format defined by Microsoft that allows rich, interactive content to be rendered natively in Teams channels.

## Role in OpenMetadata Integration

OpenMetadata v1.12.x sends alert messages to Microsoft Teams in Adaptive Cards format. This is the native format expected by [[workflow-webhooks]], the current Microsoft mechanism for receiving external alerts. The test connection feature in OpenMetadata sends a test Adaptive Card to verify the webhook is working.

## Key Characteristics

- **Platform-agnostic**: Defined by Microsoft but designed to work across multiple platforms
- **Rich content**: Supports structured layouts, images, actions, and dynamic content
- **Native Teams support**: Rendered natively in Teams channels without additional processing
- **No code changes required**: OpenMetadata v1.12.x already sends the correct Adaptive Cards format

## Related Concepts

- [[workflow-webhooks]] — The mechanism that receives Adaptive Cards in Teams
- [[microsoft-teams-alerts-configuration]] — Configuration workflow for Teams alerts
- [[data-observability-alerts]] — Alert type that uses Adaptive Cards for Teams delivery