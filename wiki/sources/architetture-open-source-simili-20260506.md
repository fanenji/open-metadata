---
type: source
title: Architetture Open Source Simili
created: 2026-05-06
updated: 2026-05-06
tags: [architecture, open-source, data-platform]
related: [data-lakehouse-on-premise-pattern, unbundled-data-architecture, data-sovereignty-strategy]
sources: ["Architetture Open Source Simili_ -20260506.md"]
authors: [Gemini]
year: 2026
url: ""
venue: ""
---
# Architetture Open Source Simili

This source provides a detailed architectural research report regarding the feasibility of an entirely open-source, on-premise Data Platform for "Regione Liguria". 

The document outlines a modular, layered architecture (Sources, Core, Consumption) and evaluates various open-source technologies for:
- **Ingestion & Orchestration**: Kafka, Airflow, Mage, dbt, and Spark.
- **Storage & Lakehouse**: MinIO (Object Storage), Apache Iceberg (Table Format), and Project Nessie (Versioning).
- **Data Virtualization**: Dremio, Trino, and Apache Drill.
- **Governance & Cataloging**: DataHub and OpenMetadata.
- **Consumption & BI**: Apache Superset, Power BI (noted as a potential tension), and CKAN.
- **Observability**: OpenSearch.

Key findings include the strategic importance of **Data Sovereignty**, the efficiency of the **Unbundled Data Architecture** (decoupling storage and compute), and the robustness of the **Lakehouse pattern** using MinIO, Ice/Iceberg, and Nessie.