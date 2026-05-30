---
type: clip
title: "Superset - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/dashboard/superset/sso"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Superset - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/dashboard/superset/sso

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationSupersetSupersetHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseDashboardOverviewDomo DashboardLightdashLookerMetabaseMicroStrategyModePowerBIQlik CloudQlik SenseQuickSightRedashSigmaSSRSSupersetOverviewRun ExternallySSOTroubleshootingTableauMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageSuperset with SSODocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Superset with SSO

OpenMetadata utilizes Superset REST APIs to retrieve metadata from Superset. These APIs support two modes of authentication: db and ldap. At this time, OAuth authentication is not supported by these APIs.

Although the Superset REST APIs do not support OAuth authentication, there are still two ways for a user to authenticate through the API:

Using admin user credentials: When a Superset instance is initialized, a default admin user is created with the username and password both set as “admin”. This admin user can be used to authenticate to the Superset APIs via the “db” authentication mode.

Using database credentials: You can fetch metadata from superset instance by providing the mysql or postgres database connection details.

Was this page helpful?YesNoSuggest editsRaise issueRun the Superset Connector ExternallyPreviousSuperset Troubleshooting Guide | OpenMetadata SupportNext⌘I
