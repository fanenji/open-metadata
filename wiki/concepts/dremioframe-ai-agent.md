---
type: concept
title: DremioFrame AI Agent
created: 2026-04-29
updated: 2026-04-29
tags: [dremio, ai, agent, code-generation, python]
related: [dremioframe, dremio-mcp-server, model-context-protocol]
sources: ["DremioFrame - Dremio Dataframe Library.md"]
---
# DremioFrame AI Agent

The DremioFrame AI Agent (DremioAgent) is an embedded code generation assistant within the [[dremioframe|DremioFrame]] library. It provides AI-powered capabilities for generating SQL queries, Python scripts, and API calls.

## Scope

The DremioAgent is explicitly positioned as a code generation assist tool, not as an alternative to Dremio's integrated agent for deeper administration and natural language analytics. Users should log into their Dremio instance's UI to leverage the integrated agent for administrative tasks.

## Capabilities

- **SQL Generation**: Generate SQL queries from natural language descriptions
- **Script Generation**: Generate Python scripts for data processing
- **API Call Generation**: Generate API call code for Dremio interactions
- **MCP Server**: Includes an MCP server component (see [[dremio-mcp-server]]) for AI agent integration
- **MCP Client Integration**: Can connect to external MCP servers
- **Document Extraction**: Extract and process document content
- **Observability**: Monitor AI agent usage and performance
- **Reflections**: Manage Dremio reflections via AI
- **Governance**: Manage governance policies via AI
- **Data Quality**: Run data quality checks via AI
- **SQL Optimization**: Optimize SQL queries via AI
- **CLI Chat**: Interactive chat interface via CLI

## Related

- [[dremioframe]] — The parent library
- [[dremio-mcp-server]] — MCP server component
- [[model-context-protocol]] — The protocol underlying MCP integration