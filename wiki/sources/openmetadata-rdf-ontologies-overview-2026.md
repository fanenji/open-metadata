---
type: source
title: "RDF & Ontologies Overview"
created: 2026-07-15
updated: 2026-07-15
tags: [rdf, ontology, semantic-web, sparql, prov-o, shacl, json-ld]
related: [rdf-ontology, ontology-explorer, knowledge-graph, unified-metadata-graph]
authors: [OpenMetadata Community]
year: 2026
source_path: "[[raw/sources/openmetadata-rdf-ontologies-overview]]"
sources: ["https://openmetadatastandards.org/rdf/overview/"]
venue: "OpenMetadata Standards"
---
# RDF & Ontologies Overview

Complete semantic web stack documentation for OpenMetadata, built on W3C standards.

## Components

- **Core Ontology** (`openmetadata.ttl`, ~48KB Turtle): Classes (Table, Dashboard, Pipeline...), Properties, Hierarchies, Constraints, Annotations
- **Provenance Ontology**: Extends W3C PROV-O for data lineage, activity tracking, attribution, derivation
- **SHACL Shapes** (~9KB): Validation rules for data quality and consistency
- **JSON-LD Contexts**: Semantic JSON, URI mapping, type coercion — available for: base, dataAsset, entityRelationship, governance, operations, quality, service, team, thread

## Architecture Stack

```
Applications (Knowledge Graphs, Semantic Search, Reasoning)
  → SPARQL Query Layer
  → SHACL Validation Layer
  → JSON-LD Mapping Layer
  → OpenMetadata Ontology Layer
```

## Use Cases

1. Knowledge Graph Construction — JSON metadata → RDF → triple store → SPARQL
2. Semantic Search — Ontology-driven query expansion
3. Data Lineage & Provenance — PROV-O tracking
4. Metadata Validation — SHACL quality rules
5. Interoperability — DCAT, Schema.org, Dublin Core exchange
6. Semantic Reasoning — Infer class hierarchies and property chains

## Relevance

Foundational reference for [[ontology-explorer]], [[knowledge-graph]], and the formal semantic layer underlying OpenMetadata's [[unified-metadata-graph]].