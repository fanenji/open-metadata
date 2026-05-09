---
type: source
title: "OpenMetadata: #1 Open Source Metadata Platform"
created: 2026-04-04
updated: 2026-04-04
tags: [openmetadata, mcp, ai, data-catalog]
related: [openmetadata, model-context-protocol, openmetadata-mcp-integration, collate]
sources: ["OpenMetadata MCP.md"]
authors: [open-metadata]
year: 2026
url: "https://open-metadata.org/mcp"
venue: ""
---
# OpenMetadata: #1 Open Source Metadata Platform

This page announces the integration of an embedded MCP (Model Context Protocol) server into OpenMetadata, starting with release v1.8.0. The key architectural decision is that the MCP server shares OpenMetadata's existing authorization engine, enabling any MCP client (such as Claude, Cursor, or OpenAI) to read from or write to OpenMetadata integrations while respecting existing roles and policies.

## Key Points

- **Embedded MCP Server**: The MCP server is fully integrated into OpenMetadata, not a separate service.
- **Authorization Reuse**: The server uses the same authorization engine as OpenMetadata APIs, ensuring AI agents inherit existing governance.
- **Use Cases**: Intelligent pipeline monitoring, dashboard generation from metadata analysis, automated data glossary creation.
- **Community**: The OpenMetadata Meetup Group hosts sessions on MCP integration.

## Limitations

This is a marketing/announcement page with no technical depth, benchmarks, or comparison with existing OpenMetadata APIs. No empirical data is provided.