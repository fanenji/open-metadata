type: entity
title: dbt Fusion
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, product, engine]
related: [dbt-mcp-server, dbt-lsp, dbt-cloud]
sources: ["dbt-labsdbt-mcp A MCP (Model Context Protocol) server for interacting with dbt..md"]
---
# dbt Fusion

**dbt Fusion** is a dbt product/engine that provides advanced SQL compilation and column-level lineage analysis capabilities. It is referenced in the [[dbt-mcp-server]] as the backend for the dbt LSP tools (`fusion.compile_sql`, `fusion.get_column_lineage`).

## Capabilities

- Advanced SQL compilation within project context.
- Column-level lineage tracing via the dbt Platform.
- Powers the dbt LSP (Language Server Protocol) tools.

## Relationship to Other dbt Products

- **dbt Core**: The open-source transformation tool. dbt Fusion provides enhanced capabilities on top of or alongside Core.
- **dbt Platform (Cloud)**: dbt Fusion capabilities are accessed through the dbt Platform infrastructure.
- **dbt MCP Server**: Exposes Fusion engine tools for AI agents.

## Status

dbt Fusion is referenced as a supported project type in the dbt MCP server documentation. Further details about its standalone capabilities and availability are limited in the current source.