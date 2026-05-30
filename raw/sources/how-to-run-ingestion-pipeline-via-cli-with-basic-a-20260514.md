---
type: clip
title: "How To Run Ingestion Pipeline Via CLI with Basic Auth - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/cli-ingestion-with-basic-auth"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# How To Run Ingestion Pipeline Via CLI with Basic Auth - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/cli-ingestion-with-basic-auth

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAdmin GuideHow To Run Ingestion Pipeline Via CLI with Basic AuthHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsAdmin GuideOverviewHow to Ingest MetadataHow to Delete a Service ConnectionManage Teams and UsersAdvanced Guide for Roles and PoliciesCLI Ingestion with Basic AuthHow to Add Custom LogoReindexing SearchData InsightsPermission DebuggerPersona and Landing Page CustomizationAudit LogsOn this pageHow To Run Ingestion Pipeline Via CLI with Basic AuthHow to get the JWT tokenHow to add JWT token into the workflow configDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​How To Run Ingestion Pipeline Via CLI with Basic Auth

Out of the box, OpenMetadata comes with a Username & Password Login Mechanism.

Basic AuthenticationBasic Authentication

From 0.12.1 OpenMetadata has changed the default no-auth to Basic auth, So to run any ingestion pipeline from CLI you will have to pass the jwtToken and authProvider in the securityConfig.

​How to get the JWT token

1. Go to the settings page from the activity bar Section. Click on the Bots and you will see the list of bots, then click on the ingestion-bot.

2. You will be redirected to the ingestion-bot details page. there you will get the JWT token, click on the copy button and copy the JWT token.

Alright, now you have the JWT token, let see how to add that into the workflow config.

​How to add JWT token into the workflow config

Now Past the copied JWT Token into your pipeline securityConfig, So your final workflow config will look like this.

AuthProvider Should be openmetadata i.e authProvider: openmetadata

workflowConfig:

openMetadataServerConfig:

hostPort: http://localhost:8585/api

authProvider: openmetadata

securityConfig:

jwtToken: 'eyJraWQiO...'

Now you can run the pipeline by running.

metadata ingest -c ./pipeline_name.yaml

Was this page helpful?YesNoSuggest editsRaise issueUse Cases - Creating Roles & Policies in OpenMetadataPreviousHow to Change the Login Page & Nav Bar Logo and FaviconNext⌘I
