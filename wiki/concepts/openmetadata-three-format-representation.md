---
type: concept
title: OpenMetadata Three-Format Representation
created: 2026-05-07
updated: 2026-05-07
tags: [openmetadata, standards, json-schema, rdf, owl, json-ld, interoperability]
related: [openmetadata, openmetadata-standards-overview, custom-connector-openmetadata, metadata-fields-definition]
sources: ["openmetadata-standards-overview.md"]
---
# OpenMetadata Three-Format Representation

Every entity in the OpenMetadata Standards specification is expressed in three interoperable formats, each serving a different purpose and audience:

1. **JSON Schema (Draft-07)**: 700+ entity schemas providing strongly typed, programmatic access. This is the primary format for tool integration, API development, and validation. It is the most widely used format in modern data stacks.

2. **RDF & OWL (W3C Ontology)**: Enables semantic reasoning, inference, and SPARQL queries. This format is valuable for knowledge graph applications, ontology alignment, and advanced governance scenarios where logical reasoning over metadata is required.

3. **JSON-LD (Linked Data Contexts)**: Provides Schema.org compatibility and web-scale integration. This format bridges the gap between internal metadata and external semantic web standards, enabling metadata to be consumed by search engines and web-based tools.

The three-format approach ensures maximum interoperability across different toolchains and use cases, but introduces maintenance complexity. Teams must decide which formats are necessary for their specific requirements. This concept connects to the wiki's [[custom-connector-openmetadata]] page by explaining why connectors need schema mapping, and contrasts with the minimal [[metadata-fields-definition]] approach documented elsewhere in the wiki.