---
type: clip
title: "Run the Oracle Connector Externally - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/oracle/yaml"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Run the Oracle Connector Externally - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/oracle/yaml

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationOracleRun the Oracle Connector ExternallyHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOracleOverviewRun ExternallyTroubleshootingPinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.OraclePRODFeature List✓ Metadata✓ Query Usage✓ Data Profiler✓ Data Quality✓ dbt✓ Lineage✓ Column-level Lineage✓ Stored Procedures✓ Sample Data✓ Auto-Classification✕ Owners✕ Tags

In this section, we provide guides and references to use the Oracle connector.

Configure and schedule Oracle metadata and profiler workflows from the OpenMetadata UI:

Requirements

Metadata Ingestion

Data Profiler

Data Quality

Lineage

dbt Integration

​How to Run the Connector Externally

To run the Ingestion via the UI you’ll need to use the OpenMetadata Ingestion Container, which comes shipped with

custom Airflow plugins to handle the workflow deployment.

If, instead, you want to manage your workflows externally on your preferred orchestrator, you can check

the following docs to run the Ingestion Framework anywhere.

External SchedulersGet more information about running the Ingestion Framework Externally

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

​Python Requirements

We have support for Python versions 3.9-3.11

To run the Oracle ingestion, you will need to install:

pip3 install "openmetadata-ingestion[oracle]"

​Metadata Ingestion

All connectors are defined as JSON Schemas.

Here

you can find the structure to create a connection to Oracle.

In order to create and run a Metadata Ingestion workflow, we will follow

the steps to create a YAML configuration able to connect to the source,

process the Entities if needed, and reach the OpenMetadata server.

The workflow is modeled around the following

JSON Schema

​1. Define the YAML Config

This is a sample config for Oracle:

Source ConfigurationConfigure the source type and service name for your Oracle connector.Usernameusername: Specify the User to connect to Oracle. It should have enough privileges to read all the metadata.Passwordpassword: Password to connect to Oracle.Host PorthostPort: Enter the fully qualified hostname and port number for your Oracle deployment in the Host and Port field.Oracle Connection TypeoracleConnectionType :

oracleServiceName: The Oracle Service name is the TNS alias that you give when you remotely connect to your database and this Service name is recorded in tnsnames.

databaseSchema: The name of the database schema available in Oracle that you want to connect with.

Oracle instant client directory: The directory pointing to where the instantclient binaries for Oracle are located. In the ingestion Docker image we provide them by default at /instantclient. If this parameter is informed (it is by default), we will run the thick oracle client.

We are shipping the binaries for ARM and AMD architectures from here and here for the instant client version 19.Database NamedatabaseName: Optional name to give to the database in OpenMetadata. If left blank, we will use default as the database name. It is recommended to use the database name same as the SID, This ensures accurate results and proper identification of tables during profiling, data quality checks and dbt workflow.Connection Options​Advanced ConfigurationConnection Options (Optional): Enter the details for any additional connection options that can be sent to database during the connection. These details must be added as Key-Value pairs.Connection ArgumentsConnection Arguments (Optional): Enter the details for any additional connection arguments such as security or protocol configs that can be sent to database during the connection. These details must be added as Key-Value pairs.

In case you are using Single-Sign-On (SSO) for authentication, add the authenticator details in the Connection Arguments as a Key-Value pair as follows: "authenticator" : "sso_login_url"

Source Config​Source Configuration - Source ConfigThe sourceConfig is defined here:markDeletedTables: To flag tables as soft-deleted if they are not present anymore in the source system.markDeletedStoredProcedures: Optional configuration to soft delete stored procedures in OpenMetadata if the source stored procedures are deleted. Also, if the stored procedures is deleted, all the associated entities like lineage, etc., with that stored procedures will be deleted.markDeletedSchemas: Optional configuration to soft delete schemas stored in OpenMetadata if the source schema is deleted. Setting this flag to true will only keep filtered schema and delete any other schemas that do not match schemaFilterPattern or do not exist at source.markDeletedDatabases: Additional optional configuration for soft deletion, providing granular option to select which particular entities should be deleted.includeTables: true or false, to ingest table data. Default is true.includeViews: true or false, to ingest views definitions.includeTags: Optional configuration to toggle the tags ingestion.includeOwners: Set the ‘Include Owners’ toggle to control whether to include owners to the ingested entity if the owner email matches with a user stored in the OM server as part of metadata ingestion. If the ingested entity already exists and has an owner, the owner will not be overwritten.includeStoredProcedures: Optional configuration to toggle the Stored Procedures ingestion.includeDDL: Optional configuration to toggle the DDL Statements ingestion.overrideMetadata (boolean): Set the ‘Override Metadata’ toggle to control whether to override the existing metadata in the OpenMetadata server with the metadata fetched from the source. If the toggle is set to true, the metadata fetched from the source will override the existing metadata in the OpenMetadata server. If the toggle is set to false, the metadata fetched from the source will not override the existing metadata in the OpenMetadata server. This is applicable for fields like description, tags, owner and displayName.queryLogDuration: Configuration to tune how far we want to look back in query logs to process Stored Procedures results.queryParsingTimeoutLimit: Configuration to set the timeout for parsing the query in seconds.useFqnForFiltering: Regex will be applied on fully qualified name (e.g service_name.db_name.schema_name.table_name) instead of raw name (e.g. table_name).databaseFilterPattern, schemaFilterPattern: Note that the filter supports regex as include or exclude. You can find examples heretableFilterPattern: Note that the filter supports regex as include or exclude. You can find examples herethreads (beta): The number of threads to use when extracting the metadata using multithreading.databaseMetadataConfigType (string): Database Source Config Metadata Pipeline type.incremental (beta): Incremental Extraction configuration. Currently implemented for:

BigQuery

Redshift

Snowflake

Sink ConfigurationTo send the metadata to OpenMetadata, it needs to be specified as type: metadata-rest.Workflow ConfigurationThe main property here is the openMetadataServerConfig, where you can define the host and security provider of your OpenMetadata installation.Logger LevelYou can specify the loggerLevel depending on your needs. If you are trying to troubleshoot an ingestion, running with DEBUG will give you far more traces for identifying issues.JWT TokenJWT tokens will allow your clients to authenticate against the OpenMetadata server. To enable JWT Tokens, you will get more details here.You can refer to the JWT Troubleshooting section link for any issues in your JWT configuration.Store Service ConnectionIf set to true (default), we will store the sensitive information either encrypted via the Fernet Key in the database or externally, if you have configured any Secrets Manager.If set to false, the service will be created, but the service connection information will only be used by the Ingestion Framework at runtime, and won’t be sent to the OpenMetadata server.SSL ConfigurationIf you have added SSL to the OpenMetadata server, then you will need to handle the certificates when running the ingestion too. You can either set verifySSL to ignore, or have it as validate, which will require you to set the sslConfig.caCertificate with a local path where your ingestion runs that points to the server certificate file.Find more information on how to troubleshoot SSL issues here.ingestionPipelineFQNFully qualified name of ingestion pipeline, used to identify the current ingestion pipeline.oracle_config.yamlsource:  type: oracle  serviceName: local_oracle  serviceConnection:    config:      type: Oracle      hostPort: hostPort      username: username      password: password      # The type can either be oracleServiceName or databaseSchema      oracleConnectionType:        oracleServiceName: serviceName        # databaseSchema: schema      databaseName: custom_db_display_name      # connectionOptions:      #   key: value      # connectionArguments:      #   key: value  sourceConfig:    config:      type: DatabaseMetadata      markDeletedTables: true      markDeletedStoredProcedures: true      markDeletedSchemas: true      markDeletedDatabases: true      includeTables: true      includeViews: true      # includeTags: true      # includeOwners: false      # includeStoredProcedures: true      # includeDDL: true      # overrideMetadata: false      # queryLogDuration: 1      # queryParsingTimeoutLimit: 300      # useFqnForFiltering: false      # threads: 1      # databaseMetadataConfigType: ()      # incremental:      #   enabled: true      #   lookbackDays: 7      #   safetyMarginDays: 1      # databaseFilterPattern:      #   includes:      #     - database1      #     - database2      #   excludes:      #     - database3      #     - database4      # schemaFilterPattern:      #   includes:      #     - schema1      #     - schema2      #   excludes:      #     - schema3      #     - schema4      # tableFilterPattern:      #   includes:      #     - users      #     - type_test      #   excludes:      #     - table3      #     - table4sink:  type: metadata-rest  config: {}workflowConfig:  loggerLevel: INFO  # DEBUG, INFO, WARNING or ERROR  openMetadataServerConfig:    hostPort: "http://localhost:8585/api"    authProvider: openmetadata    securityConfig:      jwtToken: "{bot_jwt_token}"    ## Store the service Connection information    storeServiceConnection: true  # false    ## Secrets Manager Configuration    # secretsManagerProvider: aws, azure or noop    # secretsManagerLoader: airflow or env    ## If SSL, fill the following    # verifySSL: validate  # or ignore    # sslConfig:    #   caCertificate: /local/path/to/certificate# ingestionPipelineFQN: <service name>.<ingestion name> ## e.g., "my_redshift.metadata"

​2. Run with the CLI

First, we will need to save the YAML file. Afterward, and with all requirements installed, we can run:

metadata ingest -c <path-to-yaml>

Note that from connector to connector, this recipe will always be the same. By updating the YAML configuration,

you will be able to extract metadata from different sources.

​Data Profiler

The Data Profiler workflow will be using the orm-profiler processor.

After running a Metadata Ingestion workflow, we can run the Data Profiler workflow.

While the serviceName will be the same to that was used in Metadata Ingestion, so the ingestion bot can get the serviceConnection details from the server.

​1. Define the YAML Config

This is a sample config for the profiler:

Source ConfigurationConfigure the source type and service name for your profiler workflow.Profiler Config Typetype: Set to Profiler for data profiling ingestion.Profile SampleprofileSample: Percentage of data or no. of rows we want to execute the profiler and tests on.Thread CountthreadCount: Number of threads to use during metric computations.Timeout SecondstimeoutSeconds: Profiler Timeout in Seconds.Database Filter PatterndatabaseFilterPattern: Regex to only fetch databases that matches the pattern.Schema Filter PatternschemaFilterPattern: Regex to only fetch tables or databases that matches the pattern.Table Filter PatterntableFilterPattern: Regex to only fetch tables or databases that matches the pattern.Processor ConfigurationChoose the orm-profiler. Its config can also be updated to define tests from the YAML itself instead of the UI.tableConfig: tableConfig allows you to set up some configuration at the table level including:

Profile sample settings per table

Custom profile queries

Column-level configuration (include/exclude columns, specific metrics)

Partition configuration for large tables

Sink ConfigurationTo send the metadata to OpenMetadata, it needs to be specified as type: metadata-rest.{connector}_profiler.yamlsource:  type: {connector}  serviceName: {connector}  sourceConfig:    config:      type: Profiler      # profileSample: 85      # threadCount: 5      # timeoutSeconds: 43200      # databaseFilterPattern:      #   includes:      #     - database1      #     - database2      #   excludes:      #     - database3      # schemaFilterPattern:      #   includes:      #     - schema1      #     - schema2      #   excludes:      #     - schema3      # tableFilterPattern:      #   includes:      #     - table1      #     - table2      #   excludes:      #     - table3processor:  type: orm-profiler  config: {}  # Remove braces if adding properties    # tableConfig:    #   - fullyQualifiedName: <table fqn>    #     profileSample: <number between 0 and 99> # default will be 100 if omitted    #     profileQuery: <query to use for sampling data for the profiler>    #     columnConfig:    #       excludeColumns:    #         - <column name>    #       includeColumns:    #         - columnName: <column name>    #         - metrics:    #           - MEAN    #           - MEDIAN    #           - ...    #     partitionConfig:    #       enablePartitioning: <set to true to use partitioning>    #       partitionColumnName: <partition column name>    #       partitionIntervalType: <TIME-UNIT, INTEGER-RANGE, INGESTION-TIME, COLUMN-VALUE>    #       Pick one of the variation shown below    #       ----'TIME-UNIT' or 'INGESTION-TIME'-------    #       partitionInterval: <partition interval>    #       partitionIntervalUnit: <YEAR, MONTH, DAY, HOUR>    #       ------------'INTEGER-RANGE'---------------    #       partitionIntegerRangeStart: <integer>    #       partitionIntegerRangeEnd: <integer>    #       -----------'COLUMN-VALUE'----------------    #       partitionValues:    #         - <value>    #         - <value>sink:  type: metadata-rest  config: {}

You can learn more about how to configure and run the Profiler Workflow to extract Profiler data and execute the Data Quality from here

​2. Run with the CLI

After saving the YAML config, we will run the command the same way we did for the metadata ingestion:

metadata profile -c <path-to-yaml>

Note now instead of running ingest, we are using the profile command to select the Profiler workflow.

Data ProfilerFind more information about the Data Profiler here

​Auto Classification

The Auto Classification workflow will be using the orm-profiler processor.

After running a Metadata Ingestion workflow, we can run the Auto Classification workflow.

While the serviceName will be the same to that was used in Metadata Ingestion, so the ingestion bot can get the serviceConnection details from the server.

​1. Define the YAML Config

This is a sample config for the Auto Classification Workflow:

Source ConfigurationConfigure the source type and service name for your auto classification workflow.Auto Classification Config Typetype: Set to AutoClassification for automatic PII tagging.Store Sample DatastoreSampleData: Option to turn on/off storing sample data. If enabled, we will ingest sample data for each table.Enable Auto ClassificationenableAutoClassification: Optional configuration to automatically tag columns that might contain sensitive information.Confidenceconfidence: Set the Confidence value for which you want the column to be tagged as PII. Confidence value ranges from 0 to 100. A higher number will yield less false positives but more false negatives. A lower number will yield more false positives but less false negatives.Database Filter PatterndatabaseFilterPattern: Regex to only fetch databases that matches the pattern.Schema Filter PatternschemaFilterPattern: Regex to only fetch tables or databases that matches the pattern.Table Filter PatterntableFilterPattern: Regex to only fetch tables or databases that matches the pattern.Processor ConfigurationChoose the orm-profiler. Its config can also be updated to define tests from the YAML itself instead of the UI.tableConfig: tableConfig allows you to set up some configuration at the table level.Sink ConfigurationTo send the metadata to OpenMetadata, it needs to be specified as type: metadata-rest.{connector}_auto_classification.yamlsource:  type: {connector}  serviceName: {connector}  sourceConfig:    config:      type: AutoClassification      # storeSampleData: true      # enableAutoClassification: true      # confidence: 80      # databaseFilterPattern:      #   includes:      #     - database1      #     - database2      #   excludes:      #     - database3      # schemaFilterPattern:      #   includes:      #     - schema1      #     - schema2      #   excludes:      #     - schema3      # tableFilterPattern:      #   includes:      #     - table1      #     - table2      #   excludes:      #     - table3processor:  type: orm-profiler  config: {}sink:  type: metadata-rest  config: {}

​2. Run with the CLI

After saving the YAML config, we will run the command the same way we did for the metadata ingestion:

metadata classify -c <path-to-yaml>

Now instead of running ingest, we are using the classify command to select the Auto Classification workflow.

​Data Quality

​Adding Data Quality Test Cases from yaml config

When creating a JSON config for a test workflow the source configuration is very simple.

source:

type: TestSuite

serviceName: <your_service_name>

sourceConfig:

config:

type: TestSuite

entityFullyQualifiedName: <entityFqn>

The only sections you need to modify here are the serviceName (this name needs to be unique) and entityFullyQualifiedName (the entity for which we’ll be executing tests against) keys.

Once you have defined your source configuration you’ll need to define te processor configuration.

processor:

type: "orm-test-runner"

config:

forceUpdate: <false|true>

testCases:

- name: <testCaseName>

testDefinitionName: columnValueLengthsToBeBetween

columnName: <columnName>

parameterValues:

- name: minLength

value: 10

- name: maxLength

value: 25

- name: <testCaseName>

testDefinitionName: tableRowCountToEqual

parameterValues:

- name: value

value: 10

The processor type should be set to  "orm-test-runner". For accepted test definition names and parameter value names refer to the tests page.

Note that while you can define tests directly in this YAML configuration, running the

workflow will execute ALL THE TESTS present in the table, regardless of what you are defining in the YAML.This makes it easy for any user to contribute tests via the UI, while maintaining the test execution external.

You can keep your YAML config as simple as follows if the table already has tests.

processor:

type: "orm-test-runner"

config: {}

​Key reference:

forceUpdate: if the test case exists (base on the test case name) for the entity, implements the strategy to follow when running the test (i.e. whether or not to update parameters)

testCases: list of test cases to add to the entity referenced. Note that we will execute all the tests present in the Table.

name: test case name

testDefinitionName: test definition

columnName: only applies to column test. The name of the column to run the test against

parameterValues: parameter values of the test

The sink and workflowConfig will have the same settings as the ingestion and profiler workflow.

​Full  yaml config example

source:

type: TestSuite

serviceName: MyAwesomeTestSuite

sourceConfig:

config:

type: TestSuite

entityFullyQualifiedName: MySQL.default.openmetadata_db.tag_usage

#     testCases: ["run_only_this_test_case"] # Optional, if not provided all tests will be executed

processor:

type: "orm-test-runner"

config:

forceUpdate: false

testCases:

- name: column_value_length_tagFQN

testDefinitionName: columnValueLengthsToBeBetween

columnName: tagFQN

parameterValues:

- name: minLength

value: 10

- name: maxLength

value: 25

- name: table_row_count_test

testDefinitionName: tableRowCountToEqual

parameterValues:

- name: value

value: 10

sink:

type: metadata-rest

config: {}

workflowConfig:

openMetadataServerConfig:

hostPort: <OpenMetadata host and port>

authProvider: <OpenMetadata auth provider>

​How to Run Tests

To run the tests from the CLI execute the following command

metadata test -c /path/to/my/config.yaml

​Lineage

After running a Metadata Ingestion workflow, we can run Lineage workflow.

While the serviceName will be the same to that was used in Metadata Ingestion, so the ingestion bot can get the serviceConnection details from the server.

​1. Define the YAML Config

This is a sample config for oracle Lineage:

Source ConfigurationConfigure the source type and service name for your lineage workflow.You can find all the definitions and types for the sourceConfig here.Lineage Config Typetype: Set to DatabaseLineage for database lineage ingestion.Query Log DurationqueryLogDuration: Configuration to tune how far we want to look back in query logs to process lineage data in days.Parsing Timeout LimitparsingTimeoutLimit: Configuration to set the timeout for parsing the query in seconds.Filter ConditionfilterCondition: Condition to filter the query history.Result LimitresultLimit: Configuration to set the limit for query logs.Query Log File PathqueryLogFilePath: Configuration to set the file path for query logs. If instead of getting the query logs from the database we want to pass a file with the queries.Database Filter PatterndatabaseFilterPattern: Regex to only fetch databases that matches the pattern.Schema Filter PatternschemaFilterPattern: Regex to only fetch tables or databases that matches the pattern.Table Filter PatterntableFilterPattern: Regex to only fetch tables or databases that matches the pattern.Override View LineageoverrideViewLineage: Set the ‘Override View Lineage’ toggle to control whether to override the existing view lineage.Process View LineageprocessViewLineage: Set the ‘Process View Lineage’ toggle to control whether to process view lineage.Process Query LineageprocessQueryLineage: Set the ‘Process Query Lineage’ toggle to control whether to process query lineage.Process Stored Procedure LineageprocessStoredProcedureLineage: Set the ‘Process Stored ProcedureLog Lineage’ toggle to control whether to process stored procedure lineage.Threadsthreads: Number of Threads to use in order to parallelize lineage ingestion.Sink ConfigurationTo send the metadata to OpenMetadata, it needs to be specified as type: metadata-rest.{connector}_lineage.yamlsource:  type: {connector}-lineage  serviceName: {connector}  sourceConfig:    config:      type: DatabaseLineage      # Number of days to look back      queryLogDuration: 1      parsingTimeoutLimit: 300      # filterCondition: query_text not ilike '--- metabase query %'      resultLimit: 1000      # If instead of getting the query logs from the database we want to pass a file with the queries      # queryLogFilePath: /tmp/query_log/file_path      # databaseFilterPattern:      #   includes:      #     - database1      #     - database2      #   excludes:      #     - database3      # schemaFilterPattern:      #   includes:      #     - schema1      #     - schema2      #   excludes:      #     - schema3      # tableFilterPattern:      #   includes:      #     - table1      #     - table2      #   excludes:      #     - table3      #     - table4      overrideViewLineage: false      processViewLineage: true      processQueryLineage: true      processStoredProcedureLineage: true      threads: 1sink:  type: metadata-rest  config: {}

You can learn more about how to configure and run the Lineage Workflow to extract Lineage data from here

​2. Run with the CLI

After saving the YAML config, we will run the command the same way we did for the metadata ingestion:

metadata ingest -c <path-to-yaml>

​dbt Integration

dbt IntegrationLearn more about how to ingest dbt modelsWas this page helpful?YesNoSuggest editsRaise issueOracle Connector | OpenMetadata Enterprise Database GuidePreviousOracle Troubleshooting Guide | OpenMetadata SupportNext⌘I
