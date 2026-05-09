---
type: source
title: "Analisi Architettura Data Platform Regionale"
created: 2026-02-13
updated: 2026-02-13
tags: [data-platform, architecture, review]
authors: [Gemini]
year: 2026
url: "https://gemini.google.com/u/1/app/f39f75edbd440ebf?pageId=none"
venue: "Architectural Review"
sources: ["Analisi Architettura Data Platform Regionale_ .md"]
---
# Analisi Architettura Data Platform Regionale

Architectural review of the "Regione Liguria" Data Platform. This document analyzes the modular, multi-layered system designed to manage the full data lifecycle, from ingestion to consumption.

## Key Components
- **Ingestion & Orchestration**: Kafka, Kafka Connect, NiFi, Airflow, Mage, dbt, Spark.
- **Storage & Data Lake**: MinIO, Apache Iceberg, Project Nessie.
- **Data Virtualization**: Dremio (with Reflections).
- **Governance**: DataHub, OpenMetadata.
- **Consumption**: Superset, Power BI, CKAN, Geospatial stack (DuckDB, Geopandas).

## Critical Findings
- **Complexity**: High integration and operational burden due to many open-source components.
- **Resource Intensity**: High CPU/RAM requirements for Drem-io and Spark.
- **Single Point of Failure**: Dremio is a critical nexus for the platform.
- **Decision Uncertainty**: Orchestrator and Catalog choices are still pending.
