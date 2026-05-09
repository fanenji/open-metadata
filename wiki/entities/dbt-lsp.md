type: entity
title: dbt LSP
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, tool, language-server]
related: [dbt-mcp-server, dbt-fusion, dbt-cloud]
sources: ["dbt-labsdbt-mcp A MCP (Model Context Protocol) server for interacting with dbt..md"]
---
# dbt LSP

The **dbt LSP** (Language Server Protocol) is a set of tools that leverage the [[dbt Fusion]] engine for advanced SQL compilation and column-level lineage analysis. It is exposed as a tool category in the [[dbt-mcp-server]].

## Tools

- `fusion.compile_sql`: Compiles SQL in project context via dbt Platform.
- `fusion.get_column_lineage`: Traces column-level lineage via dbt Platform.
- `get_column_lineage`: Traces column-level lineage locally (requires dbt-lsp via dbt Labs VSCE).

## Usage

These tools are accessed through the dbt MCP server, enabling AI agents to perform advanced code analysis and lineage tracing. The local `get_column_lineage` tool requires the dbt Labs Visual Studio Code Extension.