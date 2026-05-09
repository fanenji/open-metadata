---
type: concept
title: Data Lakehouse On-Premise Architecture
created: 2026-02-13
updated: 2026-02-13
tags: [architecture, lakehouse, on-premise, sovereignty]
related: [minio, apache-iceberg, nessie, dremio]
sources: ["architetture-open-source-simili.md"]
---
# Data Lakehouse On-Prime Architecture

A **Data Lakehouse On-Premise Architecture** combines the cost-effective, scalable storage of a Data Lake with the ACID transactions and schema management capabilities of a Data Warehouse, all hosted on local infrastructure to ensure **Data Sovereignty**.

## Core Components

The architecture relies on the integration of three key technologies to create a functional Lakehouse:

1.  **[[minio]] (Object Storage):** Acts as the physical storage layer, providing S3-compatible, distributed, and scalable storage for raw and processed datasets.
2.  **[[apache-iceberg]] (Table Format):** Provides the structural layer on top of object storage, enabling features like ACID transactions, schema evolution, and time travel.
3.  **[[nessie]] (Catalog & Versioning):** Serves as the metadata repository, providing "Git-like" capabilities (branching, merging, commits) for the datasets managed by Iceberg.

## Strategic Benefits

- **Data Sovereignty:** By hosting the entire stack on-premise, organizations (like Regione Liguria) can comply with strict regulations such as **NIS2** and **DORA**.
- **Cost Optimization:** Using open-source tools avoids vendor lock-in and high licensing fees associated with proprietary cloud providers.
- **Scalability:** The architecture allows for independent scaling of storage and compute.
