---
type: source
title: "FOSS4GE 2024: Towards better data platforms with semantic metadata"
created: 2026-04-29
updated: 2026-04-29
tags: [semantic-web, geospatial, metadata, dcat, inspire, geonetwork, rdf]
related: [semantic-metadata, dcat-standard, geonetwork, inspire-directive, geodcat-ap, rdf-data-model, data-catalog-critique, context-store, embedded-metadata]
sources: ["FOSS4GE 2024  Towards better data platforms with semantic metadata.md"]
---
# FOSS4GE 2024: Towards better data platforms with semantic metadata

A talk by Florent Gravin (on behalf of Olivia Guyot) at FOSS4G Europe 2024, arguing that geospatial metadata should move from rigid XML standards (ISO 19139) to semantic metadata (DCAT/RDF) to achieve true interoperability beyond the geospatial ecosystem.

## Key Arguments

- **Core Claim**: Geospatial metadata should adopt semantic web standards (DCAT, RDF) instead of rigid XML schemas (ISO 19139).
- **Backward Compatibility**: Semantic metadata allows adding new relations without breaking existing consumers, unlike ISO version upgrades which require complete rewrites.
- **Cross-Ecosystem Reach**: Semantic metadata can simultaneously target multiple ontologies (DCAT, schema.org) from a single knowledge graph, enabling connection to the broader web.
- **Existing Tooling**: Python, Java, and JavaScript libraries already handle semantic formats; GeoNetwork-UI has a working prototype importing DCAT in Turtle and JSON-LD.

## Key Concepts Introduced

- **RDF Triples**: Subject-Predicate-Object statements forming the atomic unit of semantic data.
- **Knowledge Graphs**: Networks of connected RDF triples representing metadata as an interconnected web.
- **Ontologies**: Standardized collections of terms (e.g., DCAT, Dublin Core) enabling cross-platform interoperability.
- **Application Profiles**: Guidelines on how to use an ontology for a specific purpose (e.g., GeoDCAT-AP for geospatial data).
- **Encoding**: Serialization formats (XML, Turtle, JSON-LD) that are independent of semantic content.

## Relevance to Data Platform

This source provides a conceptual foundation for integrating semantic metadata into the data platform. It connects to existing wiki concepts such as [[data-catalog-critique]] (semantic metadata as an evolution path beyond traditional catalogs), [[context-store]] (knowledge graph as an implementation pattern), and [[embedded-metadata]] (semantic approach as a method for machine-readable embedded context).

## Open Questions

- How does semantic metadata compare to OpenMetadata's approach for data platform governance?
- Can DCAT/GeoDCAT-AP be integrated with dbt's data contract YAML format?
- What is the performance cost of graph-based metadata querying vs. structured XML at scale?
- How would semantic metadata interact with the existing Iceberg/GeoParquet/GeoArrow stack?
