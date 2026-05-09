---
type: concept
title: Knowledge Graph for AI Memory
created: 2026-04-02
updated: 2026-04-02
tags: [knowledge-graph, ai-memory, graph-rag, enterprise-ai]
related: [property-graph-vs-rdf-owl, application-layer-schema-enforcement, hybrid-retrieval-vector-graph, falkordb, graphblas]
sources: ["Property Graphs vs. Rigid Ontologies Choosing the Right Foundation for Enterprise AI Memory.md"]
---
# Knowledge Graph for AI Memory

An architectural pattern for using knowledge graphs in enterprise AI systems to store and retrieve structured relationships between entities. Addresses limitations of pure vector search in RAG systems, which cannot answer relationship-based questions (e.g., "which projects does Sarah manage that depend on the delayed infrastructure migration?").

## Key Characteristics

- **Relationship-aware retrieval**: Captures connections between entities, not just semantic similarity.
- **Evolving extraction**: AI extraction models improve over time; the knowledge graph must accommodate richer extraction without schema renegotiation.
- **Hybrid retrieval**: Combines vector search (for seed nodes) with graph traversal (for expansion).

## Recommended Architecture

Based on [[Alexander Shereshevsky]]'s analysis, the recommended stack for enterprise AI memory is:

1. **Property graph database** (e.g., [[FalkorDB]]) for flexible, evolving data models.
2. **Application-layer schema enforcement** for validation without database rigidity.
3. **Native vector indexing** for hybrid retrieval (vector search + graph traversal).
4. **Migration path** from permissive ingestion to hardened core as patterns emerge.

## Hybrid Retrieval Pattern

Two-stage retrieval:
1. **Stage 1**: Vector search for seed nodes using entity embeddings.
2. **Stage 2**: Graph traversal from seed nodes to collect connected subgraph.
3. **Stage 3**: Format results as natural language context for LLM consumption.

## Related Concepts

- [[property-graph-vs-rdf-owl]] — The core trade-off decision for knowledge graph foundation.
- [[application-layer-schema-enforcement]] — Schema validation in code rather than database.
- [[hybrid-retrieval-vector-graph]] — The two-stage retrieval pattern.
- [[data-contract-platform]] — Complementary pattern for data governance.