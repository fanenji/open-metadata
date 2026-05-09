---
type: entity
title: PROJ Grid File Management
created: 2026-04-29
updated: 2026-04-29
tags: [proj, gdal, geospatial, docker, grid-files]
related: [gdal-docker-build-strategy, oracle-instant-client-docker, gdal-multi-stage-dockerfile, dremio-geospatial-limitations]
sources: ["ETL - CONVERSAZIONI LLM.md"]
---
# PROJ Grid File Management

Best practices for adding custom PROJ grid shift files (`.gsb`) to containerized environments without breaking the PROJ installation.

## The Problem

Mounting a custom directory to `/usr/share/proj` replaces the `proj.db` database file, causing PROJ to fail with errors like:
```
ERROR 1: PROJ: proj_create_from_database: /usr/share/proj/proj.db lacks DATABASE.LAYOUT.VERSION.MAJOR / DATABASE.LAYOUT.VERSION.MINOR metadata.
```

## The Solution: PROJ_DATA Environment Variable

The correct approach is to:
1. Mount custom grid files to a **separate** directory (e.g., `/opt/proj-custom-grids`)
2. Set the `PROJ_DATA` environment variable with colon-separated paths including both the default PROJ data directory and the custom directory

### Docker Run Example
```bash
docker run -d \
  -v /path/to/custom-grids:/opt/proj-custom-grids:ro \
  -e PROJ_DATA="/usr/share/proj:/opt/proj-custom-grids" \
  your-gdal-image:tag
```

### Docker Compose Example
```yaml
services:
  gdal-service:
    image: your-gdal-image:with-proj8
    volumes:
      - ./custom-proj-grids:/opt/proj-custom-grids:ro
    environment:
      PROJ_DATA: "/usr/share/proj:/opt/proj-custom-grids"
```

### Custom Docker Image
```dockerfile
FROM your-gdal-image:tag
RUN mkdir -p /opt/proj-custom-grids
COPY *.gsb /opt/proj-custom-grids/
ENV PROJ_DATA="/usr/share/proj:/opt/proj-custom-grids"
```

## Verification

- Use `projinfo` to check if a CRS transformation requires the grid file
- Use `cs2cs` to test transformations that depend on the grid
- Set `PROJ_DEBUG=3` for verbose logging

## Related Pages
- [[gdal-docker-build-strategy]] — GDAL Docker build patterns
- [[oracle-instant-client-docker]] — Oracle client installation
- [[gdal-multi-stage-dockerfile]] — Multi-stage build reference
- [[dremio-geospatial-limitations]] — Dremio spatial query challenges