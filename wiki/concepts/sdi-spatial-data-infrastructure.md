---
type: concept
title: SDI (Spatial Data Infrastructure)
created: 2026-03-18
updated: 2026-03-18
tags: [sdi, geospatial, data-infrastructure, governance]
related: [inspire-directive, ogc-standards, crs-transformation, sdi-dp-integration-patterns, data-lakehouse, data-mesh, data-catalog-critique]
sources: ["Integrazione SDI e Data Platform.md"]
---
# SDI (Spatial Data Infrastructure)

A Spatial Data Infrastructure (SDI) is a framework of policies, institutional agreements, technologies, data, and people that enables the sharing and effective use of geographic information. It is a socio-technical system that facilitates interaction between users and geospatial data.

## Core Components

1. **Data**: Fundamental geospatial datasets (administrative boundaries, addresses, cadastral parcels, elevation, land cover, transport networks, hydrography, geodetic control). The EU INSPIRE directive specifies key data themes organized in Annexes.

2. **Metadata**: Information describing geospatial datasets (origin, accuracy, update frequency, format, quality, lineage). Standards like ISO 19115 and Dublin Core are commonly used.

3. **Network Services**: Standardized interfaces for programmatic access to data and metadata, primarily based on OGC standards (WMS, WFS, WCS, CSW, WPS).

4. **Standards and Policies**: Shared agreements on data formats (GML, KML, GeoPackage), service interfaces (OGC standards), metadata profiles, and policies governing access, sharing, licensing, and pricing.

5. **Institutional Arrangements and People**: Collaboration frameworks between participating organizations, governance structures, and the community of users and data providers.

## Key Characteristics

- **Focus**: Facilitating the sharing, discovery, and interoperable use of geospatial data, often with a strong public sector emphasis.
- **Architecture**: Traditionally based on Service-Oriented Architecture (SOA) and OGC Web Services.
- **Governance**: Multi-stakeholder agreements, often driven by specific regulations (e.g., INSPIRE), focusing on data sharing policies, interoperability, and access.
- **Typical Users**: Public entities, researchers, GIS professionals, specific communities.

## Relationship to Data Platform

SDI and Data Platform (DP) have complementary capabilities. SDI provides authoritative geospatial data and interoperability standards, while DP provides broad data management, analytics, and governance capabilities. Their integration combines the "where" of spatial data with the "what, who, when" of business data.

## Evolution Pressures

Traditional SDI architectures are under pressure to evolve due to:
- Cloud computing adoption
- Big geospatial data volumes
- API-centric approaches prevalent in modern Data Platforms
- Need for integration with modern data stacks (dbt, DuckDB, Iceberg)

## Related Concepts

- [[inspire-directive]] — EU legal framework mandating interoperable SDIs
- [[ogc-standards]] — OGC Web Services and API evolution
- [[crs-transformation]] — Coordinate Reference System transformation challenges
- [[sdi-dp-integration-patterns]] — Integration approaches for SDI and DP
- [[data-lakehouse]] — Identified as ideal convergence architecture for SDI-DP integration
- [[data-mesh]] — "Geospatial domain" as a data product owner in mesh architectures