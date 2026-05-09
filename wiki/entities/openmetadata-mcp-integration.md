---
type: entity
title: OpenMetadata MCP Integration
created: 2026-04-04
updated: 2026-04-04
tags: [openmetadata, mcp, ai, data-catalog]
related: [openmetadata, model-context-protocol, collate, custom-connector-openmetadata, dremio-mcp-server]
sources: ["OpenMetadata MCP.md"]
---
# OpenMetadata MCP Integration

The OpenMetadata MCP Integration refers to the embedded Model Context Protocol (MCP) server introduced in OpenMetadata v1.8.0. Unlike standalone MCP servers that run as separate services, this integration embeds the MCP server directly into the OpenMetadata platform, sharing its authorization engine.

## Architecture

The key architectural decision is **authorization reuse**: the MCP server uses the same authorization engine as OpenMetadata's REST APIs. This means any MCP client (such as Claude, Cursor, or OpenAI) connecting to the server automatically inherits the roles, policies, and access controls already defined in OpenMetadata. AI agents cannot bypass governance — they operate under the same constraints as human users.

## Use Cases

- **Intelligent pipeline monitoring**: AI agents can query OpenMetadata for pipeline status, lineage, and quality metrics to detect and diagnose issues.
- **Dashboard generation from metadata analysis**: Agents can analyze metadata to suggest or generate dashboards.
- **Automated data glossary creation**: Agents can read schema definitions and business context to propose glossary terms and classifications.

## Comparison with Other MCP Implementations

Unlike the [[dremio-mcp-server]], which is a self-hosted standalone server for a specific query engine, the OpenMetadata MCP integration is embedded and governance-aware. The two could be complementary: the Dremio MCP server provides data access, while the OpenMetadata MCP server provides metadata context and governance.

## Open Questions

- How does the MCP server compare to OpenMetadata's existing REST API for programmatic access?
- What specific MCP tools/endpoints does the server expose?
- Are there performance or security implications of exposing OpenMetadata via MCP to AI agents?