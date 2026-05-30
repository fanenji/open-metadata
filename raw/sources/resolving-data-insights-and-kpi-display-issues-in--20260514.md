---
type: clip
title: "Resolving Data Insights and KPI Display Issues in OpenMetadata - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/data-insights"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Resolving Data Insights and KPI Display Issues in OpenMetadata - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/data-insights

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAdmin GuideResolving Data Insights and KPI Display Issues in OpenMetadataHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsAdmin GuideOverviewHow to Ingest MetadataHow to Delete a Service ConnectionManage Teams and UsersAdvanced Guide for Roles and PoliciesCLI Ingestion with Basic AuthHow to Add Custom LogoReindexing SearchData InsightsPermission DebuggerPersona and Landing Page CustomizationAudit LogsOn this pageData Insights Application (Troubleshooting)Troubleshooting Steps1. Verify Data Insights Application Installation2. Run the Data Insights Application3. Enable Backfill and Recreate Index OptionsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Data Insights Application (Troubleshooting)

If you are experiencing any of the following issues in Data Insights Application, follow the steps below to diagnose and resolve the problem.

Insights menu returns no results.

KPI charts do not display.

Data Insights reports show no data.

Filtering by “Yesterday” or “Last 3 Days” yields no results.

​Troubleshooting Steps

​1. Verify Data Insights Application Installation

Ensure that the Data Insights application is installed:

Navigate to Settings > Applications.

Check if Data Insights Application is listed.

If not, click Add Apps and install Data Insights Application.

​2. Run the Data Insights Application

Click Configure to set parameters.

Click Schedule to define execution timing.

Click Run Now to execute the Data Insights workflow.

​3. Enable Backfill and Recreate Index Options

When configuring the Data Insights application:

Enable Backfill Configuration.

Enable Recreate DataInsights DataAssets Index.

This will backfill historical data and recreate the index for accurate chart rendering.Was this page helpful?YesNoSuggest editsRaise issueReindexing SearchPreviousPermission Debugger | Analyze and Troubleshoot User AccessNext⌘I
