---
type: source
title: Embedding an MCP Server into OpenMetadata
created: 2026-04-04
updated: 2026-04-04
tags: [openmetadata, mcp, ai, agentic-ai, knowledge-graph]
related: [openmetadata, model-context-protocol, openmetadata-mcp-server, openmetadata-application-framework, openmetadata-personal-access-token]
sources: ["Embedding an MCP Server into OpenMetadata.md"]
authors: [Shihara, Moit]
year: 2025
url: "https://www.youtube.com/watch?v=AuYBaXC8-M4"
venue: OpenMetadata Community Meetup
---
# Embedding an MCP Server into OpenMetadata

This talk from the OpenMetadata community meetup (May 21, 2025) presents the architectural decision to embed a [[model-context-protocol]] (MCP) server directly into the [[openmetadata]] platform as an application, rather than running it as a separate service. The presenters, Shihara and Moit from [[Collate]], demonstrate how this approach solves three key challenges: scalability, deployment complexity, and authentication/authorization.

## Key Arguments

1. **Scalability**: Running a separate MCP server per user (e.g., on each data engineer's laptop) is not scalable. Embedding the MCP server into OpenMetadata means every user in the organization can connect their LLM client (Claude Desktop, Goose, ChatGPT) to a single, centrally managed endpoint.

2. **Deployment Simplicity**: OpenMetadata already ships with a small footprint (four components). Adding a separate MCP server would increase complexity. By using the [[openmetadata-application-framework]], the MCP server becomes a built-in, enable-able feature.

3. **Authentication and Authorization**: MCP's lack of built-in auth is a widely recognized challenge. OpenMetadata solves this by leveraging its existing RBAC/ABAC system via [[openmetadata-personal-access-token]] (PAT). When a user connects their LLM client with their PAT, all MCP requests are executed under that user's identity and permissions, ensuring users only access metadata they are authorized to see.

## Demo Use Cases

- **Data Analyst**: Uses MCP to discover tables related to "customer," understand schemas and associated queries, and build a customer retention dashboard.
- **Data Steward**: Uses MCP to find customer assets without owners, look up the "data team," and bulk-assign ownership to that team.

## Status

The MCP server was merged into OpenMetadata open source in version 1.8.8 (May 2025). At the time of the talk, basic tools (search, read, patch) were available, with more tools planned for future releases.

## Connections

- Strengthens [[model-context-protocol]] with a concrete production implementation.
- Extends [[openmetadata]] with AI integration capabilities.
- Related to [[custom-connector-openmetadata]] as another example of extending OpenMetadata via its framework.
- Relevant to [[data-catalog-tool-comparison]] as a differentiating feature.