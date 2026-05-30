---
type: clip
title: "Ingest Tags from dbt | OpenMetadata Metadata Tagging Guide - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-tags"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Ingest Tags from dbt | OpenMetadata Metadata Tagging Guide - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-tags

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationdbtIngest Tags from dbt | OpenMetadata Metadata Tagging GuideHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtOverviewdbt Cloud APIdbt CoreConfigure dbt workflowRun ExternallyAuto Ingest dbt Core ArtifactsIngest dbt OwnerIngest dbt DescriptionsIngest dbt TagsIngest dbt TiersIngest dbt GlossaryIngest dbt DomainIngest dbt Custom PropertiesIngest dbt LineageSetup Multiple dbt Projectsdbt troubleshootingDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOraclePinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageIngest Tags from dbtRequirements1. Table-Level Tags information in manifest.json file2. Column-Level Tags information in manifest.json file3. Viewing the tags on tables and columnsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Ingest Tags from dbt

Ingest the table-level tags and column-level tags from manifest.json file

Follow the link here to add the tags to your dbt project.

​Requirements

For dbt tags, if the tag is not already present it will be created under tag category DBTTags in OpenMetadata

​1. Table-Level Tags information in manifest.json file

Openmetadata fetches the table-level tags information from the manifest.json file. Below is a sample manifest.json file node containing tags information under node_name->tags.

{

"model.jaffle_shop.customers": {

"raw_sql": "sample_raw_sql",

"compiled": true,

"resource_type": "model",

"depends_on": {},

"database": "dev",

"schema": "dbt_jaffle",

"tags": [

"model_tag_one",

"model_tag_two"

]

}

}

​2. Column-Level Tags information in manifest.json file

Openmetadata fetches the column-level tags information from the manifest.json file. Below is a sample manifest.json file node containing tags information under node_name->columns->column_name->tags.

"model.jaffle_shop.customers": {

"database": "dev",

"schema": "dbt_jaffle",

"unique_id": "model.jaffle_shop.customers",

"name": "customers",

"alias": "customers",

"columns": {

"first_order": {

"name": "first_order",

"description": "Date (UTC) of a customer's first order",

"meta": {},

"data_type": null,

"quote": null,

"tags": [

"tags_column_one"

]

},

},

},

​3. Viewing the tags on tables and columns

Table and Column level tags ingested from dbt can be viewed on the node in OpenMetadata

Was this page helpful?YesNoSuggest editsRaise issueIngest Descriptions from dbt | Official DocumentationPreviousIngest Tiers from dbt | OpenMetadata Data Tiering GuideNext⌘I
