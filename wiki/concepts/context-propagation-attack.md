---
type: concept
title: Context Propagation Attack
created: 2026-05-08
updated: 2026-05-08
tags: [security, mcp, prompt-injection, context-poisoning]
related: [context-propagation, mcp-attack-surface, model-context-protocol]
sources: ["research-security-implications-of-mcp-exposure-2026-05-08.md"]
---
# Context Propagation Attack

A Context Propagation Attack is a security exploit that injects instructions into data that influence model reasoning via the [[context-propagation]] mechanism. It exploits the pipeline mechanism without modifying the model itself.

## Mechanism
1. An attacker poisons data sources (documents, tickets, database entries) that [[model-context-protocol]] (MCP) tools retrieve.
2. When this manipulated data is passed into the model context, it coerces the LLM into generating unintended tool calls or leaking data.
3. The attack exploits the context propagation pipeline, not the model weights.

## Relationship to Prompt Injection
Context propagation attacks are a variant of prompt injection that specifically targets the data pipeline rather than direct user input. They are unique to MCP as a bridge between LLMs and external data sources.

## Mitigation
- Harden all MCP tool inputs against injection attacks
- Sanitize parameters interpreted by downstream systems (Shell, SQL, etc.)
- Implement input validation on all data retrieved by MCP tools
- Monitor for anomalous tool usage patterns

## Related Pages
- [[context-propagation]] — The mechanism exploited by this attack
- [[mcp-attack-surface]] — The threat landscape
- [[mcp-security-best-practices]] — Hardening strategies