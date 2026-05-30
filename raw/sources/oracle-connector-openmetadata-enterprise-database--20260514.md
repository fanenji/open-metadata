---
type: clip
title: "Oracle Connector | OpenMetadata Enterprise Database Guide - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/oracle"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Oracle Connector | OpenMetadata Enterprise Database Guide - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/oracle

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationOracleOracle Connector | OpenMetadata Enterprise Database GuideHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOracleOverviewRun ExternallyTroubleshootingPinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageRequirementsMetadata IngestionConnection DetailsMetadata Ingestion OptionsRelatedDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.OraclePRODFeature List✓ Metadata✓ Query Usage✓ Data Profiler✓ Data Quality✓ dbt✓ Lineage✓ Column-level Lineage✓ Stored Procedures✓ Sample Data✓ Auto-Classification✕ Owners✕ Tags

In this section, we provide guides and references to use the Oracle connector.

Configure and schedule Oracle metadata and profiler workflows from the OpenMetadata UI:

Requirements

Metadata Ingestion

Data Profiler

Data Quality

Lineage

dbt Integration

Troubleshooting

​Requirements

Note: To retrieve metadata from an Oracle database, we use the python-oracledb library, which provides support for versions 12c, 18c, 19c, and 21c.

To ingest metadata from oracle user must have CREATE SESSION privilege for the user.

-- CREATE USER

CREATE USER user_name IDENTIFIED BY admin_password;

-- CREATE ROLE

CREATE ROLE new_role;

-- GRANT ROLE TO USER

GRANT new_role TO user_name;

-- Grant CREATE SESSION Privilege.

--   This allows the role to connect.

GRANT CREATE SESSION TO new_role;

-- Grant SELECT_CATALOG_ROLE Privilege.

--   This allows the role ReadOnly Access to Data Dictionaries

GRANT SELECT_CATALOG_ROLE TO new_role;

If you don’t want to create a role, and directly give permissions to the user, you can take a look at an example given below.

-- Create a New User

CREATE USER my_user IDENTIFIED by my_password;

-- Grant CREATE SESSION Privilege.

--   This allows the user to connect.

GRANT CREATE SESSION TO my_user;

-- Grant SELECT_CATALOG_ROLE Privilege.

--   This allows the user ReadOnly Access to Data Dictionaries

GRANT SELECT_CATALOG_ROLE to my_user;

Note: With just these permissions, your user should be able to ingest the metadata, but not the Profiler & Data Quality, you should grant SELECT permissions to the tables you are interested in for the Profiler & Data Quality features to work.

-- If you are using a role and do not want to specify a specific table, but any

GRANT SELECT ANY TABLE TO new_role;

-- If you are not using a role, but directly giving permission to the user and do not want to specify a specific table, but any

GRANT SELECT ANY TABLE TO my_user;

-- if you are using role

GRANT SELECT ON ADMIN.EXAMPLE_TABLE TO new_role;

-- if you are not using role, but directly giving permission to the user

GRANT SELECT ON ADMIN.EXAMPLE_TABLE TO my_user;

-- if you are using role

GRANT SELECT ON {schema}.{table} TO new_role;

-- if you are not using role, but directly giving permission to the user

GRANT SELECT ON {schema}.{table} TO my_user;

You can find further information here. Note that

there is no routine out of the box in Oracle to grant SELECT to a full schema.

​Metadata Ingestion

To ingest metadata from your sources, you need to create a service connection. The service connects your source system with OpenMetadata. Once you create a service, you can use it to configure your ingestion workflows.To create a service connection and ingest your metadata, follow the steps below:1Select the ServiceOn the left navigation bar, click Settings.On the next page, click Services, and then select the service.2Create a New ServiceTo add a new service connection, click Add New Service.3Select the ConnectorSelect Oracle as the service type and click Next.4Name and Describe the ServiceEnter a unique Service Name and Description.Service Name: OpenMetadata identifies services by their service name. Enter a name that distinguishes this deployment from other services, including other Oracle services you are ingesting metadata from.The service name cannot be changed after it is set.5Configure the Service ConnectionSet up the connection settings required for Oracle to set up the service and start ingesting metadata from your sources. The right-hand panel displays help documentation for the selected connection type in the product UI.

​Connection Details

1Connection DetailsWhen using a Hybrid Ingestion Runner, any sensitive credential fields—such as passwords, API keys, or private keys—must reference secrets using the following format:password: secret:/my/database/password

This applies only to fields marked as secrets in the connection form (these typically mask input and show a visibility toggle icon).

For a complete guide on managing secrets in hybrid setups, see the Hybrid Ingestion Runner Secret Management Guide.

Username: Specify the User to connect to Oracle. It should have enough privileges to read all the metadata.

Password: Password to connect to Oracle.

Host and Port: Enter the fully qualified hostname and port number for your Oracle deployment in the Host and Port field.

Database Name: Optional name to give to the database in OpenMetadata. If left blank, we will use default as the database name. It is recommended to use the database name same as the SID, This ensures accurate results and proper identification of tables during profiling, data quality checks and dbt workflow.

Oracle Connection Type : Select the Oracle Connection Type. The type can either be Oracle Service Name or Database Schema

Oracle Service Name: The Oracle Service name is the TNS alias that you give when you remotely connect to your database and this Service name is recorded in tnsnames.

Database Schema: The name of the database schema available in Oracle that you want to connect with.

Oracle instant client directory: The directory pointing to where the instantclient binaries for Oracle are located. In the ingestion Docker image we

provide them by default at /instantclient. If this parameter is informed (it is by default), we will run the thick oracle client.

We are shipping the binaries for ARM and AMD architectures from here

and here for the instant client version 19.

2Advanced ConfigurationDatabase Services have an Advanced Configuration section, where you can pass extra arguments to the connector

and, if needed, change the connection Scheme.This would only be required to handle advanced connectivity scenarios or customizations.

Connection Options (Optional): Enter the details for any additional connection options that can be sent to database during the connection. These details must be added as Key-Value pairs.

Connection Arguments (Optional): Enter the details for any additional connection arguments such as security or protocol configs that can be sent during the connection. These details must be added as Key-Value pairs.

3Test the ConnectionOnce the credentials have been added, click on Test Connection and Save the changes.4Configure Metadata IngestionIn this step we will configure the metadata ingestion pipeline,

Please follow the instructions below​Metadata Ingestion OptionsIf the owner’s name is openmetadata, you need to enter openmetadata@domain.com in the name section of add team/user form, click here for more info.

Name: This field refers to the name of ingestion pipeline, you can customize the name or use the generated name.

Database Filter Pattern (Optional): Use to database filter patterns to control whether or not to include database as part of metadata ingestion.

Include: Explicitly include databases by adding a list of comma-separated regular expressions to the Include field. OpenMetadata will include all databases with names matching one or more of the supplied regular expressions. All other databases will be excluded.

Exclude: Explicitly exclude databases by adding a list of comma-separated regular expressions to the Exclude field. OpenMetadata will exclude all databases with names matching one or more of the supplied regular expressions. All other databases will be included.

Schema Filter Pattern (Optional): Use to schema filter patterns to control whether to include schemas as part of metadata ingestion.

Include: Explicitly include schemas by adding a list of comma-separated regular expressions to the Include field. OpenMetadata will include all schemas with names matching one or more of the supplied regular expressions. All other schemas will be excluded.

Exclude: Explicitly exclude schemas by adding a list of comma-separated regular expressions to the Exclude field. OpenMetadata will exclude all schemas with names matching one or more of the supplied regular expressions. All other schemas will be included.

Table Filter Pattern (Optional): Use to table filter patterns to control whether to include tables as part of metadata ingestion.

Include: Explicitly include tables by adding a list of comma-separated regular expressions to the Include field. OpenMetadata will include all tables with names matching one or more of the supplied regular expressions. All other tables will be excluded.

Exclude: Explicitly exclude tables by adding a list of comma-separated regular expressions to the Exclude field. OpenMetadata will exclude all tables with names matching one or more of the supplied regular expressions. All other tables will be included.

Enable Debug Log (toggle): Set the Enable Debug Log toggle to set the default log level to debug.

Mark Deleted Tables (toggle): Set the Mark Deleted Tables toggle to flag tables as soft-deleted if they are not present anymore in the source system.

Mark Deleted Tables from Filter Only (toggle): Set the Mark Deleted Tables from Filter Only toggle to flag tables as soft-deleted if they are not present anymore within the filtered schema or database only. This flag is useful when you have more than one ingestion pipelines. For example if you have a schema

includeTables (toggle): Optional configuration to turn off fetching metadata for tables.

includeViews (toggle): Set the Include views toggle to control whether to include views as part of metadata ingestion.

includeTags (toggle): Set the ‘Include Tags’ toggle to control whether to include tags as part of metadata ingestion.

includeOwners (toggle): Set the ‘Include Owners’ toggle to control whether to include owners to the ingested entity if the owner email matches with a user stored in the OM server as part of metadata ingestion. If the ingested entity already exists and has an owner, the owner will not be overwritten.

includeStoredProcedures (toggle): Optional configuration to toggle the Stored Procedures ingestion.

includeDDL (toggle): Optional configuration to toggle the DDL Statements ingestion.

queryLogDuration (Optional): Configuration to tune how far we want to look back in query logs to process Stored Procedures results.

queryParsingTimeoutLimit (Optional): Configuration to set the timeout for parsing the query in seconds.

useFqnForFiltering (toggle): Regex will be applied on fully qualified name (e.g service_name.db_name.schema_name.table_name) instead of raw name (e.g. table_name).

Incremental (Beta): Use Incremental Metadata Extraction after the first execution. This is done by getting the changed tables instead of all of them. Only Available for BigQuery, Redshift and Snowflake

Enabled: If True, enables Metadata Extraction to be Incremental.

lookback Days: Number of days to search back for a successful pipeline run. The timestamp of the last found successful pipeline run will be used as a base to search for updated entities.

Safety Margin Days: Number of days to add to the last successful pipeline run timestamp to search for updated entities.

Threads (Beta): Use a Multithread approach for Metadata Extraction. You can define here the number of threads you would like to run concurrently.

Note that the right-hand side panel in the OpenMetadata UI will also share useful documentation when configuring the ingestion.5Schedule the Ingestion and DeployScheduling can be set up at an hourly, daily, weekly, or manual cadence. The

timezone is in UTC. Select a Start Date to schedule for ingestion. It is

optional to add an End Date.Review your configuration settings. If they match what you intended,

click Deploy to create the service and schedule metadata ingestion.If something doesn’t look right, click the Back button to return to the

appropriate step and change the settings as needed.After configuring the workflow, you can click on Deploy to create the

pipeline.6View the Ingestion PipelineOnce the workflow has been successfully deployed, you can view the

Ingestion Pipeline running from the Service Page.If AutoPilot is enabled, workflows like usage tracking, data lineage, and similar tasks will be handled automatically. Users don’t need to set up or manage them - AutoPilot takes care of everything in the system.

​Related

Usage WorkflowLearn more about how to configure the Usage Workflow to ingest Query information from the UI.Lineage WorkflowLearn more about how to configure the Lineage from the UI.Profiler WorkflowLearn more about how to configure the Data Profiler from the UI.Data Quality WorkflowLearn more about how to configure the Data Quality tests from the UI.dbt IntegrationLearn more about how to ingest dbt models’ definitions and their lineage.Was this page helpful?YesNoSuggest editsRaise issueMySQL Troubleshooting Guide | OpenMetadata SupportPreviousRun the Oracle Connector ExternallyNext⌘I
