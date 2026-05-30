---
type: clip
title: "Run the Superset Connector Externally - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/dashboard/superset/yaml"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Run the Superset Connector Externally - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/dashboard/superset/yaml

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationSupersetRun the Superset Connector ExternallyHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseDashboardOverviewDomo DashboardLightdashLookerMetabaseMicroStrategyModePowerBIQlik CloudQlik SenseQuickSightRedashSigmaSSRSSupersetOverviewRun ExternallySSOTroubleshootingTableauMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.SupersetPRODFeature List✓ Dashboards✓ Charts✓ Lineage✓ Owners✓ Datamodels✕ Tags✕ Projects

In this section, we provide guides and references to use the Superset connector.

Configure and schedule Superset metadata and profiler workflows from the OpenMetadata UI:

Requirements

Metadata Ingestion

Enable Security

​How to Run the Connector Externally

To run the Ingestion via the UI you’ll need to use the OpenMetadata Ingestion Container, which comes shipped with

custom Airflow plugins to handle the workflow deployment.

If, instead, you want to manage your workflows externally on your preferred orchestrator, you can check

the following docs to run the Ingestion Framework anywhere.

External SchedulersGet more information about running the Ingestion Framework Externally

​Requirements

The ingestion also works with Superset 2.0.0 🎉

Note:

API Connection: To extract metadata from Superset via API, user must have at least can read on Chart & can read on Dashboard permissions.

Database Connection: To extract metadata from Superset via MySQL or Postgres database, database user must have at least SELECT privilege on dashboards & slices tables within superset schema.

​Python Requirements

We have support for Python versions 3.9-3.11

To run the Superset ingestion, you will need to install:

pip3 install "openmetadata-ingestion[superset]"

​Metadata Ingestion

All connectors are defined as JSON Schemas.

Here

you can find the structure to create a connection to Superset.

In order to create and run a Metadata Ingestion workflow, we will follow

the steps to create a YAML configuration able to connect to the source,

process the Entities if needed, and reach the OpenMetadata server.

The workflow is modeled around the following

JSON Schema

​1. Define the YAML Config

This is a sample config for Superset:

Source ConfigurationConfigure the source type and service name.hostPorthostPort: The Host and Post parameter is common for all three modes of authentication which specifies the host and port of the Superset instance. This should be specified as a string in the format http://hostname:port or https://hostname:port. For example, you might set the hostPort parameter to https://org.superset.com:8088.connection: Add the connection details to fetch metadata from Superset either through APIs or Database.​For Superset API Connection:Superset API connection is the default mode of authentication where we fetch the metadata using Superset APIs.Note:Superset only supports basic or ldap authentication through APIs so if you have SSO enabled on your Superset instance then this mode of authentication will not work for you and you can opt for MySQL or Postgres Connection to fetch metadata directly from the database in the backend of Superset.username: Username to connect to Superset, for ex. user@organization.com. This user should have access to relevant dashboards and charts in Superset to fetch the metadata.password: Password of the user account to connect with Superset.provider: Choose between db(default) or ldap mode of Authentication provider for the Superset service. This parameter is used internally to connect to Superset’s REST API.For MySQL Connection:​For MySQL Connection:You can use Mysql Connection when you have SSO enabled and your Superset is backed by Mysql database.username: Specify the User to connect to MySQL. It should have enough privileges to read all the metadata. Make sure the user has select privileges on dashboards, tables & slices tables of superset schema.password: Password to connect to MySQL.hostPort: Enter the fully qualified hostname and port number for your MySQL deployment in the Host and Port field.

databaseSchema: Enter the database schema which is associated with the Superset instance..

caCertificate: Provide the path to ssl ca file.

sslCertificate: Provide the path to ssl client certificate file (ssl_cert).

sslKey: Provide the path to ssl client certificate file (ssl_key).

Connection Options (Optional): Enter the details for any additional connection options that can be sent to MySQL during the connection. These details must be added as Key-Value pairs.Connection Arguments (Optional): Enter the details for any additional connection arguments such as security or protocol configs that can be sent to MySQL during the connection. These details must be added as Key-Value pairs.

In case you are using Single-Sign-On (SSO) for authentication, add the authenticator details in the Connection Arguments as a Key-Value pair as follows: "authenticator" : "sso_login_url"

For Postgres Connection:​For Postgres Connection:You can use Postgres Connection when you have SSO enabled and your Superset is backed by Postgres database.

username: Specify the User to connect to Postgres. Make sure the user has select privileges on dashboards, tables & slices tables of superset schema.

password: Password to connect to Postgres.hostPort: Enter the fully qualified hostname and port number for your Postgres deployment in the Host and Port field.

database: Initial Postgres database to connect to. Specify the name of database associated with Superset instance.

caCertificate: Provide the path to ssl ca file.

Connection Options (Optional): Enter the details for any additional connection options that can be sent to Postgres during the connection. These details must be added as Key-Value pairs.Connection Arguments (Optional): Enter the details for any additional connection arguments such as security or protocol configs that can be sent to Postgres during the connection. These details must be added as Key-Value pairs.

In case you are using Single-Sign-On (SSO) for authentication, add the authenticator details in the Connection Arguments as a Key-Value pair as follows: "authenticator" : "sso_login_url"

Source Config​Source Configuration - Source ConfigThe sourceConfig is defined here:dbServiceNames: Database Service Names for ingesting lineage if the source supports it.dashboardFilterPattern, chartFilterPattern, dataModelFilterPattern: Note that all of them support regex as include or exclude. E.g., “My dashboard, My dash.*, .*Dashboard”.projectFilterPattern: Filter the dashboards, charts and data sources by projects. Note that all of them support regex as include or exclude. E.g., “My project, My proj.*, .*Project”.includeOwners: Set the ‘Include Owners’ toggle to control whether to include owners to the ingested entity if the owner email matches with a user stored in the OM server as part of metadata ingestion. If the ingested entity already exists and has an owner, the owner will not be overwritten.includeTags: Set the ‘Include Tags’ toggle to control whether to include tags in metadata ingestion.includeDataModels: Set the ‘Include Data Models’ toggle to control whether to include tags as part of metadata ingestion.markDeletedDashboards: Set the ‘Mark Deleted Dashboards’ toggle to flag dashboards as soft-deleted if they are not present anymore in the source system.Include Draft Dashboard (toogle): Set the ‘Include Draft Dashboard’ toggle to include draft dashboards. By default it will include draft dashboards.dataModelFilterPattern: Regex exclude or include data models that matches the pattern.includeOwners:Enabling a flag will replace the current owner with a new owner from the source during metadata ingestion, if the current owner is null. It is recommended to keep the flag enabled to obtain the owner information during the first metadata ingestion.includeOwners supports boolean value either true or false.markDeletedDashboards: Optional configuration to soft delete dashboards in OpenMetadata if the source dashboards are deleted. Also, if the dashboard is deleted, all the associated entities like lineage, etc., with that dashboard will be deleted.markDeletedDashboards supports boolean value either true or false.markDeletedDataModels: Optional configuration to soft delete data models in OpenMetadata if the source data models are deleted. Also, if the data models is deleted, all the associated entities like lineage, etc., with that data models will be deleted.includeOwners supports boolean value either true or false.includeTags:Optional configuration to toggle the tags ingestion.markDeletedDataModels supports boolean value either true or false.includeDataModels: Optional configuration to toggle the ingestion of data models.includeDataModels supports boolean value either true or false.includeDraftDashboard: Optional Configuration to include/exclude draft dashboards. By default it will include draft dashboards.includeDraftDashboard supports boolean value either true or false.overrideMetadata: Set the ‘Override Metadata’ toggle to control whether to override the existing metadata in the OpenMetadata server with the metadata fetched from the source. If the toggle is set to true, the metadata fetched from the source will override the existing metadata in the OpenMetadata server. If the toggle is set to false, the metadata fetched from the source will not override the existing metadata in the OpenMetadata server. This is applicable for fields like description, tags, owner and displayName.overrideMetadata supports boolean value either true or false.overrideLineage: Set the ‘Override Lineage’ toggle to control whether to override the existing lineage.overrideLineage supports boolean value either true or false.Sink ConfigurationTo send the metadata to OpenMetadata, it needs to be specified as type: metadata-rest.Workflow ConfigurationThe main property here is the openMetadataServerConfig, where you can define the host and security provider of your OpenMetadata installation.Logger LevelYou can specify the loggerLevel depending on your needs. If you are trying to troubleshoot an ingestion, running with DEBUG will give you far more traces for identifying issues.JWT TokenJWT tokens will allow your clients to authenticate against the OpenMetadata server. To enable JWT Tokens, you will get more details here.You can refer to the JWT Troubleshooting section link for any issues in your JWT configuration.Store Service ConnectionIf set to true (default), we will store the sensitive information either encrypted via the Fernet Key in the database or externally, if you have configured any Secrets Manager.If set to false, the service will be created, but the service connection information will only be used by the Ingestion Framework at runtime, and won’t be sent to the OpenMetadata server.SSL ConfigurationIf you have added SSL to the OpenMetadata server, then you will need to handle the certificates when running the ingestion too. You can either set verifySSL to ignore, or have it as validate, which will require you to set the sslConfig.caCertificate with a local path where your ingestion runs that points to the server certificate file.Find more information on how to troubleshoot SSL issues here.ingestionPipelineFQNFully qualified name of ingestion pipeline, used to identify the current ingestion pipeline.superset_config.yamlsource:  type: superset  serviceName: local_superset  serviceConnection:    config:      type: SupersethostPort: http://localhost:8088      connection:        # For Superset API Connection        username: admin        password: admin        provider: db # or provider: ldap# For MySQL Connection        # type: Mysql        # username: <username>        # authType:        #   password: <password>        # hostPort: <hostPort>        # databaseSchema: superset# For Postgres Connection        # type: Postgres        # username: username        # authType:        #   password: <password>        # hostPort: localhost:5432        # database: superset  sourceConfig:    config:      type: DashboardMetadata      # lineageInformation:      #   dbServiceNames:      #     - service1      #     - service2      # dashboardFilterPattern:      #   includes:      #     - dashboard1      #     - dashboard2      #   excludes:      #     - dashboard3      #     - dashboard4      # chartFilterPattern:      #   includes:      #     - chart1      #     - chart2      #   excludes:      #     - chart3      #     - chart4      # projectFilterPattern:      #   includes:      #     - project1      #     - project2      #   excludes:      #     - project3      #     - project4      # dataModelFilterPattern:      #   includes:      #     - dataModel1      #     - dataModel2      #   excludes:      #     - dataModel3      #     - dataModel4      # includeOwners: false # true      # markDeletedDashboards: true # false      # markDeletedDataModels: true # false      # includeTags: true # false      # includeDataModels: true # false      # includeDraftDashboard: true # false      # overrideMetadata: false # true      # overrideLineage: false # truesink:  type: metadata-rest  config: {}workflowConfig:  loggerLevel: INFO  # DEBUG, INFO, WARNING or ERROR  openMetadataServerConfig:    hostPort: "http://localhost:8585/api"    authProvider: openmetadata    securityConfig:      jwtToken: "{bot_jwt_token}"    ## Store the service Connection information    storeServiceConnection: true  # false    ## Secrets Manager Configuration    # secretsManagerProvider: aws, azure or noop    # secretsManagerLoader: airflow or env    ## If SSL, fill the following    # verifySSL: validate  # or ignore    # sslConfig:    #   caCertificate: /local/path/to/certificate# ingestionPipelineFQN: <service name>.<ingestion name> ## e.g., "my_redshift.metadata"

​Securing Superset Connection with SSL in OpenMetadata

To establish secure connections between OpenMetadata and Superset, in the YAML under sslConfig, we need to add caCertificate and update the certificate path. Ensure that the certificates are accessible from the Airflow Server.

sslConfig:

caCertificate: /path/to/cacert.crt

To establish secure connections between OpenMetadata and Superset’s MySQL database, you need to configure SSL certificates appropriately. If you only require SSL validation, specify the caCertificate to use the CA certificate for validating the server’s certificate. For mutual authentication, where both client and server need to authenticate each other, you must provide all three parameters: ssl_key for the client’s private key, ssl_cert for the client’s SSL certificate, and ssl_ca for the CA certificate to validate the server’s certificate.

type: Mysql

sslConfig:

caCertificate: "/path/to/ca_certificate"

sslCertificate: "/path/to/your/ssl_cert"

sslKey: "/path/to/your/ssl_key"

To establish secure connxxwections between OpenMetadata and Superset’s PostgreSQL database, you can configure SSL using different SSL modes provided by PostgreSQL, each offering varying levels of security.Under PostgresConnection Advanced Config, specify the SSL mode appropriate for your connection, such as prefer, verify-ca, allow, and others. After selecting the SSL mode, provide the CA certificate used for SSL validation (caCertificate). Note that PostgreSQL requires only the CA certificate for SSL validation.

type: Postgres

sslMode: disable #allow prefer require verify-ca verify-full

sslConfig:

caCertificate: "/path/to/ca/certificate"

​2. Run with the CLI

First, we will need to save the YAML file. Afterward, and with all requirements installed, we can run:

metadata ingest -c <path-to-yaml>

Note that from connector to connector, this recipe will always be the same. By updating the YAML configuration,

you will be able to extract metadata from different sources.Was this page helpful?YesNoSuggest editsRaise issueSuperset Connector | OpenMetadata Dashboard IntegrationPreviousSupersetNext⌘I
