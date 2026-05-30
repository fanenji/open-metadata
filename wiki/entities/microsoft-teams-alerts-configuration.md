---
type: entity
title: Microsoft Teams Alerts Configuration
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, microsoft-teams, alerts, configuration, webhooks]
related: [microsoft-teams, workflow-webhooks, adaptive-cards, data-observability-alerts, system-governance-notifications]
sources: ["microsoft-teams-alerts-configuration-openmetadata--20260514.md"]
---

# Microsoft Teams Alerts Configuration

This page documents the complete workflow for configuring Microsoft Teams as a destination for OpenMetadata alerts and notifications. It covers both the Teams-side webhook creation and the OpenMetadata-side destination setup.

## Prerequisites

- OpenMetadata v1.12.0 or later
- Access to Microsoft Teams with permission to create Workflows
- A Teams channel or chat where alerts will be posted

## Important Migration Notice

Microsoft has deprecated the legacy Office 365 Connector in favor of [[workflow-webhooks]]. If you previously saved an Office 365 Connector URL, you must replace it with a new Workflow Webhook URL. No code changes are required — OpenMetadata v1.12.x already sends the correct [[adaptive-cards]] format.

## Step 1: Create a Workflow Webhook in Microsoft Teams

1. Navigate to the channel or chat where you want alerts to be posted
2. Click **More options (...)** and select **Workflows**
3. Search and select the **"Send webhook alerts to a channel"** pre-configured template
4. Enter a **Name** for the workflow (e.g., "OpenMetadata Alerts")
5. Optionally add a **Description**
6. Review authentication settings (defaults are typically fine)
7. Click **Next**
8. Select your **Team**, **Channel**, or **Chat** destination
9. Click **Add workflow**
10. Copy the **HTTP POST URL** from the confirmation dialog

To retrieve the URL later: Open the Workflows app → Find your workflow → Edit → Expand "When a Teams webhook request is received" → Copy the HTTP POST URL.

## Step 2: Configure Microsoft Teams in OpenMetadata

1. Navigate to **Alerts & Notifications** from the main menu
2. Select the alert type:
   - [[data-observability-alerts]] (for data quality and pipeline monitoring)
   - [[system-governance-notifications]] (for metadata and governance events)
3. Click **Add Destination**
4. Select **Microsoft Teams** from the destination options
5. Paste your Workflow Webhook URL into the **MS Teams Destination (HTTP POST URL)** field
6. Optionally enter a **Display Name** (e.g., "Data Quality Alerts")

## Step 3: Test the Connection

Click **Test Connection** to verify the webhook is working. A test message will be sent to your Teams channel as an Adaptive Card. If successful, you'll see a confirmation message in OpenMetadata.

## Step 4: Save and Enable

Click **Save** to store the configuration. The Microsoft Teams destination is now ready to receive alerts.

## Best Practices

- **Dedicated Channels**: Create separate Teams channels for different alert types (e.g., #data-quality-alerts, #pipeline-failures, #governance-events)
- **Channel Members**: Ensure all relevant team members are added to the Teams channel
- **Multiple Webhooks**: Configure multiple Workflow Webhooks to send different alert types to different channels
- **Workflow Testing**: Always test your Workflow webhook in a non-production channel first
- **Notifications**: Enable notifications for the channel so team members don't miss important alerts

## Migration Guide: From Office 365 Connector to Workflow Webhook

1. Create a new Workflow Webhook following the setup steps above
2. Copy the new Webhook URL from the Workflow
3. Update OpenMetadata with the new Workflow Webhook URL
4. Test the configuration in a test channel first
5. Delete the old Office 365 Connector from Microsoft Teams once the new Workflow is working

No code changes are required — only the webhook URL needs to be updated.