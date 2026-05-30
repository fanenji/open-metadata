---
type: source
title: "Source: oracle-connector-openmetadata-enterprise-database--20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["oracle-connector-openmetadata-enterprise-database--20260514.md"]
tags: []
related: []
---

# Source: oracle-connector-openmetadata-enterprise-database--20260514.md

## Analysis of: Oracle Connector | OpenMetadata Enterprise Database Guide

### Key Entities

- **Oracle Database (12c, 18c, 19c, 21c)** — Central entity; the source system from which metadata is ingested. Supported versions are explicitly listed.
- **python-oracledb** — Python library used by the connector to interface with Oracle. Role: technical dependency.
- **OpenMetadata** — The platform ingesting metadata. Role: consumer/recipient.
- **Hybrid Ingestion Runner** — Peripheral; mentioned only in the context of secret management for sensitive credential fields.
- **AutoPilot** — Peripheral; mentioned as an automatic workflow handler for usage, lineage, etc.

**Existing wiki check:** `oracle-connector` already exists in the wiki index. `python-oracledb` does not appear. `Hybrid Ingestion Runner` and `AutoPilot` are not in the index.

### Key Concepts

- **Oracle Connection Type** — Choice between `Oracle Service Name` (TNS alias) and `Database Schema`. Critical for correct connectivity.
- **Oracle Instant Client** — Thick client binaries required for connection; provided by default at `/instantclient` in the ingestion Docker image. ARM and AMD binaries are shipped for version 19.
- **SELECT_CATALOG_ROLE** — Oracle system privilege granting read-only access to data dictionaries; required for metadata ingestion.
- **Schema-level SELECT limitation** — Explicitly noted: "there is no routine out of the box in Oracle to grant SELECT to a full schema." This is a known Oracle limitation.
- **Filter Patterns** — Database, schema, and table inclusion/exclusion via regex; standard OpenMetadata ingestion control.
- **Incremental Metadata Extraction (Beta)** — Only available for BigQuery, Redshift, and Snowflake; explicitly not supported for Oracle.
- **Soft Deletion** — `Mark Deleted Tables` and `Mark Deleted Tables from Filter Only` toggles; standard feature.

**Existing wiki check:** `oracle-schema-select-limitation` already exists. `oracle-connector` already exists. `filter-patterns` and `soft-deletion` exist. `incremental-metadata-extraction` does not exist as a separate page.

### Main Arguments & Findings

- **Core claim:** The Oracle connector supports metadata ingestion, query usage, data profiling, data quality, dbt, lineage (including column-level), stored procedures, sample data, and auto-classification. It does **not** support Owners or Tags ingestion.
- **Evidence:** The feature list table at the top of the document explicitly marks Owners and Tags as ✕ (not supported).
- **Strength:** High; this is official documentation.

### Connections to Existing Wiki

- **Strengthens:** `oracle-connector` page — this source provides the detailed procedural content that the existing wiki page summarizes.
- **Extends:** `oracle-schema-select-limitation` — the source explicitly confirms the limitation and provides the exact SQL grant syntax for workarounds.
- **Related:** `filter-patterns`, `soft-deletion`, `metadata-ingestion-workflow`, `service-connection`
