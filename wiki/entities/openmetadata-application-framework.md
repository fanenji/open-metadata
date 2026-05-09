---
type: entity
title: OpenMetadata Application Framework
created: 2026-04-29
updated: 2026-05-07
tags: ["openmetadata", "architecture", "extensibility", "plugins"]
related: ["openmetadata", "openmetadata-mcp-server", "personal-access-token-openmetadata", "custom-connector-openmetadata"]
sources: ["Embedding an MCP Server into OpenMetadata - Summary.md", "Embedding an MCP Server into OpenMetadata.md"]
---
# OpenMetadata Application Framework

The OpenMetadata Application Framework is a pluggable module system within [[openmetadata]] that allows embedding custom tools and applications directly into the OpenMetadata server. It provides a standardized way to add new capabilities without modifying core code or deploying separate services. The framework is accessible via the Settings → Applications menu in the OpenMetadata UI.

## Purpose

The framework enables extending OpenMetadata's feature set without requiring separate services or infrastructure. Built-in applications cover data insights, search indexing, telemetry, and development data tools, among others.

## Built-in Applications

- **Data Insights** — Analytics and reporting on metadata usage and quality
- **Search Indexing** — Elasticsearch/Search indexing for metadata discovery
- **MCP Server Application** — Embedded [[openmetadata-mcp-server|MCP server]] for AI agent integration
- **Telemetry** — Usage and performance data collection
- **Development Data Tools** — Utilities for development and testing

## Architecture

Applications run inside the OpenMetadata server process and share the same host, port, and authentication infrastructure. They can access internal data structures (knowledge graph, lineage, quality results) directly without going through external APIs.

## Benefits

- **Simplified deployment** — No separate services to manage
- **Shared auth** — Leverages existing RBAC and PAT mechanisms
- **Direct access** — Applications can use internal knowledge graph structures
- **Consistent lifecycle** — Enable/disable via the same management interface

## Use Cases

The framework enables extending OpenMetadata with custom applications for:

- AI/agent integration (MCP server)
- Custom governance workflows
- Automated metadata enrichment
- Integration with external systems

### Key Use Case: MCP Server

The [[openmetadata-mcp-server]] is implemented as an application within this framework. This architectural choice means:

- The MCP server starts automatically with the OpenMetadata server.
- No additional deployment or configuration is needed beyond enabling the application.
- The MCP server shares the same authentication, authorization, and networking context as the main OpenMetadata server.

## Related Patterns

This framework is conceptually similar to the [[custom-connector-openmetadata]] pattern, which allows building user-defined integrations for metadata ingestion. Both demonstrate OpenMetadata's extensibility through its own APIs and frameworks.