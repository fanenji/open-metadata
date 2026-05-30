---
type: clip
title: "Google Chat Alerts Configuration | OpenMetadata - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/alerts-notifications/google-chat-alerts-configuration"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Google Chat Alerts Configuration | OpenMetadata - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/alerts-notifications/google-chat-alerts-configuration

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAlerts & NotificationsGoogle Chat Alerts Configuration | OpenMetadataHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData Quality and ObservabilityOverviewData QualityData ProfilerAlerts & NotificationsOverviewData Observability AlertsSystem & Governance NotificationsEmail Alerts ConfigurationSlack Alerts ConfigurationMicrosoft Teams Alerts ConfigurationGoogle Chat Alerts ConfigurationGeneric Webhook Alert ConfigurationIncident ManagerOn this pageGoogle Chat Alerts ConfigurationSetting Up a Google Chat WebhookStep 1: Access Google ChatStep 2: Create a New WebhookStep 3: Configure the WebhookStep 4: Copy Your Webhook URLConfiguring Google Chat Webhooks in OpenMetadataStep 1: Access Alert ConfigurationStep 2: Add Google Chat as a DestinationStep 3: Test the ConnectionStep 4: Save and EnableBest PracticesReferenceDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Google Chat Alerts Configuration

OpenMetadata integrates with Google Chat using Webhooks to deliver alert messages directly to your Google Chat Spaces. This allows you to receive real-time notifications within your Google Chat workspace.

​Setting Up a Google Chat Webhook

Follow these steps to create a Webhook in your Google Chat Space:

​Step 1: Access Google Chat

Open Google Chat

Sign in with your Google account

Navigate to the Space where you want to receive alerts (or create a new Space)

​Step 2: Create a New Webhook

Click on the Space name at the top of the chat window

From the dropdown menu, select Space Settings

Click Apps & Integrations  in the left menu.

Click Add Webhooks

​Step 3: Configure the Webhook

Enter a Name for the webhook (e.g., “OpenMetadata Alerts”)

Select the Avatar or icon for the webhook (optional)

Click Create

​Step 4: Copy Your Webhook URL

You’ll see your new webhook listed with a Webhook URL

Copy the complete Webhook URL (it looks like https://chat.googleapis.com/v1/spaces/XXXXXXXXXXXXXXX/messages?key=...&token=...)

Keep this URL safe - you’ll need it to configure OpenMetadata

​Configuring Google Chat Webhooks in OpenMetadata

Once you have your Google Chat Webhook URL, follow these steps to configure it in OpenMetadata:

​Step 1: Access Alert Configuration

In OpenMetadata, navigate to Alerts & Notifications from the main menu

Select the type of alert you want to configure:

Data Observability Alerts (for data quality and pipeline monitoring)

System & Governance Notifications (for metadata and governance events)

​Step 2: Add Google Chat as a Destination

Click Add Destination

Select Google Chat from the available destination options

Paste your Google Chat Webhook URL into the Google Chat Webhook URL field

​Step 3: Test the Connection

Click Test Connection to verify the webhook is working

A test message will be sent to your Google Chat Space

If successful, you’ll see a confirmation message and the test message in your Space

​Step 4: Save and Enable

Click Save to store the Alert configuration

The Google Chat destination is now ready to receive alerts

​Best Practices

Dedicated Spaces: Create separate Google Chat Spaces for different types of alerts (e.g., “Data Quality Alerts”, “Pipeline Failures”, “Governance Events”)

Space Members: Ensure all relevant team members are added to the Google Chat Space

Multiple Webhooks: You can configure multiple Google Chat webhooks to send different alert types to different Spaces

Notifications: Enable notifications for the Space so team members don’t miss important alerts

Monitoring: Regularly review alerts in your Google Chat Space to ensure they’re being delivered

​Reference

For more information about Google Chat Webhooks, visit the Google Chat Webhooks DocumentationWas this page helpful?YesNoSuggest editsRaise issueMicrosoft Teams Alerts Configuration | OpenMetadataPreviousGeneric Webhook Alert Configuration | OpenMetadataNext⌘I
