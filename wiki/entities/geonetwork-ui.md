---
type: entity
title: GeoNetwork-UI
created: 2026-04-29
updated: 2026-05-07
tags: [software, metadata-catalog, geospatial, frontend, catalog, metadata, ui, semantic]
related: [geonetwork, semantic-metadata-overview, dcat-ontology, semantic-metadata, dcat-standard]
sources: ["FOSS4GE 2024  Towards better data platforms with semantic metadata - Summary.md", "FOSS4GE 2024  Towards better data platforms with semantic metadata.md"]
---

# GeoNetwork-UI

GeoNetwork-UI is a modern toolkit for building catalog frontends using contemporary web technologies. It is a sister project to [[geonetwork]] with a different metadata reading and writing model that is more abstract than the classic GeoNetwork core. GeoNetwork-UI has implemented a semantic-capable module that allows reading and outputting metadata in a variety of formats.

## Semantic Capabilities

The semantic-capable module:

- Reads metadata expressed in DCAT, DCAT-AP, and GeoDCAT-AP using Turtle and JSON-LD serializations, and internally represents it as an RDF graph.
- Uses existing RDF libraries to convert between different semantic encodings.
- Outputs metadata in any required encoding, including ISO XML, DCAT JSON-LD, Turtle, and others.
- Demonstrates how a traditional geospatial catalog can be extended to support semantic metadata without abandoning existing ISO-based records, enabling gradual migration from traditional XML-based geospatial metadata (ISO 19139) to semantic metadata (RDF/DCAT) without breaking existing consumers.

## Relevance

GeoNetwork-UI serves as a proof-of-concept for the [[semantic-metadata]] approach advocated in the source talk. It shows that semantic metadata can be practically integrated into existing geospatial infrastructure, enabling a gradual transition from ISO XML to RDF/DCAT.