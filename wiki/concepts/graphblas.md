---
type: concept
title: GraphBLAS
created: 2026-04-02
updated: 2026-04-02
tags: [graph-database, linear-algebra, performance]
related: [falkordb, property-graph-vs-rdf-owl]
sources: ["Property Graphs vs. Rigid Ontologies Choosing the Right Foundation for Enterprise AI Memory.md"]
---
# GraphBLAS

A sparse matrix algebra approach to graph processing. Used by [[FalkorDB]] under the hood to achieve sub-10ms query latency even for complex traversals. Represents graph operations as linear algebra operations on sparse matrices, enabling highly optimized computation.