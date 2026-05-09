---
type: concept
title: OGC Standards
created: 2026-03-18
updated: 2026-03-18
tags: [sdi, geospatial, standards, interoperability, ogc]
related: [sdi-spatial-data-infrastructure, inspire-directive, crs-transformation, sdi-dp-integration-patterns, cloud-native-geospatial-workflow]
sources: ["Integrazione SDI e Data Platform.md"]
---
# OGC Standards

The Open Geospatial Consortium (OGC) develops and maintains standards for geospatial data and services interoperability. These standards are foundational to Spatial Data Infrastructures (SDIs) and are evolving to meet the demands of modern data platforms.

## Traditional OGC Web Services

- **WMS (Web Map Service)**: Serves georeferenced map images (PNG, JPEG, etc.) from geospatial data
- **WFS (Web Feature Service)**: Serves vector data (features) with full geometry and attribute access
- **WCS (Web Coverage Service)**: Serves raster and coverage data (e.g., satellite imagery, elevation models)
- **CSW (Catalogue Service for the Web)**: Searches and discovers geospatial data and services through metadata catalogs
- **WPS (Web Processing Service)**: Executes remote geospatial processing operations

## Modern OGC API Standards

The OGC is transitioning from traditional SOAP/XML-based web services to modern RESTful APIs:

- **OGC API - Features**: Modern replacement for WFS, serving GeoJSON features via REST
- **OGC API - Maps**: Modern replacement for WMS
- **OGC API - Coverages**: Modern replacement for WCS
- **OGC API - Records**: Modern replacement for CSW
- **OGC API - Processes**: Modern replacement for WPS

## Key Characteristics

- **Interoperability**: Standards ensure that different systems can exchange and use geospatial data
- **Evolution**: Transition from SOA-based services to RESTful APIs aligns with modern data platform architectures
- **Complementary to Modern Stack**: OGC APIs can bridge traditional SDI with modern data platforms using SQL, Parquet, and REST

## Tension with Modern Data Stack

Traditional OGC standards (GML, WMS, WFS) use different paradigms than the Modern Data Stack (SQL, Parquet, REST APIs). The OGC API evolution addresses this gap but adoption varies. Organizations integrating SDI with DP must navigate this tension, potentially using OGC APIs as a bridge layer.

## Related Concepts

- [[sdi-spatial-data-infrastructure]] — Infrastructure built on OGC standards
- [[inspire-directive]] — EU directive that mandates OGC-based interoperability
- [[crs-transformation]] — Coordinate transformation, often handled via OGC standards
- [[sdi-dp-integration-patterns]] — How OGC APIs enable integration patterns
- [[cloud-native-geospatial-workflow]] — Modern geospatial workflows that may bypass traditional OGC services