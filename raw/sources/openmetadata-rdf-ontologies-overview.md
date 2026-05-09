---
source_url: "https://openmetadatastandards.org/rdf/overview/#standards-compliance"
fetched: 2026-04-14
title: "RDF & Ontologies Overview"
author: OpenMetadata Community
published:
original_tags: [clippings]
clipped_from: obsidian-web-clipper
---
## RDF & Ontologies Overview

OpenMetadata provides a complete semantic web stack built on W3C standards, enabling knowledge graph integration, semantic reasoning, and linked data capabilities.

## Components

The core **OpenMetadata Ontology** (`rdf/ontology/openmetadata.ttl`) defines:

- **Classes**: Formal definitions of entity types (Table, Dashboard, Pipeline, etc.)
- **Properties**: Relationships and attributes
- **Hierarchies**: Class and property taxonomies
- **Constraints**: Domain and range restrictions
- **Annotations**: Rich metadata about the ontology itself

**Size**: ~48KB, comprehensive coverage of all OpenMetadata concepts

**Format**: Turtle (TTL) - human-readable RDF syntax

### Provenance Ontology

The **OpenMetadata Provenance Ontology** extends W3C PROV-O for:

- **Data Lineage**: Track data transformations and dependencies
- **Activity Tracking**: Record metadata operations
- **Attribution**: Identify responsible agents (users, systems)
- **Derivation**: Capture how entities are derived from others

### SHACL Shapes

Validation rules ensuring data quality and consistency (~9KB of validation shapes).

### JSON-LD Contexts

Enable semantic JSON, URI mapping, type coercion, and interoperability with other systems. Available for: base, dataAsset, entityRelationship, governance, operations, quality, service, team, thread.

## Architecture

```
Applications (Knowledge Graphs, Semantic Search, Reasoning)
    ↓
SPARQL Query Layer
    ↓
SHACL Validation Layer
    ↓
JSON-LD Mapping Layer
    ↓
OpenMetadata Ontology Layer (Semantic definitions, classes, properties)
```

## Use Cases

1. **Knowledge Graph Construction**: Convert JSON metadata to RDF, load into triple store, query with SPARQL
2. **Semantic Search**: Concept-based search with ontology-driven query expansion
3. **Data Lineage & Provenance**: Track lineage using PROV-O
4. **Metadata Validation**: Enforce quality rules with SHACL
5. **Interoperability**: Exchange with DCAT, Schema.org, Dublin Core
6. **Semantic Reasoning**: Infer class hierarchies and property chains
