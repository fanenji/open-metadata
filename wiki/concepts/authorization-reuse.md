---
type: concept
title: Authorization Reuse
created: 2026-04-04
updated: 2026-04-04
tags: [governance, security, mcp, ai]
related: [embedded-mcp-server, openmetadata-mcp-integration, model-context-protocol]
sources: ["OpenMetadata MCP.md"]
---
# Authorization Reuse

Authorization reuse is the architectural pattern where an MCP server or other integration point uses the same authorization engine as the host platform's existing APIs, rather than implementing its own access control logic.

## In OpenMetadata

The OpenMetadata MCP integration exemplifies this pattern: the embedded MCP server uses the same authorization engine as OpenMetadata's REST APIs. Any MCP client connecting to the server automatically operates under the roles, policies, and access controls already defined in OpenMetadata. This ensures that AI agents cannot bypass governance — they are subject to the same constraints as human users.

## Benefits

- **Consistent governance**: AI agents inherit existing access controls without additional configuration.
- **Reduced attack surface**: No separate authorization system to secure or audit.
- **Simplified compliance**: Audit logs and policy enforcement apply uniformly.

## Related Patterns

This contrasts with standalone MCP servers that must implement their own authorization or delegate to an external identity provider, potentially creating gaps or inconsistencies in governance.