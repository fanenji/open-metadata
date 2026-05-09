---
type: entity
title: Geoscript
created: 2026-05-06
updated: 2026-05-06
tags: [etl, legacy, python]
related: [spatial-data-infrastructure, data-ingestion-layer]
sources: ["BRAINSTOR - Integrazione della Spatial Data Infrastructure (SDI) con la Data Platform (DP).md"]
---
# Geoscript

**Geoscript** is the legacy ETL (Extract, Transform, Load) system used by the Regional Spatial Data Infrastructure (SDI) to move and process geospatial data.

## Current State
- **Environment:** Windows Server 2019.
- **Language:** Groovy.
- **Core Engine:** GDAL/OGR.
- **Scheduling:** Windows Task Scheduler.

## Evolution Plan
As part of the Data Platform modernization, Geoscript is being transitioned to a modern stack:
- **Environment:** Ubuntu/Linux.

- **Language:** Python.
- **Core Engine:** Updated GDAL/OGR with Oracle (OCI) and ECW support.
- **Orchestration:** Integration with the Data Platform's orchestrator (e.g., **Airflow** or **Mage**) via SSH or API.
