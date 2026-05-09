type: concept
title: MCP Elicitation Protocol
created: 2026-04-29
updated: 2026-04-29
tags: [mcp, security, user-approval, safety]
related: [model-context-protocol, power-bi-modeling-mcp-server, opencode]
sources: ["fully-local-power-bi-development-opencode-qwen-power-bi-mcp.md"]
---
# MCP Elicitation Protocol

An approval mechanism within the Model Context Protocol (MCP) where the MCP server prompts the user before executing operations. This provides a safety layer between the AI agent's requests and actual modifications to the connected system.

## How It Works

1. The AI agent requests an operation (e.g., modifying a Power BI measure)
2. The MCP server intercepts the request and prompts the user for approval
3. The user reviews the proposed change and confirms or denies
4. Only after confirmation does the server execute the operation

## Configuration Modes

- **Read-only** (`--readonly`): No modifications allowed; elicitation not needed
- **Read-write with elicitation** (`--readwrite`): Modifications allowed but require user confirmation
- **Read-write without elicitation** (`--readwrite --skipconfirmation`): Modifications allowed without prompts (for experienced users)

## Security Implications

The elicitation protocol is a defense-in-depth measure. Even with read-write access, the user has a chance to review each change. However, `--skipconfirmation` bypasses this protection and should only be used with trusted configurations.

## See Also

- [[model-context-protocol]] — The parent protocol
- [[power-bi-modeling-mcp-server]] — Server implementing this protocol
- [[opencode]] — AI agent that interacts with the protocol