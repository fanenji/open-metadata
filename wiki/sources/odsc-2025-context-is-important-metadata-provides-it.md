---
authors: [Nick Acosta]
year: 2025
source_path: "[[raw/sources/OpenMetadata MCP - Context is Important, Metadata Provides It]]"
venue: "ODSC / Medium"
sources: ["https://open-metadata.org/mcp", "https://odsc.medium.com/context-is-important-metadata-provides-it-6ffdc777037e"]
tags: [mcp, openmetadata, agentic-ai, odsc, knowledge-graph]
related: [mcp-server, agentic-ai, model-context-protocol, unified-metadata-graph, knowledge-graph]
type: source
title: Context is Important, Metadata Provides It — ODSC Article
created: 2026-07-15
updated: 2026-07-07
---
# Context is Important, Metadata Provides It

Article by **Nick Acosta** (Developer Advocate at Collate/OpenMetadata) for ODSC West 2025, arguing that metadata platforms combined with MCP servers provide the missing context that makes AI agents and LLMs useful and safe in enterprise settings.

## Key Arguments

1. **AI without context fails**: LLMs connected directly to raw systems (CRMs, etc.) produce hallucinations, incomplete views, and access-control issues
2. **MCP alone solves connectivity, not context quality**: MCP standardizes tool/AI connections but doesn't address the quality or completeness of what's connected
3. **Metadata platforms aggregate context**: Schemas, datasets, lineage, owners, usage, quality tests, dashboards, ML models — all unified into a [[unified-metadata-graph|single knowledge graph]]
4. **OpenMetadata + MCP = organizationally-aware AI**: By exposing the knowledge graph through MCP, AI agents can read appropriate data and write back changes, continuously improving the graph
5. **Hands-on workshop**: ODSC West 2025 tutorial using OpenMetadata, MCP servers, and Goose open-source AI agent

## Relevance

This source reinforces the [[agentic-ai]] and [[mcp-server]] concepts already in the wiki, emphasizing that MCP is necessary but not sufficient without a comprehensive [[knowledge-graph]].