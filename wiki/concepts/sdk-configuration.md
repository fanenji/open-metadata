---
type: concept
title: "Sdk Configuration"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: SDK Configuration
created: 2026-05-14
updated: 2026-05-14
tags: [sdk, python, authentication, configuration]
related: [test-runner, data-quality-as-code, external-secrets-manager-setup, bot-authentication, ingestion-framework]
sources: ["testrunner---running-table-level-tests---openmetad-20260514.md"]
---

# SDK Configuration

The OpenMetadata Python SDK requires initialization before any operations (including [[test-runner|TestRunner]] and ingestion pipelines) can be performed. The `configure()` function establishes the connection to the OpenMetadata server and authenticates the client.

## Basic Configuration

```python
from metadata.sdk import configure

configure(
    host="http://localhost:8585/api",
    jwt_token="your-jwt-token"
)
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `host` | str | The URL of the OpenMetadata API endpoint |
| `jwt_token` | str | JWT token for authentication (see [[bot-authentication]]) |

## Authentication

The SDK uses JWT token authentication, the same mechanism used by [[bot-authentication|bot authentication]] for ingestion pipelines. The token embeds user identity and permissions.

## External Secrets Manager Integration

When using external secrets managers (AWS, Azure, GCP), the `SecretsManagerFactory` must be initialized **before** calling `configure()`:

```python
from metadata.utils.secrets.secrets_manager_factory import SecretsManagerFactory
from metadata.generated.schema.security.secrets.secretsManagerProvider import SecretsManagerProvider

SecretsManagerFactory(
    secrets_manager_provider=SecretsManagerProvider.managed_aws,
    secrets_manager_loader=SecretsManagerClientLoader.env,
)

configure(host="...", jwt_token="...")
```

See [[external-secrets-manager-setup]] for detailed provider-specific configuration.

## Logging

The SDK supports configurable logging levels via the `LogLevels` enum:

```python
from metadata.generated.schema.metadataIngestion.workflow import LogLevels

# Log levels: DEBUG, INFO, WARN, ERROR
```

## Related

- [[test-runner]] — Uses SDK configuration for data quality testing
- [[data-quality-as-code]] — Programmatic testing paradigm enabled by SDK
- [[external-secrets-manager-setup]] — Required setup for enterprise deployments
- [[bot-authentication]] — JWT token authentication mechanism
- [[ingestion-framework]] — Shares the same SDK infrastructure