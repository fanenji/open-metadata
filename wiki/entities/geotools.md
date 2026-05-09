---
type: entity
title: GeoTools
created: 2026-05-07
updated: 2026-05-07
tags: [gis, java, geospatial-library, coordinate-transformation]
related: [apache-sedona, sedona-st-transform-limitations, grid-shift-transformations, postgis]
sources: ["Sedona e file grigliati GSB.md"]
---
# GeoTools

GeoTools is a mature, powerful Java geospatial library that implements Open Geospatial Consortium (OGC) specifications. It serves as the underlying transformation engine for Apache Sedona's spatial SQL functions.

## Role in the Data Platform

GeoTools is the core library used by Apache Sedona for coordinate transformation operations. Sedona wraps GeoTools functionality through the `geotools-wrapper` Maven dependency, with version numbers tied to the encapsulated GeoTools release (e.g., Sedona 1.7.1 uses GeoTools 28.5).

## GSB/NTv2 Capabilities

GeoTools **does support** grid-based datum transformations, including:

- **NTv2 format** (`.gsb` files): Supported via the grid shift resource path `org/geotools/referencing/factory/gridshift/`
- **NADCON format** (`.las`/`.los` or `.laa`/`.loa` files): Implemented via the `NADCONTransform` class
- **Auto-detection**: Grid files placed in the classpath resource directory are automatically detected by the transformation engine

## The Library-Interface Gap

Despite GeoTools' intrinsic capability to perform grid-based transformations, Apache Sedona's `ST_Transform` function does not expose the parameters needed for users to specify GSB files or select grid-based transformation pipelines. This is a recurring architectural pattern in the data platform: the underlying library has the capability, but the higher-level API does not expose it.

## Related Pages

- [[apache-sedona]] — The distributed spatial system that wraps GeoTools
- [[sedona-st-transform-limitations]] — The specific limitation this gap creates
- [[grid-shift-transformations]] — Concept page on GSB/NTv2 transformations
- [[postgis]] — Comparison: PostGIS exposes PROJ's `+nadgrids` directly