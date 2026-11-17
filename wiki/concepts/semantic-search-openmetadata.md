---
type: concept
title: "Semantic Search in OpenMetadata"
created: 2026-07-07
updated: 2026-07-07
tags: [openmetadata, search, embeddings, vector, ai]
related: [openmetadata, search-indexes, keyword-search, mcp-server, advanced-search]
sources: ["Announcing OpenMetadata 1.12 1.md"]
---
# Semantic Search in OpenMetadata

**Semantic Search** is a capability introduced in OpenMetadata 1.12 that enables meaning-based search across metadata assets using vector embeddings, going beyond traditional keyword matching.

## How It Works

OpenMetadata creates vector embeddings of your metadata (table descriptions, column names, glossary terms, etc.) and stores them in OpenSearch. When a user searches, the system retrieves results based on semantic similarity — not just exact keyword matches. This is exposed through the [[mcp-server|MCP Server]] as well.

## Embedding Providers

Semantic Search supports three embedding backends:

| Provider | Type | Notes |
|----------|------|-------|
| **AWS Bedrock** | Cloud | Managed service with multiple foundation models |
| **OpenAI** | Cloud | GPT-family embedding models |
| **HuggingFace** | Self-hosted / API | Open-source embedding models |

## Relationship to Other Search Features

- **[[keyword-search]]**: Traditional BM25-based text search — exact match oriented
- **[[advanced-search]]**: Faceted, filtered search with boolean logic
- **Semantic Search**: Meaning-based — finds "revenue" when searching for "income"

These layers are complementary: Semantic Search augments, not replaces, keyword and advanced search.

## MCP Integration

The MCP Server includes tooling for Semantic Search, allowing AI agents to perform meaning-based queries against the metadata graph. This is a key enabler for the [[openmetadata-ai-sdk|AI SDK]].

## See Also

- [[openmetadata]] — Platform overview
- [[search-indexes]] — Search infrastructure (OpenSearch/Elasticsearch)
- [[mcp-server]] — MCP Server tooling