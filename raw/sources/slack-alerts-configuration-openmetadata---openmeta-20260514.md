---
type: clip
title: "Slack Alerts Configuration | OpenMetadata - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/alerts-notifications/slack-alerts-configuration"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Slack Alerts Configuration | OpenMetadata - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/alerts-notifications/slack-alerts-configuration

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAlerts & NotificationsSlack Alerts Configuration | OpenMetadataHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData Quality and ObservabilityOverviewData QualityData ProfilerAlerts & NotificationsOverviewData Observability AlertsSystem & Governance NotificationsEmail Alerts ConfigurationSlack Alerts ConfigurationMicrosoft Teams Alerts ConfigurationGoogle Chat Alerts ConfigurationGeneric Webhook Alert ConfigurationIncident ManagerOn this pageSlack Alerts ConfigurationSetting Up a Slack WebhookStep 1: Access Slack API ApplicationsStep 2: Create a New AppStep 3: Enable and Configure Incoming WebhooksStep 4: Copy Your Webhook URLConfiguring Slack Webhooks in OpenMetadataStep 1: Access Alert ConfigurationStep 2: Add Slack as a DestinationStep 3: Test the ConnectionStep 4: Save and EnableBest PracticesReferenceDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Slack Alerts Configuration

OpenMetadata integrates with Slack using Incoming Webhooks to deliver alert messages directly to your Slack channels. This allows you to receive real-time notifications without leaving Slack.

​Setting Up a Slack Webhook

Follow these steps to create an Incoming Webhook in your Slack workspace:

​Step 1: Access Slack API Applications

Go to Slack API Applications

Sign in with your Slack workspace credentials

Click Create New App or Create an App

​Step 2: Create a New App

Select From scratch

Enter an App Name (e.g., “OpenMetadata Alerts”)

Select your Slack Workspace

Click Create App

​Step 3: Enable and Configure Incoming Webhooks

In the left sidebar, navigate to Incoming Webhooks

Toggle Activate Incoming Webhooks to On

Click Add New Webhook to Workspace

Select the Slack channel where you want alerts to be posted

Click Allow to authorize the app

​Step 4: Copy Your Webhook URL

You’ll now see your new webhook listed under Webhook URLs for Your Workspace

Copy the complete Webhook URL

Keep this URL safe - you’ll need it to configure OpenMetadata

​Configuring Slack Webhooks in OpenMetadata

Once you have your Slack Webhook URL, follow these steps to configure it in OpenMetadata:

​Step 1: Access Alert Configuration

In OpenMetadata, navigate to Alerts & Notifications from the main menu

Select the type of alert you want to configure:

Data Observability Alerts (for data quality and pipeline monitoring)

System & Governance Notifications (for metadata and governance events)

​Step 2: Add Slack as a Destination

Click Add Destination

Select Slack from the available destination options

Paste your Slack Webhook URL into the Slack Webhook URL field

Optionally, enter a Display Name for this Slack destination (e.g., “Data Quality Alerts”)

​Step 3: Test the Connection

Click Test Connection to verify the webhook is working

A test message will be sent to your Slack channel

If successful, you’ll see a confirmation message

​Step 4: Save and Enable

Click Save to store the configuration

The Slack destination is now ready to receive alerts

​Best Practices

Dedicated Channels: Create separate Slack channels for different types of alerts (e.g., #data-quality-alerts, #pipeline-failures)

Channel Permissions: Ensure the Slack channel is accessible to all team members who need to receive alerts

Multiple Webhooks: You can configure multiple Slack webhooks to send different alert types to different channels

Monitoring: Regularly monitor your Slack channels to ensure alerts are being delivered

​Reference

For more information about Slack Incoming Webhooks, visit the Slack API DocumentationWas this page helpful?YesNoSuggest editsRaise issueEmail Alerts Configuration | OpenMetadataPreviousMicrosoft Teams Alerts Configuration | OpenMetadataNext⌘I
