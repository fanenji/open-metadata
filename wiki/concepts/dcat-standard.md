---
type: concept
title: DCAT Standard
created: 2026-04-29
updated: 2026-04-29
tags: [dcat, w3c, metadata, catalog, ontology]
related: [semantic-metadata, geodcat-ap, rdf-data-model, inspire-directive, data-catalog-critique]
sources: ["FOSS4GE 2024  Towards better data platforms with semantic metadata.md"]
---
# DCAT Standard

DCAT (Data Catalog Vocabulary) is a W3C standard ontology for describing data catalogs, datasets, and their distributions. It provides a set of classes and properties for representing the structure and contents of a data catalog in RDF.

## Core Classes

- **dcat:Catalog** — A collection of datasets.
- **dcat:Dataset** — A collection of data, published or curated by a single agent.
- **dcat:Distribution** — A specific representation of a dataset (e.g., CSV file, API endpoint).
- **dcat:DataService** — A service that provides access to datasets.

## Key Properties

- **dct:title** — Human-readable name.
- **dct:description** — Free-text description.
- **dct:publisher** — Responsible entity.
- **dct:issued** / **dct:modified** — Temporal metadata.
- **dcat:keyword** — Tags for discovery.
- **dcat:theme** — Category from a knowledge organization system.

## Application Profiles

DCAT is designed to be extended via **application profiles** — guidelines on how to use DCAT for specific domains. The most relevant for geospatial data is [[geodcat-ap]], the European application profile for geospatial DCAT.

## Relevance

DCAT enables data platforms to describe their holdings in a way that is interoperable with the broader web ecosystem, not just geospatial systems. It is a key component of the [[semantic-metadata]] approach advocated in the source talk.
