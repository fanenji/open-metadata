---
type: concept
title: Shadow Access (MCP)
created: 2026-05-08
updated: 2026-05-08
tags: [security, mcp, governance, access-control]
related: [model-context-protocol, mcp-attack-surface, ai-agent-governance, data-domain-governance]
sources: ["research-security-implications-of-mcp-exposure-2026-05-08.md"]
---
# Shadow Access (MCP)

Shadow Access in the context of [[model-context-protocol]] (MCP) refers to undocumented access paths that emerge as teams connect MCP servers to more data sources. These paths challenge data discovery and governance.

## Risks
- **Undocumented Access**: Teams create MCP connections without formal approval or documentation.
- **Governance Gaps**: Shadow access undermines [[data-domain-governance]] and [[federated-computational-governance]] which assume controlled, governed access.
- **Discovery Challenges**: Security teams cannot audit or monitor access paths they don't know exist.
- **Lateral Movement**: Shadow access paths can be exploited for lateral movement within the infrastructure.

## Mitigation
- Implement a formal approval process for new MCP connections
- Maintain a registry of all MCP servers and their data sources
- Regularly audit MCP connections against the registry
- Integrate MCP server discovery with existing data catalog tools

## Related Pages
- [[mcp-attack-surface]] — The threat landscape
- [[ai-agent-governance]] — Governance framework
- [[data-domain-governance]] — Domain ownership and access control