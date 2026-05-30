---
type: clip
title: "Ingest Lineage from dbt | Official Documentation - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-lineage"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Ingest Lineage from dbt | Official Documentation - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-lineage

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationdbtIngest Lineage from dbt | Official DocumentationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtOverviewdbt Cloud APIdbt CoreConfigure dbt workflowRun ExternallyAuto Ingest dbt Core ArtifactsIngest dbt OwnerIngest dbt DescriptionsIngest dbt TagsIngest dbt TiersIngest dbt GlossaryIngest dbt DomainIngest dbt Custom PropertiesIngest dbt LineageSetup Multiple dbt Projectsdbt troubleshootingDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOraclePinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageIngest Lineage from dbt1. Lineage information from dbt “depends_on” key2. Lineage information from dbt queriesDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Ingest Lineage from dbt

Ingest the lineage information from dbt manifest.json file into OpenMetadata.

OpenMetadata extracts the lineage information from the depends_on and compiled_query/compiled_code keys from the manifest file.

To capture lineage, the compiled_code field must be present in the manifest.json file.

If compiled_code is missing, lineage will not be captured for that node.

To ensure compiled_code is populated in your dbt manifest, run the following commands in your dbt project:

dbt compile

dbt docs generate

​1. Lineage information from dbt “depends_on” key

Openmetadata fetches the lineage information from the manifest.json file. Below is a sample manifest.json file node containing lineage information under node_name->depends_on->nodes.

"model.jaffle_shop.customers": {

"compiled": true,

"resource_type": "model",

"depends_on": {

"macros": [],

"nodes": [

"model.jaffle_shop.stg_customers",

"model.jaffle_shop.stg_orders",

"model.jaffle_shop.stg_payments"

]

}

}

For the above case the lineage will be created as shown in below:

​2. Lineage information from dbt queries

Openmetadata fetches the dbt query information from the manifest.json file.

Below is a sample manifest.json file node containing dbt query information under node_name->compiled_code or node_name->compiled_sql.

"model.jaffle_shop.customers": {

"compiled": true,

"resource_type": "model",

"compiled_code": "Query for the model"

}

The query from dbt will be parsed by the Lineage parser to extract source and target tables to create the lineage.

The lineage may not be created if the lineage parser is not able to parse the query. Please check the logs for any errors in this case.Was this page helpful?YesNoSuggest editsRaise issueIngest Custom Properties from dbt | OpenMetadata Custom Metadata GuidePreviousSetup Multiple dbt Projects | Official DocumentationNext⌘I
