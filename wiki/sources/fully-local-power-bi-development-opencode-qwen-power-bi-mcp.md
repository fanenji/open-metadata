type: source
title: "Fully Local Power BI Development: OpenCode + Qwen 3.5 + Microsoft's Power BI MCP Server"
created: 2026-04-29
updated: 2026-04-29
tags: [power-bi, mcp, local-llm, ai-assisted-development, data-locality]
related: [power-bi-modeling-mcp-server, opencode, local-llm-for-bi-development, qwen-models, model-context-protocol, ollama]
sources: ["fully-local-power-bi-development-opencode-qwen-power-bi-mcp.md"]
authors: ["Michael Hannecke"]
year: 2026
url: "https://medium.com/microsoft-power-bi/fully-local-power-bi-development-opencode-qwen-3-5-microsofts-power-bi-mcp-server-81a527abe5ab"
venue: "Medium (Microsoft Power BI publication)"
---
# Fully Local Power BI Development: OpenCode + Qwen 3.5 + Microsoft's Power BI MCP Server

**Author:** Michael Hannecke (Sovereign AI Architect at bluetuple.ai)
**Published:** 2026-04-21

## Summary

This article provides a step-by-step guide to setting up a fully local AI-assisted Power BI development environment. The stack combines Ollama (serving Qwen 3.5–35B-A3B locally), OpenCode (an open-source terminal-based AI agent), and Microsoft's Power BI Modeling MCP Server. The key value proposition is complete data locality — no DAX, schema, or query results leave the machine — making it suitable for regulated industries (GDPR, HIPAA, BaFin).

## Key Technical Details

- **Model:** Qwen 3.5–35B-A3B (36B total parameters, 3.3B active via Mixture-of-Experts, 256K native context)
- **Hardware recommendation:** 48GB+ RAM (32GB works but tight), GPU with 24GB+ VRAM optional
- **Critical gotcha:** Ollama defaults to 4K context window, silently breaking tool calling. Must expand to 32K+.
- **Mac VM setup:** Ollama runs natively on macOS; Power BI Desktop, OpenCode, and MCP server run in Windows VM. Networking requires Ollama to listen on `0.0.0.0` and config to point to Mac's gateway IP.
- **Safety pattern:** Start with `--readonly` mode, escalate to `--readwrite` with confirmation, then optionally `--skipconfirmation`.

## Practical Workflows

The article demonstrates several effective prompts: model structure overview, DAX generation, DAX review, documentation generation, naming convention audit, and relationship analysis.

## Security Considerations

- MCP command injection risk: `mcp.command` array executes arbitrary binaries
- Model weight integrity via HTTPS downloads
- Local conversation history in `~/.local/share/opencode/`
- Network isolation recommendations

## Relevance to Wiki

This source provides a concrete implementation of the [[model-context-protocol]] for Power BI, extending the wiki's coverage of MCP beyond the existing [[dbt-mcp-server]] example. It introduces the concept of [[local-llm-for-bi-development]] and documents the [[power-bi-modeling-mcp-server]] and [[opencode]] tools. The data locality argument connects to the wiki's existing themes around regulated data handling and sovereign AI.