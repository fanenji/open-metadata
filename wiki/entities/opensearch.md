---
type: entity
title: OpenSearch
created: 2026-01-15
updated: 2026-05-07
tags:
  - logging
  - monitoring
  - search
  - analytics
  - infrastructure
  - tool
  - vector-store
  - observability
related:
  - data-platform-infrastructure-sizing
  - rag-for-table-selection
  - pinterest-text-to-sql-architecture
  - kestra
  - dbt
  - dremio
  - gitlab-ci-cd-data-platform
sources:
  - Analisi Architettura.md
  - Dimensionamento.md
  - How we built Text-to-SQL at Pinterest.md
  - Sintesi Architettura (Claude).md
---
# OpenSearch

OpenSearch is an open-source search and analytics suite derived from Elasticsearch. It is a fork of Elasticsearch v7, providing all features free and on-premises. It serves as the centralized log aggregator, monitoring platform, and search and analytics layer for the Regione Liguria Data Platform, providing capabilities to archive and analyze application and system logs for debugging and performance monitoring. It also offers built-in similarity search for embedding vectors, which can be leveraged for tasks such as vector-based table retrieval.

## Data Collection

Metricbeat agents provide push-based metric collection from all platform nodes and components. The platform also aggregates logs from [[kestra]], [[dbt]], [[dremio]], and other components.

## Key Features

- **Full-text Search**: Search across all collected logs and metrics.
- **Alerting**: Configurable alerts based on log patterns and metric thresholds.
- **ML Anomaly Detection**: Machine learning-based detection of unusual patterns in metrics.
- **Dashboard**: Visualization of platform health and performance.
- **Vector Search**: Built-in similarity search for embedding vectors, used for table retrieval in the Text-to-SQL pipeline.

## Role in Architecture

OpenSearch provides cross-cutting observability for the entire platform. It monitors [[kestra]] orchestration flows, [[dbt]] transformation runs, [[dremio]] query performance, and infrastructure health. It is part of the governance and infrastructure layer alongside [[OpenMetadata]] and [[GitLab]].

In the Text-to-SQL feature at Pinterest, OpenSearch was used as the vector store for NLP-based table search. Its similarity search capabilities enable efficient retrieval of relevant tables based on embedding vectors, supporting the natural‑language to SQL translation pipeline.

## Infrastructure Sizing

The recommended deployment consists of three node types:

### Coordinating Node
- 1 node: 12 vCPU, 8 GB RAM, 50 GB storage

### Cluster Manager Node
- 1 node: 2 vCPU, 8 GB RAM, 50 GB storage

### Data Nodes
- 2 nodes: 4 vCPU, 64 GB RAM, 500 GB storage each