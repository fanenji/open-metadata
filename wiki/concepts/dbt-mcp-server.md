type: concept
title: dbt MCP Server
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, mcp, ai, integration]
related: [model-context-protocol, dbt-cloud, dbt-catalog, dbt-fusion, dbt-lsp, dbt-mcp-server]
sources: ["dbt-labsdbt-mcp A MCP (Model Context Protocol) server for interacting with dbt..md"]
---
# dbt MCP Server

The **dbt MCP Server** is a concrete implementation of the [[model-context-protocol]] for the dbt ecosystem. It provides a standardized interface for AI agents to interact with dbt projects, enabling capabilities such as SQL execution, semantic layer queries, project discovery, job management, code generation, and documentation search.

## Key Characteristics

- **Official**: Developed and maintained by [[dbt-labs]].
- **Comprehensive**: 40+ tools across 9 categories covering the full dbt lifecycle.
- **Multi-platform**: Supports dbt Core, dbt Fusion, and dbt Platform.
- **Extensible**: Exposes both read-only (Discovery, Semantic Layer) and write-capable (CLI, Admin API) tools.
- **Portable**: Experimental MCP Bundle format for easy client import.

## Use Cases

- AI-assisted dbt project development and debugging.
- Natural language querying of dbt project metadata and lineage.
- Automated job management and monitoring.
- Semantic layer exploration and metric querying.
- Documentation search and retrieval.

## Security Model

The server distinguishes between safe (read-only) and potentially destructive (write) tools. The dbt CLI tools carry an explicit security warning, as they can modify warehouse objects. Production deployments should carefully consider client trust and access controls.

## Relationship to Existing Wiki Concepts

- Strengthens [[model-context-protocol]] with a concrete, production-grade implementation.
- Extends [[dbt-cloud]] by providing an AI-native interface to its APIs.
- Complements [[dbt-catalog]] with programmatic discovery and lineage tools.
- Connects to [[dbt-observability-implementation]] via model health and performance tools.
- Connects to [[dbt-data-contract-implementation]] via discovery tools that can surface contract metadata.