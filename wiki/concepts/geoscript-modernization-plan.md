---
type: concept
title: Geoscript Modernization Plan
created: 2026-02-13
updated: 2026-02-13
tags: [sdi, etl, modernization, geospatial]
related: [geoscript-system, sdi-dp-integration-strategy, legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl]
sources: ["Integrazione SDI_DP_ Analisi e Proposte_ .md"]
---
# Geoscript Modernization Plan

The Geoscript system, the existing ETL system within the SDI of Regione Liguria, requires modernization to address critical technical debt and enable effective integration with the Data Platform.

## Current State

- **OS**: Windows Server 2019
- **Language**: Groovy
- **Libraries**: GDAL/OGR (obsolete version)
- **Scheduling**: Windows Task Scheduler
- **Configuration**: Complex GDAL/OGR setup on Windows

## Target State

- **OS**: Ubuntu Linux
- **Language**: Python
- **Libraries**: GDAL/OGR with Oracle (OCI) and ECW support
- **Deployment**: VM or containerized
- **Scheduling**: cron or external orchestrator (e.g., Airflow via SSH operator)

## Benefits

- Simplified GDAL/OGR configuration and maintenance.
- Access to modern Python ecosystem for geospatial processing.
- Better monitoring and observability options.
- Easier integration with modern orchestration tools.
- Containerization enables reproducible environments.

## Prerequisites for Integration

The modernization is a prerequisite for both integration hypotheses:
- **Hypothesis 1**: Modernized Geoscript continues to handle Oracle → PostGIS phase.
- **Hypothesis 2**: Modernized Geoscript handles direct Oracle → DP ingestion.