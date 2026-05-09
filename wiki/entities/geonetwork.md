---
type: entity
title: GeoNetwork
created: 2026-04-29
updated: 2026-05-07
tags: [metadata-catalog, geospatial, inspire, open-source, catalog, metadata, semantic-metadata, dcat-standard, inspire-directive, geodcat-ap]
related: [geonetwork-ui, dcat-ontology, semantic-metadata-overview, data-catalog-tool-comparison, inspire, semantic-metadata, dcat-standard, inspire-directive, geodcat-ap]
sources: ["FOSS4GE 2024  Towards better data platforms with semantic metadata - Summary.md", "FOSS4GE 2024  Towards better data platforms with semantic metadata.md"]
---
# GeoNetwork

GeoNetwork is an open-source catalog platform for managing geospatial metadata. It is the dominant open-source geospatial metadata catalog in the INSPIRE ecosystem, widely used in INSPIRE-compliant Spatial Data Infrastructures (SDIs) across Europe. The platform is built on strictly structured XML formats (ISO 19139, CSW), which makes semantic metadata challenging to handle natively.

## Key Features

- **Metadata Management**: Create, edit, and publish ISO 19139/19115‑3 metadata records.
- **Catalog Services**: Supports CSW (Catalog Service for the Web) for metadata harvesting and discovery.
- **Semantic Support**: Recent versions support export to DCAT, GeoDCAT‑AP, and DCAT Mobility formats.
- **Harvesting**: Can harvest metadata from semantic catalogs in addition to traditional ISO sources.

## Current Semantic Capabilities

| Capability | Status |
|---|---|
| DCAT export (catalog endpoint) | Available via GeoNetwork for matters and CSW output |
| DCAT-AP / DCAT Mobility export | Available |
| Harvesting semantic catalogs | Supported |
| Import of DCAT/Turtle in new editor (GeoNetwork‑UI) | Available — with automatic conversion between formats |

## GeoNetwork-UI

**GeoNetwork-UI** is a modern sister project — a toolkit for building catalog frontends using contemporary web technologies. It has a different metadata reading and writing model that is more abstract than the classic GeoNetwork core. This abstraction makes it possible to implement a **semantic-capable module** that:

1. Reads metadata expressed as DCAT/Turtle/JSON‑LD
2. Internally represents it as an RDF graph
3. Outputs it in any required encoding (ISO XML, DCAT JSON‑LD, Turtle, etc.)

Thus, GeoNetwork‑UI demonstrates the practical feasibility of the [[semantic-metadata]] approach, providing a concrete implementation of the proposed evolution path.

## Relevance to the Data Platform

GeoNetwork‑UI is a candidate for the Data Platform's catalog layer, particularly for geospatial metadata. It should be evaluated against [[datahub]], [[openmetadata]], and [[amundsen]] for the specific use case of managing geospatial datasets alongside non-geospatial data.

GeoNetwork represents the legacy approach (ISO XML) that the source talk argues should evolve toward semantic metadata. Its GeoNetwork‑UI sibling provides a concrete implementation of the proposed evolution path.