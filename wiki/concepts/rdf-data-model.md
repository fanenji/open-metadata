---
type: concept
title: RDF Data Model
created: 2026-04-29
updated: 2026-04-29
tags: [rdf, semantic-web, data-model, triple, knowledge-graph]
related: [semantic-metadata, dcat-standard, knowledge-graph, ontology]
sources: ["FOSS4GE 2024  Towards better data platforms with semantic metadata.md"]
---
# RDF Data Model

The Resource Description Framework (RDF) is the foundational data model of the semantic web. It represents information as a collection of **triples** — Subject-Predicate-Object statements — that form a graph when connected.

## Triple Structure

- **Subject**: The entity being described (identified by a URI).
- **Predicate**: The relationship or property (identified by a URI from an ontology).
- **Object**: The value or target entity (either a URI or a literal string/number).

## Example

```
<dataset-123>  <dcat:title>  "Population Data" .
<dataset-123>  <dcat:publisher>  <organization-456> .
<organization-456>  <foaf:phone>  "+1234567890" .
```

This forms a graph where `dataset-123` is connected to `organization-456` via the `publisher` relationship.

## Key Properties

- **URI-Based**: Every entity and relationship is globally identifiable via URIs.
- **Graph Structure**: Triples form a directed, labeled graph.
- **Encoding Independence**: The same graph can be serialized as XML, Turtle, JSON-LD, or N-Triples.
- **Open World Assumption**: Absence of a statement does not imply falsehood; new statements can always be added.

## Relevance

RDF is the foundation of [[semantic-metadata]] and enables the creation of [[knowledge-graphs]] that can connect data across organizational and ecosystem boundaries.
