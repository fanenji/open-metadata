---
type: concept
title: DCAT Ontology
created: 2026-04-29
updated: 2026-04-29
tags: [dcat, ontology, metadata, w3c, geospatial]
related: [semantic-metadata-overview, rdf-encodings-comparison, geonetwork, inspire, metadata-fields-definition]
sources: ["FOSS4GE 2024  Towards better data platforms with semantic metadata - Summary.md"]
---
# DCAT Ontology

**DCAT** (Data Catalog Vocabulary) is a W3C ontology for describing datasets and data catalogs. It is **not a format** — it is a set of terms (like `dcat:Dataset`, `dcat:Distribution`, `dct:publisher`) that give meaning to relationships.

## DCAT-AP

**DCAT-AP** (Application Profile for European Data Portals) is the set of guidelines from SEMIC on how to use DCAT to describe datasets across European open data catalogs.

## GeoDCAT-AP

**GeoDCAT-AP** extends DCAT-AP specifically for geospatial data. Key properties:
- A complete GeoDCAT-AP metadata record contains enough information to derive **INSPIRE compliance** — SEMIC provides XSLT transforms for this
- Bridges the geospatial world (INSPIRE) with the broader open data world (DCAT-AP)
- Being adopted progressively across European national data portals

## OGC GeoDCAT

The OGC is developing a non-European-specific equivalent: **OGC GeoDCAT** — best practices for representing geospatial metadata semantically for a global audience.

## Relevance to the Data Platform

DCAT provides a standardized vocabulary that could inform or extend the [[metadata-fields-definition]] for the Data Platform. Adopting DCAT would align with EU open data standards and enable cross-platform interoperability.