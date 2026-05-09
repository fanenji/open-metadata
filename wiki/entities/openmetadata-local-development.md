---
type: entity
title: OpenMetadata Local Development
created: 2026-02-17
updated: 2026-02-17
tags: [openmetadata, docker, development, data-catalog]
related: [openmetadata, openmetadata-dbt-ingestion, openmetadata-mcp-server]
sources: ["OPENMETADATA - NOTE.md"]
---
# OpenMetadata Local Development

Local development setup for OpenMetadata using Docker Compose. This configuration is used for testing integrations (dbt ingestion, MCP server) before deploying to production.

## Installation

```bash
curl -sL -o docker-compose.yml https://github.com/open-metadata/OpenMetadata/releases/download/1.11.0-release/docker-compose.yml
```

The Docker Compose file is downloaded directly from the OpenMetadata GitHub release page. The local instance runs at `http://openmetadata-server.openmetadata-docker.orb.local`.

## Directory Structure

- **Base Path**: `~/Development/DP/openmetadata-docker`
- **Project Path**: `/Users/stefano/Development/DP/dbt-projects/test_local_openmetadata`

## Version

- **OpenMetadata Server**: 1.11.0
- **dbt Ingestion Package**: 1.10.14 (pinned)

## Usage

1. Download the Docker Compose file
2. Start the containers: `docker-compose up -d`
3. Configure dbt project with local OpenMetadata connection details
4. Run dbt ingestion: `metadata --debug ingest-dbt`
5. Test MCP server connection to local instance

## Connections

- Provides the development environment for [[openmetadata-dbt-ingestion]] testing
- Serves as a local test target for [[openmetadata-mcp-server]] configuration
- Supports the broader [[openmetadata]] platform development workflow