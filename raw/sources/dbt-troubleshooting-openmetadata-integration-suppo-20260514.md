---
type: clip
title: "dbt Troubleshooting | OpenMetadata Integration Support - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/dbt-troubleshooting"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# dbt Troubleshooting | OpenMetadata Integration Support - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/dbt-troubleshooting

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...Navigationdbtdbt Troubleshooting | OpenMetadata Integration SupportHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtOverviewdbt Cloud APIdbt CoreConfigure dbt workflowRun ExternallyAuto Ingest dbt Core ArtifactsIngest dbt OwnerIngest dbt DescriptionsIngest dbt TagsIngest dbt TiersIngest dbt GlossaryIngest dbt DomainIngest dbt Custom PropertiesIngest dbt LineageSetup Multiple dbt Projectsdbt troubleshootingDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOraclePinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageTroubleshooting1. dbt tab not displaying in the UI2. Lineage not getting displayed from dbt3. An error occurred (AccessDenied) when calling the ListBuckets operation: Access DeniedDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Troubleshooting

​1. dbt tab not displaying in the UI

After the dbt workflow is finished, check the logs to see if the dbt files were successfully validated or not. Any missing keys in the manifest.json or catalog.json files will displayed in the logs and those keys are needed to be added.

The dbt workflow requires the below keys to be present in the node of a manifest.json file:

resource_type (required)

alias/name (any one of them required)

schema (required)

description (required if description needs to be updated)

compiled_code/compiled_sql (required if the dbt model query is to be shown in dbt tab and for query lineage)

depends_on (required if lineage information needs to extracted )

columns (required if column description is to be processed)

The name/alias, schema and database values from dbt manifest.json should match values of the name, schema and database of the table/view ingested in OpenMetadata.dbt will only be processed if these values match

Below is a sample manifest.json node for reference:

"model.jaffle_shop.customers": {

"resource_type": "model",

"depends_on": {

"nodes": [

"model.jaffle_shop.stg_customers",

"model.jaffle_shop.stg_orders",

"model.jaffle_shop.stg_payments"

]

},

"database": "dev",

"schema": "dbt_jaffle",

"name": "customers",

"alias": "customers",

"description": "sample description",

"columns": {

"customer_id": {

"name": "customer_id",

"description": "This is a unique identifier for a customer",

"meta": {},

"data_type": null,

"quote": null,

"tags": []

},

"first_name": {

"name": "first_name",

"description": "Customer's first name. PII.",

"meta": {},

"data_type": null,

"quote": null,

"tags": []

}

},

"compiled_code": "sample query",

}

​2. Lineage not getting displayed from dbt

For dbt lineage to happen we need to have the tables (models) involved previously ingested in OM. The process would be as follows:

We have a dbt project that creates tables A -> B -> C

We run the metadata ingestion in our database service so that A , B and C are ingested in OpenMetadata.

We run the dbt ingestion in the same service so that 2 things would happen:

We will add all the dbt-related metadata to the tables such as the model definition and descriptions.

We will draw the lineage A -> B -> C that comes from the model dependency in the manifest.json

If lineage is not appearing:

Make sure that all the tables are ingested in OpenMetadata.

Follow to docs here to see if necessary details are present in the manifest.json file.

Search for the following string Processing dbt lineage for in the dbt workflow logs and see if any errors are causing the lineage creation to fail.

​3. An error occurred (AccessDenied) when calling the ListBuckets operation: Access Denied

You might see this error when you have placed your dbt artifacts in S3 without the correct policies.

If we have the artifacts on the bucket MyBucket, the user running the ingestion should have, at least, the permissions

from the following policy:

{

"Version": "2012-10-17",

"Statement": [

{

"Effect": "Allow",

"Action": [

"s3:GetObject",

"s3:ListBucket"

],

"Resource": [

"arn:aws:s3:::MyBucket",

"arn:aws:s3:::MyBucket/*"

]

}

]

}

Note that it’s not enough to point the resource to arn:aws:s3:::MyBucket. We need its contents as well!Was this page helpful?YesNoSuggest editsRaise issueSetup Multiple dbt Projects | Official DocumentationPreviousDeltaLake Connector | OpenMetadata Data Lake IntegrationNext⌘I
