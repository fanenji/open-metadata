---
type: concept
title: MCP Attack Surface
created: 2026-05-08
updated: 2026-05-08
tags: [security, mcp, attack-surface, ai-governance]
related: [model-context-protocol, mcp-security-best-practices, dremio-mcp-server, context-propagation, ai-agent-governance]
sources: ["research-security-implications-of-mcp-exposure-2026-05-08.md"]
---
# MCP Attack Surface

The MCP Attack Surface is the aggregate of vulnerabilities introduced by exposing [[model-context-protocol]] (MCP) servers to networks. It defines the threat landscape for AI agent infrastructure.

## Key Threat Vectors

### Network Exposure and Lack of Authentication
- Knostic found 100% of ~2,000 verified MCP servers lacked authentication.
- Trend Micro confirmed 492 instances running without client authentication or traffic encryption.
- Many servers bind to `0.0.0.0`, making them discoverable to anyone on the network.

### Overscoping
- Granting MCP agents more permissions than necessary is the most pervasive default risk.
- Enables OS command injection and path traversal attacks.
- Privileges often persist across workspaces and tools, compounding the risk.

### Prompt Injection and Context Poisoning
- Attackers poison data sources that MCP tools retrieve, coercing the LLM into unintended actions.
- The [[context-propagation]] mechanism can be exploited to inject instructions that influence model reasoning.

### Server Impersonation and Supply Chain Risks
- An attacker can replace a legitimate MCP server in a registry to gain access.
- Flawed token scope enforcement enables "confused deputy" attacks.
- Weak certificate checks increase man-in-the-middle risk.

### Shadow Access
- Undocumented access paths emerge as teams connect MCP servers to more sources.
- Challenges data discovery and governance.

## Implications

The MCP attack surface is novel because it bridges LLM-specific threats (prompt injection) with traditional infrastructure vulnerabilities (network exposure, credential mismanagement). Traditional security frameworks do not yet address this combined threat landscape.

## Related Pages
- [[mcp-security-best-practices]] — Hardening strategies
- [[dremio-mcp-server-security]] — Case study
- [[ai-agent-governance]] — Broader governance context