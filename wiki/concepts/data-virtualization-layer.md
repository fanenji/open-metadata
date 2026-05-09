---
type: concept
title: Data Virtualization Layer
created: 2026-02-13
updated: 2026-02-13
tags: [architecture, abstraction]
related: [dremio, trino, apache-iceberg]
sources: ["Analili Architettura Data Platform Regionale_ .md"]
---
# Data Virtualization Layer

The Data Virtualization Layer provides a unified SQL interface across heterogeneous sources, abstracting the physical storage complexity from the end users and BI tools.

## Key Functions
- **Unified Access**: Accessing data in the [[data-storage-layer]] (MinIO, Iceberg) and external databases through a single interface.
- **Semantic Modeling**: Defining business logic via Virtual Datasets (VDS).
- **Performance Optimization**: Utilizing caching or materialized views to reduce latency.
