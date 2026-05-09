type: concept
title: Data Storage Layer
created: 2026-05-22
updated: 2026-05-22
tags: [storage, data-lake, virtualization]
related: [dremio, nessie, minio]
sources: ["AMBIENTI.md"]
---
# Data Storage Layer

The data storage layer is a multi-tiered architecture combining object storage, data cataloging, and data virtualization to create a scalable and governed data lake.

## Components
- **Physical Storage (Minio)**: An S3-compatible object storage layer that serves as the physical substrate for all data.
- **Data Catalog (Nessie)**: Provides the versioning and metadata management layer, enabling Git-like operations on the data stored in Minio.
- **Data Virtualization (Dremio)**: The engine that sits atop Nessie and Minio, providing a semantic layer (VDS) and high-performance query execution.

## Environment Configuration
The storage layer is partitioned to match the compute environment isolation:
- **Development Stack**: A single Dremio instance pointing to a Nessie catalog backed by a specific Minio bucket.
- **Production Stack**: Two separate Dremio instances (Production and Staging), each pointing to its own independent Nessie catalog and Minio bucket.

This configuration ensures that the **Production** environment is physically and logically isolated from **Staging** and **Development**.
