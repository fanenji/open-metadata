---
type: entity
title: Claude Code
created: 2026-05-06
updated: 2026-05-06
tags: [claude, cli, ai-agent]
related: [model-context-protocol, openmetadata]
sources: ["Configurare Claude con server MCP di OpenMetadata.md"]
---
# Claude Code

**Claude Code** is a CLI-based interface for Claude, designed for agentic software engineering and data engineering tasks directly from the terminal.

## Integration with Data Platforms
Claude Code can be extended using the [[model-context-protocol]] to gain semantic awareness of the data landscape. By configuring an MCP server, Claude Code can query [[openmetadata]] to understand schemas, lineage, and data quality metrics.

## Configuration
Configuration is managed via a JSON file located at `~/.config/claude-code/config.json`. The configuration allows for the definition of `mcpServers`, enabling the tool to execute commands and access environment variables required for external data connections.
