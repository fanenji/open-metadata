---
type: concept
title: External Connector Execution
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, ingestion, cli, orchestration, external-schedulers]
related: [rest-connector-yaml-config, metadata-cli, cli-ingestion-with-basic-auth, ingestion-framework, rest-api-connector]
sources: ["run-the-openapi-rest-connector-externally---openme-20260514.md"]
---

# External Connector Execution

External Connector Execution is the pattern of running OpenMetadata ingestion pipelines outside the UI-based ingestion container, using a YAML configuration file and the `metadata ingest` CLI command. This approach allows users to manage ingestion workflows on their preferred orchestrator (e.g., Apache Airflow, Kubernetes CronJobs, or other schedulers) rather than relying on the built-in OpenMetadata ingestion container.

## How It Works

1. **Create a YAML Config**: Define the source connection, sink, and workflow configuration in a YAML file. The structure varies by connector type but follows a consistent pattern.
2. **Run with CLI**: Execute `metadata ingest -c <path-to-yaml>` to trigger the ingestion pipeline.
3. **Orchestrate Externally**: Schedule the CLI command using external schedulers or orchestration tools.

## Supported Connectors

The external execution pattern is documented for multiple connector types, including:
- [[rest-api-connector|REST API Connector]] (via [[rest-connector-yaml-config]])
- Database connectors (via [[cli-ingestion-with-basic-auth]])
- Other connectors following the same YAML + CLI pattern

## Authentication

External execution requires authentication with the OpenMetadata server. The primary method is using a [[personal-access-token|JWT token]] (bot token) configured in the `workflowConfig.openMetadataServerConfig.securityConfig.jwtToken` field. The `authProvider` must be set to `openmetadata`.

## Advantages

- **Flexibility**: Use existing orchestration infrastructure instead of the OpenMetadata ingestion container.
- **Custom Scheduling**: Fine-grained control over when and how often ingestion runs.
- **Integration**: Embed ingestion into existing data pipelines and workflows.

## Considerations

- The YAML config must be maintained separately from the UI-based configuration.
- JWT token lifecycle management (rotation, expiration) must be handled externally.
- Troubleshooting external execution may require familiarity with the CLI and YAML config structure, as UI-based troubleshooting tools may not apply.
- The `storeServiceConnection` flag determines whether connection details are persisted in OpenMetadata.