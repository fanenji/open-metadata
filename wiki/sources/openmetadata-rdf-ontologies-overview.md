---
type: source
title: "RDF & Ontologies Overview"
created: 2026-05-07
updated: 2026-05-07
tags: [openmetadata, rdf, ontology, semantic-web, provenance, shacl, json-ld]
related: [openmetadata, openmetadata-ontology, openmetadata-provenance-ontology, openmetadata-shacl-validation, openmetadata-jsonld-contexts, semantic-web-for-data-platforms, data-observability-three-pillars, openmetadata-data-quality, data-catalog-tool-comparison]
sources: ["openmetadata-rdf-ontologies-overview.md"]
---
# RDF & Ontologies Overview

This source document describes OpenMetadata's complete semantic web stack built on W3C standards, enabling knowledge graph integration, semantic reasoning, and linked data capabilities. It covers the core OpenMetadata Ontology (Turtle RDF, ~48KB), the Provenance Ontology extending W3C PROV-O, SHACL validation shapes (~9KB), and nine JSON-LD contexts for interoperability.

## Key Components

- **OpenMetadata Ontology**: Formal semantic definitions of all entity types (Table, Dashboard, Pipeline, etc.), properties, hierarchies, constraints, and annotations in Turtle RDF format.
- **Provenance Ontology**: W3C PROV-O extension for data lineage, activity tracking, attribution, and derivation.
- **SHACL Shapes**: Validation rules ensuring metadata quality and consistency.
- **JSON-LD Contexts**: Nine contexts enabling semantic JSON with URI mapping and type coercion (base, dataAsset, entityRelationship, governance, operations, quality, service, team, thread).

## Architecture

The stack is organized in four layers: Ontology Layer → JSON-LD Mapping Layer → SHACL Validation Layer → SPARQL Query Layer, supporting applications like knowledge graphs, semantic search, and reasoning.

## Use Cases

Knowledge graph construction, semantic search with ontology-driven query expansion, data lineage and provenance tracking, metadata validation, interoperability with DCAT/Schema.org/Dublin Core, and semantic reasoning.

## Significance

This source reveals that OpenMetadata is not merely a metadata catalog but a full semantic web platform — a unique differentiator among open-source data catalogs. The RDF/SPARQL capabilities enable advanced use cases not available in [[datahub]] or [[amundsen]].