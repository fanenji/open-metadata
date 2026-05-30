---
type: entity
title: "Application Framework"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: entity
title: Application Framework
created: 2026-05-14
updated: 2026-05-14
tags: [architecture, extensibility, applications, mcp]
related: [mcp-server, openmetadata-code-layout, unified-metadata-graph]
sources: ["Embedding an MCP Server into OpenMetadata.md"]
---

# Application Framework

The Application Framework is a pluggable system within OpenMetadata that allows tools and features to be embedded directly into the OpenMetadata server as applications. It is accessible via **Settings → Applications** in the UI and serves as the architectural mechanism for extending the platform without requiring separate deployments.

## Built-in Applications

The framework hosts a variety of applications, including:

- **Data Insights Reports** — Analytics and reporting on data estate usage
- **Search Indexing** — Management of Elasticsearch/OpenSearch indices
- **Telemetry** — Usage data collection
- **MCP Server** — The embedded Model Context Protocol server for AI integration

## Role in MCP Integration

The Application Framework is the implementation mechanism for the embedded MCP server. By building MCP as an application rather than a separate component, OpenMetadata achieves:

- **Zero additional deployment** — The MCP server starts when the OpenMetadata server starts
- **Simplified enablement** — Administrators enable it via the Applications UI
- **Unified authentication** — MCP inherits the platform's existing authentication and authorization

## Extensibility

The framework is designed to be pluggable, allowing both OpenMetadata-maintained and custom applications to extend the platform's capabilities.