---
type: clip
title: "Run the OpenAPI/REST Connector Externally - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/api/rest/yaml"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Run the OpenAPI/REST Connector Externally - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/api/rest/yaml

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationRESTRun the OpenAPI/REST Connector ExternallyHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIOverviewRESTOverviewRun ExternallyTroubleshootingDatabaseDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.RESTBETAFeature List✓ API Endpoint✓ Request Schema✓ Response Schema

In this section, we provide guides and references to use the OpenAPI/REST connector.

Configure and schedule REST metadata workflows from the OpenMetadata UI:

Requirements

Metadata Ingestion

​How to Run the Connector Externally

To run the Ingestion via the UI you’ll need to use the OpenMetadata Ingestion Container, which comes shipped with

custom Airflow plugins to handle the workflow deployment.

If, instead, you want to manage your workflows externally on your preferred orchestrator, you can check

the following docs to run the Ingestion Framework anywhere.

External SchedulersGet more information about running the Ingestion Framework Externally

​Requirements

​Python Requirements

We have support for Python versions 3.9-3.11

​Generate OpenAPI Schema URL

Generate OpenAPI schema URL for your serviceOpenAPI spec

​Metadata Ingestion

​1. Define the YAML Config

This is a sample config for OpenAPI:

Source ConfigurationConfigure the source type and service name for your REST API connector.Connection Typetype: Set to Rest for REST API connections.OpenAPI Schema URLopenAPISchemaURL: An OpenAPI schema URL typically refers to the URL where the OpenAPI Specification (OAS) document of a web service is hosted. The document defines the service’s API, including available endpoints, request/response formats, authentication methods, etc. It is usually in JSON format. for e.g. https://petstore3.swagger.io/api/v3/openapi.jsonToken: An authentication token to connect to an OpenAPI schema URL. It is only required if the API schema is protected or secured.rest_config.yamlsource:  type: rest  serviceName: openapi_rest  serviceConnection:    config:      type: Rest      openAPISchemaURL: https://docs.open-metadata.org/swagger.json  sourceConfig:    config:      type: ApiMetadata      markDeletedApiCollections: true      overrideMetadata: false      # apiCollectionFilterPattern:      #   includes:      #     - apiCollection1      #     - apiCollection2      #   excludes:      #     - apiCollection3      #     - apiCollection4sink:  type: metadata-rest  config: {}workflowConfig:  loggerLevel: INFO  # DEBUG, INFO, WARNING or ERROR  openMetadataServerConfig:    hostPort: "http://localhost:8585/api"    authProvider: openmetadata    securityConfig:      jwtToken: "{bot_jwt_token}"    ## Store the service Connection information    storeServiceConnection: true  # false    ## Secrets Manager Configuration    # secretsManagerProvider: aws, azure or noop    # secretsManagerLoader: airflow or env    ## If SSL, fill the following    # verifySSL: validate  # or ignore    # sslConfig:    #   caCertificate: /local/path/to/certificate# ingestionPipelineFQN: <service name>.<ingestion name> ## e.g., "my_redshift.metadata"

​2. Run with the CLI

First, we will need to save the YAML file. Afterward, and with all requirements installed, we can run:

metadata ingest -c <path-to-yaml>

Note that from connector to connector, this recipe will always be the same. By updating the YAML configuration,

you will be able to extract metadata from different sources.Was this page helpful?YesNoSuggest editsRaise issueREST API Connector | OpenMetadata Integration DocumentationPreviousREST Connector Troubleshooting Guide | OpenMetadata SupportNext⌘I
