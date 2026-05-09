---
type: concept
title: Knowledge Graph
created: 2026-05-05
updated: 2026-05-07
tags: ["metadata", "semantic-layer", "graph-database", "knowledge-graph", "semantic-web", "rdf"]
related: ["openmetadata-1.13-features", "model-context-protocol-mcp", "data-lineage", "semantic-metadata", "rdf-data-model", "context-store", "data-catalog-critique"]
sources: ["announcing-openmetadata-1-13.md", "FOSS4GE 2024  Towards better data platforms with semantic metadata.md"]
---

# Knowledge Graph

A knowledge graph is a network of connected entities and their relationships, typically represented using the [[rdf-data-model]]. In the context of modern data governance, it serves as a unified structure that merges technical metadata (the "what" and "where") with semantic metadata (the "meaning"). Unlike hierarchical structures (XML trees) or relational tables, a knowledge graph allows metadata to be represented as an interconnected web of meaning.

## Key Properties

- **Graph Structure**: Nodes represent entities (datasets, people, organizations), edges represent relationships.
- **Global Connectivity**: Through URIs, a knowledge graph can connect to external graphs (e.g., Wikidata, schema.org).
- **Open World**: New entities and relationships can always be added without breaking existing structure.
- **Machine-Readable**: Both humans and machines can traverse the graph to discover related information.

## Functionality

In OpenMetadata 1.13, the Knowledge Graph allows for:
- **Semantic Context**: Providing LLMs and AI agents with a deep understanding of how data interconnects.
- **Interoperability**: Using W3C standards (RDF, OWL, PROV-O) to ensure the graph can be consumed by external tools and agents.
- **Automated Discovery**: Deriving ownership chains and pipeline associations through inferred relationships.
- **Bidirectional Navigation**: Allowing users to traverse from a business term to its underlying physical assets or from a data asset to its governing business glossary.

## Example

A dataset node might connect to:
- A publisher (organization node)
- A spatial coverage (place node)
- A temporal coverage (time node)
- Related datasets (other dataset nodes)
- External references (Wikidata entries)

## Relevance to Data Platform

A knowledge graph could serve as the implementation pattern for a [[context-store]], providing a queryable, versioned store of semantic definitions, entity classifications, and relationship maps. It aligns with the [[ECL-framework]]'s "Link" phase and addresses the [[data-catalog-critique]] by embedding meaning directly into the data representation.