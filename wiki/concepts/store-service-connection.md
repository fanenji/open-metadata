---
type: concept
title: Store Service Connection
created: 2026-05-14
updated: 2026-05-14
tags: [security, configuration, secrets, ingestion]
related: [superset-external-execution, personal-access-token, ingestion-framework, service-connection]
sources: ["run-the-superset-connector-externally---openmetada-20260514-2.md"]
---

# Store Service Connection

The Store Service Connection is a configuration toggle in OpenMetadata ingestion workflows that controls whether sensitive service connection information (credentials, host/port details) is persisted in the OpenMetadata database or used only at runtime.

## Behavior

- **`true` (default)**: The service connection details are stored encrypted in the database using the Fernet Key, or in an external Secrets Manager if configured. This allows the ingestion pipeline to be re-run without re-providing credentials.
- **`false`**: The service connection is created temporarily and used only by the Ingestion Framework at runtime. The connection details are **not** sent to the OpenMetadata server. This means the connection information must be provided again each time the ingestion pipeline is executed.

## Use Cases

- **Security-conscious deployments**: Setting `storeServiceConnection: false` minimizes the exposure of credentials by not persisting them in the metadata store.
- **Ephemeral or CI/CD pipelines**: When ingestion is run in short-lived environments where storing credentials is unnecessary or undesirable.
- **Compliance requirements**: Organizations with strict data residency or credential rotation policies may prefer runtime-only connections.

## Important Considerations

- When `storeServiceConnection` is `false`, the service will be created in OpenMetadata, but the connection details will not be retrievable from the UI or API.
- Re-running the ingestion pipeline requires the full YAML configuration with credentials to be provided again.
- This toggle is configured in the `workflowConfig.openMetadataServerConfig` section of the YAML.

## Configuration Example

```yaml
workflowConfig:
  openMetadataServerConfig:
    hostPort: "http://localhost:8585/api"
    authProvider: openmetadata
    securityConfig:
      jwtToken: "{bot_jwt_token}"
    storeServiceConnection: false
```

## See Also

- [[superset-external-execution]] — Concrete example of this toggle in a Superset YAML config
- [[service-connection]] — The concept of a service connection in OpenMetadata
- [[personal-access-token]] — JWT token authentication for CLI ingestion
- [[ingestion-framework]] — The framework that uses this configuration
