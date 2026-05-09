---
type: entity
title: OpenMetadata Personal Access Token
created: 2026-04-04
updated: 2026-04-04
tags: [openmetadata, authentication, security]
related: [openmetadata, openmetadata-mcp-server, model-context-protocol]
sources: ["Embedding an MCP Server into OpenMetadata.md"]
---
# OpenMetadata Personal Access Token

A Personal Access Token (PAT) in [[openmetadata]] is an authentication mechanism that allows users to generate a token tied to their identity. The token is configurable with an expiration date and is used to authenticate API requests on behalf of the user.

## Role in MCP

The PAT is a critical component of the [[openmetadata-mcp-server]] architecture. When a user connects their LLM client (e.g., Claude Desktop) to the MCP server, they provide their PAT. This token carries the user's identity, roles, and permissions, ensuring that all MCP requests are executed under the user's security context.

## Benefits

- **Identity Injection**: Solves the MCP authentication challenge by embedding user identity into every request.
- **RBAC/ABAC Enforcement**: Users only access metadata they are authorized to see, preventing unauthorized data exposure through LLM interactions.
- **Auditability**: All actions performed via MCP are traceable to the specific user who initiated them.