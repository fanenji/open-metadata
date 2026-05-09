---
type: entity
title: Map Service Performance Issues
created: 2026-04-29
updated: 2026-04-29
tags: [performance, gis, map-services, legacy-architecture]
related: [legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, geospatial-etl-pipeline-iceberg, etl-pattern]
sources: ["ETL ATTUALE.md"]
---
# Map Service Performance Issues

Known performance bottlenecks in the map service layer of the [[legacy-geospatial-etl-pipeline]], documented in [[ETL ATTUALE.md]].

## Description
The map service layer (servizi cartografici) experiences performance criticality (CRITICITÀ PRESTAZIONI). This is a key driver for modernization efforts documented elsewhere in the wiki.

## Impact
- Degraded user experience for web clients consuming map services
- Potential scalability limitations
- Integration challenges between cartographic and visualization layers

## Relationship to Modern Stack
The performance issues in this legacy pipeline implicitly support the adoption of modern architectures such as [[geospatial-etl-pipeline-iceberg]], [[duckdb]], and [[dremio]], which are designed to eliminate these bottlenecks through cloud-native, columnar, and lakehouse approaches.