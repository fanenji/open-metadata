---
type: clip
title: "Run the PowerBI Connector Externally - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/dashboard/powerbi/yaml"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Run the PowerBI Connector Externally - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/dashboard/powerbi/yaml

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationPowerBIRun the PowerBI Connector ExternallyHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseDashboardOverviewDomo DashboardLightdashLookerMetabaseMicroStrategyModePowerBIOverviewRun ExternallyLineage from pbit filesTroubleshootingQlik CloudQlik SenseQuickSightRedashSigmaSSRSSupersetTableauMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.PowerBIPRODFeature List✓ Dashboards✓ Charts✓ Datamodels✓ Projects✓ Lineage✓ Column Lineage✓ Owners✕ Tags✕ Usage

In this section, we provide guides and references to use the PowerBI connector.

Supported Authentication Types:

OAuth 2.0 Service Principal — Azure AD application authentication using Client ID, Client Secret, and Tenant ID

Configure and schedule PowerBI metadata and profiler workflows from the OpenMetadata UI:

Requirements

Metadata Ingestion

​How to Run the Connector Externally

To run the Ingestion via the UI you’ll need to use the OpenMetadata Ingestion Container, which comes shipped with

custom Airflow plugins to handle the workflow deployment.

If, instead, you want to manage your workflows externally on your preferred orchestrator, you can check

the following docs to run the Ingestion Framework anywhere.

External SchedulersGet more information about running the Ingestion Framework Externally

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

​Python Requirements

We have support for Python versions 3.9-3.11

To run the PowerBI ingestion, you will need to install:

pip3 install "openmetadata-ingestion[powerbi]"

​Metadata Ingestion

All connectors are defined as JSON Schemas.

Here

you can find the structure to create a connection to PowerBI.

In order to create and run a Metadata Ingestion workflow, we will follow

the steps to create a YAML configuration able to connect to the source,

process the Entities if needed, and reach the OpenMetadata server.

The workflow is modeled around the following

JSON Schema

​1. Define the YAML Config

This is a sample config for PowerBI:

Source ConfigurationConfigure the source type and service name.clientIdclientId: PowerBI Client ID.

To get the client ID (also know as application ID), follow these steps:

Log into Microsoft Azure.

Search for App registrations and select the App registrations link.

Select the Azure AD app you’re using for embedding your Power BI content.

From the Overview section, copy the Application (client) ID.

clientSecretclientSecret: PowerBI Client Secret.

To get the client secret, follow these steps:

Log into Microsoft Azure.

Search for App registrations and select the App registrations link.

Select the Azure AD app you’re using for embedding your Power BI content.

Under Manage, select Certificates & secrets.

Under Client secrets, select New client secret.

In the Add a client secret pop-up window, provide a description for your application secret, select when the application secret expires, and select Add.

From the Client secrets section, copy the string in the Value column of the newly created application secret.

tenantIdtenantId: PowerBI Tenant ID.

To get the tenant ID, follow these steps:

Log into Microsoft Azure.

Search for App registrations and select the App registrations link.

Select the Azure AD app you’re using for Power BI.

From the Overview section, copy the Directory (tenant) ID.

scopescope: Service scope.

To let OM use the Power BI APIs using your Azure AD app, you’ll need to add the following scopes:

https://analysis.windows.net/powerbi/api/.default

Instructions for adding these scopes to your app can be found by following this link: https://analysis.windows.net/powerbi/api/.default.

authorityUriauthorityUri: Authority URI for the service.

To identify a token authority, you can provide a URL that points to the authority in question.

If you don’t specify a URL for the token authority, we’ll use the default value of https://login.microsoftonline.com/.hostPorthostPort: URL to the PowerBI instance.

To connect with your Power BI instance, you’ll need to provide the host URL. If you’re using an on-premise installation of Power BI, this will be the domain name associated with your instance.

If you don’t specify a host URL, we’ll use the default value of https://app.powerbi.com to connect with your Power BI instance.Pagination Entity Per PagePagination Entity Per Page:

The pagination limit for Power BI APIs can be set using this parameter. The limit determines the number of records to be displayed per page.

By default, the pagination limit is set to 100 records, which is also the maximum value allowed.Use Admin APIsUse Admin APIs:

Option for using the PowerBI admin APIs:

Refer to the section here to get more information.

Enabled (Use PowerBI Admin APIs)

Disabled (Use Non-Admin PowerBI APIs)

pbitFilesSourcepbitFilesSource: Source to get the .pbit files to extract lineage information. Select one of local, azureConfig, gcsConfig, s3Config.

pbitFileConfigType: Determines the storage backend type (azure, gcs, or s3).

securityConfig: Authentication credentials for accessing the storage backend.

prefixConfig: Details of the location in the storage backend.

pbitFilesExtractDir: Specifies the local directory where extracted .pbit files will be stored for processing.

Source Config​Source Configuration - Source ConfigThe sourceConfig is defined here:dbServiceNames: Database Service Names for ingesting lineage if the source supports it.dashboardFilterPattern, chartFilterPattern, dataModelFilterPattern: Note that all of them support regex as include or exclude. E.g., “My dashboard, My dash.*, .*Dashboard”.projectFilterPattern: Filter the dashboards, charts and data sources by projects. Note that all of them support regex as include or exclude. E.g., “My project, My proj.*, .*Project”.includeOwners: Set the ‘Include Owners’ toggle to control whether to include owners to the ingested entity if the owner email matches with a user stored in the OM server as part of metadata ingestion. If the ingested entity already exists and has an owner, the owner will not be overwritten.includeTags: Set the ‘Include Tags’ toggle to control whether to include tags in metadata ingestion.includeDataModels: Set the ‘Include Data Models’ toggle to control whether to include tags as part of metadata ingestion.markDeletedDashboards: Set the ‘Mark Deleted Dashboards’ toggle to flag dashboards as soft-deleted if they are not present anymore in the source system.Include Draft Dashboard (toogle): Set the ‘Include Draft Dashboard’ toggle to include draft dashboards. By default it will include draft dashboards.dataModelFilterPattern: Regex exclude or include data models that matches the pattern.includeOwners:Enabling a flag will replace the current owner with a new owner from the source during metadata ingestion, if the current owner is null. It is recommended to keep the flag enabled to obtain the owner information during the first metadata ingestion.includeOwners supports boolean value either true or false.markDeletedDashboards: Optional configuration to soft delete dashboards in OpenMetadata if the source dashboards are deleted. Also, if the dashboard is deleted, all the associated entities like lineage, etc., with that dashboard will be deleted.markDeletedDashboards supports boolean value either true or false.markDeletedDataModels: Optional configuration to soft delete data models in OpenMetadata if the source data models are deleted. Also, if the data models is deleted, all the associated entities like lineage, etc., with that data models will be deleted.includeOwners supports boolean value either true or false.includeTags:Optional configuration to toggle the tags ingestion.markDeletedDataModels supports boolean value either true or false.includeDataModels: Optional configuration to toggle the ingestion of data models.includeDataModels supports boolean value either true or false.includeDraftDashboard: Optional Configuration to include/exclude draft dashboards. By default it will include draft dashboards.includeDraftDashboard supports boolean value either true or false.overrideMetadata: Set the ‘Override Metadata’ toggle to control whether to override the existing metadata in the OpenMetadata server with the metadata fetched from the source. If the toggle is set to true, the metadata fetched from the source will override the existing metadata in the OpenMetadata server. If the toggle is set to false, the metadata fetched from the source will not override the existing metadata in the OpenMetadata server. This is applicable for fields like description, tags, owner and displayName.overrideMetadata supports boolean value either true or false.overrideLineage: Set the ‘Override Lineage’ toggle to control whether to override the existing lineage.overrideLineage supports boolean value either true or false.Sink ConfigurationTo send the metadata to OpenMetadata, it needs to be specified as type: metadata-rest.Workflow ConfigurationThe main property here is the openMetadataServerConfig, where you can define the host and security provider of your OpenMetadata installation.Logger LevelYou can specify the loggerLevel depending on your needs. If you are trying to troubleshoot an ingestion, running with DEBUG will give you far more traces for identifying issues.JWT TokenJWT tokens will allow your clients to authenticate against the OpenMetadata server. To enable JWT Tokens, you will get more details here.You can refer to the JWT Troubleshooting section link for any issues in your JWT configuration.Store Service ConnectionIf set to true (default), we will store the sensitive information either encrypted via the Fernet Key in the database or externally, if you have configured any Secrets Manager.If set to false, the service will be created, but the service connection information will only be used by the Ingestion Framework at runtime, and won’t be sent to the OpenMetadata server.SSL ConfigurationIf you have added SSL to the OpenMetadata server, then you will need to handle the certificates when running the ingestion too. You can either set verifySSL to ignore, or have it as validate, which will require you to set the sslConfig.caCertificate with a local path where your ingestion runs that points to the server certificate file.Find more information on how to troubleshoot SSL issues here.ingestionPipelineFQNFully qualified name of ingestion pipeline, used to identify the current ingestion pipeline.connector_config.yamlsource:  type: powerbi  serviceName: local_powerbi  serviceConnection:    config:      type: PowerBIclientId: clientId  # REQUIRED - Azure AD application client IDclientSecret: secret  # REQUIRED - Azure AD application client secrettenantId: tenant  # REQUIRED - Azure AD tenant ID# scope:      #    - https://analysis.windows.net/powerbi/api/.default (default)# authorityURI: https://login.microsoftonline.com/ (default)# hostPort: https://analysis.windows.net/powerbi (default)# pagination_entity_per_page: 100 (default)# useAdminApis: true (default)# Select one of local, azureConfig, gcsConfig, s3Config.      # For Azure      # pbitFilesSource:      #   pbitFileConfigType: azure  # Specify the storage type as Azure Blob Storage      #   securityConfig:      #     clientId: ""            # Azure application Client ID      #     clientSecret: ""        # Azure application Client Secret      #     tenantId: ""            # Azure tenant ID      #     accountName: ""         # Azure storage account name      #     vaultName: ""           # Optional: Azure vault name for secrets management      #     scopes: ""              # Optional: OAuth scopes for Azure      #   prefixConfig:      #     bucketName: ""          # Name of the Azure Blob Storage container      #     objectPrefix: ""        # Path prefix to locate files within the container      #   pbitFilesExtractDir: /tmp/pbitFiles  # Local directory for extracted files      # For gcsConfig      # GCP credentials configurations      # We support two ways of authenticating to GCP: via GCP Credentials Values or GCP Credentials Path.      # Option 1: Authenticate using GCP Credentials Values      # pbitFilesSource:      #   pbitFileConfigType: gcs  # Specify the storage type as Google Cloud Storage      #   securityConfig:      #     type: service_account  # Authentication type      #     projectId: ""          # GCP project ID (can be single or multiple)      #     privateKeyId: ""       # Private Key ID from GCP service account      #     privateKey: ""         # Private Key from GCP service account      #     clientEmail: ""        # Service account email      #     clientId: ""           # Client ID      #     authUri: "https://accounts.google.com/o/oauth2/auth"  # OAuth URI      #     authProviderX509CertUrl: "https://www.googleapis.com/oauth2/v1/certs"      #     clientX509CertUrl: ""  # Certificate URL      #   prefixConfig:      #     bucketName: ""         # Name of the GCS bucket      #     objectPrefix: ""       # Path prefix to locate files within the bucket      #   pbitFilesExtractDir: /tmp/pbitFiles  # Local directory for extracted files      # Option 2: Authenticate using Raw Credential Values      # pbitFilesSource:      #   pbitFileConfigType: gcs  # Specify the storage type as Google Cloud Storage      #   securityConfig:      #     type: external_account # Authentication type      #     externalType: "external_account"  # External account authentication      #     audience: ""           # Audience for token validation      #     subjectTokenType: ""   # Type of subject token      #     tokenURL: ""           # URL to obtain the token      #     credentialSource: {}   # Raw JSON object with credential source details      #   prefixConfig:      #     bucketName: ""         # Name of the GCS bucket      #     objectPrefix: ""       # Path prefix to locate files within the bucket      #   pbitFilesExtractDir: /tmp/pbitFiles  # Local directory for extracted files      # For s3Config      # pbitFilesSource:      #   pbitFileConfigType: s3  # Specify the storage type as Amazon S3      #   securityConfig:      #     awsAccessKeyId: ""          # AWS Access Key ID      #     awsSecretAccessKey: ""      # AWS Secret Access Key      #     awsRegion: ""               # AWS region for the bucket      #     awsSessionToken: ""         # Optional session token      #     endPointURL: ""             # Optional custom S3 endpoint URL      #     profileName: ""             # Optional AWS CLI profile name      #     assumeRoleArn: ""           # ARN of the role to assume (if required)      #     assumeRoleSessionName: ""   # Session name for assumed role      #     assumeRoleSourceIdentity: "" # Source identity for assumed session      #   prefixConfig:      #     bucketName: ""              # Name of the S3 bucket      #     objectPrefix: ""            # Path prefix to locate files within the bucket      #   pbitFilesExtractDir: /tmp/pbitFiles  # Local directory for extracted files  sourceConfig:    config:      type: DashboardMetadata      # lineageInformation:      #   dbServiceNames:      #     - service1      #     - service2      # dashboardFilterPattern:      #   includes:      #     - dashboard1      #     - dashboard2      #   excludes:      #     - dashboard3      #     - dashboard4      # chartFilterPattern:      #   includes:      #     - chart1      #     - chart2      #   excludes:      #     - chart3      #     - chart4      # projectFilterPattern:      #   includes:      #     - project1      #     - project2      #   excludes:      #     - project3      #     - project4      # dataModelFilterPattern:      #   includes:      #     - dataModel1      #     - dataModel2      #   excludes:      #     - dataModel3      #     - dataModel4      # includeOwners: false # true      # markDeletedDashboards: true # false      # markDeletedDataModels: true # false      # includeTags: true # false      # includeDataModels: true # false      # includeDraftDashboard: true # false      # overrideMetadata: false # true      # overrideLineage: false # truesink:  type: metadata-rest  config: {}workflowConfig:  loggerLevel: INFO  # DEBUG, INFO, WARNING or ERROR  openMetadataServerConfig:    hostPort: "http://localhost:8585/api"    authProvider: openmetadata    securityConfig:      jwtToken: "{bot_jwt_token}"    ## Store the service Connection information    storeServiceConnection: true  # false    ## Secrets Manager Configuration    # secretsManagerProvider: aws, azure or noop    # secretsManagerLoader: airflow or env    ## If SSL, fill the following    # verifySSL: validate  # or ignore    # sslConfig:    #   caCertificate: /local/path/to/certificate# ingestionPipelineFQN: <service name>.<ingestion name> ## e.g., "my_redshift.metadata"

​2. Run with the CLI

First, we will need to save the YAML file. Afterward, and with all requirements installed, we can run:

metadata ingest -c <path-to-yaml>

Note that from connector to connector, this recipe will always be the same. By updating the YAML configuration,

you will be able to extract metadata from different sources.Was this page helpful?YesNoSuggest editsRaise issuePowerBI Connector | OpenMetadata Integration DocumentationPreviousLineage from pbit filesNext⌘I
