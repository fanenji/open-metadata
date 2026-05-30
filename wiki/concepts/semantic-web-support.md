---
type: concept
title: Semantic Web Support
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, semantic-web, rdf, owl, shacl, json-ld, prov-o, knowledge-graph, linked-data]
related: [metadata-standard, jsonschemas, unified-metadata-graph, schema-first-approach]
sources: ["metadata-standard-openmetadata-core-schema-guide---20260514.md"]
---

# Semantic Web Support

OpenMetadata provides **semantic web readiness** through its [[metadata-standard]], which includes support for RDF/OWL ontologies, SHACL shapes, JSON-LD serialization, and PROV-O provenance. These standards enable knowledge graph and linked data use cases beyond the core platform's JSON Schema-based metadata model.

## Supported Standards

### RDF/OWL (Resource Description Framework / Web Ontology Language)
RDF/OWL ontologies provide a formal, machine-readable way to define the concepts and relationships in the OpenMetadata domain model. They enable:
- **Knowledge graph construction** — Entities and their relationships can be represented as a graph of RDF triples.
- **Reasoning and inference** — OWL-based reasoning can derive implicit relationships from explicit metadata.
- **Interoperability** — RDF/OWL data can be consumed by any semantic web tool or triple store.

### SHACL (Shapes Constraint Language)
SHACL shapes define validation constraints for RDF graphs. They allow:
- **Graph validation** — Ensuring that RDF data conforms to expected shapes and patterns.
- **Data quality enforcement** — Applying constraints to metadata in the knowledge graph.

### JSON-LD (JSON for Linked Data)
JSON-LD provides a way to serialize linked data using JSON syntax. It enables:
- **Linked data interoperability** — OpenMetadata metadata can be consumed by external systems that understand JSON-LD.
- **Context-based mapping** — JSON-LD `@context` maps JSON property names to RDF/OWL terms.

### PROV-O (Provenance Ontology)
PROV-O is a W3C standard for representing provenance information. It supports:
- **Data lineage** — Tracking the origins, transformations, and dependencies of data assets.
- **Provenance tracking** — Recording who performed what action on which resource and when.

## Relationship to the Unified Metadata Graph

The [[unified-metadata-graph]] is the central architectural concept of OpenMetadata — a single graph database organizing all ingested metadata. The semantic web standards (RDF/OWL, PROV-O) provide the formal foundation for representing this graph in a standards-compliant way, enabling interoperability with external knowledge graphs and semantic web tools.

## Current Status

The semantic web support is documented as part of the [[metadata-standard]] but its active usage within the current OpenMetadata platform (v1.12.x) is not fully detailed. It represents a capability for knowledge graph and linked data use cases that may be leveraged in future integrations or by advanced users.

## Related Wiki Pages

- [[metadata-standard]] — The overarching standards project that includes semantic web support.
- [[jsonschemas]] — The primary schema format used for code generation.
- [[unified-metadata-graph]] — The central metadata graph concept.
- [[schema-first-approach]] — The architectural principle for schema-driven development.