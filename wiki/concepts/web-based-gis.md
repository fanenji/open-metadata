---
type: concept
title: Web-based GIS
created: 2026-04-29
updated: 2026-04-29
tags: [gis, web, geospatial, jupyter]
related: [jupytergis, jupyterlab]
sources: ["JupyterGIS.md"]
---
# Web-based GIS

Web-based GIS refers to Geographic Information System tools that run entirely in a web browser rather than as desktop applications. [[JupyterGIS]] represents a new generation of web-based GIS tools that combine browser-based accessibility with collaborative editing capabilities.

## Advantages

- No installation required for end users
- Integration with notebook-based workflows (Jupyter)
- Multi-window and multi-device operation
- Plugin extensibility
- Centralized updates and maintenance

## Relationship to Existing Wiki

The existing wiki covers backend geospatial processing ([[dremio]], [[duckdb]], [[iceberg-table-versioning]], [[geoparquet-vs-iceberg-metadata]]). Web-based GIS tools like JupyterGIS provide the frontend visualization and authoring layer that could consume data from these backend systems.