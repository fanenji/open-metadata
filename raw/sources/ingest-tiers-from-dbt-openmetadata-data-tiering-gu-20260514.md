---
type: clip
title: "Ingest Tiers from dbt | OpenMetadata Data Tiering Guide - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-tier"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Ingest Tiers from dbt | OpenMetadata Data Tiering Guide - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-tier

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationdbtIngest Tiers from dbt | OpenMetadata Data Tiering GuideHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtOverviewdbt Cloud APIdbt CoreConfigure dbt workflowRun ExternallyAuto Ingest dbt Core ArtifactsIngest dbt OwnerIngest dbt DescriptionsIngest dbt TagsIngest dbt TiersIngest dbt GlossaryIngest dbt DomainIngest dbt Custom PropertiesIngest dbt LineageSetup Multiple dbt Projectsdbt troubleshootingDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOraclePinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageIngest Tiers from dbtRequirementsSteps for ingesting dbt Tier1. Add a Tier at OpenMetadata or Select a Tier2. Add Table-Level Tier information in schema.yml file3. Viewing the Tier on tablesDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Ingest Tiers from dbt

Ingest the table-level tier from manifest.json file

​Requirements

For dbt Tier, Tiers must be created or present in OpenMetadata beforehand for data ingestion to work.

​Steps for ingesting dbt Tier

​1. Add a Tier at OpenMetadata or Select a Tier

Tiering is an important concept of data classification in OpenMetadata. Tiers should be based on the importance of data. Using Tiers, data producers or owners can define the importance of data to an organization.

For details on adding or selecting tiers, refer to the OpenMetadata documentation

​2. Add Table-Level Tier information in schema.yml file

Suppose you want to add the Tier Tier2 to a table model customers.

Go to your schema.yml file at dbt containing the table model information customers and add the tier FQN under model->name->meta->openmetadata->tier as Tier.Tier2.

For more details on dbt meta field follow the link here

models:

- name: customers

meta:

openmetadata:

tier: 'Tier.Tier2'

description: This table has basic information about a customer, as well as some derived facts based on a customer's orders

columns:

- name: customer_id

description: This is a unique identifier for a customer

tests:

- unique

- not_null

After adding the tier information to your schema.yml file, run your dbt workflow. The generated manifest.json file will then reflect the tier assignment. You’ll find it under node_name->config->meta->openmetadata->tier as Tier.Tier2.

"model.jaffle_shop.customers": {

"raw_sql": "sample_raw_sql",

"compiled": true,

"resource_type": "model",

"depends_on": {},

"database": "dev",

"schema": "dbt_jaffle",

"config": {

"enabled": true,

"alias": null,

"meta": {

"openmetadata": {

"tier": "Tier.Tier2"

}

}

}

}

​3. Viewing the Tier on tables

Table level Tier ingested from dbt can be viewed on the node in OpenMetadata

Was this page helpful?YesNoSuggest editsRaise issueIngest Tags from dbt | OpenMetadata Metadata Tagging GuidePreviousIngest Glossary from dbt | Official DocumentationNext⌘I
