---
type: clip
title: "Run the PostgreSQL Connector Externally - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/postgres/yaml"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Run the PostgreSQL Connector Externally - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/postgres/yaml

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationPostgreSQLRun the PostgreSQL Connector ExternallyHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOraclePinotDBPostgreSQLOverviewRun ExternallyTroubleshootingPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.PostgreSQLPRODFeature List✓ Metadata✓ Query Usage✓ Data Profiler✓ Data Quality✓ dbt✓ Lineage✓ Column-level Lineage✓ Owners✓ Tags✓ Stored Procedures✓ Sample Data✓ Auto-Classification✕ Stored Procedures Lineage

In this section, we provide guides and references to use the PostgreSQL connector.

Configure and schedule PostgreSQL metadata and profiler workflows from the OpenMetadata UI:

Requirements

Metadata Ingestion

Query Usage

Lineage

Data Profiler

Data Quality

dbt Integration

Enable Security

​How to Run the Connector Externally

To run the Ingestion via the UI you’ll need to use the OpenMetadata Ingestion Container, which comes shipped with

custom Airflow plugins to handle the workflow deployment.

If, instead, you want to manage your workflows externally on your preferred orchestrator, you can check

the following docs to run the Ingestion Framework anywhere.

External SchedulersGet more information about running the Ingestion Framework Externally

​Requirements

Note: Note that we only support officially supported PostgreSQL versions. You can check the version list here.

​Usage & Lineage

For the usage and lineage workflow, OpenMetadata relies on the pg_stat_statements extension to read query history. You need to enable the extension and grant your user read access to query statistics.

1. Load the extension at server startup by adding the following to your postgresql.conf:

shared_preload_libraries = 'pg_stat_statements'

After making this change, restart the PostgreSQL server.

2. Enable the extension and grant access by running the following SQL as a superuser:

CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Grant read access to the OpenMetadata user

GRANT pg_read_all_stats TO your_user;

pg_stat_statements is a fixed-size, in-memory statistics collector — not a persistent query log. Entries can be evicted when the table is full (default: 5000 entries), and server restarts clear all data. This can lead to incomplete lineage and usage results. For best practices on maximizing query retention, see the Usage & Lineage section in the connector overview.

​Python Requirements

We have support for Python versions 3.9-3.11

To run the PostgreSQL ingestion, you will need to install:

pip3 install "openmetadata-ingestion[postgres]"

​IAM Authentication

In order to be able to connect via IAM, you need to have the following:

Database is configured to use IAM authentication

Ensure that the RDS has IAM DB authentication enabled. Otherwise, you can click on Modify to enable it.

The user has the necessary IAM permissions

Even if you use IAM to connect to postgres, you need to specify a user to prepare the connection. You need to create a user as follows:

CREATE USER iam_user WITH LOGIN;

GRANT rds_iam TO iam_user;

The AWS Role has the necessary permissions

The role that is going to be used to perform the ingestion, needs to have the following permissions:

{

"Version": "2012-10-17",

"Statement": [

{

"Effect": "Allow",

"Action": [

"rds-db:connect"

],

"Resource": [

"arn:aws:rds-db:eu-west-1:<aws_account_number>:dbuser:<rds_db_resource_id>/<postgres_user>"

]

}

]

}

Otherwise, you might be finding issues such as

PAM authentication failed for user “<user>“

​Metadata Ingestion

All connectors are defined as JSON Schemas.

Here

you can find the structure to create a connection to PostgreSQL.

In order to create and run a Metadata Ingestion workflow, we will follow

the steps to create a YAML configuration able to connect to the source,

process the Entities if needed, and reach the OpenMetadata server.

The workflow is modeled around the following

JSON Schema

​1. Define the YAML Config

Source ConfigurationConfigure the source type and service name for your PostgreSQL connector.Usernameusername: Specify the User to connect to PostgreSQL. It should have enough privileges to read all the metadata.Basic AuthenticationauthType: Choose from basic auth and IAM based auth.password: Password comes under Basic Auth type.IAM AuthenticationawsAccessKeyId & awsSecretAccessKey: When you interact with AWS, you specify your AWS security credentials to verify who you are and whether you have permission to access the resources that you are requesting. AWS uses the security credentials to authenticate and authorize your requests (docs).Access keys consist of two parts: An access key ID (for example, AKIAIOSFODNN7EXAMPLE), and a secret access key (for example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY).You must use both the access key ID and secret access key together to authenticate your requests.You can find further information on how to manage your access keys here.awsSessionToken: If you are using temporary credentials to access your services, you will need to inform the AWS Access Key ID and AWS Secrets Access Key. Also, these will include an AWS Session Token.awsRegion: Each AWS Region is a separate geographic area in which AWS clusters data centers (docs).As AWS can have instances in multiple regions, we need to know the region the service you want reach belongs to.Note that the AWS Region is the only required parameter when configuring a connection. When connecting to the services programmatically, there are different ways in which we can extract and use the rest of AWS configurations.You can find further information about configuring your credentials here.endPointURL: To connect programmatically to an AWS service, you use an endpoint. An endpoint is the URL of the entry point for an AWS web service. The AWS SDKs and the AWS Command Line Interface (AWS CLI) automatically use the default endpoint for each service in an AWS Region. But you can specify an alternate endpoint for your API requests.Find more information on AWS service endpoints.profileName: A named profile is a collection of settings and credentials that you can apply to a AWS CLI command. When you specify a profile to run a command, the settings and credentials are used to run that command. Multiple named profiles can be stored in the config and credentials files.You can inform this field if you’d like to use a profile other than default.Find here more information about Named profiles for the AWS CLI.assumeRoleArn: Typically, you use AssumeRole within your account or for cross-account access. In this field you’ll set the ARN (Amazon Resource Name) of the policy of the other account.A user who wants to access a role in a different account must also have permissions that are delegated from the account administrator. The administrator must attach a policy that allows the user to call AssumeRole for the ARN of the role in the other account.This is a required field if you’d like to AssumeRole.Find more information on AssumeRole.When using Assume Role authentication, ensure you provide the following details:

AWS Region: Specify the AWS region for your deployment.

Assume Role ARN: Provide the ARN of the role in your AWS account that OpenMetadata will assume.

assumeRoleSessionName: An identifier for the assumed role session. Use the role session name to uniquely identify a session when the same role is assumed by different principals or for different reasons.By default, we’ll use the name OpenMetadataSession.Find more information about the Role Session Name.assumeRoleSourceIdentity: The source identity specified by the principal that is calling the AssumeRole operation. You can use source identity information in AWS CloudTrail logs to determine who took actions with a role.Find more information about Source Identity.Host PorthostPort: Enter the fully qualified hostname and port number for your PostgreSQL deployment in the Host and Port field.Databasedatabase: Initial PostgreSQL database to connect to. If you want to ingest all databases, set ingestAllDatabases to true.Ingest All DatabasesingestAllDatabases: Ingest data from all databases in PostgreSQL. You can use databaseFilterPattern on top of this.Connection OptionsConnection Options (Optional): Enter the details for any additional connection options that can be sent to database during the connection. These details must be added as Key-Value pairs.Connection ArgumentsConnection Arguments (Optional): Enter the details for any additional connection arguments such as security or protocol configs that can be sent to database during the connection. These details must be added as Key-Value pairs.

In case you are using Single-Sign-On (SSO) for authentication, add the authenticator details in the Connection Arguments as a Key-Value pair as follows: "authenticator" : "sso_login_url"

SSL ConfigurationThe sslConfig and sslMode are used to configure the SSL (Secure Sockets Layer) connection between your application and the PostgreSQL server. PostgreSQL will require only rootCertificate i.e caCertificate.caCertificate: This is the path to the CA (Certificate Authority) certificate file. This file is used to verify the server’s certificate.sslMode: This field controls whether a secure SSL/TLS connection will be negotiated with the server. There are several modes you can choose:

disable: No SSL/TLS encryption will be used; the data sent over the network is not encrypted.

allow: The driver will try to negotiate a non-SSL connection but if the server insists on SSL, it will switch to SSL.

prefer (the default): The driver will try to negotiate an SSL connection but if the server does not support SSL, it will switch to a non-SSL connection.

require: The driver will try to negotiate an SSL connection. If the server does not support SSL, the driver will not fall back to a non-SSL connection.

verify-ca: The driver will negotiate an SSL connection and verify that the server certificate is issued by a trusted certificate authority (CA).

verify-full: The driver will negotiate an SSL connection, verify that the server certificate is issued by a trusted CA and check that the server host name matches the one in the certificate.

Source Config​Source Configuration - Source ConfigThe sourceConfig is defined here:markDeletedTables: To flag tables as soft-deleted if they are not present anymore in the source system.markDeletedStoredProcedures: Optional configuration to soft delete stored procedures in OpenMetadata if the source stored procedures are deleted. Also, if the stored procedures is deleted, all the associated entities like lineage, etc., with that stored procedures will be deleted.markDeletedSchemas: Optional configuration to soft delete schemas stored in OpenMetadata if the source schema is deleted. Setting this flag to true will only keep filtered schema and delete any other schemas that do not match schemaFilterPattern or do not exist at source.markDeletedDatabases: Additional optional configuration for soft deletion, providing granular option to select which particular entities should be deleted.includeTables: true or false, to ingest table data. Default is true.includeViews: true or false, to ingest views definitions.includeTags: Optional configuration to toggle the tags ingestion.includeOwners: Set the ‘Include Owners’ toggle to control whether to include owners to the ingested entity if the owner email matches with a user stored in the OM server as part of metadata ingestion. If the ingested entity already exists and has an owner, the owner will not be overwritten.includeStoredProcedures: Optional configuration to toggle the Stored Procedures ingestion.includeDDL: Optional configuration to toggle the DDL Statements ingestion.overrideMetadata (boolean): Set the ‘Override Metadata’ toggle to control whether to override the existing metadata in the OpenMetadata server with the metadata fetched from the source. If the toggle is set to true, the metadata fetched from the source will override the existing metadata in the OpenMetadata server. If the toggle is set to false, the metadata fetched from the source will not override the existing metadata in the OpenMetadata server. This is applicable for fields like description, tags, owner and displayName.queryLogDuration: Configuration to tune how far we want to look back in query logs to process Stored Procedures results.queryParsingTimeoutLimit: Configuration to set the timeout for parsing the query in seconds.useFqnForFiltering: Regex will be applied on fully qualified name (e.g service_name.db_name.schema_name.table_name) instead of raw name (e.g. table_name).databaseFilterPattern, schemaFilterPattern: Note that the filter supports regex as include or exclude. You can find examples heretableFilterPattern: Note that the filter supports regex as include or exclude. You can find examples herethreads (beta): The number of threads to use when extracting the metadata using multithreading.databaseMetadataConfigType (string): Database Source Config Metadata Pipeline type.incremental (beta): Incremental Extraction configuration. Currently implemented for:

BigQuery

Redshift

Snowflake

Sink ConfigurationTo send the metadata to OpenMetadata, it needs to be specified as type: metadata-rest.Workflow ConfigurationThe main property here is the openMetadataServerConfig, where you can define the host and security provider of your OpenMetadata installation.Logger LevelYou can specify the loggerLevel depending on your needs. If you are trying to troubleshoot an ingestion, running with DEBUG will give you far more traces for identifying issues.JWT TokenJWT tokens will allow your clients to authenticate against the OpenMetadata server. To enable JWT Tokens, you will get more details here.You can refer to the JWT Troubleshooting section link for any issues in your JWT configuration.Store Service ConnectionIf set to true (default), we will store the sensitive information either encrypted via the Fernet Key in the database or externally, if you have configured any Secrets Manager.If set to false, the service will be created, but the service connection information will only be used by the Ingestion Framework at runtime, and won’t be sent to the OpenMetadata server.SSL ConfigurationIf you have added SSL to the OpenMetadata server, then you will need to handle the certificates when running the ingestion too. You can either set verifySSL to ignore, or have it as validate, which will require you to set the sslConfig.caCertificate with a local path where your ingestion runs that points to the server certificate file.Find more information on how to troubleshoot SSL issues here.ingestionPipelineFQNFully qualified name of ingestion pipeline, used to identify the current ingestion pipeline.postgres_config.yamlsource:  type: postgres  serviceName: local_postgres  serviceConnection:    config:      type: PostgreSQL      username: username  # REQUIRED      authType:        password: <password>  # Basic Auth - most common      authType:        awsConfig:  # IAM Auth for AWS RDS PostgreSQL          awsAccessKeyId: access key id          awsSecretAccessKey: access secret key          awsRegion: aws region name      hostPort: localhost:5432  # REQUIRED - format: host:port      database: database  # REQUIRED - database name      ingestAllDatabases: true      # queryStatementSource: pg_stat_statements  # Custom view/table for query history      # connectionOptions:      #   key: value      # connectionArguments:      #   key: value      # sslConfig:      #   caCertificate: "path/to/ca/certificate"      # sslMode: disable #allow prefer require verify-ca verify-full  sourceConfig:    config:      type: DatabaseMetadata      markDeletedTables: true      markDeletedStoredProcedures: true      markDeletedSchemas: true      markDeletedDatabases: true      includeTables: true      includeViews: true      # includeTags: true      # includeOwners: false      # includeStoredProcedures: true      # includeDDL: true      # overrideMetadata: false      # queryLogDuration: 1      # queryParsingTimeoutLimit: 300      # useFqnForFiltering: false      # threads: 1      # databaseMetadataConfigType: ()      # incremental:      #   enabled: true      #   lookbackDays: 7      #   safetyMarginDays: 1      # databaseFilterPattern:      #   includes:      #     - database1      #     - database2      #   excludes:      #     - database3      #     - database4      # schemaFilterPattern:      #   includes:      #     - schema1      #     - schema2      #   excludes:      #     - schema3      #     - schema4      # tableFilterPattern:      #   includes:      #     - users      #     - type_test      #   excludes:      #     - table3      #     - table4sink:  type: metadata-rest  config: {}workflowConfig:  loggerLevel: INFO  # DEBUG, INFO, WARNING or ERROR  openMetadataServerConfig:    hostPort: "http://localhost:8585/api"    authProvider: openmetadata    securityConfig:      jwtToken: "{bot_jwt_token}"    ## Store the service Connection information    storeServiceConnection: true  # false    ## Secrets Manager Configuration    # secretsManagerProvider: aws, azure or noop    # secretsManagerLoader: airflow or env    ## If SSL, fill the following    # verifySSL: validate  # or ignore    # sslConfig:    #   caCertificate: /local/path/to/certificate# ingestionPipelineFQN: <service name>.<ingestion name> ## e.g., "my_redshift.metadata"

​2. Run with the CLI

First, we will need to save the YAML file. Afterward, and with all requirements installed, we can run:

metadata ingest -c <path-to-yaml>

Note that from connector to connector, this recipe will always be the same. By updating the YAML configuration,

you will be able to extract metadata from different sources.

​Query Usage

The Query Usage workflow will be using the query-parser processor.

After running a Metadata Ingestion workflow, we can run Query Usage workflow.

While the serviceName will be the same to that was used in Metadata Ingestion, so the ingestion bot can get the serviceConnection details from the server.

​1. Define the YAML Config

This is a sample config for postgres Usage:

Source ConfigurationConfigure the source type and service name for your usage workflow.Usage Config Typetype: Set to DatabaseUsage for database usage ingestion.Query Log DurationqueryLogDuration: Configuration to tune how far we want to look back in query logs to process usage data (in days).Stage File LocationstageFileLocation: Temporary file name to store the query logs before processing. Absolute file path required.Note that the location is a directory that will be cleaned at the end of the ingestion.Result LimitresultLimit: Configuration to set the limit for query logs.Query Log File PathqueryLogFilePath: Configuration to set the file path for query logs. If instead of getting the query logs from the database we want to pass a file with the queries.Processor ConfigurationChoose the query-parser processor to parse and process the query logs.Stage ConfigurationConfigure the staging location for table usage data before it’s sent to OpenMetadata.Bulk Sink ConfigurationConfigure the bulk sink for metadata usage ingestion.{connector}_usage.yamlsource:  type: {connector}-usage  serviceName: {connector}  sourceConfig:    config:      type: DatabaseUsage      # Number of days to look back      queryLogDuration: 7      # This is a directory that will be DELETED after the usage runs      stageFileLocation: <path to store the stage file>      # resultLimit: 1000      # If instead of getting the query logs from the database we want to pass a file with the queries      # queryLogFilePath: path-to-fileprocessor:  type: query-parser  config: {}stage:  type: table-usage  config:    filename: /tmp/{connector}_usagebulkSink:  type: metadata-usage  config:    filename: /tmp/{connector}_usage

​2. Run with the CLI

After saving the YAML config, we will run the command the same way we did for the metadata ingestion:

metadata usage -c <path-to-yaml>

​Lineage

After running a Metadata Ingestion workflow, we can run Lineage workflow.

While the serviceName will be the same to that was used in Metadata Ingestion, so the ingestion bot can get the serviceConnection details from the server.

​1. Define the YAML Config

This is a sample config for postgres Lineage:

Source ConfigurationConfigure the source type and service name for your lineage workflow.You can find all the definitions and types for the sourceConfig here.Lineage Config Typetype: Set to DatabaseLineage for database lineage ingestion.Query Log DurationqueryLogDuration: Configuration to tune how far we want to look back in query logs to process lineage data in days.Parsing Timeout LimitparsingTimeoutLimit: Configuration to set the timeout for parsing the query in seconds.Filter ConditionfilterCondition: Condition to filter the query history.Result LimitresultLimit: Configuration to set the limit for query logs.Query Log File PathqueryLogFilePath: Configuration to set the file path for query logs. If instead of getting the query logs from the database we want to pass a file with the queries.Database Filter PatterndatabaseFilterPattern: Regex to only fetch databases that matches the pattern.Schema Filter PatternschemaFilterPattern: Regex to only fetch tables or databases that matches the pattern.Table Filter PatterntableFilterPattern: Regex to only fetch tables or databases that matches the pattern.Override View LineageoverrideViewLineage: Set the ‘Override View Lineage’ toggle to control whether to override the existing view lineage.Process View LineageprocessViewLineage: Set the ‘Process View Lineage’ toggle to control whether to process view lineage.Process Query LineageprocessQueryLineage: Set the ‘Process Query Lineage’ toggle to control whether to process query lineage.Process Stored Procedure LineageprocessStoredProcedureLineage: Set the ‘Process Stored ProcedureLog Lineage’ toggle to control whether to process stored procedure lineage.Threadsthreads: Number of Threads to use in order to parallelize lineage ingestion.Sink ConfigurationTo send the metadata to OpenMetadata, it needs to be specified as type: metadata-rest.{connector}_lineage.yamlsource:  type: {connector}-lineage  serviceName: {connector}  sourceConfig:    config:      type: DatabaseLineage      # Number of days to look back      queryLogDuration: 1      parsingTimeoutLimit: 300      # filterCondition: query_text not ilike '--- metabase query %'      resultLimit: 1000      # If instead of getting the query logs from the database we want to pass a file with the queries      # queryLogFilePath: /tmp/query_log/file_path      # databaseFilterPattern:      #   includes:      #     - database1      #     - database2      #   excludes:      #     - database3      # schemaFilterPattern:      #   includes:      #     - schema1      #     - schema2      #   excludes:      #     - schema3      # tableFilterPattern:      #   includes:      #     - table1      #     - table2      #   excludes:      #     - table3      #     - table4      overrideViewLineage: false      processViewLineage: true      processQueryLineage: true      processStoredProcedureLineage: true      threads: 1sink:  type: metadata-rest  config: {}

You can learn more about how to configure and run the Lineage Workflow to extract Lineage data from here

​2. Run with the CLI

After saving the YAML config, we will run the command the same way we did for the metadata ingestion:

metadata ingest -c <path-to-yaml>

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

​Securing PostgreSQL Connection with SSL in OpenMetadata

To configure SSL for secure connections between OpenMetadata and a PostgreSQL database, PostgreSQL offers various SSL modes, each providing different levels of connection security.

When running the ingestion process externally, specify the SSL mode to be used for the PostgreSQL connection, such as prefer, verify-ca, allow, and others. Once you’ve chosen the SSL mode, provide the CA certificate for SSL validation (caCertificate). Only the CA certificate is required for SSL validation in PostgreSQL.

For IAM authentication, it is recommended to select the allow mode or another SSL mode that aligns with your specific needs.

sslMode: disable #allow prefer require verify-ca verify-full

sslConfig:

caCertificate: "/path/to/ca/certificate"

​dbt Integration

You can learn more about how to ingest dbt models’ definitions and their lineage here.Was this page helpful?YesNoSuggest editsRaise issuePostgreSQL Connector | OpenMetadata Database IntegrationPreviousPostgreSQL Connector TroubleshootingNext⌘I
