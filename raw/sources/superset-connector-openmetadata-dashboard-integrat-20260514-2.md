---
type: clip
title: "Superset Connector | OpenMetadata Dashboard Integration - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/dashboard/superset"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Superset Connector | OpenMetadata Dashboard Integration - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/dashboard/superset

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationSupersetSuperset Connector | OpenMetadata Dashboard IntegrationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseDashboardOverviewDomo DashboardLightdashLookerMetabaseMicroStrategyModePowerBIQlik CloudQlik SenseQuickSightRedashSigmaSSRSSupersetOverviewRun ExternallySSOTroubleshootingTableauMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pageRequirementsMetadata IngestionConnection DetailsMetadata Ingestion OptionsSecuring Superset Connection with SSL in OpenMetadataLineageDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.SupersetPRODFeature List✓ Dashboards✓ Charts✓ Lineage✓ Owners✓ Datamodels✓ Column Lineage✕ Tags✕ Projects

In this section, we provide guides and references to use the Superset connector.

Configure and schedule Superset metadata and profiler workflows from the OpenMetadata UI:

Requirements

Metadata Ingestion

Enable Security

Lineage

Troubleshooting

​Requirements

The ingestion also works with Superset 2.0.0 🎉

API Connection: To extract metadata from Superset via API, user must have at least can read on Chart & can read on Dashboard permissions.

Database Connection: To extract metadata from Superset via MySQL or Postgres database, database user must have at least SELECT privilege on dashboards & slices tables within superset schema.

​Metadata Ingestion

To ingest metadata from your sources, you need to create a service connection. The service connects your source system with OpenMetadata. Once you create a service, you can use it to configure your ingestion workflows.To create a service connection and ingest your metadata, follow the steps below:1Select the ServiceOn the left navigation bar, click Settings.On the next page, click Services, and then select the service.2Create a New ServiceTo add a new service connection, click Add New Service.3Select the ConnectorSelect Superset as the service type and click Next.4Name and Describe the ServiceEnter a unique Service Name and Description.Service Name: OpenMetadata identifies services by their service name. Enter a name that distinguishes this deployment from other services, including other Superset services you are ingesting metadata from.The service name cannot be changed after it is set.5Configure the Service ConnectionSet up the connection settings required for Superset to set up the service and start ingesting metadata from your sources. The right-hand panel displays help documentation for the selected connection type in the product UI.

​Connection Details

1Connection DetailsWhen using a Hybrid Ingestion Runner, any sensitive credential fields—such as passwords, API keys, or private keys—must reference secrets using the following format:password: secret:/my/database/password

This applies only to fields marked as secrets in the connection form (these typically mask input and show a visibility toggle icon).

For a complete guide on managing secrets in hybrid setups, see the Hybrid Ingestion Runner Secret Management Guide.

Host and Port: The Host and Post parameter is common for all three modes of authentication which specifies the host and port of the Superset instance. This should be specified as a string in the format http://hostname:port or https://hostname:port. For example, you might set the hostPort parameter to https://org.superset.com:8088.

Superset Connection: Add the connection details to fetch metadata from Superset either through APIs or Database.

For Superset API ConnectionSuperset API connection is the default mode of authentication where we fetch the metadata using Superset APIs.Superset only supports basic or ldap authentication through APIs so if you have SSO enabled on your Superset instance then this mode of authentication will not work for you and you can opt for MySQL or Postgres Connection to fetch metadata directly from the database in the backend of Superset.

Username: Username to connect to Superset, for ex. user@organization.com. This user should have access to relevant dashboards and charts in Superset to fetch the metadata.

Password: Password of the user account to connect with Superset.

Provider: Choose between db(default) or ldap mode of Authentication provider for the Superset service. This parameter is used internally to connect to Superset’s REST API.

Verify SSL:

Client SSL verification. Make sure to configure the SSLConfig if enabled.

Possible values:

validate: Validate the certificate using the public certificate (recommended).

ignore: Ignore the certification validation (not recommended for production).

no-ssl: SSL validation is not needed.

SSL Config: Client SSL configuration in case we are connection to a host with SSL enabled.

Certificate Path: CA certificate path in the instance where the ingestion run. E.g., /path/to/public.cert. Will be used if Verify SSL is set to validate.

For MySQL Connection

You can use Mysql Connection when you have SSO enabled and your Superset is backed by Mysql database.

Username: Specify the User to connect to MySQL. It should have enough privileges to read all the metadata. Make sure the user has select privileges on dashboards, tables & slices tables of superset schema.

Password: Password to connect to MySQL.

Host and Port: Enter the fully qualified hostname and port number for your MySQL deployment in the Host and Port field.

databaseSchema: Enter the database schema which is associated with the Superset instance.

caCertificate: Provide the path to ssl ca file.

sslCertificate: Provide the path to ssl client certificate file (ssl_cert).

sslKey: Provide the path to ssl client certificate file (ssl_key).

2Advanced ConfigurationDatabase Services have an Advanced Configuration section, where you can pass extra arguments to the connector

and, if needed, change the connection Scheme.This would only be required to handle advanced connectivity scenarios or customizations.

Connection Options (Optional): Enter the details for any additional connection options that can be sent to database during the connection. These details must be added as Key-Value pairs.

Connection Arguments (Optional): Enter the details for any additional connection arguments such as security or protocol configs that can be sent during the connection. These details must be added as Key-Value pairs.

3For Postgres ConnectionYou can use Postgres Connection when you have SSO enabled and your Superset is backed by Postgres database.

Username: Specify the User to connect to Postgres. Make sure the user has select privileges on dashboards, tables & slices tables of superset schema.

Password: Password to connect to Postgres.

Host and Port: Enter the fully qualified hostname and port number for your Postgres deployment in the Host and Port field.

Database: Initial Postgres database to connect to. Specify the name of database associated with Superset instance.

caCertificate: Provide the path to ssl ca file.

4Advanced ConfigurationDatabase Services have an Advanced Configuration section, where you can pass extra arguments to the connector

and, if needed, change the connection Scheme.This would only be required to handle advanced connectivity scenarios or customizations.

Connection Options (Optional): Enter the details for any additional connection options that can be sent to database during the connection. These details must be added as Key-Value pairs.

Connection Arguments (Optional): Enter the details for any additional connection arguments such as security or protocol configs that can be sent during the connection. These details must be added as Key-Value pairs.

5Test the ConnectionOnce the credentials have been added, click on Test Connection and Save the changes.6Configure Metadata IngestionIn this step we will configure the metadata ingestion pipeline,

Please follow the instructions below​Metadata Ingestion Options

Name: This field refers to the name of ingestion pipeline, you can customize the name or use the generated name.

Dashboard Filter Pattern (Optional): Use it to control whether to include dashboard as part of metadata ingestion.

Include: Explicitly include dashboards by adding a list of comma-separated regular expressions to the ‘Include’ field. OpenMetadata will include all dashboards with names matching one or more of the supplied regular expressions. All other dashboards will be excluded.

Exclude: Explicitly exclude dashboards by adding a list of comma-separated regular expressions to the ‘Exclude’ field. OpenMetadata will exclude all dashboards with names matching one or more of the supplied regular expressions. All other dashboards will be included.

projectFilterPattern: Filter the dashboards, charts and data sources by projects. Note that all of them support regex as include or exclude. E.g., “My project, My proj.*, .*Project”.

We filter the projects by concatenating the entire project hierarchy using dot notation

(e.g., Project1.NestedProjectA.OtherProject).

Make sure the regex filter pattern accounts for this fully-qualified format.

Chart Pattern (Optional): Use it to control whether to include charts as part of metadata ingestion.

Include: Explicitly include charts by adding a list of comma-separated regular expressions to the ‘Include’ field. OpenMetadata will include all charts with names matching one or more of the supplied regular expressions. All other charts will be excluded.

Exclude: Explicitly exclude charts by adding a list of comma-separated regular expressions to the ‘Exclude’ field. OpenMetadata will exclude all charts with names matching one or more of the supplied regular expressions. All other charts will be included.

Data Model Pattern (Optional): Use it to control whether to include data modes as part of metadata ingestion.

Include: Explicitly include data models by adding a list of comma-separated regular expressions to the ‘Include’ field. OpenMetadata will include all data models with names matching one or more of the supplied regular expressions. All other data models will be excluded.

Exclude: Explicitly exclude data models by adding a list of comma-separated regular expressions to the ‘Exclude’ field. OpenMetadata will exclude all data models with names matching one or more of the supplied regular expressions. All other data models will be included.

Database Service Name (Optional): Enter the name of Database Service which is already ingested in OpenMetadata to create lineage between dashboards and database tables.

Enable Debug Log (toggle): Set the ‘Enable Debug Log’ toggle to set the default log level to debug.

Include Owners (toggle): Set the ‘Include Owners’ toggle to control whether to include owners to the ingested entity if the owner email matches with a user stored in the OM server as part of metadata ingestion. If the ingested entity already exists and has an owner, the owner will not be overwritten.

Include Tags (toggle): Set the ‘Include Tags’ toggle to control whether to include tags in metadata ingestion.

Include Data Models (toggle): Set the ‘Include Data Models’ toggle to control whether to include tags as part of metadata ingestion.

Mark Deleted Dashboards (toggle): Set the ‘Mark Deleted Dashboards’ toggle to flag dashboards as soft-deleted if they are not present anymore in the source system.

Include Draft Dashboard (toogle): Set the ‘Include Draft Dashboard’ toggle to include draft dashboards. By default it will include draft dashboards.

7Schedule the Ingestion and DeployScheduling can be set up at an hourly, daily, weekly, or manual cadence. The

timezone is in UTC. Select a Start Date to schedule for ingestion. It is

optional to add an End Date.Review your configuration settings. If they match what you intended,

click Deploy to create the service and schedule metadata ingestion.If something doesn’t look right, click the Back button to return to the

appropriate step and change the settings as needed.After configuring the workflow, you can click on Deploy to create the

pipeline.8View the Ingestion PipelineOnce the workflow has been successfully deployed, you can view the

Ingestion Pipeline running from the Service Page.If AutoPilot is enabled, workflows like usage tracking, data lineage, and similar tasks will be handled automatically. Users don’t need to set up or manage them - AutoPilot takes care of everything in the system.

​Securing Superset Connection with SSL in OpenMetadata

To establish secure connections between OpenMetadata and Superset, navigate to the Advanced Config section. We need to update the Certificate Path and ensure that the certificates are accessible from the Airflow Server.

To establish secure connections between OpenMetadata and Superset’s MySQL database, you need to configure SSL certificates appropriately. If you only require SSL validation, specify the caCertificate to use the CA certificate for validating the server’s certificate. For mutual authentication, where both client and server need to authenticate each other, you must provide all three parameters: ssl_key for the client’s private key, ssl_cert for the client’s SSL certificate, and ssl_ca for the CA certificate to validate the server’s certificate.

To establish secure connections between OpenMetadata and Superset’s PostgreSQL database, you can configure SSL using different SSL modes provided by PostgreSQL, each offering varying levels of security.Under PostgresConnection Advanced Config, specify the SSL mode appropriate for your connection, such as prefer, verify-ca, allow, and others. After selecting the SSL mode, provide the CA certificate used for SSL validation (caCertificate). Note that PostgreSQL requires only the CA certificate for SSL validation.

​Lineage

To establish lineage from your database tables to dashboards, you must add the corresponding database service name.

Was this page helpful?YesNoSuggest editsRaise issueSSRS Troubleshooting | OpenMetadata ConnectorPreviousRun the Superset Connector ExternallyNext⌘I
