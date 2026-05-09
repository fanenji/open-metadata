---
type: concept
title: Emergent Schema Discovery
created: 2026-04-02
updated: 2026-04-02
tags: [schema, knowledge-graph, pattern]
related: [property-graph-vs-rdf-owl, application-layer-schema-enforcement, knowledge-graph-for-ai-memory]
sources: ["Property Graphs vs. Rigid Ontologies Choosing the Right Foundation for Enterprise AI Memory.md"]
---
# Emergent Schema Discovery

A pattern for identifying natural entity types and relationship patterns from property graph data by analyzing property frequency and co-occurrence. Part of the migration path from permissive ingestion to hardened schema.

## Process

1. Track which properties actually appear in practice across nodes.
2. Analyze property frequency and co-occurrence patterns.
3. Identify natural entity types from clustering of property sets.
4. Document the implicit schema that emerged from actual usage.

## Role in Migration Path

Phase 2 of the recommended migration path (Phase 1: permissive ingestion → Phase 2: emergent schema discovery → Phase 3: soft constraints → Phase 4: hardened core). This phase informs which entity types and properties should receive application-layer validation in Phase 3.