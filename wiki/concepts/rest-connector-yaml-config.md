---
type: concept
title: REST Connector YAML Configuration
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, rest-api-connector, yaml-config, ingestion, configuration]
related: [rest-api-connector, external-connector-execution, metadata-cli, filter-patterns, bot-authentication, personal-access-token]
sources: ["run-the-openapi-rest-connector-externally---openme-20260514.md"]
---

# REST Connector YAML Configuration

The REST Connector YAML Configuration is the structured configuration file used to run the [[rest-api-connector|OpenAPI/REST Connector]] externally via the `metadata ingest` CLI command. It defines the source connection, ingestion scope, sink, and workflow parameters.

## Structure

The YAML config has three main sections:

### Source Configuration

```yaml
source:
  type: rest
  serviceName: openapi_rest
  serviceConnection:
    config:
      type: Rest
      openAPISchemaURL: https://example.com/openapi.json
  sourceConfig:
    config:
      type: ApiMetadata
      markDeletedApiCollections: true
      overrideMetadata: false
      # apiCollectionFilterPattern:
      #   includes:
      #     - apiCollection1
      #   excludes:
      #     - apiCollection2
```

- **type**: Must be `Rest` for REST API connections.
- **serviceName**: User-defined name for the service in OpenMetadata.
- **openAPISchemaURL**: URL to the OpenAPI Specification (OAS) document in JSON format (e.g., `https://petstore3.swagger.io/api/v3/openapi.json`).
- **Token**: Optional authentication token for protected API schemas (not shown in the example but referenced in the documentation).
- **ApiMetadata source config**: Defines the ingestion scope for API metadata.
- **markDeletedApiCollections**: Boolean flag to mark removed API endpoints as deleted in OpenMetadata.
- **overrideMetadata**: Boolean flag controlling whether existing metadata is overwritten.
- **apiCollectionFilterPattern**: Inclusion/exclusion patterns for API collections (related to [[filter-patterns]]).

### Sink Configuration

```yaml
sink:
  type: metadata-rest
  config: {}
```

The sink type is `metadata-rest` with an empty config object.

### Workflow Configuration

```yaml
workflowConfig:
  loggerLevel: INFO
  openMetadataServerConfig:
    hostPort: "http://localhost:8585/api"
    authProvider: openmetadata
    securityConfig:
      jwtToken: "{bot_jwt_token}"
    storeServiceConnection: true
```

- **loggerLevel**: Logging verbosity (DEBUG, INFO, WARNING, ERROR).
- **hostPort**: OpenMetadata server API endpoint.
- **authProvider**: Must be `openmetadata` for JWT-based authentication.
- **jwtToken**: The [[personal-access-token|JWT token]] (bot token) for authentication.
- **storeServiceConnection**: Boolean flag to persist the service connection configuration in OpenMetadata.
- **Secrets Manager Configuration**: Optional fields for `secretsManagerProvider` (aws, azure, noop) and `secretsManagerLoader` (airflow, env).
- **SSL Configuration**: Optional `verifySSL` and `sslConfig` fields.

## Usage

Save the YAML file and run:

```bash
metadata ingest -c <path-to-yaml>
```

This command works identically across all connectors — only the YAML configuration changes.

## Important Notes

- The JWT token must be generated from the OpenMetadata UI (Settings → Bots → Add Bot) or obtained from the bot configuration.
- The `storeServiceConnection` flag can be set to `false` to avoid persisting connection details, but no guidance is provided on when to use each value.
- The `overrideMetadata` flag's interaction with existing metadata from previous UI-based ingestion runs is not documented.
- External schedulers are referenced as an alternative orchestration method but no detailed guidance is provided.