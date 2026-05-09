---
type: concept
title: Natural Language Data Discovery
created: 2026-04-08
updated: 2026-04-08
tags: [data-discovery, llm, natural-language, openmetadata]
related: [local-llm-openmetadata-extension, openmetadata, data-discovery-tools, text2sql-patterns]
sources: ["Local LLM for OpenMetadata - Visual Studio Marketplace.md"]
---
# Natural Language Data Discovery

The practice of querying data catalogs and metadata repositories using conversational language instead of SQL or formal query syntax. Enabled by LLMs, this approach lowers the barrier for non-technical users to explore and understand available data assets.

## Implementation

The [[local-llm-openmetadata-extension]] implements natural language data discovery by:
- Accepting queries like "show me customer tables" or "find sales data"
- Translating natural language to OpenMetadata API queries
- Returning results with AI-powered insights and lineage visualization

## Relevance to Wiki

This concept extends [[data-discovery-tools]] by adding an IDE-integrated, conversational interface as an alternative to traditional web-based catalog browsing. It connects to [[text2sql-patterns]] as a related approach for querying data rather than metadata.