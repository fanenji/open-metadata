---
type: source
title: OpenMetadata Ontology Introduction
created: 2026-05-07
updated: 2026-05-07
tags: [openmetadata, ontology, rdf, owl, semantic-web]
related: [openmetadata, openmetadata-ontology, custom-connector-openmetadata, data-catalog-tool-comparison]
sources: ["openmetadata-ontology-introduction.md"]
authors: [OpenMetadata Community]
year: 2026
url: "https://openmetadatastandards.org/rdf/ontology/introduction/"
venue: ""
---
# OpenMetadata Ontology Introduction

This page introduces the OpenMetadata RDF/OWL ontology, which provides formal semantic definitions of metadata concepts using W3C standards. The ontology file is located at `rdf/ontology/openmetadata.ttl` and uses the namespace `om:`.

## Purpose

The ontology serves four main purposes:

- **Formal semantic definitions** — Standardizing metadata concepts in a machine-readable format.
- **Knowledge graph integration** — Enabling graph-based traversal and discovery of metadata entities.
- **SPARQL querying** — Allowing complex queries across the metadata graph.
- **Semantic reasoning** — Inferring new relationships from existing metadata using OWL axioms.

## Namespaces

The ontology defines the following namespaces:

- `om:` — `<http://open-metadata.org/ontology#>`
- `rdf:` — `<http://www.w3.org/1999/02/22-rdf-syntax-ns#>`
- `rdfs:` — `<http://www.w3.org/2000/01/rdf-schema#>`
- `owl:` — `<http://www.w3.org/2002/07/owl#>`

## Related Documentation

For detailed class and property definitions, see the [Core Concepts, Classes, Properties](https://openmetadatastandards.org/rdf/ontology/) page.

## Significance

OpenMetadata is the only major open-source data catalog with a formal W3C-standard semantic layer. This ontology differentiates it from tools like [[datahub]] and [[amundsen]], which lack equivalent RDF/OWL definitions. The ontology can guide [[custom-connector-openmetadata]] development and enable advanced governance use cases such as automated data classification and rule inference.

## Open Questions

- What specific classes and properties does the ontology define?
- How does the ontology map to OpenMetadata's internal JSON schema data model?
- Is the ontology actively maintained and aligned with the latest OpenMetadata release?
- Can the ontology be used for automated data classification or governance rule inference?