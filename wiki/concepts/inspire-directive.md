---
type: concept
title: INSPIRE Directive
created: 2026-04-29
updated: 2026-05-07
tags: [inspire, eu, geospatial, metadata, directive, sdi, regulation, european-union, governance]
related: [geodcat-ap, dcat-standard, semantic-metadata, geonetwork, sdi-spatial-data-infrastructure, ogc-standards, crs-transformation, sdi-dp-integration-patterns]
sources: ["FOSS4GE 2024  Towards better data platforms with semantic metadata.md", "Integrazione SDI e Data Platform.md"]
---
# INSPIRE Directive

The INSPIRE Directive (Infrastructure for Spatial Information in Europe, 2007/2/EC) is a European Union legal framework that establishes a framework for a Spatial Data Infrastructure (SDI) across member states. It mandates standards for metadata, data interoperability, and network services for geospatial data. The directive aims to facilitate the sharing of spatial information to support EU environmental policies and other activities that may have an environmental impact.

## Key Requirements

INSPIRE sets out several key requirements for member states:

- **Technical specifications**: Detailed specifications for 34 spatial data themes organized in three Annexes
- **Metadata profiles**: Standardized metadata for discovery, evaluation, and use of spatial datasets and services
- **Interoperable network services**: Discovery, view, download, transformation, and invoke services
- **Data sharing agreements**: Arrangements between public administrations for data access and use
- **Monitoring and reporting**: Regular reporting on implementation progress

## Network Services

The directive mandates five types of network services:

1. **Discovery Services**: Search for spatial datasets and services based on metadata
2. **View Services**: Display, navigate, zoom, pan, and overlay spatial data
3. **Download Services**: Download complete datasets or portions
4. **Transformation Services**: Transform coordinate reference systems
5. **Invoke Services**: Invoke spatial data processing services

## Metadata Standards Evolution

INSPIRE’s metadata requirements have gone through several standards evolutions:

- **Legacy**: ISO 19139 (XML schema) — rigid, hierarchical, geospatial-specific.
- **Current**: ISO 19115-3 — newer version but backward-incompatible with 19139.
- **Emerging**: [[dcat-standard]] and [[geodcat-ap]] — semantic web approach.

The shift from ISO-based metadata to semantic models reflects a broader trend in data infrastructure.

## Challenges

- **Version Migration**: Only one upgrade in 15 years due to the difficulty of rewriting XML documents between ISO versions.
- **Ecosystem Isolation**: ISO-based metadata is only understandable within geospatial systems, limiting cross-domain interoperability.
- **Push for Change**: INSPIRE is now encouraging adoption of [[semantic-metadata]] (DCAT/GeoDCAT-AP) to improve interoperability with the broader web.

## Integration with Modern Data Platforms

INSPIRE compliance is a key driver for European organizations integrating SDI with modern Data Platforms. The directive's requirements for metadata, interoperability, and data sharing create both obligations and opportunities for integration. However, the tension between INSPIRE's OGC-based standards and the Modern Data Stack's SQL/Parquet/API-driven approach requires architectural resolution.

The evolution of INSPIRE from rigid ISO standards toward semantic metadata serves as an important case study. It demonstrates both the limitations of traditional XML schemas and the potential of semantic web technologies for large-scale data infrastructure.

## Related Concepts

- [[sdi-spatial-data-infrastructure]] — The infrastructure that INSPIRE mandates
- [[ogc-standards]] — Standards that underpin INSPIRE technical specifications
- [[crs-transformation]] — Coordinate transformation requirements under INSPIRE
- [[sdi-dp-integration-patterns]] — How to achieve INSPIRE compliance while adopting modern tools
- [[geonetwork]] — Often used as a metadata catalog for INSPIRE
- [[geodcat-ap]] and [[dcat-standard]] — Emerging semantic metadata standards