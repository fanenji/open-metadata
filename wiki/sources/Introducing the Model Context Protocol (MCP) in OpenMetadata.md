---
type: source
title: "Introducing the Model Context Protocol (MCP) in OpenMetadata"
created: 2026-04-29
updated: 2026-04-29
tags: [openmetadata, mcp, ai, metadata, governance]
related: [openmetadata, model-context-protocol, openmetadata-mcp-server, mcp-enterprise-implementation-patterns, data-catalog-tool-comparison, data-observability-definition, data-discovery-tools]
sources: ["Introducing the Model Context Protocol (MCP) in OpenMetadata.md"]
authors: [Sriharsha Chintalapani, Ezio, Pere Miquel Brull]
year: 2025
url: "https://blog.open-metadata.org/introducing-the-model-context-protocol-mcp-in-openmetadata-e757385f4fb2"
venue: "OpenMetadata Blog"
---
# Introducing the Model Context Protocol (MCP) in OpenMetadata

This article announces enterprise-grade support for the Model Context Protocol (MCP) built natively into the OpenMetadata platform. It argues that OpenMetadata's Unified Knowledge Graph, combined with MCP, transforms the platform from a human-only metadata interface into a central hub for both human and AI agents.

## Key Claims

- OpenMetadata's MCP server is embedded directly into the platform, requiring no extra components to deploy.
- The MCP server inherits OpenMetadata's RBAC, policy engine, and audit capabilities, ensuring consistent governance for AI agents.
- The server returns only the necessary information to LLMs, optimizing limited context windows.
- Use cases include conversational metadata access, governance automation, and on-demand lineage tracing.

## Architecture

The MCP server is backed by OpenMetadata's Application Framework. Installing the MCP application exposes the `/mcp` endpoint within the same server. When an LLM executes a tool, the server: (1) identifies the user via JWT token, (2) authorizes the action via RBAC, (3) audits the sequence of actions, and (4) uses the knowledge graph to retrieve or update information.

## Limitations

- The article is a product announcement with no independent benchmarks or user validation.
- Claims of "enterprise-grade" readiness lack independent security audits.
- The implementation requires Personal Access Tokens or JWT authentication, creating a technical barrier for non-technical users.