---
type: source
title: "Run the OpenAPI/REST Connector Externally - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, rest-api-connector, ingestion, cli, yaml-config]
related: [rest-api-connector, metadata-cli, cli-ingestion-with-basic-auth, filter-patterns, bot-authentication, personal-access-token, rest-connector-yaml-config, external-connector-execution]
sources: ["run-the-openapi-rest-connector-externally---openme-20260514.md"]
---

# Run the OpenAPI/REST Connector Externally - OpenMetadata Documentation

This source is the official OpenMetadata v1.12.x documentation page for running the [[rest-api-connector|OpenAPI/REST Connector]] externally (outside the UI) using a YAML configuration file and the `metadata ingest` CLI command. It provides a complete YAML config template covering the source configuration (type, service name, OpenAPI schema URL, token), sink configuration, and workflow configuration (logger level, OpenMetadata server connection with JWT token authentication). The page also references external schedulers as an alternative orchestration method and notes the Python version requirements (3.9-3.11).

## Key Content

- **External Execution Method**: Running the REST connector via CLI with a YAML config file, as an alternative to the UI-based ingestion container.
- **YAML Config Structure**: Complete example with `source`, `sink`, and `workflowConfig` sections, including the `ApiMetadata` source config type, `markDeletedApiCollections`, `overrideMetadata`, and `apiCollectionFilterPattern` fields.
- **Authentication**: JWT token (`bot_jwt_token`) required for CLI-based execution, configured under `securityConfig`.
- **CLI Command**: `metadata ingest -c <path-to-yaml>` to execute the ingestion.
- **External Schedulers**: Reference to running ingestion workflows on external orchestrators (no detailed guidance provided).

## Connections

- Strengthens the [[rest-api-connector]] page by documenting the external execution method.
- Extends [[metadata-cli]] with REST connector-specific usage.
- Related to [[cli-ingestion-with-basic-auth]] as a similar external execution pattern.
- The `apiCollectionFilterPattern` is an API-specific variant of the general [[filter-patterns]] concept.