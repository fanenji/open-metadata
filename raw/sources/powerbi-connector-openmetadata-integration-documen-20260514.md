---
type: clip
title: "PowerBI Connector | OpenMetadata Integration Documentation - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/dashboard/powerbi"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# PowerBI Connector | OpenMetadata Integration Documentation - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/dashboard/powerbi

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationPowerBIPowerBI Connector | OpenMetadata Integration DocumentationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseDashboardOverviewDomo DashboardLightdashLookerMetabaseMicroStrategyModePowerBIQlik CloudQlik SenseQuickSightRedashSigmaSSRSSupersetTableauMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageRequirementsPowerBI Admin and Non-Admin APIs:PowerBI Account SetupStep 1: Enable API permissions from the PowerBI Admin consoleStep 2: Create the App in Azure ADStep 3: Provide necessary API permissions to the Azure AD appStep 4: PowerBI WorkspacesMetadata IngestionConnection DetailsMetadata Ingestion OptionsLineageDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.PowerBIPRODFeature List✓ Dashboards✓ Charts✓ Datamodels✓ Projects✓ Lineage✓ Column Lineage✓ Owners

In this section, we provide guides and references to use the PowerBI connector.

Supported Authentication Types:

OAuth 2.0 Service Principal — Azure AD application authentication using Client ID, Client Secret, and Tenant ID

Configure and schedule PowerBI metadata and profiler workflows from the OpenMetadata UI:

Requirements

Metadata Ingestion

Lineage

Troubleshooting

​Requirements

To access the PowerBI APIs and import dashboards, charts, and datasets from PowerBI into OpenMetadata, a PowerBI Pro license is necessary.

PowerBI dataflows are not yet supported.

OpenMetadata does not support Power BI usage ingestion because the Power BI Usage API does not support Service Principal authentication.

When configuring Azure Authentication, ensure that “Allow public client flows” is enabled. This setting is required to support authentication for public client applications.

​PowerBI Admin and Non-Admin APIs:

While configuring the PowerBI ingestion you can choose whether to use the PowerBI Admin APIs to retrieve the metadata or use the PowerBI Non-Admin APIs. Please check below for the the difference in their functionality:

Enabled (Use PowerBI Admin APIs)

Using the admin APIs will fetch the dashboard and chart metadata from all the workspaces available in the PowerBI instance.

When using the PowerBI Admin APIs, the table and dataset information used to generate lineage is gathered using the PowerBI Scan Result API. This API has no limitations and hence does not restrict getting the necessary data for generating lineage.

Disabled (Use Non-Admin PowerBI APIs)

Using the non-admin APIs will only fetch the dashboard and chart metadata from the workspaces that have the security group of the service principal assigned to them.

When using the PowerBI Non-Admin APIs, the table and dataset information used to generate lineage is gathered using the PowerBI Get Dataset Tables API. This API only retrieves the table information if the dataset is a Push Dataset.

Hence the lineage can only be created for push datasets in this case.

For more information please visit the PowerBI official documentation here.

​PowerBI Account Setup

Follow the steps below to configure the account setup for PowerBI connector:

​Step 1: Enable API permissions from the PowerBI Admin console

We extract the information from PowerBI using APIs, this is a manual step a PowerBI Admin needs to do to ensure we can get the right information.

Login to the Power BI as Admin and from Tenant settings allow below permissions.

Allow service principles to use Power BI APIs

Allow service principals to use read-only Power BI admin APIs

Enhance admin APIs responses with detailed metadata

​Step 2: Create the App in Azure AD

Please follow the steps mentioned here for setting up the Azure AD application service principle.

​Step 3: Provide necessary API permissions to the Azure AD app

Go to the Azure Ad app registrations page, select your app and add the dashboard permissions to the app for PowerBI service and grant admin consent for the same:

The required permissions are:

Dashboard.Read.All

Optional Permissions: (Without granting these permissions, the dataset information cannot be retrieved and the datamodel and lineage processing will be skipped)

Dataset.Read.All

Make sure that in the API permissions section Tenant related permissions are not being given to the app

Please refer here for detailed explanation

​Step 4: PowerBI Workspaces

The service principal does not take into account the default user workspaces e.g My Workspace.

Create new workspaces in PowerBI by following the document here

For reference here is a thread referring to the same

​Metadata Ingestion

To ingest metadata from your sources, you need to create a service connection. The service connects your source system with OpenMetadata. Once you create a service, you can use it to configure your ingestion workflows.To create a service connection and ingest your metadata, follow the steps below:1Select the ServiceOn the left navigation bar, click Settings.On the next page, click Services, and then select the service.2Create a New ServiceTo add a new service connection, click Add New Service.3Select the ConnectorSelect PowerBI as the service type and click Next.4Name and Describe the ServiceEnter a unique Service Name and Description.Service Name: OpenMetadata identifies services by their service name. Enter a name that distinguishes this deployment from other services, including other PowerBI services you are ingesting metadata from.The service name cannot be changed after it is set.5Configure the Service ConnectionSet up the connection settings required for PowerBI to set up the service and start ingesting metadata from your sources. The right-hand panel displays help documentation for the selected connection type in the product UI.

​Connection Details

1Connection DetailsWhen using a Hybrid Ingestion Runner, any sensitive credential fields—such as passwords, API keys, or private keys—must reference secrets using the following format:password: secret:/my/database/password

This applies only to fields marked as secrets in the connection form (these typically mask input and show a visibility toggle icon).

For a complete guide on managing secrets in hybrid setups, see the Hybrid Ingestion Runner Secret Management Guide.clientId: PowerBI Client ID.

To get the client ID (also known as application ID), follow these steps:

Log into Microsoft Azure.

Search for App registrations and select the App registrations link.

Select the Azure AD app you’re using for embedding your Power BI content.

From the Overview section, copy the Application (client) ID.

clientSecret: PowerBI Client Secret.

To get the client secret, follow these steps:

Log into Microsoft Azure.

Search for App registrations and select the App registrations link.

Select the Azure AD app you’re using for embedding your Power BI content.

Under Manage, select Certificates & secrets.

Under Client secrets, select New client secret.

In the Add a client secret pop-up window, provide a description for your application secret, select when the application secret expires, and select Add.

From the Client secrets section, copy the string in the Value column of the newly created application secret.

tenantId: PowerBI Tenant ID.

To get the tenant ID, follow these steps:

Log into Microsoft Azure.

Search for App registrations and select the App registrations link.

Select the Azure AD app you’re using for Power BI.

From the Overview section, copy the Directory (tenant) ID.

scope: Service scope.

To let OM use the Power BI APIs using your Azure AD app, you’ll need to add the following scopes:

https://analysis.windows.net/powerbi/api/.default

Instructions for adding these scopes to your app can be found by following this link: https://analysis.windows.net/powerbi/api/.default.

authorityUri: Authority URI for the service.

To identify a token authority, you can provide a URL that points to the authority in question.

If you don’t specify a URL for the token authority, we’ll use the default value of https://login.microsoftonline.com/.

hostPort: URL to the PowerBI instance.

To connect with your Power BI instance, you’ll need to provide the host URL. If you’re using an on-premise installation of Power BI, this will be the domain name associated with your instance.

If you don’t specify a host URL, we’ll use the default value of https://app.powerbi.com to connect with your Power BI instance.

Pagination Entity Per Page:

The pagination limit for Power BI APIs can be set using this parameter. The limit determines the number of records to be displayed per page.

By default, the pagination limit is set to 100 records, which is also the maximum value allowed.

Use Admin APIs:

Option for using the PowerBI admin APIs:

Refer to the section here to get more information.

Enabled (Use PowerBI Admin APIs)

Disabled (Use Non-Admin PowerBI APIs)

2Test the ConnectionOnce the credentials have been added, click on Test Connection and Save the changes.3Configure Metadata IngestionIn this step we will configure the metadata ingestion pipeline,

Please follow the instructions below​Metadata Ingestion Options

Name: This field refers to the name of ingestion pipeline, you can customize the name or use the generated name.

Dashboard Filter Pattern (Optional): Use it to control whether to include dashboard as part of metadata ingestion.

Include: Explicitly include dashboards by adding a list of comma-separated regular expressions to the ‘Include’ field. OpenMetadata will include all dashboards with names matching one or more of the supplied regular expressions. All other dashboards will be excluded.

Exclude: Explicitly exclude dashboards by adding a list of comma-separated regular expressions to the ‘Exclude’ field. OpenMetadata will exclude all dashboards with names matching one or more of the supplied regular expressions. All other dashboards will be included.

projectFilterPattern: Filter the dashboards, charts and data sources by projects. Note that all of them support regex as include or exclude. E.g., “My project, My proj.*, .*Project”.

We filter the projects by concatenating the entire project hierarchy using dot notation

(e.g., Project1.NestedProjectA.OtherProject).

Make sure the regex filter pattern accounts for this fully-qualified format.

Chart Pattern (Optional): Use it to control whether to include charts as part of metadata ingestion.

Include: Explicitly include charts by adding a list of comma-separated regular expressions to the ‘Include’ field. OpenMetadata will include all charts with names matching one or more of the supplied regular expressions. All other charts will be excluded.

Exclude: Explicitly exclude charts by adding a list of comma-separated regular expressions to the ‘Exclude’ field. OpenMetadata will exclude all charts with names matching one or more of the supplied regular expressions. All other charts will be included.

Data Model Pattern (Optional): Use it to control whether to include data modes as part of metadata ingestion.

Include: Explicitly include data models by adding a list of comma-separated regular expressions to the ‘Include’ field. OpenMetadata will include all data models with names matching one or more of the supplied regular expressions. All other data models will be excluded.

Exclude: Explicitly exclude data models by adding a list of comma-separated regular expressions to the ‘Exclude’ field. OpenMetadata will exclude all data models with names matching one or more of the supplied regular expressions. All other data models will be included.

Database Service Name (Optional): Enter the name of Database Service which is already ingested in OpenMetadata to create lineage between dashboards and database tables.

Enable Debug Log (toggle): Set the ‘Enable Debug Log’ toggle to set the default log level to debug.

Include Owners (toggle): Set the ‘Include Owners’ toggle to control whether to include owners to the ingested entity if the owner email matches with a user stored in the OM server as part of metadata ingestion. If the ingested entity already exists and has an owner, the owner will not be overwritten.

Include Tags (toggle): Set the ‘Include Tags’ toggle to control whether to include tags in metadata ingestion.

Include Data Models (toggle): Set the ‘Include Data Models’ toggle to control whether to include tags as part of metadata ingestion.

Mark Deleted Dashboards (toggle): Set the ‘Mark Deleted Dashboards’ toggle to flag dashboards as soft-deleted if they are not present anymore in the source system.

Include Draft Dashboard (toogle): Set the ‘Include Draft Dashboard’ toggle to include draft dashboards. By default it will include draft dashboards.

4Schedule the Ingestion and DeployScheduling can be set up at an hourly, daily, weekly, or manual cadence. The

timezone is in UTC. Select a Start Date to schedule for ingestion. It is

optional to add an End Date.Review your configuration settings. If they match what you intended,

click Deploy to create the service and schedule metadata ingestion.If something doesn’t look right, click the Back button to return to the

appropriate step and change the settings as needed.After configuring the workflow, you can click on Deploy to create the

pipeline.5View the Ingestion PipelineOnce the workflow has been successfully deployed, you can view the

Ingestion Pipeline running from the Service Page.If AutoPilot is enabled, workflows like usage tracking, data lineage, and similar tasks will be handled automatically. Users don’t need to set up or manage them - AutoPilot takes care of everything in the system.

​Lineage

To establish lineage from your database tables to dashboards, you must add the corresponding database service name.

Was this page helpful?YesNoSuggest editsRaise issueMode Dashboard Troubleshooting Guide | OpenMetadata SupportPreviousRun the PowerBI Connector ExternallyNext⌘I
