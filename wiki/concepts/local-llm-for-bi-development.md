type: concept
title: Local LLM for BI Development
created: 2026-04-29
updated: 2026-04-29
tags: [power-bi, local-llm, ai-assisted-development, data-locality, sovereign-ai]
related: [model-context-protocol, power-bi-modeling-mcp-server, opencode, qwen-models, ollama, dbt-osmosis-llm-module]
sources: ["fully-local-power-bi-development-opencode-qwen-power-bi-mcp.md"]
---
# Local LLM for BI Development

An architectural pattern for AI-assisted Business Intelligence (BI) development that runs entirely on local hardware, with no cloud dependencies. The stack combines a local LLM serving platform (e.g., [[ollama]]), an AI agent (e.g., [[opencode]]), and an MCP server (e.g., [[power-bi-modeling-mcp-server]]) to provide AI assistance for BI tools like Power BI Desktop.

## Key Benefits

- **Complete data locality:** No DAX expressions, column names, measure definitions, or query results leave the machine
- **No API costs:** Heavy development sessions don't incur per-token charges
- **Offline capability:** Works on planes, in secure facilities, or during internet outages
- **Auditability:** Every interaction can be traced and logged for compliance
- **Full model control:** Choose which model version runs; no surprise updates or deprecated endpoints

## Architecture Components

1. **BI Desktop** (e.g., Power BI Desktop) — the development environment
2. **MCP Server** (e.g., Power BI Modeling MCP Server) — exposes semantic model operations
3. **AI Agent** (e.g., OpenCode) — orchestrates LLM and MCP tools
4. **Local LLM** (e.g., Qwen 3.5 via Ollama) — provides intelligence

## Critical Configuration

The most common failure point is the LLM's context window. Ollama defaults to 4K tokens, which silently breaks tool calling. The context must be explicitly expanded to at least 32K for MCP-based workflows to function.

## Hardware Requirements

- **Minimum:** 32GB RAM (tight), 30GB free disk space
- **Recommended:** 48GB+ RAM, GPU with 24GB+ VRAM (optional)
- **Apple Silicon:** Unified memory architecture works well with MoE models

## Practical Workflows

- Model structure overview and relationship analysis
- DAX measure generation and review
- Documentation generation
- Naming convention audits
- Performance analysis of existing measures

## Trade-offs

- Local models historically trail frontier cloud models on complex reasoning, though the gap has narrowed dramatically
- Hardware requirements are substantial (48GB+ RAM recommended)
- Mac users need a Windows VM, adding complexity

## See Also

- [[model-context-protocol]] — The protocol enabling this architecture
- [[power-bi-modeling-mcp-server]] — MCP server for Power BI
- [[opencode]] — AI agent for orchestrating the stack
- [[qwen-models]] — Recommended local LLM family
- [[dbt-osmosis-llm-module]] — Related pattern for dbt documentation generation