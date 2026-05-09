---
type: entity
title: FlatGeoBuf (FGB)
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, file-format, binary, cloud-optimized]
related: [geoparquet, apache-iceberg, ogc-api-features, ingo-simonis, geospatial-format-comparison-framework, cloud-native-geospatial-workflow, gdal]
sources: ["FlatGeoBuf vs. GeoParquet vs. Apache Iceberg vs. OGC API-Features A Cloud Geospatial Comparison.md"]
---
# FlatGeoBuf (FGB)

FlatGeoBuf (FGB) is a single-file binary format for geospatial vector data based on Google's FlatBuffers serialization library. It stores a collection of features in a row-oriented layout, with each feature's geometry and attributes encoded sequentially. An optional packed Hilbert R-tree spatial index enables fast bounding-box queries.

## Key Characteristics

- **Row-oriented storage**: All attributes and geometry for a feature are stored together, enabling efficient retrieval of complete features by location.
- **Cloud-optimized**: Supports HTTP range requests so clients can fetch only the bytes for features within a spatial area, rather than downloading the entire file.
- **Embedded spatial index**: The Hilbert R-tree index allows efficient spatial filtering without external index files.
- **Immutable**: Files are meant for static or append-only use; no in-place edits.
- **No column pruning**: Cannot skip unused attributes during reads.
- **No built-in compression**: Binary encoding is more compact than text, but no columnar compression.
- **64-bit offsets**: No 2GB or 4GB file size limitations.

## Ecosystem Support

- **GDAL** (since v3.1): Read/write support, enabling QGIS, MapServer, and other GDAL-based software.
- **GeoServer**: Supports FGB as an output format (e.g., WFS/OGC API output).
- **Web clients**: OpenLayers, Leaflet, and MapLibre can consume FGB directly via JavaScript libraries or plugins.
- **OGC Community Standard candidate**: Not yet a formal standard, but an open specification.
- **Implementations**: Available in C++, Python (via GDAL or fgb library), JavaScript, Rust, etc.

## Limitations

- Not suitable for large-scale analytics (no column pruning, no distributed processing support).
- Static nature makes updates expensive (requires rewriting the entire file).
- No ACID transactions or multi-user editing.
- Not supported by mainstream big-data platforms (BigQuery, Athena, Snowflake).
- Limited attribute filtering without scanning candidate features.

## Use Cases

- Publishing open datasets for download and browser-based spatial queries.
- Data exchange between systems or environments (cloud to desktop, offline use).
- Web mapping with static data layers that don't warrant a full server.
- Hybrid cloud workflows where cloud systems generate FGB files for edge clients.

## Related

- [[geoparquet]] — Columnar alternative for analytics
- [[apache-iceberg]] — Table format for dynamic data lakes
- [[ogc-api-features]] — Web API standard for on-demand access
- [[geospatial-format-comparison-framework]] — Decision framework for format selection
- [[cloud-native-geospatial-workflow]] — Cloud-native patterns for geospatial data