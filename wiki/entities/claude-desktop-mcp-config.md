---
type: entity
title: Claude Desktop MCP Configuration
created: 2026-05-06
updated: 2026-05-06
tags: [claude, mcp, configuration, json]
related: [model-context-protocol, openmetadata, @modelcontextprotocol/server-openmetadata]
sources: ["Configurare Claude con server MCP di OpenMetadata.md"]
---
# Claude Desktop MCP Configuration

This page details the configuration required to enable the [[model-context-protocol]] within the Claude Desktop application.

## Configuration Files
The location of the configuration file depends on the operating system:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

## JSON Template for OpenMetadata
To connect Claude Desktop to [[openmetadata]], add the following block to the `mcpServers` section:

```json
{
  "mcpServers": {
    "openmetadata": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-openmetadata"
      ],
      "env": {
        "OPENMETADATA_HOST": "https://your-openmetadata-instance.com",
        "OPENMETADATA_TOKEN": "your-jwt-token"
      }
    }
  }
}
```

## Requirements
- **Authentication**: A valid JWT token generated from an [[openmetadata]] service account or bot.
- **Runtime**: Access to `npx` or a globally installed `@modelcontextprotocol/server-openmetadata` package.
