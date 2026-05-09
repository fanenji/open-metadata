---
type: entity
title: OpenMetadata Ontology
created: 2026-05-07
updated: 2026-05-07
tags: ["openmetadata", "ontology", "rdf", "owl", "semantic-web", "knowledge-graph"]
related: ["openmetadata", "openmetadata-ontology-introduction", "custom-connector-openmetadata", "data-catalog-tool-comparison", "openmetadata-provenance-ontology", "openmetadata-shacl-validation", "openmetadata-jsonld-contexts", "semantic-web-for-data-platforms"]
sources: ["openmetadata-ontology-introduction.md", "openmetadata-rdf-ontologies-overview.md"]
---
# OpenMetadata Ontology

The OpenMetadata Ontology is a formal RDF/OWL semantic definition of all entity types, properties, hierarchies, and constraints in the [[openmetadata]] platform. It is published at `rdf/ontology/openmetadata.ttl` under the namespace `om:` (`@prefix om: <http://open-metadata.org/ontology#> .`). The ontology is expressed in Turtle (TTL) RDF format, is approximately 48KB in size, and covers all OpenMetadata concepts. It serves as the foundational layer of OpenMetadata's semantic web stack, enabling knowledge graph integration, SPARQL querying, and semantic reasoning.

## Purpose and Significance

- **Knowledge graph integration**: Metadata entities are connected in a graph structure, enabling traversal and discovery across the entire metadata landscape.
- **SPARQL querying**: Complex queries across the metadata graph using the W3C SPARQL query language.
- **Semantic reasoning**: OWL axioms allow inference of new relationships from existing metadata, including deriving implicit knowledge from class hierarchies and property chains. This enables automated discovery and classification.
- **Concept-based search**: Ontology-driven query expansion that goes beyond simple keyword matching to leverage the semantic relationships defined in the ontology.
- **Interoperability**: The ontology facilitates mapping to external standards and vocabularies such as DCAT, Schema.org, and Dublin Core.
- **Standardized validation**: SHACL shapes reference ontology classes and properties to provide a standardized validation framework.
- **Differentiation**: OpenMetadata is the only major open-source data catalog that provides a formal W3C-standard semantic layer. Both [[datahub]] and [[amundsen]] lack equivalent RDF/OWL definitions, making this a key differentiator for organizations pursuing knowledge graph integration and advanced governance use cases. The ontology also guides [[custom-connector-openmetadata]] development.

## Technical Foundation

Based on W3C standards:

- **RDF** — Resource Description Framework for representing metadata as subject-predicate-object triples.
- **OWL** — Web Ontology Language for defining classes, properties, and logical axioms.
- **SPARQL** — Query language for RDF graphs.

### Namespace

```
@prefix om: <http://open-metadata.org/ontology#> .
```

### Format and Location

- **Format**: Turtle (TTL) – human-readable RDF syntax.
- **Size**: ~48KB (comprehensive coverage of all OpenMetadata concepts).
- **Location**: `rdf/ontology/openmetadata.ttl`

### Contents

The ontology defines:

- **Classes**: Formal definitions of entity types (Table, Dashboard, Pipeline, etc.)
- **Properties**: Relationships and attributes between entities
- **Hierarchies**: Class and property taxonomies
- **Constraints**: Domain and range restrictions
- **Annotations**: Rich metadata about the ontology itself

## Role in Architecture

The ontology sits at the bottom of OpenMetadata's semantic web stack:

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

## Open Questions

- What specific classes and properties does the ontology define?
- How actively is the ontology maintained and aligned with the latest OpenMetadata release?
- How does the ontology map to OpenMetadata's internal JSON schema data model?
- Does the ontology support custom extensions (e.g., for the [[custom-connector-openmetadata]] pattern)?
- Can the ontology be used for automated data classification or governance rule inference?
- What is the performance profile of SPARQL queries against the ontology at scale?