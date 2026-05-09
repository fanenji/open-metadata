---
type: entity
title: JupyterGIS
created: 2026-04-29
updated: 2026-04-29
tags: [jupyter, gis, collaborative-editing, geospatial, tool]
related: [yjs-framework, sylvain-corlay, quantstack, simula-research-lab, jupytercad, jupyterlab]
sources: ["JupyterGIS.md"]
---
# JupyterGIS

JupyterGIS is a web-based, open-source Geographic Information System (GIS) tool being developed as a JupyterLab extension. It is funded by the European Space Agency (ESA) and led by a consortium of [[QuantStack]] and [[Simula Research Lab]].

## Key Features

- **Collaborative editing**: Built from the ground up with [[Yjs framework]] (CRDT-based) for real-time multi-user editing — the first open-source GIS tool to offer this.
- **Web-based**: Runs entirely in the browser, leveraging the [[JupyterLab]] application framework for extensibility, keyboard shortcuts, theming, and multi-window support.
- **Notebook integration**: GIS capabilities will be available inline in Jupyter notebooks via the display system, following the same architecture as [[JupyterCAD]].
- **QGIS project file support**: Will support collaborative editing of QGIS project files.

## Architecture

JupyterGIS is built as a JupyterLab extension, reusing the collaborative editing infrastructure developed for JupyterLab core over the past three years. The data model is designed from inception around CRDT data structures to avoid the difficulty of retrofitting collaboration into an existing application.

## Target Integrations

- [[Copernicus Data Space Ecosystem (CDSE)]]
- [[European Open Science Cloud (EOSC)]]

## Relationship to Existing Wiki

JupyterGIS operates at the frontend/UI layer of the geospatial stack, complementing the existing wiki content on backend data processing ([[dremio]], [[duckdb]], [[iceberg-table-versioning]], [[geoparquet-vs-iceberg-metadata]]). It could serve as a visualization and authoring frontend for data processed through the [[geospatial-etl-pipeline-iceberg]].