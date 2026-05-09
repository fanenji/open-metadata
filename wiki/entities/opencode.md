type: entity
title: OpenCode
created: 2026-04-29
updated: 2026-04-29
tags: [ai-agent, mcp, open-source, terminal]
related: [model-context-protocol, power-bi-modeling-mcp-server, local-llm-for-bi-development, ollama]
sources: ["fully-local-power-bi-development-opencode-qwen-power-bi-mcp.md"]
---
# OpenCode

An open-source, terminal-based AI coding agent that orchestrates large language models (LLMs) and MCP (Model Context Protocol) servers. It provides a text-based user interface (TUI) for interacting with AI models and managing tool integrations.

## Key Features

- **MCP server integration**: Connects to any MCP-compatible server (e.g., Power BI Modeling MCP Server)
- **Multi-provider support**: Works with Ollama, OpenAI-compatible APIs, and other providers
- **Local-first**: Can run entirely on local infrastructure with no cloud dependencies
- **Conversation history**: Stores interactions locally at `~/.local/share/opencode/`

## Configuration

OpenCode uses a JSON configuration file at `~/.config/opencode/opencode.json`. Key configuration sections include:

- **Provider**: LLM backend configuration (e.g., Ollama with Qwen models)
- **MCP**: MCP server definitions with command, arguments, and enabled state
- **Model**: Default model selection

## Security Considerations

- The `mcp.command` array executes arbitrary binaries — only add MCP servers from trusted sources
- Project-level `opencode.json` files in cloned repositories can execute code
- Conversation history is stored locally and may contain sensitive data

## Installation

```bash
npm install -g opencode-ai
```

## Usage

```bash
opencode
```

Commands within the TUI include `/models` (list available models), `/mcp` (list connected MCP servers), and `/exit`.

## See Also

- [[model-context-protocol]] — The protocol OpenCode uses for tool integration
- [[power-bi-modeling-mcp-server]] — An MCP server commonly used with OpenCode
- [[local-llm-for-bi-development]] — The architecture pattern this enables
- [[ollama]] — The local LLM serving platform