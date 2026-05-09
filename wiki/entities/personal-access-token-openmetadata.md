---
type: entity
title: Personal Access Token (OpenMetadata)
created: 2026-04-29
updated: 2026-04-29
tags: [openmetadata, authentication, security, rbac]
related: [openmetadata, openmetadata-mcp-server, model-context-protocol]
sources: ["Embedding an MCP Server into OpenMetadata - Summary.md"]
---
# Personal Access Token (OpenMetadata)

A Personal Access Token (PAT) is an authentication mechanism in [[openmetadata|OpenMetadata]] that enables programmatic and AI-driven access to the platform while preserving per-user Role-Based Access Control (RBAC).

## How It Works

1. A user generates a PAT from their OpenMetadata profile page with a configurable expiry date.
2. The token embeds the user's identity and inherits all their permissions, roles, and inherited policies.
3. The user configures their LLM client (e.g., Claude Desktop, Goose, ChatGPT) with the PAT as the MCP auth credential.
4. Every call made through the [[openmetadata-mcp-server|MCP server]] is executed on behalf of that user's identity.

## Security Properties

- **No privilege escalation** — The LLM can only surface data the user is already authorized to see
- **Configurable expiry** — Tokens can be set to expire after a defined period
- **Per-user identity** — Each token carries a specific user's identity, not a generic service account
- **Existing RBAC enforcement** — All permissions, roles, and data restrictions apply automatically

## Use Cases

- Configuring LLM clients for [[model-context-protocol|MCP]] access to OpenMetadata
- API access for automation scripts and CI/CD pipelines
- Service-to-service authentication within the data platform
