---
type: concept
title: PROJ_DATA Environment Variable
created: 2026-04-29
updated: 2026-04-29
tags: [proj, gdal, geospatial, environment-variable, grid-files]
related: [proj-grid-file-management, gdal-docker-build-strategy, dremio-geospatial-limitations]
sources: ["ETL - CONVERSAZIONI LLM.md"]
---
# PROJ_DATA Environment Variable

The `PROJ_DATA` environment variable controls where the PROJ library searches for its data files, including the `proj.db` database and grid shift files (`.gsb`, `.gtx`). It is the canonical method for adding custom grid files to a PROJ installation without breaking the core database dependency.

## Usage

The variable takes a colon-separated list of directory paths (semicolon-separated on Windows). PROJ searches each directory in order for needed resource files.

```bash
export PROJ_DATA="/usr/share/proj:/opt/proj-custom-grids"
```

## Why Not Mount to /usr/share/proj

Mounting a custom directory to `/usr/share/proj` replaces the entire directory, including the `proj.db` SQLite database. This database contains metadata about projections, transformations, and grid file locations. If the mounted directory lacks a compatible `proj.db`, PROJ cannot initialize and returns errors like:

```
ERROR 1: PROJ: proj_create_from_database: /usr/share/proj/proj.db lacks DATABASE.LAYOUT.VERSION.MAJOR / DATABASE.LAYOUT.VERSION.MINOR metadata.
```

## Best Practices

1. Mount custom grid files to a separate directory (e.g., `/opt/proj-custom-grids`)
2. Do NOT place a `proj.db` file in the custom directory
3. Set `PROJ_DATA` to include both the default PROJ data directory and the custom directory
4. Use read-only mounts (`:ro`) for safety

## Related Pages
- [[proj-grid-file-management]] — Complete guide for grid file management
- [[gdal-docker-build-strategy]] — GDAL Docker build patterns
- [[dremio-geospatial-limitations]] — Dremio spatial query challenges