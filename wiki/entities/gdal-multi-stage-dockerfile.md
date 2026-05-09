---
type: entity
title: GDAL Multi-Stage Dockerfile
created: 2026-04-29
updated: 2026-04-29
tags: [gdal, docker, multi-stage, build, reference]
related: [gdal-docker-build-strategy, proj-grid-file-management, oracle-instant-client-docker, container-image-strategy-for-data-pipelines]
sources: ["ETL - CONVERSAZIONI LLM.md"]
---
# GDAL Multi-Stage Dockerfile

Reference implementation of a multi-stage GDAL Docker build with OCI, PostGIS, and GeoParquet support. This Dockerfile separates compilation from runtime to produce a smaller final image.

## Architecture

### Stage 1: Builder
- Base: `ubuntu:22.04`
- Installs: build-essential, cmake, g++, swig, all dev libraries
- Compiles: libecwj2 (ECW 3.3 SDK), GDAL 3.10.0
- GDAL configuration uses CMake with flags for:
  - Oracle OCI (`-DGDAL_USE_ORACLE=ON`)
  - PostgreSQL (`-DGDAL_USE_POSTGRESQL=ON`)
  - Arrow/Parquet (`-DGDAL_USE_ARROW=ON`, `-DGDAL_USE_PARQUET=ON`)
  - ECW (`-DGDAL_USE_ECW=ON`)
  - Python bindings (`-DBUILD_PYTHON_BINDINGS=ON`)
  - Various image formats (TIFF, PNG, JPEG, GIF, WebP)

### Stage 2: Final
- Base: `ubuntu:22.04`
- Installs only runtime libraries (no -dev packages)
- Copies from builder:
  - `/usr/local/lib/libNCSEcw*` (ECW libraries)
  - Oracle Instant Client directory
  - `/usr/lib/libgdal.so*`
  - `/usr/share/gdal` (GDAL data files)
  - `/usr/bin/gdal*`, `/usr/bin/ogr*` (executables)
  - Python bindings from `/usr/lib/python3/dist-packages/osgeo`
- Configures ldconfig for Oracle and ECW libraries

## Known Issues

- Python binding path (`/usr/lib/python3/dist-packages/osgeo`) may vary by Python/Ubuntu version
- The simpler Dockerfile (using `./configure`) omits several libraries present in the multi-stage build (libpng, libjpeg, libgif, libwebp, libzstd, libxml2, libjson-c, liblzma, libssl)

## Related Pages
- [[gdal-docker-build-strategy]] — Overall build strategy
- [[proj-grid-file-management]] — PROJ configuration
- [[oracle-instant-client-docker]] — Oracle client installation
- [[container-image-strategy-for-data-pipelines]] — General container design