---
type: entity
title: "@modelcontextprotocol/server-openmetadata"
created: 2026-05-06
updated: 2026-05-06
tags: [mcp, npm, openmetadata, tool]
related: [model-context-protocol, openmetadata]
sources: ["Configurare Claude con server $\text{server MCP di OpenMetadata.md"]
---
# @modelcontextprotocol/server-openmetadata

The `@modelcontextprotocol/server-openmetadata` is a specialized MCP server implementation that acts as a bridge between LLM clients (like Claude) and the [[openmetadata]] platform.

## Functionality
It allows AI agents to browse metadata, inspect table schemas, and understand data lineage by translating MCP requests into OpenMetadata API calls.

## Installation and Execution
The server can be run using `npm` or `npx`:

```bash
# Global installation
npm install -g @modelcontextprotocol/server-openmetadata

# Execution via npx
npx @modelcontextprotocol/server-openmetadata
```

## Required Environment Variables
For the server to authenticate and connect to the metadata repository, the following variables must be provided in the MCP client configuration:
- `OPENMETADATA_HOST`: The base URL of the OpenMetadata instance.
- `OPENJWT_TOKEN`: A valid JSON Web Token (JWT) generated from an OpenMetadata service account.
