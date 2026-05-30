---
type: clip
title: "REST API Connector | OpenMetadata Integration Documentation - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/api/rest"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# REST API Connector | OpenMetadata Integration Documentation - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/api/rest

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationRESTREST API Connector | OpenMetadata Integration DocumentationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIOverviewRESTOverviewRun ExternallyTroubleshootingDatabaseDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageRequirementsGenerate OpenAPI Schema URLMetadata IngestionConnection OptionsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.RESTBETAFeature List✓ API Endpoint✓ Request Schema✓ Response Schema

In this section, we provide guides and references to use the OpenAPI/REST connector.

Configure and schedule REST metadata workflows from the OpenMetadata UI:

Requirements

Metadata Ingestion

Troubleshooting

​Requirements

​Generate OpenAPI Schema URL

Generate OpenAPI schema URL for your serviceOpenAPI spec

​Metadata Ingestion

To ingest metadata from your sources, you need to create a service connection. The service connects your source system with OpenMetadata. Once you create a service, you can use it to configure your ingestion workflows.To create a service connection and ingest your metadata, follow the steps below:1Select the ServiceOn the left navigation bar, click Settings.On the next page, click Services, and then select the service.2Create a New ServiceTo add a new service connection, click Add New Service.3Select the ConnectorSelect REST as the service type and click Next.4Name and Describe the ServiceEnter a unique Service Name and Description.Service Name: OpenMetadata identifies services by their service name. Enter a name that distinguishes this deployment from other services, including other REST services you are ingesting metadata from.The service name cannot be changed after it is set.5Configure the Service ConnectionSet up the connection settings required for REST to set up the service and start ingesting metadata from your sources. The right-hand panel displays help documentation for the selected connection type in the product UI.

​Connection Options

1OpenAPI Schema URL:

An OpenAPI schema URL typically refers to the URL where the OpenAPI Specification (OAS) document of a web service is hosted. The document defines the service’s API, including available endpoints, request/response formats, authentication methods, etc. It is usually in JSON format. for e.g. https://petstore3.swagger.io/api/v3/openapi.json

Token: An authentication token to connect to an OpenAPI schema URL. It is only required if the API schema is protected or secured.2Test the ConnectionOnce the credentials have been added, click on Test Connection and Save the changes.3Schedule the Ingestion and DeployScheduling can be set up at an hourly, daily, weekly, or manual cadence. The

timezone is in UTC. Select a Start Date to schedule for ingestion. It is

optional to add an End Date.Review your configuration settings. If they match what you intended,

click Deploy to create the service and schedule metadata ingestion.If something doesn’t look right, click the Back button to return to the

appropriate step and change the settings as needed.After configuring the workflow, you can click on Deploy to create the

pipeline.4View the Ingestion PipelineOnce the workflow has been successfully deployed, you can view the

Ingestion Pipeline running from the Service Page.If AutoPilot is enabled, workflows like usage tracking, data lineage, and similar tasks will be handled automatically. Users don’t need to set up or manage them - AutoPilot takes care of everything in the system.Was this page helpful?YesNoSuggest editsRaise issueAPI Services | OpenMetadata Connector Integration GuidePreviousRun the OpenAPI/REST Connector ExternallyNext⌘I
