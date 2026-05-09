---
type: entity
title: Upwind
created: 2026-05-08
updated: 2026-05-08
tags: [security, mcp, context-poisoning]
related: [model-context-protocol, context-propagation, mcp-attack-surface]
sources: ["research-security-implications-of-mcp-exposure-2026-05-08.md"]
---
# Upwind

Upwind is a security research organization that analyzed context poisoning risks in [[model-context-protocol]] (MCP) servers. Their research documented how attackers can poison data sources that MCP tools retrieve, coercing LLMs into unintended actions.

## Key Findings
- Documented context poisoning attack vectors in MCP
- Published "Unpacking the Security Risks of Model Context Protocol (MCP) Servers"
- Their findings connect to the [[context-propagation]] concept

## Related Pages
- [[mcp-attack-surface]] — The threat landscape
- [[context-propagation]] — The mechanism exploited by context poisoning
- [[model-context-protocol]] — The protocol under analysis