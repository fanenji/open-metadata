---
type: source
title: "FOSS4GE 2024: Towards Better Data Platforms with Semantic Metadata"
created: 2026-04-04
updated: 2026-04-29
tags: [semantic-metadata, rdf, dcat, geonetwork, inspire, metadata, geospatial]
related: [semantic-metadata-overview, geonetwork, dcat-ontology, rdf-encodings-comparison, semantic-metadata-vs-xml-metadata, metadata-fields-definition, data-catalog-tool-comparison]
sources: ["FOSS4GE 2024  Towards better data platforms with semantic metadata - Summary.md"]
---
# FOSS4GE 2024: Towards Better Data Platforms with Semantic Metadata

**Speakers:** Florent Gravin (presenting on behalf of Olivia Guyot), Camp to Camp
**Event:** FOSS4G Europe 2024 — General Track, Room QFieldCloud (246), July 4, 2024
**Video:** https://www.youtube.com/watch?v=DjF2NC-43Rc
**Slides:** https://talks.osgeo.org/foss4g-europe-2024/talk/K3TSFH/

## Summary

This talk argues that semantic metadata (RDF/DCAT) is superior to traditional XML-based geospatial metadata (ISO 19115/19139) for interoperability beyond the GIS world. The core thesis is that DCAT is the bridge between geospatial infrastructure and mainstream data ecosystems (cloud warehouses, BI tools, search engines). The presenters demonstrate how GeoNetwork-UI's semantic module can ingest DCAT/Turtle/JSON-LD and output multiple formats, enabling gradual migration from XML-based standards.

## Key Arguments

1. **Semantic metadata (RDF/DCAT) is superior to traditional XML-based geospatial metadata (ISO 19115/19139)** for interoperability beyond the GIS world.
2. **DCAT is the bridge** between geospatial infrastructure and mainstream data ecosystems (cloud warehouses, BI tools, search engines).
3. **GeoNetwork-UI's semantic module** can ingest DCAT/Turtle/JSON-LD and output multiple formats, enabling gradual migration.

## Key Concepts Introduced

- [[semantic-metadata-overview]] — Core concepts: RDF triples, knowledge graphs, ontologies vs. encodings
- [[dcat-ontology]] — DCAT vocabulary, DCAT-AP, GeoDCAT-AP, OGC GeoDCAT
- [[rdf-encodings-comparison]] — Turtle, JSON-LD, RDF/XML, N-Triples
- [[semantic-metadata-vs-xml-metadata]] — Decision framework: when to use RDF/DCAT vs. ISO 19139/19115

## Connections to Existing Wiki

- [[metadata-fields-definition]] — DCAT provides a standardized vocabulary that could inform or extend the minimal metadata field set
- [[data-catalog-tool-comparison]] — GeoNetwork-UI should be evaluated as a candidate with semantic metadata capabilities
- [[data-lakehouse]] — Semantic metadata could be the "glue" between geospatial and non-geospatial data in a lakehouse
- [[dremio]] / [[duckdb]] — The interoperability argument is relevant to the data lakehouse stack