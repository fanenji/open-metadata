---
type: entity
title: GDAL Docker Build Strategy
created: 2026-04-29
updated: 2026-04-29
tags: [gdal, docker, build, geospatial, etl]
related: [proj-grid-file-management, oracle-instant-client-docker, gdal-multi-stage-dockerfile, container-image-strategy-for-data-pipelines, geospatial-etl-pipeline-iceberg]
sources: ["ETL - CONVERSAZIONI LLM.md"]
---
# GDAL Docker Build Strategy

A comprehensive approach for building GDAL Docker images with various database drivers (Oracle, PostGIS) and format support (GeoParquet, ECW). The strategy encompasses two main build systems (CMake and `./configure`) and two deployment patterns (single-stage and multi-stage).

## Key Patterns

### Multi-stage Build (Recommended)
- **Builder Stage**: Contains all compilation tools (g++, cmake, swig), dev libraries, and source code. Downloads and compiles GDAL with all required drivers.
- **Final Stage**: Starts from a clean base image (ubuntu:22.04), installs only runtime dependencies, and copies compiled artifacts from the builder stage.
- **Benefits**: Significantly reduces final image size by excluding build tools and intermediate files.

### Build Systems
- **CMake** (used in multi-stage build): More comprehensive format support including Arrow, Parquet, ECW. Uses `-D` flags for configuration.
- **`./configure`** (used in simpler Dockerfile): Traditional autotools-based build. Simpler but may have reduced format support.

### Required Drivers
- Oracle OCI (via Instant Client SDK)
- PostgreSQL/PostGIS
- GeoParquet (via Arrow/Parquet libraries)
- ECW (via libecwj2 SDK)
- GeoTIFF, PNG, JPEG, GIF, WebP, ZSTD

## Dockerfile Structure

The multi-stage Dockerfile follows this structure:
1. Base image: `ubuntu:22.04`
2. Builder stage: Install build deps, compile libecw, install Oracle SDK, compile GDAL with CMake
3. Final stage: Install runtime deps, copy compiled artifacts, configure ldconfig

## Platform Considerations

- Separate Dockerfiles needed for amd64 and arm64
- Different Oracle Instant Client zip files for each platform
- Platform-specific compilation flags (e.g., `--build=aarch64-unknown-linux-gnu` for ARM)

## Related Pages
- [[proj-grid-file-management]] — PROJ configuration for custom grid files
- [[oracle-instant-client-docker]] — Oracle Instant Client installation pattern
- [[gdal-multi-stage-dockerfile]] — Reference implementation
- [[container-image-strategy-for-data-pipelines]] — General container image design
- [[geospatial-etl-pipeline-iceberg]] — Geospatial data ingestion patterns