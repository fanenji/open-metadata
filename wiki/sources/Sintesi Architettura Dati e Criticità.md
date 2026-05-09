---
type: source
title: "Source: Sintesi Architettura Dati e Criticità.md"
created: 2026-05-07
updated: 2026-05-07
sources: ["Sintesi Architettura Dati e Criticità.md"]
tags: []
related: []
---

# Source: Sintesi Architettura Dati e Criticità.md

# Structured Analysis: Sintesi Architettura Dati e Criticità

## Key Entities

| Name | Type | Role | In Wiki? |
|------|------|------|----------|
| **MinIO** | Product (Object Storage) | Central — physical storage layer for Data Lake | No |
| **Apache Iceberg** | Product (Table Format) | Central — ACID transactions, schema evolution, time travel | Yes ([[iceberg-table-versioning]], [[iceberg-geospatial-support]]) |
| **Project Nessie** | Product (Table Catalog) | Central — Git-like versioning for Iceberg tables | Yes ([[nessie-catalog-versioning]]) |
| **Dremio** | Product (Query Engine) | Central — SQL interface, virtualization, security enforcement | Yes ([[dremio]], [[dremio-geospatial-limitations]]) |
| **Kafka / Kafka Connect** | Product (Streaming) | Central — ingestion decoupling and streaming | No |
| **Airflow** | Product (Orchestrator) | Central — pipeline orchestration candidate | No |
| **Mage** | Product (Orchestrator) | Peripheral — younger alternative to Airflow | No |
| **dbt** | Product (Transformation) | Central — SQL transformation orchestration | Yes (multiple pages) |
| **Spark** | Product (Processing) | Central — distributed processing for complex transforms | No |
| **DataHub** | Product (Catalog) | Peripheral — under evaluation for catalog/governance | Yes ([[datahub]]) |
| **OpenMetadata** | Product (Catalog) | Peripheral — under evaluation for catalog/governance | Yes ([[openmetadata]]) |
| **Superset** | Product (BI) | Central — BI and dashboarding | No |
| **Power BI** | Product (BI) | Central — BI and dashboarding | No |
| **CKAN** | Product (Open Data Portal) | Central — open data publication | No |
| **OpenSearch** | Product (Logging) | Central — log aggregation and monitoring | No |
| **GDAL** | Tool (Geospatial) | Peripheral — geospatial format conversion | Yes ([[oracle-to-postgresql-gdal-etl]]) |
| **DuckDB** | Product (Query Engine) | Peripheral — geospatial analysis | Yes ([[duckdb]]) |
| **Geopandas** | Library | Peripheral — geospatial analysis in Python | No |
| **Leafmap** | Library | Peripheral — geospatial visualization | No |
| **deck.gl** | Library | Peripheral — geospatial visualization | No |
| **WSO2** | Product (API Gateway) | Peripheral — API gateway integration | No |

## Key Concepts

| Concept | Definition | Why It Matters | In Wiki? |
|---------|------------|----------------|----------|
| **Three-Layer Architecture** | Logical separation into Sources, Core, Consumption | Foundational design pattern for the entire platform | No |
| **ELT Pattern** | Extract-Load-Transform paradigm | Core processing model for the platform | Yes ([[elt-pattern]]) |
| **Medallion Architecture** | Bronze → Silver → Gold data refinement stages | Implicit in transformation layer description | Yes ([[data-quality-certification-vs-usability-certification]]) |
| **Data Virtualization** | Unified SQL interface abstracting physical storage | Dremio's primary role in the architecture | Yes ([[data-virtualization-pattern]]
