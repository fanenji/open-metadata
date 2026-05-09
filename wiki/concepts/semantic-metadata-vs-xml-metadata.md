---
type: concept
title: Semantic Metadata vs. XML Metadata
created: 2026-04-29
updated: 2026-04-29
tags: [metadata, comparison, rdf, xml, geospatial]
related: [semantic-metadata-overview, dcat-ontology, metadata-fields-definition, geonetwork]
sources: ["FOSS4GE 2024  Towards better data platforms with semantic metadata - Summary.md"]
---
# Semantic Metadata vs. XML Metadata

This page provides a decision framework for when to use semantic metadata (RDF/DCAT) vs. traditional XML-based geospatial metadata (ISO 19139/19115).

## Comparison

| Aspect | XML Metadata (ISO 19139) | Semantic Metadata (RDF/DCAT) |
|---|---|---|
| **Structure** | Hierarchical, schema-driven | Graph of relationships |
| **Schema Evolution** | Breaking changes on migration | Add predicates without breaking |
| **Interoperability** | GIS-only | Web-native (search engines, BI, cloud) |
| **Flexible Targeting** | One schema per document | Multiple ontologies simultaneously |
| **Tooling Maturity** | Mature in GIS ecosystem | Mature in web ecosystem |
| **Learning Curve** | Familiar to GIS professionals | Requires understanding of RDF/graph concepts |

## When to Use Each

### Use XML Metadata (ISO 19139) when:
- You are operating entirely within the GIS/INSPIRE ecosystem
- Your consumers are exclusively geospatial tools (WMS, CSW)
- You have existing infrastructure and workflows built around XML

### Use Semantic Metadata (RDF/DCAT) when:
- You need to bridge geospatial and non-geospatial systems
- You want search engine indexing (Google Dataset Search)
- You need cross-platform interoperability (cloud warehouses, BI tools)
- You want to avoid breaking schema changes over time
- You are building a new metadata system from scratch

## Migration Path

[[geonetwork-ui]] can handle both formats, enabling gradual migration from XML to semantic metadata without breaking existing consumers.