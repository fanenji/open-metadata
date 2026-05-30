---
type: clip
title: "Microsoft Teams Alerts Configuration | OpenMetadata - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/alerts-notifications/microsoft-teams-alerts-configuration"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Microsoft Teams Alerts Configuration | OpenMetadata - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/alerts-notifications/microsoft-teams-alerts-configuration

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAlerts & NotificationsMicrosoft Teams Alerts Configuration | OpenMetadataHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData Quality and ObservabilityOverviewData QualityData ProfilerAlerts & NotificationsOverviewData Observability AlertsSystem & Governance NotificationsEmail Alerts ConfigurationSlack Alerts ConfigurationMicrosoft Teams Alerts ConfigurationGoogle Chat Alerts ConfigurationGeneric Webhook Alert ConfigurationIncident ManagerOn this pageMicrosoft Teams Alerts ConfigurationImportant Migration NoticeSetting Up a Microsoft Teams Workflow WebhookStep 1: Access Workflows from Your ChannelStep 2: Select the Webhook TemplateStep 3: Name and Configure the WebhookStep 4: Select the DestinationStep 5: Copy Your Webhook URLFinding Your Webhook URL LaterConfiguring Microsoft Teams Webhooks in OpenMetadataStep 1: Access Alert ConfigurationStep 2: Add Microsoft Teams as a DestinationStep 3: Test the ConnectionStep 4: Save and EnableBest PracticesMigration Guide: From Office 365 Connector to Workflow WebhookReferenceDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Microsoft Teams Alerts Configuration

OpenMetadata integrates with Microsoft Teams using Workflow Webhooks to deliver alert messages directly to your Teams channels. This allows you to receive real-time notifications within Microsoft Teams.

​Important Migration Notice

Microsoft Deprecation Update: Microsoft has deprecated the legacy Office 365 Connector approach in favor of Workflow Webhooks.If you are using OpenMetadata v1.12.0 or later:

✅ No code changes are required

✅ OpenMetadata already sends Adaptive Cards format

⚠️ Action Required: If you previously saved an Office 365 Connector URL, you must replace it with a new Workflow Webhook URL

For detailed Microsoft guidance, see: Create incoming webhooks with Workflows for Microsoft Teams

​Setting Up a Microsoft Teams Workflow Webhook

An incoming webhook allows OpenMetadata to share alert content directly in your Teams channels and chats. Follow these steps using Microsoft’s pre-configured webhook templates.

​Step 1: Access Workflows from Your Channel

In Microsoft Teams, navigate to the channel or chat where you want alerts to be posted

Click More options (…) next to the channel or chat name

Select Workflows

​Step 2: Select the Webhook Template

Microsoft provides pre-configured webhook templates. Search and select the “Send webhook alerts to a channel” pre-configured Webhook template to continue.

​Step 3: Name and Configure the Webhook

Enter a Name for the workflow (e.g., “OpenMetadata Alerts”)

Optionally, add a Description (e.g., “Receives data quality and governance alerts from OpenMetadata”)

Review the authentication settings (the defaults are typically fine)

If you need to use a different account to post messages, click Switch account

Click Next

​Step 4: Select the Destination

The workflow will ask you to specify where to post messages

Select your Team, Channel, or Chat (these fields auto-populate if you started from a specific channel)

Verify the account authentication is correct

Click Add workflow to create the workflow

​Step 5: Copy Your Webhook URL

A confirmation dialog will appear displaying your HTTP POST URL

Copy the complete URL exactly as shown (do not modify or truncate it)

Store this URL securely - you’ll paste it into OpenMetadata next

​Finding Your Webhook URL Later

If you need to retrieve your webhook URL again:

Open the Workflows app in Microsoft Teams

Find and select your OpenMetadata workflow

Click Edit

Expand When a Teams webhook request is received

Copy the HTTP POST URL displayed there

​Configuring Microsoft Teams Webhooks in OpenMetadata

Once you have your Workflow Webhook URL, follow these steps to configure it in OpenMetadata:

​Step 1: Access Alert Configuration

In OpenMetadata, navigate to Alerts & Notifications from the main menu

Select the type of alert you want to configure:

Data Observability Alerts (for data quality and pipeline monitoring)

System & Governance Notifications (for metadata and governance events)

​Step 2: Add Microsoft Teams as a Destination

Click Add Destination

Select Microsoft Teams from the available destination options

Paste your Workflow Webhook HTTP POST URL into the MS Teams Destination (HTTP POST URL) field

Optionally, enter a Display Name for this Teams destination (e.g., “Data Quality Alerts”)

​Step 3: Test the Connection

Click Test Connection to verify the webhook is working

A test message will be sent to your Teams channel

If successful, you’ll see a confirmation message and the test message will appear in your Teams channel as an Adaptive Card

​Step 4: Save and Enable

Click Save to store the configuration

The Microsoft Teams destination is now ready to receive alerts

​Best Practices

Dedicated Channels: Create separate Teams channels for different types of alerts (e.g., #data-quality-alerts, #pipeline-failures, #governance-events)

Channel Members: Ensure all relevant team members are added to the Teams channel

Multiple Webhooks: You can configure multiple Workflow Webhooks to send different alert types to different channels

Workflow Testing: Always test your Workflow webhook in a non-production channel first

Notifications: Enable notifications for the channel so team members don’t miss important alerts

​Migration Guide: From Office 365 Connector to Workflow Webhook

If you’re currently using the legacy Office 365 Connector URLs:

Create a new Workflow Webhook following the setup steps above

Copy the new Webhook URL from the Workflow

Update OpenMetadata with the new Workflow Webhook URL

Test the configuration in a test channel first

Delete the old Office 365 Connector from Microsoft Teams once the new Workflow is working

No code changes are required - only the webhook URL needs to be updated.

​Reference

For more information about Microsoft Teams Workflow Webhooks, visit Create incoming webhooks with Workflows for Microsoft Teams.Was this page helpful?YesNoSuggest editsRaise issueSlack Alerts Configuration | OpenMetadataPreviousGoogle Chat Alerts Configuration | OpenMetadataNext⌘I
