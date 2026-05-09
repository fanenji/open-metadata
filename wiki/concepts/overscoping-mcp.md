---
type: concept
title: Overscoping (MCP)
created: 2026-05-08
updated: 2026-05-08
tags: [security, mcp, permissions, least-privilege]
related: [model-context-protocol, mcp-attack-surface, mcp-security-best-practices, ai-agent-governance]
sources: ["research-security-implications-of-mcp-exposure-2026-05-08.md"]
---
# Overscoping (MCP)

Overscoping in the context of [[model-context-protocol]] (MCP) refers to granting MCP agents more permissions than necessary to perform their intended functions. It is identified as the most pervasive default risk across published MCP servers.

## Risks
- **OS Command Injection**: Excessive permissions enable agents to execute arbitrary shell commands.
- **Path Traversal**: Over-privileged agents can access files and directories outside their intended scope.
- **Cascading Privileges**: MCP servers can chain tool calls. An over-privileged agent can use a simple tool to cascade into network access, shell commands, or mass data exfiltration.
- **Persistence**: Privileges granted to agents often persist across workspaces and tools, meaning a breach in one context affects many others.

## Mitigation
- Implement least privilege for all MCP agents
- Use tool-level access control within MCP servers
- Avoid persistent privileges across workspaces
- Regularly audit and review agent permissions

## Related Pages
- [[mcp-attack-surface]] — The threat landscape
- [[mcp-security-best-practices]] — Hardening strategies
- [[ai-agent-governance]] — Governance framework for agent permissions