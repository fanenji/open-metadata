---
type: concept
title: Semantic Layer for Text-to-SQL
created: 2026-05-07
updated: 2026-05-07
tags: [semantic-layer, text2sql, metadata, genbi]
related: [genbi-architecture, rag-for-database-schema, golden-queries-few-shot, context-store, data-catalog-tool-comparison]
sources: ["Text-to-SQL is Finally Production-Ready Building a Semantic Layer for GenBI.md"]
---
# Semantic Layer for Text-to-SQL

An "AI-Native Semantic Layer" is a structured repository of metadata designed not just for humans, but for embedding models to understand. It bridges the gap between vague human intent and precise database execution.

## Structure

A raw `CREATE TABLE` statement is insufficient context. The semantic layer requires enriched metadata that describes what tables and columns *actually mean* in plain English. Example structure:

```python
{
    "table_name": "fact_orders",
    "description": "The central fact table containing individual customer order transactions.",
    "columns": [
        {"name": "order_total_usd", "description": "The final, post-tax, post-discount total value of the order in US dollars. Use this for revenue calculations."},
        {"name": "is_active_member", "description": "Boolean flag indicating if the user currently holds an active premium membership subscription."}
    ]
}
```

## Key Design Principles

- **Enriched Descriptions**: Column descriptions must use plain English that maps to business concepts (e.g., "revenue" → `order_total_usd`)
- **Embedding-Optimized**: The text representation must be designed for embedding models to perform semantic matching
- **Retrievable**: Metadata is indexed in a vector database for semantic retrieval
- **Maintainable**: The semantic layer must evolve as schemas change over time

## Relationship to Existing Wiki

This concept is closely related to [[context-store]] — the semantic layer is a specialized context store for database schema. It can be sourced from data catalogs like [[DataHub]] or [[Amundsen]], or from tools like [[dbt-osmosis-llm-module]] that generate enriched metadata.