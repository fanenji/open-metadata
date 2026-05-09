---
type: concept
title: Semantic Metadata
created: 2026-04-29
updated: 2026-04-29
tags: [metadata, semantic-web, rdf, knowledge-graph, ontology]
related: [rdf-data-model, dcat-standard, geodcat-ap, knowledge-graph, ontology, data-catalog-critique, context-store, embedded-metadata]
sources: ["FOSS4GE 2024  Towards better data platforms with semantic metadata.md"]
---
# Semantic Metadata

Semantic metadata describes the meaning of data and its relationships to other data using standardized terms (ontologies) rather than rigid structural schemas. It is built on the [[rdf-data-model]] of Subject-Predicate-Object triples, which form a [[knowledge-graph]] when connected.

## Key Characteristics

- **Meaning over Structure**: Focuses on what data *is* and how it *relates* to other things, rather than where elements appear in a hierarchy.
- **Graph-Based**: Metadata forms a graph of interconnected entities, not a tree or document.
- **Ontology-Driven**: Uses standardized vocabularies (e.g., [[dcat-standard]], Dublin Core) to define terms and relationships.
- **Encoding-Agnostic**: The same semantic content can be serialized in XML, Turtle, JSON-LD, or other formats without changing meaning.
- **Backward Compatible**: New relationships can be added without breaking existing consumers, unlike rigid XML schemas.

## Advantages Over XML Standards

| Aspect | ISO 19139 (XML) | Semantic Metadata (RDF/DCAT) |
|--------|-----------------|------------------------------|
| Schema evolution | Breaking changes between versions | Backward-compatible extension |
| Interoperability | Geospatial ecosystem only | Whole web (schema.org, Wikidata) |
| Flexibility | Rigid hierarchy | Free-form graph |
| Machine readability | Requires XML parsers | Native to web architecture |

## Relevance to Data Platform

Semantic metadata offers a path to evolve beyond traditional [[data-catalog-critique]] by embedding meaning directly into the data representation. It aligns with the [[ECL-framework]]'s "Link" phase and could serve as the foundation for a [[context-store]] implementation.
