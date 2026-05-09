---
type: concept
title: Confused Deputy (MCP)
created: 2026-05-08
updated: 2026-05-08
tags: [security, mcp, authorization, token-scope]
related: [model-context-protocol, mcp-attack-surface, mcp-security-best-practices]
sources: ["research-security-implications-of-mcp-exposure-2026-05-08.md"]
---
# Confused Deputy (MCP)

The Confused Deputy attack in the context of [[model-context-protocol]] (MCP) occurs when flawed token scope enforcement allows one client or tool to act on behalf of another, leading to unauthorized actions.

## Mechanism
1. An MCP server grants a token with specific scopes to a client.
2. Due to flawed scope enforcement, another client can use the same token to perform actions beyond its intended scope.
3. The deputy (MCP server) is "confused" about which client is making the request.

## Risks
- Unauthorized data access
- Privilege escalation
- Data exfiltration

## Mitigation
- Rigorously validate token scopes on every request
- Implement per-request identity verification
- Use short-lived tokens with narrow scopes
- Audit all token usage patterns

## Related Pages
- [[mcp-attack-surface]] — The threat landscape
- [[mcp-security-best-practices]] — Authentication and authorization recommendations