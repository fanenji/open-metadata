---
type: clip
title: "Alerts & Notifications | OpenMetadata Guide - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/alerts-notifications"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Alerts & Notifications | OpenMetadata Guide - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/alerts-notifications

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAlerts & NotificationsAlerts & Notifications | OpenMetadata GuideHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData Quality and ObservabilityOverviewData QualityData ProfilerAlerts & NotificationsOverviewData Observability AlertsSystem & Governance NotificationsEmail Alerts ConfigurationSlack Alerts ConfigurationMicrosoft Teams Alerts ConfigurationGoogle Chat Alerts ConfigurationGeneric Webhook Alert ConfigurationIncident ManagerOn this pageAlerts & NotificationsObservability Alerts & NotificationsRequired PermissionsConfiguration WorkflowAdditional Details for the Configuration of External DestinationsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Alerts & Notifications

OpenMetadata has been providing observability alerts right from the start to notify users of important data lifecycle events: schema modifications, ownership shifts, and tagging updates. Users can define fine-grained alerts and notifications.

Starting from the 1.3 release, Data Observability alerts have been completely revamped, simplifying the process of monitoring data. Users can quickly create alerts for:

Changes in the Metadata: such as schema changes,

Data Quality Failures: to filter by Test Suite,

Pipeline Status Failures: when ingesting runs from your ETL systems, and

Ingestion Pipeline Monitoring: for OpenMetadata’s ingestion workflows

Depending on your use cases, notifications can be sent to owners, admins, teams, or users, providing a more personalized and informed experience. Teams can configure their dedicated Slack, MS Teams, or Google Chat channels to receive notifications related to their data assets, streamlining communication and collaboration. With the alerts and notifications in OpenMetadata, users can send Announcements over email, Slack, or Teams. Alerts are sent to a user when they are mentioned in a task or an activity feed.

​Observability Alerts & Notifications

OpenMetadata provides a unified Event Subscription framework that allows you to configure alerts for two main purposes:

Data Observability: Monitoring the health of data systems (e.g., Data Quality failures, Schema Drift, Pipeline failures).

System & Governance Notifications: Monitoring metadata changes and collaboration events (e.g., new Glossary terms, Tag updates, Ownership changes).

While these alerts serve different use cases and are accessed from different menus within the platform, the configuration process follows a similar workflow.

​Required Permissions

Required PermissionsSetting up alerts and notifications requires Create permission on the EventSubscription entity.

​Configuration Workflow

Select your use case below to see the specific configuration steps:

Data Observability AlertsMonitor the health of your data systems with alerts for pipeline failures, data quality issues, and schema changes.System & Governance NotificationsStay informed about metadata changes, governance events, and collaboration activities across your data catalog.

​Additional Details for the Configuration of External Destinations

OpenMetadata supports multiple external destinations for delivering alerts outside the platform. Each destination type requires a specific setup process.

EmailSend alerts directly to recipient email addresses using your OpenMetadata server’s email configuration.SlackDeliver alerts to Slack channels using Incoming Webhooks.Microsoft TeamsPost alerts to Teams channels using Workflow Webhooks with Adaptive Cards.Google ChatSend alerts to Google Chat Spaces using Webhooks.Generic WebhookIntegrate with custom applications using generic webhooks.Was this page helpful?YesNoSuggest editsRaise issueExternal Profiler Workflow | Official DocumentationPreviousData Observability Alerts | OpenMetadataNext⌘I
