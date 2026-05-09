---
type: entity
title: OpenMetadata Ontology Explorer
created: 2026-05-06
updated: 2026-05-06
tags: [openmetadata, ontology, glossary, semantic-graph]
related: [openmetadata, openmetadata-knowledge-graph, semantic-context-graph, w3c-semantic-standards-for-data-platforms]
sources: ["OpenMetadata - build-ai-you-can-trust-with-knowledge-graph.md"]
---
# OpenMetadata Ontology Explorer

The Ontology Explorer is a feature shipping in OpenMetadata 1.13 that provides a business-glossary-centric view of the semantic context graph. It is the complement of the [[openmetadata-knowledge-graph]].

## Relationship to Knowledge Graph

While the Knowledge Graph is asset-centric (starting from any table, dashboard, or pipeline and showing everything connected to that asset), the Ontology Explorer starts from business concepts and maps how they relate to each other, then downward into the data assets that implement them.

Together, the two tools give teams both directions of the same underlying [[semantic-context-graph]]:
- **Knowledge Graph:** Data assets → upward into business meaning.
- **Ontology Explorer:** Business concepts → downward into the data that implements them.

## Underlying Technology

Both tools are built on the same graph, which is constructed using open W3C standards including RDF, OWL, DCAT, DPROD, SKOS, PROV-O, and Schema.org. See [[w3c-semantic-standards-for-data-platforms]].