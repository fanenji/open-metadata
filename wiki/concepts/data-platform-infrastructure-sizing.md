---
type: concept
title: Data Platform Infrastructure Sizing
created: 2026-04-29
updated: 2026-04-29
tags: [infrastructure, sizing, capacity-planning]
related: [minio, nessie-catalog-versioning, dremio-geospatial-limitations, kestra, datahub, openmetadata, opensearch, superset, spark, apache-zeppelin, jupyter-notebook, erasure-coding-configuration]
sources: ["Dimensionamento.md"]
---
# Data Platform Infrastructure Sizing

This concept page consolidates the hardware specifications for the complete data platform stack, organized by component. The sizing is prescriptive and actionable for procurement and deployment.

## Component Summary

| Component | Nodes | vCPU (total) | RAM (total) | Storage (total) |
|-----------|-------|--------------|-------------|-----------------|
| MinIO | 4 | 64 | 128 GB | 64 TB raw (32 TiB usable) |
| Project Nessie | 1 | 2 | 8 GB | 50 GB |
| Dremio Coordinator | 1 | 16 | 32 GB | 200 GB |
| Dremio Executor | 3 | 48 | 384 GB | 900 GB |
| Kafka Broker+Zookeeper | 3 | 36 | 192 GB | 3 TB |
| Kafka Worker | 2 | 24 | 16 GB | 100 GB |
| Pipeline Orchestrator | 1 | 2 | 8 GB | 100 GB |
| DataHub / OpenMetadata | 1 | 6 | 8 GB | 50 GB |
| OpenSearch Coordinating | 1 | 12 | 8 GB | 50 GB |
| OpenSearch Manager | 1 | 2 | 8 GB | 50 GB |
| OpenSearch Data | 2 | 8 | 128 GB | 1 TB |
| Superset | 1 | 2 | 8 GB | 50 GB |
| Spark | 4 | 16 | 64 GB | 400 GB |
| Apache Zeppelin | 1 | 2 | 8 GB | 50 GB |
| Jupyter Notebook | 1 | 2 | 8 GB | 50 GB |

## Key Design Decisions

- **MinIO Erasure Coding**: Stripe size 16, parity 8 yields 50% storage efficiency but high failure tolerance (8 drives, 2 servers).
- **Dremio Distributed Storage**: 300-500 GB sourced from MinIO — must be included in usable capacity planning.
- **Data Catalog**: Both DataHub and OpenMetadata are sized but no selection is indicated.
- **Pipeline Orchestrator**: Tool is unspecified — sizing is generic.
- **OpenMetadata Bare Metal**: Can co-locate server, search engine, and database on a single node.

## Open Questions

- Which Data Catalog (DataHub vs. OpenMetadata) is selected?
- Which Pipeline Orchestrator is used?
- Is the Dremio distributed storage included in the MinIO usable capacity calculation (32 TiB)?
- What is the expected data growth rate?