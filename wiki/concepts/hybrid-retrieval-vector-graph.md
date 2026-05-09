---
type: concept
title: Hybrid Retrieval (Vector + Graph)
created: 2026-04-02
updated: 2026-04-02
tags: [retrieval, rag, knowledge-graph, vector-search]
related: [knowledge-graph-for-ai-memory, falkordb, property-graph-vs-rdf-owl]
sources: ["Property Graphs vs. Rigid Ontologies Choosing the Right Foundation for Enterprise AI Memory.md"]
---
# Hybrid Retrieval (Vector + Graph)

A two-stage retrieval pattern for knowledge-graph-enhanced RAG systems. Combines vector search for initial seed node discovery with graph traversal for contextual expansion.

## Stages

1. **Vector search**: Find seed nodes by cosine similarity on entity embeddings.
2. **Graph traversal**: From seed nodes, traverse relationships (1 to N hops) to collect connected subgraph.
3. **Deduplication and structuring**: Merge results, remove duplicates, format for LLM consumption.

## Implementation

[[FalkorDB]] supports this pattern natively with its vector index and Cypher query language. The hybrid retrieval runs entirely within FalkorDB, eliminating the need for a separate vector database.

## Benefits

- Answers relationship-based questions that pure vector search cannot.
- Provides structured context (entities + relationships) for LLM consumption.
- Efficient: vector search narrows the search space, graph traversal expands context.