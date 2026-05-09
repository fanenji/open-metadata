---
type: entity
title: Keycloak
created: 2026-05-08
updated: 2026-05-08
tags: [identity, authentication, authorization]
related: [mcp-security-best-practices, ai-agent-governance]
sources: ["research-security-implications-of-mcp-exposure-2026-05-08.md"]
---
# Keycloak

Keycloak is an open-source identity and access management solution. It is recommended as an identity provider for integrating RBAC with [[model-context-protocol]] (MCP) servers to enforce granular permissions at the tool level.

## Role in MCP Security
- Provides centralized identity management for MCP deployments
- Enables RBAC integration for tool-level access control
- Supports OAuth 2.0 and OIDC protocols used by MCP

## Related Pages
- [[mcp-security-best-practices]] — Authentication and authorization recommendations
- [[ai-agent-governance]] — Broader governance framework