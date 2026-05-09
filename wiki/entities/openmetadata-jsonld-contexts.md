---
type: entity
title: OpenMetadata JSON-LD Contexts
created: 2026-05-07
updated: 2026-05-07
tags: [openmetadata, json-ld, rdf, semantic-web, interoperability]
related: [openmetadata, openmetadata-ontology, semantic-web-for-data-platforms, custom-connector-openmetadata]
sources: ["openmetadata-rdf-ontologies-overview.md"]
---
# OpenMetadata JSON-LD Contexts

OpenMetadata provides nine JSON-LD contexts that enable semantic JSON with URI resolution and type coercion, bridging JSON metadata to RDF without requiring full RDF expertise.

## Available Contexts

1. **base** — Core context for fundamental entity types
2. **dataAsset** — Context for data asset definitions (tables, dashboards, etc.)
3. **entityRelationship** — Context for entity relationship mappings
4. **governance** — Context for governance-related metadata
5. **operations** — Context for operational metadata
6. **quality** — Context for data quality metadata
7. **service** — Context for service definitions
8. **team** — Context for team and user metadata
9. **thread** — Context for collaboration and discussion metadata

## Purpose

JSON-LD contexts serve as a mapping layer that:

- Maps JSON property names to RDF URIs
- Enables type coercion (e.g., strings to dates, integers)
- Provides interoperability with external systems using DCAT, Schema.org, Dublin Core
- Allows JSON-based tools to participate in the semantic web without native RDF support

## Role in Architecture

The JSON-LD mapping layer sits between the ontology and SHACL validation in OpenMetadata's semantic stack, translating JSON metadata into RDF for validation and querying.

## Significance

These contexts make OpenMetadata's semantic capabilities accessible to developers and tools that work with JSON rather than RDF directly. This lowers the barrier to adoption while maintaining semantic rigor.

## Open Questions

- Are these contexts versioned and documented individually?
- Can users define custom contexts for their own entity types?
- How do contexts interact with the [[custom-connector-openmetadata]] pattern?