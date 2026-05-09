---
type: entity
title: OpenMetadata dbt Ingestion
created: 2026-02-17
updated: 2026-02-17
tags: [openmetadata, dbt, metadata-ingestion, data-catalog]
related: [openmetadata, dbt, openmetadata-mcp-server, openmetadata-local-development, custom-connector-openmetadata, model-context-protocol]
sources: ["OPENMETADATA - NOTE.md"]
---
# OpenMetadata dbt Ingestion

The OpenMetadata dbt Ingestion workflow is the process of importing metadata from dbt projects (models, tests, lineage, documentation) into OpenMetadata. It is the primary integration pattern for synchronizing dbt's transformation metadata with the central data catalog.

## Setup

The integration uses the `openmetadata-ingestion[dbt]` Python package:

```bash
pip install "openmetadata-ingestion[dbt]"==1.10.14
metadata --debug ingest-dbt
```

## Configuration

Configuration is specified in `dbt-project.yml` under the `vars` block:

```yaml
vars:
  openmetadata_host_port: "http://openmetadata-server.openmetadata-docker.orb.local"
  openmetadata_jwt_token: "your-jwt-token-here"
  openmetadata_service_name: "your-database-service-name"
```

Key parameters:
- **openmetadata_host_port**: URL of the OpenMetadata server
- **openmetadata_jwt_token**: JWT token for API authentication
- **openmetadata_service_name**: Name of the database service in OpenMetadata to associate with the dbt models

## Workflow

1. dbt runs and produces artifacts (manifest, run_results, catalog JSON files)
2. The `openmetadata-ingestion[dbt]` package reads these artifacts
3. Metadata is ingested into OpenMetadata, including:
   - Model definitions and schemas
   - Test results and status
   - Column-level lineage
   - Documentation and descriptions

## Version Notes

The note pins the ingestion package to version 1.10.14 while the OpenMetadata server is version 1.11.0. This version mismatch should be monitored for compatibility issues.

## Connections

- Complements [[openmetadata-dremio-connector]] as an alternative metadata ingestion path
- Provides the metadata foundation for [[openmetadata-mcp-server]] to query
- Enables [[model-context-protocol]] agents to access dbt metadata through OpenMetadata
- Contrasts with [[custom-connector-openmetadata]] which requires building a custom integration