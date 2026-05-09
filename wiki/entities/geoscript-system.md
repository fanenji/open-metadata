---
type: entity
title: Geoscript System
created: 2026-02-13
updated: 2026-02-13
tags: [sdi, etl, geospatial, legacy]
related: [legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, sdi-dp-integration-strategy, geoscript-modernization-plan]
sources: ["Integrazione SDI_DP_ Analisi e Proposte_ .md"]
---
# Geoscript System

The Geoscript system is the existing ETL system within the Spatial Data Infrastructure (SDI) of Regione Liguria. It uses Groovy scripts with GDAL/OGR to perform format and coordinate reference system (CRS) transformations, running on a Windows Server 2019 machine (srvcarto.regione.liguria.it) scheduled via Windows Task Scheduler.

## Criticalities

- **Windows Environment**: Preference for Ubuntu Linux for better compatibility and management.
- **Groovy Language**: Preference for Python scripts for maintainability and ecosystem.
- **Outdated GDAL/OGR**: Version is obsolete, missing modern features and optimizations.
- **Complex GDAL/OGR Configuration on Windows**: Difficult to set up and maintain.
- **Pipeline Monitoring Difficulty**: Lack of visibility into ETL process health and performance.

## Modernization Plan

The proposed evolution migrates the Geoscript system to an Ubuntu/Python environment with:
- GDAL/OGR with Oracle (OCI) and ECW support
- Python as the scripting language
- VM or containerized deployment
- Scheduling via cron or external orchestrator (e.g., Airflow via SSH operator)

## Role in SDI-DP Integration

The Geoscript system is central to both integration hypotheses:
- **Hypothesis 1**: Geoscript continues to copy data from Oracle to PostGIS (Phase 1), while Phase 2 (PostGIS to DP) is handled by the DP's orchestration.
- **Hypothesis 2**: Geoscript creates a parallel process to write directly to the DP's object storage, alongside the existing PostGIS feed.