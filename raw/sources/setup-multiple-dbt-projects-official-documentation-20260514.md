---
type: clip
title: "Setup Multiple dbt Projects | Official Documentation - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/setup-multiple-dbt-projects"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Setup Multiple dbt Projects | Official Documentation - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/setup-multiple-dbt-projects

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationdbtSetup Multiple dbt Projects | Official DocumentationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtOverviewdbt Cloud APIdbt CoreConfigure dbt workflowRun ExternallyAuto Ingest dbt Core ArtifactsIngest dbt OwnerIngest dbt DescriptionsIngest dbt TagsIngest dbt TiersIngest dbt GlossaryIngest dbt DomainIngest dbt Custom PropertiesIngest dbt LineageSetup Multiple dbt Projectsdbt troubleshootingDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOraclePinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageSetup Multiple dbt Projects1. Organizing the dbt Files in the S3 Bucket2. Setup the configuration in OpenMetadata3. Run the dbt WorkflowDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Setup Multiple dbt Projects

You can set up the dbt workflow to ingest metadata from multiple dbt projects, each containing multiple manifest.json, catalog.json, and run_results.json files.

This functionality is supported for s3, GCS, and Azure configurations only.

To ensure the workflow operates smoothly, organize the dbt files for each project into separate directories and name the files manifest.json, catalog.json, and run_results.json.

If your dbt tests are split across multiple run_results.json files, place these files in the same directory as their corresponding manifest.json file. Ensure that each file retains run_results in its name, and append a unique suffix as needed. For example: run_results_one.json, run_results_two.json, run_results_three.json

The workflow will scan through the specified prefix path in the designated bucket, traversing each folder to locate these dbt files.

Here’s an example of setting up the dbt workflow for multiple dbt projects in an s3 configuration:

​1. Organizing the dbt Files in the S3 Bucket

Place the dbt files (manifest.json, catalog.json, and run_results.json) in separate directories within the S3 bucket.

For this example, let’s explore a directory structure where we have set up three distinct dbt projects: dbt_project_one, dbt_project_two, and dbt_project_three. We will configure the dbt workflow to pickup the dbt files from each of these directories.

Bucket name: dbt_bucket

bucket_home/

├── dbt_files/

├── dbt_project_one/

│   ├── manifest.json

│   ├── catalog.json

│   └── run_results.json

└── dbt_new_projects/

├── dbt_project_two/

│   ├── manifest.json

│   ├── catalog.json

│   └── run_results_one.json

|   └── run_results_two.json

|   └── run_results_three.json

└── dbt_project_three/

├── manifest.json

├── catalog.json

└── run_results.json

​2. Setup the configuration in OpenMetadata

In the dbt Bucket Name field, enter the name of your bucket, which in this case is dbt_bucket.

Specify the dbt Object Prefix path for the parent folder where your dbt projects are located. In this example, the prefix path should be set to bucket_home/dbt_files/.

If you wish to scan the entire bucket, only enter the dbt Bucket Name and keep the dbt Object Prefix field empty.

​3. Run the dbt Workflow

After running the dbt workflow, the dbt metadata from all the three projects will be ingested.Was this page helpful?YesNoSuggest editsRaise issueIngest Lineage from dbt | Official DocumentationPreviousdbt Troubleshooting | OpenMetadata Integration SupportNext⌘I
