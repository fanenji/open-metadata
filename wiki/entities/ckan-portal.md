---
type: entity
title: CKAN Portal
created: 2026-05-07
updated: 2026-05-07
tags: [open-data, distribution, catalog, public-sector]
related: [dcat-ap-agid-compliance, pdnd-interoperability, wso2-api-gateway, bronze-silver-gold-architecture]
sources: ["Sintesi Architettura (Claude).md"]
---
# CKAN Portal

CKAN (Comprehensive Knowledge Archive Network) is the open data portal used for public distribution of datasets from the Regione Liguria Data Platform. It provides a front-office interface for citizens and systems to discover and access open data.

## Role in Architecture

CKAN serves as the public-facing catalog for open data, distinct from [[OpenMetadata]] which is the internal metadata catalog. Datasets are published from the Gold layer of the [[bronze-silver-gold-architecture]] through an OpenData Downloader service (to be developed).

## Key Features

- **Public Catalog**: Searchable, browsable catalog of open datasets
- **Dataset Download**: Direct download of datasets in multiple formats
- **API Access**: Programmatic access to catalog metadata and datasets
- **DCAT-AP Compliance**: Metadata conforming to DCAT-AP and AGID standards

## Related Components

- **OpenData Downloader**: Service to extract datasets from the Data Lake for publication (to be developed)
- **WSO2 API Gateway**: API management for interoperability with [[pdnd-interoperability|PDND]] and external systems