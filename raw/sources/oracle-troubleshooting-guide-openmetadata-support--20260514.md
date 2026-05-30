---
type: clip
title: "Oracle Troubleshooting Guide | OpenMetadata Support - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/oracle/troubleshooting"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Oracle Troubleshooting Guide | OpenMetadata Support - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/oracle/troubleshooting

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationOracleOracle Troubleshooting Guide | OpenMetadata SupportHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOracleOverviewRun ExternallyTroubleshootingPinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageTroubleshootingWorkflow Deployment ErrorConnector Debug TroubleshootingHow to Enable Debug Logging for Any IngestionPermission IssuesDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Troubleshooting

​Workflow Deployment Error

If there were any errors during the workflow deployment process, the

Ingestion Pipeline Entity will still be created, but no workflow will be

present in the Ingestion container.

You can then Edit the Ingestion Pipeline and Deploy it again.

From the Connection tab, you can also Edit the Service if needed.

​Connector Debug Troubleshooting

This section provides instructions to help resolve common issues encountered during connector setup and metadata ingestion in OpenMetadata. Below are some of the most frequently observed troubleshooting scenarios.

​How to Enable Debug Logging for Any Ingestion

To enable debug logging for any ingestion workflow in OpenMetadata:

Navigate to Services

Go to Settings > Services > Service Type (e.g., Database) in the OpenMetadata UI.

Select a Service

Choose the specific service for which you want to enable debug logging.

Access Ingestion Tab

Go to the Ingestion tab and click the three-dot menu on the right-hand side of the ingestion type, and select Edit.

Enable Debug Logging

In the configuration dialog, enable the Debug Log option and click Next.

Schedule and Submit

Configure the schedule if needed and click Submit to apply the changes.

​Permission Issues

If you encounter permission-related errors during connector setup or metadata ingestion, ensure that all the prerequisites and access configurations specified for each connector are properly implemented. Refer to the connector-specific documentation to verify the required permissions.Was this page helpful?YesNoSuggest editsRaise issueRun the Oracle Connector ExternallyPreviousPinotDB Connector | OpenMetadata Real-Time Analytics GuideNext⌘I
