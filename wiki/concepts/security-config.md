---
type: concept
title: securityConfig
created: 2026-05-14
updated: 2026-05-14
tags: [ingestion, authentication, configuration, jwt]
related: [cli-ingestion-with-basic-auth, bot-authentication, metadata-agent]
sources: ["how-to-run-ingestion-pipeline-via-cli-with-basic-a-20260514.md"]
---

# securityConfig

The `securityConfig` is a YAML configuration block within an ingestion pipeline workflow configuration that holds authentication credentials required to connect to the OpenMetadata server. It is mandatory for CLI-based ingestion and must be placed under `workflowConfig.openMetadataServerConfig`.

## Required Fields

| Field | Value | Description |
|-------|-------|-------------|
| `jwtToken` | string | The JWT token copied from the ingestion-bot (Settings > Bots > ingestion-bot). |
| `authProvider` | `openmetadata` | Must be set to `openmetadata` to use the platform's built-in authentication. |

## Example

```yaml
workflowConfig:
  openMetadataServerConfig:
    hostPort: http://localhost:8585/api
    authProvider: openmetadata
    securityConfig:
      jwtToken: 'eyJraWQiO...'
```

## Context

The `securityConfig` block is required because OpenMetadata moved from a no-auth default to Basic Auth starting in version 0.12.1. The JWT token authenticates the CLI as the ingestion-bot, leveraging the [[bot-authentication]] mechanism. This configuration is used when triggering ingestion via the `metadata` CLI rather than through the UI or the [[kubernetes-native-orchestrator]].

## See Also

- [[cli-ingestion-with-basic-auth]] — Full procedural guide for CLI ingestion.
- [[bot-authentication]] — Underlying mechanism for bot-based JWT authentication.
- [[metadata-agent]] — The pipeline that consumes this configuration.