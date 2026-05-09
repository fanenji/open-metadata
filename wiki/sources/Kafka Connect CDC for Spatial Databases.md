---
type: source
title: "Source: Kafka Connect CDC for Spatial Databases.md"
created: 2026-05-07
updated: 2026-05-07
sources: ["Kafka Connect CDC for Spatial Databases.md"]
tags: []
related: []
---

# Source: Kafka Connect CDC for Spatial Databases.md

## Analysis of: Kafka Connect CDC for Spatial Databases.md

### Key Entities

| Name | Type | Role | In Wiki? |
|------|------|------|----------|
| **Kafka Connect** | Framework | Central — the core integration platform for CDC | No |
| **Confluent Oracle CDC Source Connector** | Tool/Connector | Central — captures Oracle changes via LogMiner | No |
| **Debezium PostgreSQL Connector** | Tool/Connector | Central — captures PostGIS changes via logical decoding | No |
| **Oracle 11g Spatial** | Database | Central — source database with SDO_GEOMETRY | No |
| **PostgreSQL/PostGIS** | Database | Central — source database with geometry type | Yes ([[oracle-to-postgresql-gdal-etl]], [[legacy-geospatial-etl-pipeline]]) |
| **Oracle LogMiner** | Technology | Peripheral — mechanism for Oracle CDC | No |
| **pgoutput** | Plugin | Peripheral — logical decoding plugin for PostgreSQL | No |
| **JTS (Java Topology Suite)** | Library | Peripheral — for WKB parsing in consumers | No |

### Key Concepts

| Concept | Definition | Why It Matters | In Wiki? |
|---------|------------|----------------|----------|
| **Change Data Capture (CDC)** | Capturing real-time data modifications from database transaction logs | Enables event-driven geospatial pipelines | No |
| **SDO_GEOMETRY handling** | Oracle's spatial data type; unclear serialization in Kafka | Critical unknown for Oracle CDC pipeline | No |
| **PostGIS geometry representation** | Debezium represents geometry as STRUCT(srid, wkb) | Well-defined, enabling reliable consumer development | No |
| **Logical decoding** | PostgreSQL feature for streaming row-level changes | Foundation for Debezium PostgreSQL connector | No |
| **LogMiner** | Oracle utility for reading redo logs | Required for Oracle CDC connector operation | No |

### Main Arguments & Findings

- **Core claim**: CDC with Kafka Connect is feasible for both Oracle 11g Spatial and PostgreSQL/PostGIS, but with significantly different maturity levels.
- **Evidence**: Debezium PostgreSQL connector has explicit PostGIS support with documented STRUCT format. Confluent Oracle CDC connector lacks explicit SDO_GEOMETRY documentation.
- **Strength**: Moderate — the PostGIS path is well-documented and reliable; the Oracle path is speculative and requires empirical testing.
- **Key finding**: Confluent's Oracle 11g support ends June 30, 2025, making this approach time-limited for production use.

### Connections to Existing Wiki

- **[[legacy-geospatial-etl-pipeline]]** — The current Oracle → GDAL → PostgreSQL pipeline could be replaced or augmented by this CDC approach.
- **[[oracle-to-postgresql-gdal-etl]]** — Directly related; CDC offers a real-time alternative to batch ETL.
- **[[elt-pattern]]** — CDC aligns with modern ELT patterns by streaming raw changes before transformation.
- **[[stream-processing-ingestion]]** — CDC is a specific implementation of stream processing for database changes.
- **[[data-ingestion-architectural-patterns]]** — CDC fits within t
