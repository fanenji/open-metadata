---
type: concept
title: dbt MCP Server Deployment Modes
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, mcp, architecture, deployment]
related: [dbt-mcp-server, model-context-protocol, dbt-cloud, dbt-core, dbt-mcp-server-setup-guide]
sources: ["the-dbt-mcp-server-how-ai-finally-gets-to-talk-to-your-data-the-right-way.md"]
---
# dbt MCP Server Deployment Modes

The [[dbt-mcp-server]] supports two distinct deployment modes optimized for different user personas and use cases.

## Local MCP Server

Runs on the developer's machine. Designed for analytics engineers and data engineers actively building dbt projects.

**Capabilities:**
- Full dbt CLI access (`run`, `test`, `build`, `compile`, `docs`, `show`, `list`, `parse`)
- Code generation (model YAML, source YAML, staging model SQL)
- Column-level lineage via the [[dbt-fusion]] engine
- Works with or without a [[dbt-cloud]] account
- Works with [[dbt-core]], dbt CLI, and dbt Fusion
- Access to dbt platform APIs when account is connected

**Best for:** Day-to-day development, model authoring, debugging, AI-assisted refactoring

## Remote MCP Server

Hosted by dbt, requires zero local installation. Connects to the dbt platform via HTTP in pure consumption mode.

**Capabilities:**
- Semantic Layer queries (governed metrics, live)
- SQL execution against the warehouse
- Metadata discovery (models, sources, lineage, health)
- Administrative API access

**Best for:** Business analysts, stakeholders, non-engineers who want conversational access to data without touching a CLI

## Key Differences

| Aspect | Local | Remote |
|--------|-------|--------|
| Installation | Required (uv + dbt-mcp) | None |
| CLI Access | Full | None |
| Semantic Layer | Via platform connection | Native |
| Code Generation | Yes | No |
| Target User | Developer | Consumer |
| Credit Consumption | text_to_sql only | text_to_sql only |
| Risk Profile | Higher (warehouse modification) | Lower (read-only by default) |