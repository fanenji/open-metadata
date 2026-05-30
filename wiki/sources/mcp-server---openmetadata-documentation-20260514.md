---
type: source
title: "MCP Server - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [mcp, ai, metadata, openmetadata, integration]
related: [mcp-server, model-context-protocol, openmetadata, unified-metadata-graph, roles-and-policies]
sources: ["mcp-server---openmetadata-documentation-20260514.md"]
authors: []
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/mcp"
venue: "OpenMetadata Official Documentation"
---
# MCP Server - OpenMetadata Documentation

Official documentation for the OpenMetadata MCP Server (v1.12.x), a built-in application that exposes the platform's unified metadata graph to AI assistants via the Model Context Protocol (MCP).

## Overview

The MCP Server enables technical and non-technical users to interact with organizational metadata through natural language conversations with AI systems such as ChatGPT or Claude. It bridges the gap between AI reasoning and real-world data context by providing live access to definitions, lineage, ownership, and other metadata from the unified knowledge graph.

## Key Topics

- **Model Context Protocol (MCP)**: An open standard (spearheaded by Anthropic) for connecting AI systems to external tools and data in a uniform, secure way.
- **Installation**: The MCP Server is an OpenMetadata application installed from the marketplace at `/marketplace/apps/McpApplication`.
- **Authentication**: Supports OAuth 2.0 (recommended, using existing SSO login) and Personal Access Tokens (PATs) for headless environments. PATs inherit the user's roles and policies.
- **Client Integration**: Dedicated getting-started guides for Claude Desktop, Claude Code, Cursor, VS Code, and Goose.
- **MCP Tools**: Discovery & Search tools and Governance & Lineage tools exposed to AI assistants.

## Significance

This source documents a shipped feature that extends OpenMetadata's capabilities into AI-driven interactions, making the unified metadata graph queryable through natural language. It establishes the MCP Server as an enterprise-ready bridge between metadata governance and AI-assisted workflows.