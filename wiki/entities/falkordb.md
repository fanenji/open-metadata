---
type: entity
title: FalkorDB
created: 2026-04-02
updated: 2026-04-02
tags: [graph-database, property-graph, ai-memory, tool]
related: [property-graph-vs-rdf-owl, knowledge-graph-for-ai-memory, application-layer-schema-enforcement, neo4j, kuzu, graphblas]
sources: ["Property Graphs vs. Rigid Ontologies Choosing the Right Foundation for Enterprise AI Memory.md"]
---
# FalkorDB

A property graph database recommended by [[Alexander Shereshevsky]] for enterprise AI memory systems. Uses GraphBLAS (sparse matrix algebra) for sub-10ms query latency. Runs on the Redis protocol, making deployment familiar for teams with existing Redis infrastructure. Supports native vector indexing, enabling hybrid retrieval (vector search + graph traversal) without a separate vector database.

## Key Features

- **GraphBLAS engine**: Sparse matrix algebra for fast graph traversals.
- **Redis protocol**: Familiar deployment and operations for Redis users.
- **Native vector indexing**: Supports cosine similarity search on entity embeddings.
- **Cypher query language**: Compatible with property graph query patterns.

## Comparison

- [[Neo4j]] and [[Kuzu]] are alternative property graph databases.
- FalkorDB's GraphBLAS approach differentiates it for latency-sensitive AI memory workloads.