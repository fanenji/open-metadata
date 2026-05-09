---
type: concept
title: Unified Knowledge Graph (OpenMetadata)
created: 2026-04-29
updated: 2026-05-07
tags: [openmetadata, knowledge-graph, metadata, lineage, governance, ai]
related: [openmetadata, openmetadata-mcp-server, data-observability-three-pillars, data-catalog-tool-comparison, model-context-protocol]
sources: ["Embedding an MCP Server into OpenMetadata - Summary.md", "Embedding an MCP Server into OpenMetadata.md"]
---
# Unified Knowledge Graph (OpenMetadata)

The Unified Knowledge Graph is the core data structure and data model of [[openmetadata|OpenMetadata]]. It is a living, breathing graph that encodes not just the structure of data assets but also the relationships, quality, governance policies, and user context around them, combining multiple layers of metadata into a single, interconnected representation. It is the foundation that the [[openmetadata-mcp-server|MCP server]] exposes to AI agents.

## Layers and Components

The knowledge graph consists of multiple layers that capture different aspects of the data landscape:

| Layer | Examples |
|---|---|
| **Physical metadata** | Tables, columns, schemas, data types, partitions, pipelines, dashboards |
| **Lineage** | Pipeline → table → dashboard (column-level) |
| **Semantic** | PII classifications, data ownership, glossary terms, descriptions, account ID meaning |
| **Quality** | Profiling results, unique constraints, completeness checks, test results |
| **Usage** | Queries run against a table, join patterns, access frequency |
| **Governance** | Owners, teams, policies, tags |
| **User Interactions** | Documentation updates, questions, permissions requests, and other user-generated context |

## Why It Matters for AI

Traditional API wrappers expose only physical metadata (table names, column types). The Unified Knowledge Graph enables AI agents to make quality-aware decisions — for example, recommending `dim_customers` over `raw_customers` because it has a higher data quality tier and more passing test results.

When an LLM connects to OpenMetadata via the [[openmetadata-mcp-server|MCP server]], it gains access to this rich context, allowing it to:

- Find the most relevant tables for a given question, preferring those with high data quality scores.
- Understand the meaning and relationships of data assets.
- Take actions on behalf of users (e.g., assigning ownership, updating descriptions) with full awareness of governance policies.

## Significance

The Unified Knowledge Graph distinguishes OpenMetadata from simple data catalogs by providing not just a list of assets, but a contextualized, quality-aware, and governance-enforced view of the entire data landscape. This context is what makes the MCP integration powerful: LLMs are not just querying an API; they are querying a semantically rich graph.

## Relationship to Other Concepts

- The knowledge graph is the **what** — the structured representation of all metadata
- The [[model-context-protocol|MCP protocol]] is the **how** — the standard for exposing it to AI
- The [[openmetadata-mcp-server|MCP server]] is the **where** — the implementation that bridges the two