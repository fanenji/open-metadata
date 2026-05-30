---
type: clip
title: "dbt Artifact Configuration Guide | OpenMetadata - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/storage-configuration-overview"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# dbt Artifact Configuration Guide | OpenMetadata - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/storage-configuration-overview

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...Navigationdbt Coredbt Artifact Configuration Guide | OpenMetadataHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtOverviewdbt Cloud APIdbt CoreOverviewS3 ConfigurationGCS ConfigurationAzure ConfigurationHTTP ConfigurationLocal ConfigurationConfigure dbt workflowRun ExternallyAuto Ingest dbt Core ArtifactsIngest dbt OwnerIngest dbt DescriptionsIngest dbt TagsIngest dbt TiersIngest dbt GlossaryIngest dbt DomainIngest dbt Custom PropertiesIngest dbt LineageSetup Multiple dbt Projectsdbt troubleshootingDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOraclePinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pagedbt Artifact ConfigurationHow It WorksStorage Options for dbt CoreQuick Setup SummaryAWS S3Google Cloud StorageAzure Blob StorageHTTP ServerLocal/Shared FilesystemCommon Requirements Across All Methods1. Required dbt Artifacts2. dbt Command Sequence3. OpenMetadata ConfigurationTroubleshooting Common IssuesNext StepsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​dbt Artifact Configuration

Using dbt Cloud? You don’t need storage configuration. Go directly to the dbt Cloud API guide for a simpler setup.

This guide is for dbt Core users. When using dbt Core, OpenMetadata needs access to dbt-generated artifacts (manifest.json, catalog.json, run_results.json) to extract metadata, lineage, and test results. Since dbt Core runs within your infrastructure, you must configure a storage method to make these artifacts accessible to OpenMetadata.

​How It Works

If you’re using dbt Core, you need to set up artifact storage:

Generate artifacts: Run dbt run, dbt test, and dbt docs generate to create manifest.json, catalog.json, and run_results.json

Upload to storage: Configure your workflow to upload these files to S3, GCS, Azure, HTTP server, or shared filesystem

Configure OpenMetadata: Point OpenMetadata to the storage location to pull and process the artifacts

​Storage Options for dbt Core

Choose the storage method that matches your infrastructure:

AWS S3Complete S3 setup with Airflow DAG, IAM policies, and configurationGoogle Cloud StorageGCS bucket setup with service accounts and Cloud Composer integrationAzure Blob StorageAzure storage account setup with managed identity and container configHTTP ServerNginx, Apache, or S3+CloudFront configuration for artifact hostingLocal FilesystemDocker volumes, Kubernetes PVC, or NFS shared filesystem setup

​Quick Setup Summary

​AWS S3

# Create bucket

aws s3 mb s3://your-dbt-artifacts

# Upload artifacts (manual)

aws s3 sync target/ s3://your-dbt-artifacts/dbt/ --include "*.json"

# Or use automated Airflow DAG (see detailed guide)

View complete S3 guide →

​Google Cloud Storage

# Create bucket

gsutil mb gs://your-dbt-artifacts

# Upload artifacts (manual)

gsutil -m cp target/*.json gs://your-dbt-artifacts/dbt/

# Or use Cloud Composer DAG (see detailed guide)

View complete GCS guide →

​Azure Blob Storage

# Create storage account and container

az storage account create --name yourdbtartifacts

az storage container create --name dbt-artifacts

# Upload artifacts

az storage blob upload-batch \

--destination dbt-artifacts \

--source target/ \

--pattern "*.json"

View complete Azure guide →

​HTTP Server

# Upload via rsync to static file server

rsync -avz target/*.json user@server:/var/www/dbt/

# Or configure S3 + CloudFront for HTTPS access

View complete HTTP guide →

​Local/Shared Filesystem

# Docker Compose volume mount example

volumes:

- ./dbt/target:/dbt-artifacts

# OpenMetadata reads directly from /dbt-artifacts path

View complete Local guide →

​Common Requirements Across All Methods

Regardless of which storage method you choose, you need:

​1. Required dbt Artifacts

FileGenerated ByPurposemanifest.jsondbt run, dbt compile, dbt buildRequired - Model definitions, sources, lineage, testscatalog.jsondbt docs generateRecommended - Column names, types, descriptionsrun_results.jsondbt test, dbt run, dbt buildOptional - Test execution results and timing

​2. dbt Command Sequence

Run these commands to generate all artifacts:

dbt run          # Execute models, generates manifest.json

dbt test         # Run tests, updates run_results.json

dbt docs generate # Generate catalog.json with column metadata

​3. OpenMetadata Configuration

After artifacts are accessible, configure OpenMetadata ingestion:

UI Method: See Configure dbt Workflow

CLI Method: See Run dbt Workflow Externally

Auto-ingest: See Auto Ingest dbt Core

​Troubleshooting Common Issues

IssuePossible CauseSolutionArtifacts not foundUpload failed or wrong pathVerify artifacts uploaded successfully to correct locationAccess deniedInsufficient permissionsCheck IAM policies, service account permissions, or access keysStale metadataOld artifactsEnsure upload happens after dbt completes; verify timestampsMissing lineageNo compiled_code in manifestRun dbt compile or dbt docs generate before uploadMissing column descriptionsNo catalog.jsonEnsure dbt docs generate runs and catalog.json is uploadedTest results not showingNo run_results.jsonEnsure dbt test runs and run_results.json is uploaded

For storage-specific troubleshooting, see the individual guides.

​Next Steps

Choose your storage method using the decision matrix above

Follow the detailed guide for your chosen method

Configure OpenMetadata ingestion after artifacts are accessible

Set up scheduling to keep metadata synchronized

Questions? See the main dbt Overview or dbt Troubleshooting guide.Was this page helpful?YesNoSuggest editsRaise issuedbt Cloud API Configuration | OpenMetadataPreviousdbt Artifact Storage - AWS S3 Configuration | OpenMetadataNext⌘I
