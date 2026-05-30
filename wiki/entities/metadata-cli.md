---
type: entity
title: metadata CLI
created: 2026-05-14
updated: 2026-05-15
tags:
  - cli
  - ingestion
  - tooling
  - openmetadata
  - command-line
  - automation
related: ["ingestion-framework", "cli-ingestion-with-basic-auth", "security-config", "rest-api-connector", "rest-connector-yaml-config", "external-connector-execution", "bot-authentication", "personal-access-token", "external-ingestion-workflow", "postgresql-connector", "data-quality", "data-profiling", "auto-classification"]sources:
  - how-to-run-ingestion-pipeline-via-cli-with-basic-a-20260514.md
  - run-the-openapi-rest-connector-externally---openme-20260514.md
  - run-the-postgresql-connector-externally---openmeta-20260514.md
---

# metadata CLI

The `metadata` command-line tool is the primary CLI interface for interacting with OpenMetadata ingestion pipelines. It is part of the OpenMetadata ingestion framework and allows users to trigger, manage, and configure metadata ingestion workflows directly from the terminal. The tool provides commands for running different workflow types externally, outside the OpenMetadata UI.

## Commands

| Command | Purpose | Workflow Type |
|---------|---------|---------------|
| `metadata ingest` | Run metadata ingestion or lineage extraction | Metadata Ingestion, Lineage |
| `metadata usage` | Run query usage extraction | Query Usage |
| `metadata profile` | Run data profiling | Data Profiler |
| `metadata classify` | Run auto-classification | Auto Classification |
| `metadata test` | Run data quality tests | Data Quality |

## Usage

All commands follow the same pattern:

```bash
metadata <command> -c <config.yaml>
```

The `-c` flag specifies the path to the YAML configuration file. This works identically across all connectors — only the YAML configuration changes.

### Key Details

- The `metadata ingest` command is used for both Metadata Ingestion (with `type: DatabaseMetadata`) and Lineage (with `type: DatabaseLineage`).
- The `metadata profile` and `metadata classify` commands both use the `orm-profiler` processor but with different source config types (`Profiler` vs `AutoClassification`).
- The `metadata test` command uses the `orm-test-runner` processor and executes ALL tests present on the table, not just those defined in the YAML.

### Usage Context

The `metadata` CLI provides an alternative ingestion trigger method outside the OpenMetadata UI and the [[kubernetes-native-orchestrator]]. It is particularly useful for:

- Automation scripts and CI/CD pipelines
- Environments where OAuth or SSO is not available
- Testing and debugging ingestion configurations locally

## Authentication

CLI-based ingestion requires authentication with the OpenMetadata server. When running ingestion via CLI, the workflow configuration YAML must include a `securityConfig` block with a valid JWT token from the ingestion-bot.

Specifically, set the `authProvider` to `openmetadata` and provide the token in `workflowConfig.openMetadataServerConfig.securityConfig.jwtToken`. The primary method is using a [[personal-access-token|JWT token]] (bot token). See [[cli-ingestion-with-basic-auth]] for an alternative authentication pattern using Basic Auth, and [[security-config]] for general security configuration details.

Example:

```yaml
workflowConfig:
  openMetadataServerConfig:
    hostPort: "http://localhost:8585/api"
    authProvider: openmetadata
    securityConfig:
      jwtToken: "{bot_jwt_token}"
```

## Connector-Specific Usage

### REST Connector

When using the [[rest-api-connector|REST API Connector]], the CLI is used for external execution. The YAML configuration must include:

- Source configuration with `type: Rest`, `openAPISchemaURL`, and optional token.
- Source config with `type: ApiMetadata`.
- Sink configuration with `type: metadata-rest`.
- Workflow configuration with OpenMetadata server connection and JWT token authentication.

For the complete configuration reference, see [[rest-connector-yaml-config]].

### PostgreSQL Connector

For the [[postgresql-connector]], complete YAML configurations for all workflow types are available in the connector documentation.

## Relationship to the Ingestion Framework

The `metadata` CLI is a front-end to the [[ingestion-framework]], which handles the actual extraction and loading of metadata from source systems into OpenMetadata.

## See Also

- [[cli-ingestion-with-basic-auth]] — Alternative CLI ingestion pattern for database connectors.
- [[external-connector-execution]] — General guide for running connectors externally via CLI.
- [[external-ingestion-workflow]] — The concept of running ingestion pipelines externally.
- [[bot-authentication]] — How automated applications authenticate using JWT tokens.
- [[rest-connector-yaml-config]] — YAML configuration reference for the REST connector.
- [[postgresql-connector]] — Example connector with complete YAML configurations.
- [[kubernetes-native-orchestrator]] — Alternative orchestration method.