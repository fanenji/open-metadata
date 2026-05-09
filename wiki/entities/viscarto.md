---
type: entity
title: Viscarto
created: 2026-05-06
updated: 2026-05-06
tags: [database, postgis, spatial]
related: [spatial-data-infrastructure, data-lakehouse-on-premise-architecture]
sources: ["BRAINSTOR - Integrazione della Spatial Data Infrastructure (SDI) con la Data Platform (DP).md"]
---
# Viscarto

**Viscarto** is the PostgreSQL/PostGIS database instance used by the Regional Spatial Data Infrastructure (SDI) as an analytical and staging environment.

## Role in the Architecture
- **Staging Area:** Acts as an intermediate repository for data moving from Oracle to the Data Platform.
- **Spatial Engine:** Provides advanced spatial functions (e.g., `ST_Transform` with regional grids) and geometry validation (`ST_IsValid`) that are difficult to replicate in pure Spark environments.
- **Analytical Hub:** Serves as the backend for SDI visualization and analysis tools.

## Integration with Data Platform
In the proposed **Hybrid Optimized Architecture**, Viscarto serves as the source for the Data Platform's ingestion layer. The DP uses Spark via JDBC to read transformed geometries from Viscartary and write them to the Lakehouse.
