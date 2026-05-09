---
type: source
title: "Context is Important, Metadata Provides It"
created: 2026-02-17
updated: 2026-02-17
tags: [openmetadata, mcp, ai-agents, metadata, context]
related: [openmetadata, model-context-protocol, openmetadata-mcp-server, ai-agent-metadata-feedback-loop, data-catalog-critique, dbt-mcp-server]
sources: ["OpenMetadata MCP - Context is Important, Metadata Provides It.md"]
authors: [Nick Acosta]
year: 2025
url: "https://odsc.medium.com/context-is-important-metadata-provides-it-6ffdc777037e"
venue: "ODSC Blog"
---
# Context is Important, Metadata Provides It

A blog post by Nick Acosta (Developer Advocate at Collate and OpenMetadata community advocate) promoting a hands-on tutorial at ODSC West 2025. The article argues that AI agents and LLMs fail not due to model weakness but due to lack of organizational context, and that metadata platforms like [[openmetadata]] combined with [[model-context-protocol]] (MCP) servers provide the missing context.

## Key Arguments

- **AI Context Problem**: Data scientists, AI agents, and LLMs often fail because they lack organizational context about customers, systems, and permissions. Simply connecting an LLM directly to a CRM leads to hallucinations, incomplete views, and access-control issues.
- **MCP as Connectivity Layer**: MCP standardizes how AI connects to tools and data sources but does not solve the quality or completeness of context. Connectivity ≠ context.
- **Metadata Platform as Context Provider**: Metadata platforms aggregate schemas, datasets, lineage, owners, usage, quality tests, dashboards, and ML models into a unified knowledge graph, providing the missing context for AI.
- **OpenMetadata + MCP for AI**: By exposing OpenMetadata's knowledge graph through its MCP server, AI agents can become organizationally-aware assistants that both read data for analysis and write back improvements to the knowledge graph.

## Workshop Focus

The article promotes a hands-on ODSC West 2025 tutorial using OpenMetadata, MCP servers, and the Goose open-source AI agent to build extendable, fully open-source AI systems using metadata proactively.

## Connections

- Strengthens [[model-context-protocol]] with a concrete use case (OpenMetadata + MCP for AI context).
- Extends [[openmetadata]] with the MCP integration dimension and AI agent use case.
- Indirectly supports [[data-catalog-critique]] by arguing that catalogs need to be embedded in workflows (here, AI agent workflows).
- Parallels [[dbt-mcp-server]] in the pattern of exposing data platform capabilities via MCP.

## Caveats

The article is promotional (workshop advertisement) with a single illustrative example. No benchmarks, case studies, or quantitative results are provided.