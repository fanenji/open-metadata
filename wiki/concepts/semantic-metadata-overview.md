---
type: concept
title: Semantic Metadata Overview
created: 2026-04-29
updated: 2026-04-29
tags: [semantic-metadata, rdf, knowledge-graph, ontology]
related: [dcat-ontology, rdf-encodings-comparison, semantic-metadata-vs-xml-metadata, geonetwork, metadata-fields-definition]
sources: ["FOSS4GE 2024  Towards better data platforms with semantic metadata - Summary.md"]
---
# Semantic Metadata Overview

Semantic metadata describes **what connections a dataset has to the rest of the world**, using a formalised system of meaning rather than rigid structure. Instead of a hierarchically structured XML document, semantic metadata is expressed as a **graph of relationships**.

## RDF: The Foundation

**RDF (Resource Description Framework)** models all information as **triples**:

```
Subject → Predicate → Object
```

Each triple is called a **statement**. Every subject, predicate, and object is either:
- A **URI** — a globally unique identifier pointing to a standardised concept
- A **literal** — plain text (e.g. a title, a date, a phone number)

## Knowledge Graphs

When many RDF statements are combined, they form a **Knowledge Graph**: a network of nodes (objects) connected by typed edges (predicates). The key property: **the graph is traversable** — from any node, you can follow edges to connected nodes, potentially reaching entirely different domains.

## Ontologies vs. Encodings

A critical distinction:

- **Ontology**: A standardised vocabulary of terms — a collection of defined concepts and relationships (e.g., DCAT, Dublin Core, FOAF, Schema.org)
- **Encoding**: How semantic data is serialised to disk or transmitted over the network (e.g., Turtle, JSON-LD, RDF/XML, N-Triples)

**The graph is the same regardless of encoding.** Encoding is a matter of tooling preference, not semantic meaning.

## Key Advantages

1. **Backward Compatibility**: Add new predicates to existing resources without breaking anything — no breaking schema changes
2. **Flexible Targeting**: A single resource can simultaneously satisfy multiple ontologies (dcat:Dataset, schema:Dataset, geodcat:Dataset)
3. **Cross-Platform Interoperability**: Semantic metadata is the native language of the web — understood by search engines, BI tools, and cloud warehouses