---
type: source
title: Data Platform Infrastructure Sizing
created: 2026-01-15
updated: 2026-05-07
tags: [infrastructure, sizing, data-platform, architecture]
related: ["data-platform-infrastructure-sizing", "minio", "nessie-catalog-versioning", "dremio-geospatial-limitations", "kestra", "datahub", "openmetadata", "opensearch", "superset", "spark", "apache-zeppelin", "jupyter-notebook", "dremio", "kafka", "pipeline-orchestrator", "erasure-coding-configuration", "bare-metal-vs-containerized-deployment"]
sources: ["Dimensionamento.md"]
---
# Data Platform Infrastructure Sizing

This document provides a detailed, prescriptive hardware sizing blueprint for a complete modern data platform stack. It specifies CPU, RAM, storage, and node counts for each component: MinIO (storage), Project Nessie (catalog versioning), Dremio (query engine), Kafka (event streaming), a pipeline orchestrator (unspecified), a data catalog (DataHub or OpenMetadata), OpenSearch (search/analytics), Superset (visualization), Spark (distributed processing), Apache Zeppelin, and Jupyter Notebook. The sizing represents a concrete architectural decision for the platform's compute and storage resources.

## MinIO

MinIO is the distributed storage layer, providing S3-compatible object storage. It is sized as **4 nodes** with the following per-node configuration:

- **vCPU:** 16
- **RAM:** 32 GB
- **Storage:** 4 × 4 TB NVMe SSDs (16 TB raw per node, 64 TB total)

**Erasure Coding Configuration (16+8):** With a stripe size of 16 data shards and 8 parity shards, the configuration yields:

- **Usable capacity:** 32 TiB (from 64 TiB raw)
- **Storage efficiency:** 50%
- **Fault tolerance:** Up to 8 drive failures or 2 server failures

This is the most critical sizing decision in the platform, as it directly impacts durability and efficiency. The 16+8 scheme provides robust protection for the storage layer while maintaining a reasonable capacity overhead.

## Project Nessie

Project Nessie provides catalog versioning for the data lake. It is a lightweight component:

- **Nodes:** 1
- **vCPU:** 2
- **RAM:** 8 GB
- **Storage:** 50 GB

It can be co-located with other lightweight services.

## Dremio

Dremio is the query engine, consisting of a coordinator and multiple executors. It requires 300–500 GB of distributed storage from MinIO for intermediate results and data caching.

- **Coordinator:** 1 node, 16 vCPU, 32 GB RAM, 200 GB storage
- **Executors:** 3 nodes, each with 16 vCPU, 128 GB RAM, 300 GB storage

## Kafka

Kafka handles event streaming. The cluster includes:

- **Brokers + ZooKeeper:** 3 nodes, each with 12 vCPU, 64 GB RAM, 1 TB storage
- **Workers (Connect, Schema Registry, REST Proxy):** 2 nodes, each with 12 vCPU, 8 GB RAM, 50 GB storage

## Pipeline Orchestrator

The pipeline orchestrator is unspecified; only generic sizing is provided. This represents a placeholder for tools such as Airflow, Kestra, Dagster, or Prefect.

- **Nodes:** 1
- **vCPU:** 2
- **RAM:** 8 GB
- **Storage:** 100 GB

## Data Catalog (DataHub or OpenMetadata)

A choice between DataHub and OpenMetadata is pending; both receive identical sizing:

- **Nodes:** 1
- **vCPU:** 6
- **RAM:** 8 GB
- **Storage:** 50 GB

OpenMetadata offers deployment flexibility: it can be installed bare metal with bundled Elasticsearch/OpenSearch and a database (MySQL or PostgreSQL), eliminating the need for separate services in some cases.

## OpenSearch

OpenSearch provides search and analytics capabilities. The cluster is sized as:

- **Coordinating node:** 1 node, 12 vCPU, 8 GB RAM, 50 GB storage
- **Cluster Manager:** 1 node, 2 vCPU, 8 GB RAM, 50 GB storage
- **Data nodes:** 2 nodes, each with 4 vCPU, 64 GB RAM, 500 GB storage

## Superset

Superset is the visualization layer:

- **Nodes:** 1
- **vCPU:** 2
- **RAM:** 8 GB
- **Storage:** 50 GB

## Spark

Spark provides distributed processing:

- **Nodes:** 4
- **vCPU:** 4 per node
- **RAM:** 16 GB per node
- **Storage:** 100 GB per node

## Apache Zeppelin

Apache Zeppelin is a notebook interface:

- **Nodes:** 1
- **vCPU:** 2
- **RAM:** 8 GB
- **Storage:** 50 GB

## Jupyter Notebook

Jupyter Notebook is another notebook option:

- **Nodes:** 1
- **vCPU:** 2
- **RAM:** 8 GB
- **Storage:** 50 GB

## Open Questions

The following questions remain open and should be addressed as part of the final architectural decisions:

- **Erasure Coding Choice:** Why was the 16+8 configuration chosen over a more storage-efficient 8+4 scheme?
- **Pipeline Orchestrator:** Which specific orchestrator (Airflow, Kestra, Dagster, Prefect) will be adopted?
- **Data Volume Growth:** What is the expected data volume growth rate? This sizing is a static snapshot.
- **Network Topology:** Network throughput, latency, and bandwidth assumptions are not documented and could affect performance.
- **Data Catalog Selection:** The identical sizing for DataHub and OpenMetadata implies a decision is still pending. Each has distinct licensing, feature sets, and operational requirements.

These items should be resolved before final procurement and deployment.