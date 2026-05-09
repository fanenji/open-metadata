---
type: source
title: "Configurare Claude con server MCP di OpenMetadata"
created: 2026-02-13
updated: 2026-05-06
tags: [claude-code, mcp, openmetadata, tools]
authors: []
year: 2026
url: "https://claude.ai/chat/8/838a8df9-232f-49f7-9fc2-d59158f1041c"
venue: "Claude AI Chat"
sources: ["Configurare Claude con server MCP di OpenMetadata.md"]
---
# Configurare Claude con server MCP di OpenMetadata

Technical guide for configuring Claude Desktop and Claude Code to interact with OpenMetadata using the Model Context Protocol (MCP).

## Overview
This source provides instructions for installing the `@modelcontextprotocol/server-openmetadata` package and configuring the environment variables (`OPENMETADATA_HOST` and `OPENMETADATA_TOKEN`) within the JSON configuration files of Claude's interfaces.

## Key Steps
1. **Installation**: Using `npm` or `npx` to run the OpenMetadata MCP server.
2. **Claude Desktop Configuration**: Editing `claude_desktop_config.json` on macOS or Windows.
3. **Claude Code Configuration**: Editing `~/.config/claude-code/config.json`.
4. **Authentication**: Generating a JWT token via OpenMetadata Service Accounts/Bots.
