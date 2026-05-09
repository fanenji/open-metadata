type: concept
title: MCP Command Injection Risk
created: 2026-04-29
updated: 2026-04-29
tags: [mcp, security, injection, configuration]
related: [model-context-protocol, opencode, power-bi-modeling-mcp-server]
sources: ["fully-local-power-bi-development-opencode-qwen-power-bi-mcp.md"]
---
# MCP Command Injection Risk

A security concern in MCP-based AI agent systems where the `mcp.command` array in configuration files executes arbitrary binaries. Since the configuration specifies the exact command and arguments to launch an MCP server, an attacker who controls the configuration can execute arbitrary code on the user's machine.

## Attack Vector

1. A user clones a repository containing a project-level `opencode.json`
2. The configuration specifies a malicious `mcp.command` array
3. When the AI agent starts, it executes the malicious binary

## Mitigations

- Only add MCP servers from trusted sources
- Be cautious with project-level `opencode.json` files in repositories you clone
- Review the `mcp.command` array before running any MCP server
- Consider network isolation for maximum assurance

## Related

This risk was flagged in a January 2026 security writeup. The principle is that "config files can execute code" — similar to risks in other extensible systems (e.g., VS Code tasks, npm scripts).

## See Also

- [[model-context-protocol]] — The protocol this risk applies to
- [[opencode]] — AI agent that processes MCP configurations
- [[data-locality-sovereign-ai]] — Security context for local AI infrastructure