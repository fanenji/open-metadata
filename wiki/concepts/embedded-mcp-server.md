---
type: concept
title: Embedded MCP Server
created: 2026-04-29
updated: 2026-05-07
tags: [mcp, architecture, deployment, ai, openmetadata, governance]
related: [openmetadata-mcp-server, model-context-protocol, openmetadata-application-framework, dremio-mcp-server, dbt-mcp-server, openmetadata-mcp-integration, openmetadata, authorization-reuse]
sources: ["Embedding an MCP Server into OpenMetadata - Summary.md", "OpenMetadata MCP.md"]
---
# Embedded MCP Server

An Embedded MCP Server is a [[model-context-protocol|Model Context Protocol]] server that runs inside the host application's server process rather than as a separate, independently deployed service. By integrating directly into an existing platform, it shares the platform's authorization engine, authentication mechanisms, and data access patterns. This architectural pattern is exemplified by the [[openmetadata-mcp-server|OpenMetadata MCP Server]], which runs as an [[openmetadata-application-framework|OpenMetadata Application]].

## OpenMetadata Implementation

OpenMetadata v1.8.0 introduced an embedded MCP server that shares its authorization engine with the platform's REST APIs. This means:

- AI agents (Claude, Cursor, OpenAI) connect to the same OpenMetadata instance.
- Agents inherit existing roles, policies, and access controls.
- No separate authentication or authorization setup is needed for AI access.
- Governance policies apply uniformly to human and AI interactions.

## Advantages Over External MCP Servers

| Aspect | Embedded | External |
|--------|----------|----------|
| **Deployment** | Single service to deploy | Requires separate server setup |
| **Authentication** | Leverages host's existing auth | Must implement auth independently |
| **Authorization** | Inherits host's RBAC | Must replicate or proxy RBAC |
| **Performance** | Direct in-process access to data | Network round-trip overhead |
| **Maintenance** | Updated with host application | Independent update cycle |
| **Consistency** | Same APIs and data accessible via MCP and REST | Risk of divergence between interfaces |

### Benefits in Practice

Organizations adopting the embedded pattern experience:

- **Security** — AI agents cannot bypass existing governance policies; the same access controls apply to both human and AI interactions.
- **Simplicity** — No separate MCP server to deploy, configure, or secure, reducing operational overhead.
- **Consistency** — The same data and metadata are accessible through both REST APIs and MCP, providing a unified view for all consumers.

## Challenges

- **Tight coupling** — The MCP server is tied to the host application's version and lifecycle.
- **Resource contention** — MCP operations share CPU and memory with the host application.
- **Limited isolation** — A bug in the MCP server could affect the host application.

## When to Use

- The host application already has rich internal data structures (e.g., a knowledge graph) that are expensive to expose via external APIs.
- The host application has a mature RBAC system that should be preserved for AI access.
- Deployment simplicity is a priority over isolation.

## Comparison with Other Implementations

Standalone MCP servers like [[dremio-mcp-server]] and [[dbt-mcp-server]] follow the external server pattern, requiring separate deployment and authentication configuration. The embedded pattern in OpenMetadata offers simpler deployment, stronger auth integration, and unified governance, but provides less isolation between the MCP server and the host application.