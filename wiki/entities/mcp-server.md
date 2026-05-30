---
type: entity
title: MCP Server
created: 2026-05-14
updated: 2026-05-14
tags: [mcp, ai, metadata, openmetadata, integration]
related: [model-context-protocol, openmetadata, unified-metadata-graph, roles-and-policies, google-oauth, openmetadata-features]
sources: ["mcp-server---openmetadata-documentation-20260514.md"]
---
# MCP Server

The OpenMetadata MCP Server is a built-in application that exposes the platform's [[unified-metadata-graph]] to AI assistants via the [[model-context-protocol|Model Context Protocol (MCP)]]. It enables technical and non-technical users to interact with organizational metadata through natural language conversations with AI systems such as ChatGPT or Claude.

## Installation

The MCP Server is an OpenMetadata application installed from the marketplace:

1. Navigate to `<YOUR-OpenMetadata-SERVER>/marketplace/apps/McpApplication`
2. Select **Install**

It is installed by default in OpenMetadata v1.12.x.

## Authentication

The MCP Server supports two authentication methods:

### OAuth 2.0 (Recommended)

Connect using your existing OpenMetadata login — the same way you sign in to the OpenMetadata UI. No tokens to generate or manage. OAuth works with all supported SSO providers (Google, Azure, Okta, Auth0, LDAP, SAML, and more), leveraging the existing [[google-oauth]] and SSO infrastructure.

### Personal Access Token (PAT)

For environments where browser-based login is not available (headless agents, automation), a Personal Access Token can be used. Generate a PAT at `<YOUR-OpenMetadata-SERVER>/users/<YOUR-USERNAME>/access-token`.

**Important**: A PAT grants the AI agent the same role and access policy assigned to the user who generated it. To provide different role-based access controls, create a dedicated user with scoped permissions. This directly ties into the [[roles-and-policies]] framework.

## Value Proposition

- **Real-time metadata context**: AI assistants can query live organizational metadata — definitions, lineage, ownership, last-updated timestamps.
- **Natural language interface**: Users ask questions like "What is the definition of this metric?" or "Show me the lineage of data feeding this dashboard."
- **Enterprise-ready**: Access is governed by existing OpenMetadata roles and policies; all relationships and context from the unified knowledge graph are available.
- **Broad client support**: Dedicated guides for Claude Desktop, Claude Code, Cursor, VS Code, and Goose.

## MCP Tools

The server exposes two categories of tools to AI assistants:

- **Discovery & Search**: Tools for finding and exploring metadata assets.
- **Governance & Lineage**: Tools for understanding data provenance, ownership, and governance context.

## See Also

- [[model-context-protocol]] — The underlying open standard enabling this integration.
- [[unified-metadata-graph]] — The core architectural component that the MCP Server queries.
- [[roles-and-policies]] — The access control framework governing MCP Server permissions.
- [[openmetadata-features]] — Comprehensive feature overview including AI-powered interaction.