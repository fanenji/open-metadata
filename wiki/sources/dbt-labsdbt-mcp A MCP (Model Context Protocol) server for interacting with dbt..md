type: source
title: dbt-labs/dbt-mcp: A MCP server for interacting with dbt
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, mcp, ai, dbt-labs]
related: [dbt-mcp-server, model-context-protocol, dbt-cloud, dbt-catalog, dbt-fusion, dbt-lsp]
sources: ["dbt-labsdbt-mcp A MCP (Model Context Protocol) server for interacting with dbt..md"]
---
# dbt-labs/dbt-mcp: A MCP server for interacting with dbt

**Source:** [GitHub Repository](https://github.com/dbt-labs/dbt-mcp)  
**Author:** dbt Labs  
**Published:** 2026-04-04

## Summary

This is the official dbt MCP (Model Context Protocol) server developed and maintained by dbt Labs. It provides a comprehensive set of tools for AI agents to interact with dbt projects across multiple dimensions: SQL execution, Semantic Layer queries, Discovery API, dbt CLI commands, Administrative API, dbt Codegen, dbt LSP (Fusion engine), and product documentation search. The server enables AI agents to understand project context, execute queries, manage jobs, and explore lineage.

## Key Points

- Official dbt Labs project, production-ready.
- Supports dbt Core, dbt Fusion, and dbt Platform.
- 40+ tools across 9 categories.
- Includes an experimental MCP Bundle (MCPB) for easy client import.
- Security warning: CLI tools can modify warehouse objects.
- Dependencies are pinned; only security updates are automated.

## Connections

- Strengthens [[model-context-protocol]] with a concrete implementation.
- Relies on [[dbt-cloud]] APIs (Discovery, Admin, Semantic Layer).
- Extends [[dbt-catalog]] with programmatic discovery tools.
- Introduces [[dbt-fusion]] and [[dbt-lsp]] as new concepts.
- Complements [[dbt-observability-implementation]] with model health and performance tools.