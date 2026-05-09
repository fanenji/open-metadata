---
type: concept
title: DCAT-AP/AGID Compliance
created: 2026-05-07
updated: 2026-05-07
tags: [open-data, standards, compliance, public-administration, metadata]
related: [ckan-portal, pdnd-interoperability, openmetadata, data-product-definition]
sources: ["Sintesi Architettura (Claude).md"]
---
# DCAT-AP/AGID Compliance

DCAT-AP (Data Catalog Vocabulary - Application Profile) and AGID (Agenzia per l'Italia Digitale) are metadata standards for open data in the Italian public administration. The Regione Liguria Data Platform must comply with these standards for publishing open data.

## DCAT-AP

- **Definition**: An RDF-based vocabulary for describing datasets and data catalogs, standardized by the European Commission
- **Purpose**: Enables cross-border and cross-sector discovery of open data across EU member states
- **Key Elements**: Dataset description, distribution formats, temporal/geographic coverage, publisher information

## AGID Requirements

- **Definition**: Italian national guidelines for open data publication, based on DCAT-AP
- **Purpose**: Ensures consistency and interoperability of open data across Italian public administrations
- **Additional Requirements**: Italian-language metadata, specific license types, contact information

## Implementation in the Platform

- **[[openmetadata]]**: Internal metadata catalog that can export metadata in DCAT-AP format
- **[[ckan-portal]]**: Public-facing catalog that exposes DCAT-AP compliant metadata
- **[[pdnd-interoperability]]**: National platform that consumes DCAT-AP metadata for cross-administration data discovery