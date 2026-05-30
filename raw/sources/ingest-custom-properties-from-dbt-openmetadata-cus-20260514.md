---
type: clip
title: "Ingest Custom Properties from dbt | OpenMetadata Custom Metadata Guide - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-custom-properties"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Ingest Custom Properties from dbt | OpenMetadata Custom Metadata Guide - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-custom-properties

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationdbtIngest Custom Properties from dbt | OpenMetadata Custom Metadata GuideHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtOverviewdbt Cloud APIdbt CoreConfigure dbt workflowRun ExternallyAuto Ingest dbt Core ArtifactsIngest dbt OwnerIngest dbt DescriptionsIngest dbt TagsIngest dbt TiersIngest dbt GlossaryIngest dbt DomainIngest dbt Custom PropertiesIngest dbt LineageSetup Multiple dbt Projectsdbt troubleshootingDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOraclePinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageIngest Custom Properties from dbtRequirementsSteps for ingesting dbt Custom Properties1. Define Custom Properties in OpenMetadata2. Add Custom Properties in schema.yml file3. Supported Custom Property Types4. Advanced ExamplesEntity ReferenceEntity Reference ListTime IntervalTable Custom Property5. Resulting manifest.json structure6. Viewing Custom Properties in OpenMetadataValidation and Error HandlingComplete ExampleDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Ingest Custom Properties from dbt

Ingest custom property values from manifest.json file to enrich table metadata with organization-specific attributes in OpenMetadata.

Custom properties allow you to extend the standard metadata model with additional fields specific to your organization’s needs, such as SLA hours, data classification levels, or refresh frequencies.

​Requirements

For dbt Custom Properties, the custom properties must be pre-defined on the Table entity type in OpenMetadata before ingestion. If a custom property is not defined, a warning will be logged and that property will be skipped.

​Steps for ingesting dbt Custom Properties

​1. Define Custom Properties in OpenMetadata

Before ingesting custom properties from dbt, you need to define them on the Table entity type in OpenMetadata.

Navigate to Settings > Custom Properties > Tables

Click Add Property

Define the property name and type

For detailed instructions, refer to the Custom Properties documentation.

​2. Add Custom Properties in schema.yml file

To set custom property values for a table in your dbt model, add them under model->name->meta->openmetadata->customProperties in your schema.yml file.

For more details on dbt meta field follow the link here.

models:

- name: customers

meta:

openmetadata:

customProperties:

sla_hours: 24

data_steward: "John Doe"

refresh_frequency: "daily"

description: This table has basic information about a customer

columns:

- name: customer_id

description: This is a unique identifier for a customer

tests:

- unique

- not_null

​3. Supported Custom Property Types

OpenMetadata supports various custom property types. The following table shows all supported types and their expected formats:

TypeDescriptionExample ValuestringPlain text value"value"integerWhole number42numberDecimal number3.14markdownMarkdown formatted text"# Header\nContent"sqlQuerySQL query string"SELECT * FROM table"emailValid email address"user@example.com"date-cpDate string"2024-01-15"dateTime-cpDateTime string"2024-01-15T10:30:00"time-cpTime string"10:30:00"timestampMilliseconds since epoch1705315200000durationISO 8601 duration format"P23DT23H"enumSingle or multi-select value"High" or ["High", "Critical"]entityReferenceReference to another entitySee example belowentityReferenceListList of entity referencesSee example belowtimeIntervalTime interval with start/endSee example belowtable-cpTabular data with rowsSee example below

​4. Advanced Examples

​Entity Reference

Reference another entity (user, team, dashboard, etc.) in OpenMetadata:

models:

- name: customers

meta:

openmetadata:

customProperties:

data_owner:

type: "user"

fqn: "john.doe"

related_dashboard:

type: "dashboard"

fqn: "service.dashboard_name"

​Entity Reference List

Reference multiple entities:

models:

- name: customers

meta:

openmetadata:

customProperties:

stakeholders:

- type: "user"

fqn: "john.doe"

- type: "user"

fqn: "jane.smith"

​Time Interval

Specify a time range with start and end timestamps:

models:

- name: customers

meta:

openmetadata:

customProperties:

valid_period:

start: 1705315200000

end: 1705401600000

​Table Custom Property

For table-type custom properties with rows and columns:

models:

- name: customers

meta:

openmetadata:

customProperties:

data_quality_rules:

- rule_name: "not_null_check"

threshold: 99.5

severity: "high"

- rule_name: "unique_check"

threshold: 100

severity: "critical"

​5. Resulting manifest.json structure

After running your dbt workflow, the generated manifest.json file will include the custom properties under node_name->config->meta->openmetadata->customProperties:

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

"customProperties": {

"sla_hours": 24,

"data_steward": "John Doe",

"refresh_frequency": "daily"

}

}

}

}

}

​6. Viewing Custom Properties in OpenMetadata

Custom properties ingested from dbt can be viewed on the table details page under the Custom Properties section.

​Validation and Error Handling

The ingestion process validates custom property values against their defined types:

ScenarioBehaviorCustom property not defined on Table entityWarning logged, property skippedInvalid value for property typeWarning logged with details, property skippedInvalid enum value (single-select)Warning logged, property skippedInvalid enum value (multi-select)Invalid values filtered out, valid values applied with warningMissing required fields for complex typesWarning logged, property skipped

Example warning message:

Validation failed for custom property 'sla_hours' (type: integer): Expected integer value. Provided value: "24 hours"

​Complete Example

Here’s a comprehensive example showing multiple custom property types:

version: 2

models:

- name: customers

description: "Customer master data table"

meta:

openmetadata:

domain: "Sales"

tier: "Tier.Tier2"

customProperties:

sla_hours: 24

data_classification: "Confidential"

refresh_frequency: "hourly"

last_certified: "2024-01-15"

data_owner:

type: "user"

fqn: "john.doe"

data_quality_rules:

- rule_name: "completeness"

threshold: 99.9

severity: "high"

owner:

- "john_doe"

- "data_engineering_team"

columns:

- name: customer_id

description: "Unique customer identifier"

Was this page helpful?YesNoSuggest editsRaise issueIngest Domain from dbt | OpenMetadata Domain Assignment GuidePreviousIngest Lineage from dbt | Official DocumentationNext⌘I
