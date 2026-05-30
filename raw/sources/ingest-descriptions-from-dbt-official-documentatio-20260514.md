---
type: clip
title: "Ingest Descriptions from dbt | Official Documentation - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-descriptions"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Ingest Descriptions from dbt | Official Documentation - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-descriptions

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationdbtIngest Descriptions from dbt | Official DocumentationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtOverviewdbt Cloud APIdbt CoreConfigure dbt workflowRun ExternallyAuto Ingest dbt Core ArtifactsIngest dbt OwnerIngest dbt DescriptionsIngest dbt TagsIngest dbt TiersIngest dbt GlossaryIngest dbt DomainIngest dbt Custom PropertiesIngest dbt LineageSetup Multiple dbt Projectsdbt troubleshootingDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOraclePinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageIngest Descriptions from dbtOverriding the existing table and column descriptionsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Ingest Descriptions from dbt

Ingest the descriptions from dbt manifest.json or catalog.json file into OpenMetadata tables and columns.

By default descriptions from manifest.json will be imported. Descriptions from catalog.json will only be updated if catalog.json file is passed.If only the manifest.json file is passed, descriptions from the manifest.json will be updated.If the manifest.json and catalog.json both are passed, descriptions from the catalog.json will be updated.

​Overriding the existing table and column descriptions

To establish a unified and reliable system for descriptions, a single source of truth is necessary. It either is directly OpenMetadata, if individuals want to go there and keep updating, or if they prefer to keep it centralized in dbt, then we can always rely on that directly.

When the Update Descriptions toggle is enabled during the configuration of dbt ingestion, existing descriptions of tables and columns will be overwritten with the dbt descriptions.

If toggle is disabled during the configuration of dbt ingestion, dbt descriptions will only be updated for tables and columns in OpenMetadata that currently have no descriptions. Existing descriptions will remain unchanged and will not be overwritten with dbt descriptions.

Was this page helpful?YesNoSuggest editsRaise issueIngest Owner from dbt | Official DocumentationPreviousIngest Tags from dbt | OpenMetadata Metadata Tagging GuideNext⌘I
