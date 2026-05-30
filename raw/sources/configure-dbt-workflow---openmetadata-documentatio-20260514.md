---
type: clip
title: "Configure dbt workflow - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/configure-dbt-workflow"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Configure dbt workflow - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/configure-dbt-workflow

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationdbtConfigure dbt workflowHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtOverviewdbt Cloud APIdbt CoreConfigure dbt workflowRun ExternallyAuto Ingest dbt Core ArtifactsIngest dbt OwnerIngest dbt DescriptionsIngest dbt TagsIngest dbt TiersIngest dbt GlossaryIngest dbt DomainIngest dbt Custom PropertiesIngest dbt LineageSetup Multiple dbt Projectsdbt troubleshootingDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOraclePinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageConfigure dbt workflowConfiguration1. Add a dbt Ingestion2. Configure the dbt Ingestiondbt CoreAWS S3 BucketsGoogle Cloud Storage BucketsAzure Storage BucketsLocal StorageFile Serverdbt Cloud3. Schedule and DeployDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.dbtPRODFeature List✓ Metadata✓ Queries✓ Lineage✓ Tags✓ Tiers✓ Domains✓ Custom Properties✓ Glossary✓ Owners✓ Descriptions✓ Tests✓ Exposures

​Configure dbt workflow

Learn how to configure the dbt workflow to ingest dbt data from your data sources.

Prerequisites for dbt Core: Before configuring the workflow, ensure you have set up artifact storage. dbt Core requires artifacts (manifest.json, catalog.json) to be accessible to OpenMetadata.See the Storage Configuration Overview for setup guides:

AWS S3 | Google Cloud Storage | Azure Blob | HTTP Server | Local/Shared Filesystem

This step is not required for dbt Cloud - artifacts are managed automatically via API.

OpenMetadata supports both dbt Core and dbt Cloud for databases. After metadata ingestion, OpenMetadata extracts model information from dbt and integrates it accordingly.

Additionally, dbt Cloud supports executing models directly. OpenMetadata enables ingestion of these executions as a Pipeline Service for enhanced tracking and visibility.

​Configuration

Once the dbt metadata ingestion pipeline runs successfully and the service entities are available in OpenMetadata, dbt metadata is automatically ingested and associated with the corresponding data assets.

As part of dbt ingestion, OpenMetadata can ingest and apply the following metadata from dbt:

dbt models and their relationships

Model and source lineage

dbt tests and test execution results

dbt tags

dbt owners

dbt descriptions

dbt tiers

dbt glossary terms

This ingestion enriches the Table Entity and populates the dbt tab on the Table Entity page, providing a consolidated view of dbt-related context for each table.

No additional manual configuration is required in the UI after a successful dbt ingestion run.

We can create a workflow that will obtain the dbt information from the dbt files and feed it to OpenMetadata. The dbt Ingestion will be in charge of obtaining this data.

​1. Add a dbt Ingestion

From the Service Page, go to the Ingestions tab to add a new ingestion and click on Add dbt Ingestion.

​2. Configure the dbt Ingestion

Here you can enter the configuration required for OpenMetadata to get the dbt files (manifest.json, catalog.json and run_results.json) required to extract the dbt metadata.

Select any one of the source from below from where the dbt files can be fetched:

Only the manifest.json file is required for dbt ingestion.

​dbt Core

​AWS S3 Buckets

OpenMetadata connects to the AWS s3 bucket via the credentials provided and scans the AWS s3 buckets for manifest.json, catalog.json and run_results.json files.

The name of the s3 bucket and prefix path to the folder in which the dbt files are stored can be provided. In the case where these parameters are not provided all the buckets are scanned for the files.

Follow the link here for instructions on setting up multiple dbt projects.

​Google Cloud Storage Buckets

OpenMetadata connects to the GCS bucket via the credentials provided and scans the gcp buckets for manifest.json, catalog.json and run_results.json files.

The name of the GCS bucket and prefix path to the folder in which the dbt files are stored can be provided. In the case where these parameters are not provided all the buckets are scanned for the files.

GCS credentials can be stored in two ways:

1. Entering the credentials directly into the form

Follow the link here for instructions on setting up multiple dbt projects.

2. Entering the path of file in which the GCS bucket credentials are stored.

For more information on Google Cloud Storage authentication click here.

​Azure Storage Buckets

OpenMetadata connects to Azure Storage using the credentials provided and scans the configured storage containers for manifest.json, catalog.json and run_results.json files.

The Azure Storage account, container name, and optional folder (prefix) path where the dbt files are stored can be provided. If these parameters are not provided, all accessible containers in the storage account are scanned for the files.

Follow the link here for instructions on setting up multiple dbt projects.

​Local Storage

Path of the manifest.json, catalog.json and run_results.json files stored in the local system or in the container in which OpenMetadata server is running can be directly provided.

​File Server

File server path of the manifest.json, catalog.json and run_results.json files stored on a file server directly provided.

​dbt Cloud

Click on the the link here for getting started with dbt cloud account setup if not done already.

The APIs need to be authenticated using an Authentication Token. Follow the link here to generate an authentication token for your dbt cloud account.

The Account Viewer permission is the minimum requirement for the dbt cloud token.

The dbt Cloud workflow leverages the dbt Cloud v2 APIs to retrieve dbt run artifacts (manifest.json, catalog.json, and run_results.json) and ingest the dbt metadata.It uses the /runs API to obtain the most recent successful dbt run, filtering by account_id, project_id and job_id if specified. The artifacts from this run are then collected using the /artifacts API.Refer to the code here

The fields for Dbt Cloud Account Id, Dbt Cloud Project Id and Dbt Cloud Job Id should be numeric values.To know how to get the values for Dbt Cloud Account Id, Dbt Cloud Project Id and Dbt Cloud Job Id fields check here.

​3. Schedule and Deploy

After clicking Next, you will be redirected to the Scheduling form. This will be the same as the Metadata Ingestion. Select your desired schedule and click on Deploy to find the lineage pipeline being added to the Service Ingestions.

Was this page helpful?YesNoSuggest editsRaise issuedbt Artifact Storage - Local Filesystem Configuration | OpenMetadataPreviousRun dbt Workflow Externally | OpenMetadata GuideNext⌘I
