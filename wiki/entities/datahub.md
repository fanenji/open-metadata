---
type: entity
title: DataHub
created: 2026-04-29
updated: 2026-05-08
tags: [data-catalog, open-source, metadata-platform, linkedin, metadata, data-platform-infrastructure-sizing, data-mesh, catalog]
related: [openmetadata, amundsen, data-catalog-tool-comparison, data-observability-definition, great-expectations-for-data-contracts, apache-kafka, elasticsearch, data-platform-infrastructure-sizing, data-mesh, data-mesh-maturity-assessment, data-mesh-kpis, data-product-definition]
sources: ["Data Observability is Key A Hands-on Comparison of Open Source Data Catalog Tools.md", "Dimensionamento.md", "research-data-mesh-organizational-maturity-assessment-2026-05-08.md"]
---
# DataHub

DataHub is an event-based open-source metadata platform originally developed by LinkedIn and released in early 2020. It is now primarily maintained by Acryl, which also offers a SaaS version. DataHub is one of the three major open-source data catalog tools, alongside [[OpenMetadata]] and [[Amundsen]], and is one of two options being evaluated for the data platform.

## Architecture

DataHub has the most complex architecture among the compared tools, built on an event-driven model using [[Apache Kafka]] for communication between components. Key components include:

- **Relational database** (MySQL, Postgres, or MariaDB) as the source of truth for metadata
- **Elasticsearch** for search and optionally as a graph index
- **Apache Kafka** as the message broker for event-based communication
- **Backend services**: Metadata Change Event (MCE) consumer and Metadata Audit Event (MAE) consumer
- **Frontend** communicating with the backend via GraphQL

## Key Features

- **Metadata ingestion** via UI (cron-scheduled) or YAML recipes via CLI/SDK
- **Table lineage** extraction using SQL parser, DDL statements, or job logs (e.g., BigQuery)
- **Column-level lineage** (added in recent releases)
- **Profiling** as part of ingestion recipes, with configurable metrics and partition-aware processing
- **Testing** via [[great-expectations-for-data-contracts|Great Expectations]] integration (external test execution, results reported via REST API)
- **Authorization** with roles, policies, and fine-grained access control based on teams, domains, or other levels
- **File-based lineage definition** and programmatic ingestion

## Infrastructure Sizing

For a containerized Docker deployment, the recommended sizing is 1 node with 6 vCPU, 8 GB RAM, and 50 GB storage. This sizing is provided alongside that of OpenMetadata, indicating that a final decision between the two tools is pending.

## Data Mesh Context

DataHub is referenced in the [[data-mesh-maturity-assessment]] as:

- A tool for publishing and discovering [[data-product-definition|data products]]
- A key indicator of data accessibility/discoverability maturity
- A source of implementation guidance for data mesh

DataHub is one of several data catalog tools (alongside [[OpenMetadata]] and [[Amundsen]]) that serve as maturity indicators in the [[data-mesh-kpis]].

## Strengths

- Highly extensible and customizable due to event-driven architecture
- Strong community-driven development model
- Automated upgrades via Kubernetes jobs for Kafka, Elasticsearch, SQL DB, and system migration
- Supports a wide range of connectors with varying maturity levels

## Weaknesses

- Most complex architecture, requiring Kafka and multiple services
- UI-based ingestion configuration is less polished than OpenMetadata's
- Some features (e.g., advanced metadata tests) are only available in the SaaS version

## Deployment

DataHub can be deployed on Kubernetes using official Helm charts. The authors successfully deployed it on GKE with MySQL, Kafka, and Elasticsearch.