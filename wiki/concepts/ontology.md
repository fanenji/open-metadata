---
type: concept
title: Ontology
created: 2026-04-29
updated: 2026-04-29
tags: [ontology, semantic-web, vocabulary, rdf, standardization]
related: [semantic-metadata, dcat-standard, rdf-data-model, knowledge-graph]
sources: ["FOSS4GE 2024  Towards better data platforms with semantic metadata.md"]
---
# Ontology

In the context of the semantic web, an ontology is a standardized collection of terms (classes, properties, relationships) used to describe entities and their relationships. Ontologies provide the shared vocabulary that enables interoperability across different systems and domains.

## Key Components

- **Classes**: Categories of things (e.g., `dcat:Dataset`, `foaf:Person`).
- **Properties**: Attributes or relationships (e.g., `dct:title`, `dcat:publisher`).
- **Relationships**: Links between classes (e.g., `dcat:distribution` links a Dataset to a Distribution).

## Examples

- **DCAT**: W3C ontology for data catalogs ([[dcat-standard]]).
- **Dublin Core**: General-purpose ontology for describing resources.
- **schema.org**: Google's ontology for web indexing.
- **FOAF**: Ontology for describing persons and their relationships.

## Application Profiles

Because ontologies define terms but not how to use them, **application profiles** provide guidelines for applying an ontology to a specific domain. For example, [[geodcat-ap]] is an application profile for using DCAT with geospatial data.

## Relevance

Ontologies are the backbone of [[semantic-metadata]]. They enable the creation of [[knowledge-graphs]] that can be understood across organizational and ecosystem boundaries, addressing the [[data-catalog-critique]] by providing a shared language for describing data.
