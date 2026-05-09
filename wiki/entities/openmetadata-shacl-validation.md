---
type: entity
title: OpenMetadata SHACL Validation
created: 2026-05-07
updated: 2026-05-07
tags: [openmetadata, shacl, validation, data-quality, rdf, semantic-web]
related: [openmetadata, openmetadata-ontology, openmetadata-data-quality, semantic-web-for-data-platforms]
sources: ["openmetadata-rdf-ontologies-overview.md"]
---
# OpenMetadata SHACL Validation

OpenMetadata provides SHACL (Shapes Constraint Language) validation shapes (~9KB) for enforcing metadata quality and consistency at the semantic level.

## What is SHACL?

SHACL is a W3C standard for validating RDF graphs against a set of conditions (shapes). Shapes define constraints on classes, properties, and values, enabling automated validation of metadata integrity.

## Role in OpenMetadata

SHACL shapes sit between the JSON-LD mapping layer and the SPARQL query layer in OpenMetadata's semantic stack:

```
SPARQL Query Layer
    ↑
SHACL Validation Layer  ←  Enforces metadata quality rules
    ↑
JSON-LD Mapping Layer
    ↑
OpenMetadata Ontology Layer
```

## Relationship to Existing Wiki Concepts

- [[openmetadata-data-quality]] — SHACL provides an additional validation mechanism beyond OpenMetadata's native data quality tests. While native tests validate data content, SHACL validates metadata structure and consistency.
- [[semantic-web-for-data-platforms]] — SHACL is a key component of the semantic web stack for metadata management.

## Significance

SHACL validation enables automated enforcement of metadata quality rules at the semantic level, catching inconsistencies that might be missed by application-level validation. This is particularly important for organizations using OpenMetadata as a knowledge graph hub.

## Open Questions

- What specific shapes are defined? (e.g., required properties, cardinality constraints, value ranges)
- How does SHACL validation perform on large metadata graphs?
- Can users define custom SHACL shapes for their own entity types?
- How are SHACL violations surfaced to users?