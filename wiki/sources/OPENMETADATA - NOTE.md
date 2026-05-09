---
type: source
title: OpenMetadata - Technical Setup Note
created: 2026-02-17
updated: 2026-02-17
tags: [openmetadata, dbt, mcp, data-platform, configuration]
related: [openmetadata, openmetadata-dbt-ingestion, openmetadata-mcp-server, openmetadata-local-development, model-context-protocol, custom-connector-openmetadata]
sources: ["OPENMETADATA - NOTE.md"]
---
# OpenMetadata - Technical Setup Note

This internal project note documents the technical setup for integrating OpenMetadata into the Data Platform. It covers three main areas:

1. **Local OpenMetadata installation** via Docker Compose (version 1.11.0).
2. **dbt metadata ingestion** using the `openmetadata-ingestion[dbt]` Python package (version 1.10.14) with JWT authentication, configured via `dbt-project.yml` variables.
3. **MCP server configuration** for two AI coding tools — Claude Code and OpenCode — pointing to a remote OpenMetadata instance at `openmetadata-test.dataliguria.it`. The MCP setup uses `mcp-remote` as a proxy with OAuth2-style authentication headers.

The note is a configuration reference rather than an analytical document. It provides concrete, copy-pasteable configuration blocks for each integration point. Key details include the Docker Compose download URL, the pip install command with version pinning, the dbt project YAML variables for OpenMetadata connection, and the JSON configuration for both Claude Code and OpenCode MCP servers.

## Key Technical Details

- **OpenMetadata Version**: 1.11.0 (server), 1.10.14 (dbt ingestion package)
- **Authentication**: JWT token for dbt ingestion, Bearer token header for MCP
- **MCP Proxy**: `mcp-remote` npm package used to connect to remote OpenMetadata MCP endpoint
- **Test Server**: `openmetadata-test.dataliguria.it` (Dataliguria organization)
- **Local Path**: `~/Development/DP/openmetadata-docker`

## Connections

- Provides concrete implementation details for [[openmetadata]]
- Documents the [[openmetadata-dbt-ingestion]] workflow
- Configures the [[openmetadata-mcp-server]] for AI agent interaction
- Demonstrates [[model-context-protocol]] in practice with a real metadata platform
- Shows an alternative to [[custom-connector-openmetadata]] for metadata ingestion