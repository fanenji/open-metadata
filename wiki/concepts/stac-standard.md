---
type: concept
title: STAC Standard
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, standard, metadata, catalog, earth-observation]
related: [cloud-native-geospatial-architecture, data-catalog-tool-comparison, datahub, openmetadata]
sources: ["Ingestione dati cartografici_ analisi alternative.md"]
---
# STAC Standard

STAC (SpatioTemporal Asset Catalog) is an open standard for describing and cataloging geospatial assets, with a particular focus on Earth observation data (satellite imagery, aerial data, etc.).

## Purpose

STAC is not an ingestion tool but a **metadata standard** that facilitates discovery, querying, and access to geospatial data. A STAC catalog contains items that describe individual data "granules" (e.g., a satellite scene) and point to the actual data assets, which are often stored as COG but can also be other formats including GeoParquet.

## Relevance to the Architecture

The ingestion pipeline produces COG as output for raster data. Adopting STAC to catalog these generated COGs would offer significant interoperability and usability benefits:

- **External Discoverability**: While the internal Data Catalog (DataHub/OpenMetadata) serves discovery and governance within the platform, a STAC catalog would make raster assets discoverable and usable by a wide range of external geospatial tools and platforms that support the STAC standard.
- **Standardized Metadata**: Provides a consistent way to describe spatial and temporal properties of assets.
- **Integration Potential**: Could be generated as an additional output of the raster ingestion pipeline or via a separate process that scans COG output.

## Relationship with Internal Catalog

The internal Data Catalog and STAC serve complementary purposes:
- **Internal Catalog (DataHub/OpenMetadata)**: Platform-wide governance, lineage, and discovery
- **STAC Catalog**: Geospatial-specific discovery and interoperability with external GIS tools

## Related

- [[cloud-native-geospatial-architecture]] — Broader cloud-native architecture context
- [[data-catalog-tool-comparison]] — Comparison of internal data catalog tools
- [[datahub]] — Internal metadata platform
- [[openmetadata]] — Internal metadata platform
