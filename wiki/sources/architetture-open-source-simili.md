---
type: source
title: Architetture Open Source Simili
authors: [Gemini]
year: 2026
url: ""
venue: "AI-generated research"
tags: [architecture, open-source, data-platform]
related: [data-lakehouse-on-premise-architecture, unbundled-data-architecture]
created: 2026-02-13
updated: 2026-02-13
---
# Architetture Open Source Simili

This source provides a technical research report on building an on-premise, open-source Data Platform for **Regione Liguria**. It explores modular, layered architectures that ensure data sovereignty and scalability, specifically focusing on technologies that can replace proprietary cloud stacks.

## Key Architectural Patterns

The research highlights the importance of a **Modular/Layered Architecture**, organizing the platform into logical tiers:
- **Sources $\rightarrow$ Ingestion $\rightarrow$ Storage $\rightarrow$ Transformation $\rightarrow$ Virtualization $\rightarrow$ Consumption**.

A critical strategic driver identified is the **Unbundled Architecture**, which decouples storage (e.g., [[minio]]) from compute (e.g., [[spark]], [[dremio]]), allowing for independent scaling and cost optimization.

## Technology Stack Components

### Ingestion & Orchestration
- **Streaming:** [[kafka]] for real-time data hubs.
- **Orchestration:** [[airflow]], [[mage]], and [[dbt]] for managing complex ETL/ELT pipelines.
- **Integration:** [[kafka-connect]] for connecting to external RDBMS and APIs.

### Storage & Lakehouse Core
- **Object Storage:** [[minio]] (S3-compatible).
- **Table Format:** [[apache-iceberg]] for ACID transactions and schema evolution.
- **Catalog & Versioning:** [[nessie]] for Git-like data versioning (branching, merging).

### Data Virtualization & Access
- **Primary Engine:** [[dremio]] for creating a semantic layer and unified SQL interface.
- **Alternatives:** [[trino]] and [[apache-drill]] for federated queries.

### Transformation & Analysis
- **Processing:** [[spark]] for large-scale distributed processing.
- **SQL Transformation:** [[dbt]] for modeling and documentation.
- **Interactive Analysis:** [[python]] with [[jupyter]] for data science and geospatial workflows.

### Governance & Catalog
- **Metadata Management:** [[openmetadata-1.12-release-notes]] and [[datahub]] for discovery, lineage, and quality.

### Consumption & BI
- **Visualization:** [[superset]], [[metabase]], and [[grafana]].
- **Open Data:** [[ckan]] for public data dissemination.

### Observability
- **Logging:** [[opensearch]] for centralized monitoring and debugging.
