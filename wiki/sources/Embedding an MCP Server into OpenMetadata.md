---
type: source
title: "Embedding An Mcp Server Into Openmetadata"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
authors: []
year: 2026
url: ""
venue: ""
---

type: source
title: "Embedding an MCP Server into OpenMetadata"
created: 2026-05-14
updated: 2026-05-14
tags: [mcp, ai, agentic-ai, architecture, authentication]
related: [mcp-server, unified-metadata-graph, application-framework, personal-access-token, hybrid-rbac-abac-model, model-context-protocol]
sources: ["Embedding an MCP Server into OpenMetadata.md"]
authors: [OpenMetadata]
year: 2025
url: "https://www.youtube.com/watch?v=AuYBaXC8-M4"
venue: "OpenMetadata Community Meetup"
---

# Embedding an MCP Server into OpenMetadata

This source is a community meetup presentation (May 21, 2025) by Collate, Inc. detailing the rationale, architecture, and use cases for embedding a Model Context Protocol (MCP) server directly into OpenMetadata. The presentation covers why MCP bridges the gap between LLMs and OpenMetadata's unified knowledge graph, the challenges of standalone MCP deployments, and how OpenMetadata solves these by embedding MCP as a built-in application with identity-preserving authentication via Personal Access Tokens (PAT).

## Key Takeaways

- **MCP bridges LLMs and the unified knowledge graph.** LLMs need context about data assets; MCP provides a standardized interface to expose that context.
- **Embedded architecture solves scalability, simplicity, and accessibility.** Running MCP as an application within the OpenMetadata server eliminates the need for every user to run a local MCP server, maintains a small deployment footprint, and makes AI accessible to non-technical users.
- **Personal Access Tokens enable identity-preserving AI interactions.** When a user connects via PAT, all MCP calls inherit their RBAC/ABAC permissions, preventing unauthorized data exposure.
- **The unified knowledge graph provides richer context than simple API wrappers.** MCP exposes not just schema but lineage, data quality results, profiling, queries, ownership, and semantic tags.
- **Two demo scenarios:** A data analyst using MCP to discover customer tables and generate a retention dashboard; a data steward using MCP to bulk-assign ownership of unowned customer assets.
- **Feature status:** Work in progress, targeting v1.8.8 release.

## Architecture

The MCP server is built using OpenMetadata's pluggable Application Framework (Settings → Applications). When enabled, it exposes MCP server APIs alongside the existing REST APIs. Users connect their LLM clients (Claude Desktop, Goose, ChatGPT) directly to the OpenMetadata server endpoint using a Personal Access Token, which embeds their identity and permissions.