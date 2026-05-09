---
type: concept
title: GeoDCAT-AP
created: 2026-04-29
updated: 2026-04-29
tags: [dcat, geospatial, inspire, metadata, application-profile]
related: [dcat-standard, inspire-directive, semantic-metadata, geonetwork]
sources: ["FOSS4GE 2024  Towards better data platforms with semantic metadata.md"]
---
# GeoDCAT-AP

GeoDCAT-AP (GeoDCAT Application Profile) is a European standard that defines how to use the [[dcat-standard]] vocabulary for describing geospatial datasets. It provides guidelines for representing INSPIRE-compliant metadata in RDF/DCAT format.

## Purpose

- Bridge the gap between INSPIRE's ISO-based metadata and the semantic web.
- Enable geospatial data catalogs to be discoverable by non-geospatial search engines and tools.
- Provide a machine-readable representation that can be transformed to/from ISO 19139.

## Key Features

- **INSPIRE Compliance**: GeoDCAT-AP metadata can be transformed to satisfy INSPIRE requirements using XSLT tools provided by [[SEMIC]].
- **Cross-Domain Interoperability**: Allows geospatial metadata to be indexed by general-purpose search engines (via schema.org).
- **OGC Alignment**: The Open Geospatial Consortium (OGC) is working on a global GeoDCAT best practice, extending beyond Europe.

## Relationship to INSPIRE

GeoDCAT-AP is part of the evolution of the [[inspire-directive]] ecosystem from rigid XML standards toward semantic metadata. It represents a practical application profile that makes semantic metadata usable for the geospatial community.
