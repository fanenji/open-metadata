---
type: concept
title: Metadata Standard
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, metadata-standard, json-schema, rdf, owl, shacl, json-ld, prov-o, semantic-web, governance]
related: [semantic-web-support, jsonschemas, schema-first-approach, unified-metadata-graph, openmetadata-system-architecture, openmetadata]
sources: ["metadata-standard-openmetadata-core-schema-guide---20260514.md"]
---

# Metadata Standard

The **OpenMetadata Standards** project is the community-driven home for all schemas and ontologies behind OpenMetadata. It provides the canonical set of definitions that power data cataloging, governance, lineage, quality, and observability across the platform.

## Scope

The Metadata Standard encompasses:

- **700+ JSON Schemas** covering all entities (tables, topics, pipelines, dashboards, etc.), relationships, events, and configuration.
- **RDF/OWL ontologies** for semantic web and knowledge graph use cases.
- **SHACL shapes** for validating RDF graphs.
- **JSON-LD** serialization for linked data interoperability.
- **PROV-O** provenance ontology for tracking data lineage.
- **API specifications** for REST and event-driven interactions (search, feeds, webhooks, bulk operations).

## Relationship to the Schema-First Approach

The Metadata Standard is the authoritative source of the JSON Schema definitions used in OpenMetadata's [[schema-first-approach]]. These schemas are the single source of truth from which Java and Python code is automatically generated, ensuring consistency across the entire platform.

## Community-Driven Governance

Unlike an internal implementation detail, the Metadata Standard is an externally hosted, community-driven project. The canonical definitions live on [GitHub](https://github.com/open-metadata/OpenMetadata), and the official portal is [openmetadatastandards.org](https://openmetadatastandards.org), which provides quick starts, schema references, semantic web resources, and contribution guides.

## Standards Compliance

The Metadata Standard complies with:
- JSON Schema Draft 07 and 2020-12
- RDF/OWL (W3C)
- SHACL (W3C)
- JSON-LD (W3C)
- PROV-O (W3C)

## Related Wiki Pages

- [[semantic-web-support]] — Details on RDF/OWL, SHACL, JSON-LD, and PROV-O support.
- [[jsonschemas]] — The JSON Schema definitions that implement the standard.
- [[schema-first-approach]] — The architectural principle enabled by the standard.
- [[unified-metadata-graph]] — The central metadata graph, supported by semantic web ontologies.
- [[openmetadata-system-architecture]] — The high-level architecture that the standard defines.