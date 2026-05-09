---
type: concept
title: SDI-DP Integration Strategy
created: 2026-05-06
updated: 2026-05-07
tags:
  - architecture
  - geospatial
  - ingestion
  - sdi
  - data-platform
  - integration
related:
  - geospatial-data-stack
  - data-lakehouse-on-premise-architecture
  - spatial-data-infrastructure
  - geoscript-system
  - postgis-viscarto
  - oracle-database-sdi
  - geoscript-modernization-plan
  - postgis-to-dp-ingestion
  - raster-ingestion-pipeline
  - legacy-geospatial-etl-pipeline
  - geospatial-etl-pipeline-iceberg
sources:
  - "BRAINSTOR - Integrazione della Spatial Data Infrastructure (SDI) con la Data Platform (DP).md"
  - "Integrazione SDI_DP_ Analisi e Proposte_ .md"
---
# SDI-DP Integration Strategy

The integration of the Spatial Data Infrastructure (SDI) with the Data Platform (DP) is a critical architectural milestone for Regione Liguria. The two systems have overlapping functions — the SDI already contains ETL capabilities and analytical database environments similar to those planned for the DP. The integration strategy defines how the legacy SDI connects to the modern DP.

## Integration Strategies

Three approaches have been identified for vector data ingestion.

### 1. Hybrid Optimized Architecture (Two-Phase Ingestion) — Recommended

This strategy uses a two-phase approach to balance the robustness of existing spatial tools with the scalability of the modern Data Lakehouse.

**Phase 1 (Oracle → PostGIS):** The evolved **Geoscript** (Python/GDAL) copies data from Oracle to PostGIS (`viscarto`). The script reads layer configuration from the Catalogo SIT, builds `ogr2ogr` commands, and executes them. Updates occur via daily scheduling, monthly scheduling, or on-command via SITAR. Orchestration can be via cron on Geoscript or via the DP's orchestrator (Airflow or Mage).

**Phase 2 (PostGIS → DP):** A Spark job reads from PostGIS via JDBC, performs the final CRS transformation to **EPSG:7791** (RDN2008 / UTM zone 32N), and writes to **Apache Iceberg** on **MinIO** in GeoParquet format with Iceberg/GeoIceberg table format. Orchestration is handled by the DP's orchestrator.

**Key Benefits:**
- Leverages existing, proven data copy procedures.
- PostGIS/Viscarto already contains most of the data needed.
- Easy to extend for new layers.
- Geometry validation and CRS transformation using native PostGIS functions.
- Native gridded transformation solves CRS issues within the DP, leveraging PostGIS's ability to handle complex regional coordinate grids, which is a significant technical hurdle in pure Spark/Python environments.

**Disadvantages:**
- Cascading synchronization between Oracle → PostGIS → DP.
- Two-phase process adds latency.

### 2. Direct Ingestion via Geoscript (Oracle → DP)

Data is ingested directly from Oracle to the DP within the Geoscript system, through a parallel process alongside the existing PostGIS feed.

**Advantages:**
- Single process avoids cascading synchronization issues.

**Disadvantages:**
- Requires modifying the legacy Geoscript system.
- Creates parallel processes that must be maintained.
- Loses PostGIS geometry validation and transformation capabilities.

### 3. Native DP Ingestion (Oracle → DP using DP tools)

A direct approach where the Data Platform's tools (Kafka Connect or Spark) ingest data directly from Oracle.

**Key Risk:** High complexity in replicating specialized spatial transformations and coordinate grid support within the DP's compute layer. This is an area open for further evaluation (see Open Questions).

## Geoscript Modernization

A prerequisite for any integration path that uses Geoscript (Strategies 1 and 2) is the modernization of the Geoscript system:
- Migrate from Windows Server 2019 to Ubuntu Linux.
- Replace Groovy scripts with Python.
- Update GDAL/OGR to a modern version with Oracle (OCI) and ECW support.
- Deploy as VM or container.
- Schedule via cron or external orchestrator (e.g., Airflow via SSH operator).

## Raster Data Ingestion

Raster data ingestion occurs within the Geoscript system using Python scripts that:
- Perform CRS transformation via `gdalwarp`.
- Perform format transformation via `gdal_translate`.
- Output data in **Cloud Optimized GeoTIFF (COG)** format to the DP's S3 object storage (MinIO).

## Technical Requirements

- **CRS Standardization:** All incoming spatial data must be reprojected to a unified regional system (**EPSG:7791** / RDN2008 / UTM zone 32N).
- **Orchestration:** Centralized management via **Airflow** or **Mage** to monitor both the SDI and DP phases.
- **Raster Handling:** Use of **Cloud Optimized GeoTIFF (COG)** for all raster data.
- **Geometry Validation:** Leverage native PostGIS functions where possible.

## Open Questions

1. Performance impact of the two-phase approach (latency, throughput).
2. Target CRS for raster COG data (not yet specified).
3. Governance model for the integrated system (data quality checks, metadata synchronization).
4. Whether a third hypothesis (direct Oracle → DP bypassing both PostGIS and Geoscript, similar to Native DP Ingestion) should be evaluated.