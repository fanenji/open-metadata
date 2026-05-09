---
type: concept
title: Unbundled Data Architecture
created: 2026-02-13
updated: 2026-02-13
tags: [architecture, decoupling, scalability]
related: [minio, spark, dremio]
sources: ["architetture-open-source-simili.md"]
---
# Unbundled Data Architecture

**Unbundled Data Architecture** is a design principle where the storage layer is decoupled from the compute layer. This separation allows each component to be scaled, managed, and optimized independently based on specific workload requirements.

## Key Advantages

- **Independent Scaling:** Compute resources (e.g., [[spark]], [[dremio]]) can be scaled up during heavy processing periods without needing to increase storage capacity. Conversely, storage (e.g., [[minio]]) can grow indefinitely without requiring more CPU/RAM.
- **Cost Efficiency:** Organizations can use cheaper, high-density hardware for storage and high-performance, specialized hardware for compute.
- **Flexary & Flexibility:** Different engines can access the same data stored in a common format (like [[apache-iceberg]]), allowing a "plug-and-play" approach to the technology stack.
- **Workload Optimization:** Specific engines can be chosen for specific tasks (e.g., [[trino]] for federated queries vs. [[spark]] for heavy ETL) without re-architecting the entire platform.
