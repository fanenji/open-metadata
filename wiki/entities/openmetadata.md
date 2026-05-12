---
type: entity
title: OpenMetadata
created: 2026-05-06
updated: 2026-05-10
tags:
  - metadata
  - metadata-management
  - data-governance
  - open-source
  - data-catalog
  - metadata-platform
  - collate
  - governance
  - openmetadata
  - active-metadata
  - data-mesh
  - catalog
related:
  - semantic-context-layer
  - knowledge-graph
  - ontology-explorer
  - data-catalog-comparison
  - model-context-protocol
  - data-virtualization-layer
  - datahub
  - amundsen
  - data-catalog-tool-comparison
  - data-observability-definition
  - apache-airflow
  - elasticsearch
  - data-platform-infrastructure-sizing
  - openmetadata-data-quality
  - openmetadata-mcp-server
  - data-discovery-tools
  - openmetadata-unified-knowledge-graph
  - openmetadata-integration-patterns
  - data-catalog-critique
  - collate
  - openmetadata-dremio-connector
  - active-metadata-platform
  - openmetadata-cloud-vs-os
  - data-mesh
  - data-mesh-maturity-assessment
  - data-mesh-kpis
  - data-product-definition
  - federated-computational-governance
  - openmetadata-permission-limitations
sources:
  - announcing-openmetadata-1-13-20260506.md
  - "Cosa è Openmetadata Unified Knowledge Graph_.md"
  - "Data Observability is Key A Hands-on Comparison of Open Source Data Catalog Tools.md"
  - Dimensionamento.md
  - "Introducing the Model Context Protocol (MCP) in OpenMetadata.md"
  - "Data Quality  OpenMetadata Quality Management Guide.md"
  - "Data Catalog - A Broken Promise.md"
  - Openmetadata Unified Knowledge Graph.md
  - OpenMetadata.md
  - research-data-mesh-organizational-maturity-assessment-2026-05-08.md
  - permission-control-open-metadata-openmetadata-disc-20260510.md
---

# OpenMetadata

OpenMetadata is an open-source active metadata platform with strong governance features for data discovery, observability, and governance. It acts as a **semantic context layer** designed for AI‑ready data teams, maintained by [[Collate]] (which also offers a SaaS solution). Started in mid‑2021, the platform positions itself as an “active metadata platform” with a graph-based architecture. Metadata is not just cataloged but actively used for governance, quality, and discovery. It is the recommended metadata platform for the data platform, and in a specific evaluation it is being considered alongside [[DataHub]] as one of two primary candidates. OpenMetadata provides a centralized repository that unifies metadata from various data assets, moving beyond simple schemas to standardize the meaning of data. The platform provides over 100 pre‑built connectors and a schema‑first architecture.

## Architecture

OpenMetadata operates on a **4‑component system**: API, Ingestion, Search, and UI. In practice, the platform is deployed via two core services:

- **openmetadata-ingestion** – extracts metadata from sources; often orchestrated by [[Apache Airflow]].
- **openmetadata-server** – contains both the backend and frontend components.

Prerequisites include **Elasticsearch** (or OpenSearch) for search and graph indexing, and a relational database (**Postgres** or **MySQL**). While Airflow is recommended for orchestration, it is optional; any orchestration tool can be used.

The platform is designed with a **schema‑first architecture**, prioritizing defined schemas to support massive scalability and customization via APIs, making it suitable for integration with AI agents via [[model-context-protocol]].

### Unified Knowledge Graph

At the core of OpenMetadata is a **Unified Knowledge Graph** that structures metadata with:

- **Nodes** representing entities (datasets, tables, models, pipelines, etc.)
- **Edges** representing relationships (lineage, ownership, dependencies)
- **Ontology Explorer** for visualizing business relationships
- **Glossary Terms & Relations** defining typed relationships (e.g., “calculated from”) for AI reasoning
- **Columns as Assets**: columns are treated as first‑class, discoverable objects

This graph-based approach enables:
- Enhanced data discovery with complete context and lineage visualization
- Scalable queries through keyword search, associations, and lineage tracing
- Governance features like versioning, tags, and compliance enforcement

The [[openmetadata-unified-knowledge-graph]] page provides additional details.

### Metadata Ingestion

OpenMetadata uses a **pull-based mechanism** with over **100 pre‑built connectors** for databases, dashboards, pipelines, ML models, and API services. Ingestion can be configured through the UI (preferred), or via YAML, CLI, or SDK. The platform actively retrieves metadata to ensure consistency with the actual state of data sources. Connectors support scheduled ingestion and real-time updates via webhooks or APIs. In addition to pre‑built connectors, OpenMetadata supports custom integrations; for example, the [[openmetadata-dremio-connector]] enables metadata ingestion from Dremio. Custom connectors can be built using the SDK.

### Metadata Federation

OpenMetadata can act as a federator by ingesting metadata from other data catalog tools, including [[datahub]], [[amundsen]], [[atlas]], [[alation]], and [[collibra]]. This allows organizations to maintain a single‑pane‑of‑glass view for governance without forced migrations. The integration is enabled through its connector library, allowing cross-catalog query and unified lineage across hybrid ecosystems. See [[openmetadata-integration-patterns]] for details.

### Enterprise Architecture

OpenMetadata is built to handle millions of metadata entities and relationships. The MCP server (see below) benefits from the same proven foundation, requiring no separate server cluster or special scaling strategy. Security is handled through bot tokens or Personal Access Tokens (PAT), with the same RBAC and policy engine governing all access.

### Deployment Options

OpenMetadata can be deployed on **Kubernetes** using official **Helm charts**, with a successful deployment on **GKE** (together with Apache Airflow, Elasticsearch, and MySQL) demonstrated. For smaller or non‑Kubernetes environments, the recommended sizing is **1 node with 6 vCPU, 8 GB RAM, and 50 GB storage** for Docker deployments. OpenMetadata also offers a bare‑metal installation where the following components can be co‑located on a single node with the same dimensions:

- OpenMetadata server
- Elasticsearch / OpenSearch
- Database (MySQL or PostgreSQL)

Sizing documentation covers both OpenMetadata and [[DataHub]] without indicating a selection, implying the decision between the two is still pending in the evaluated context.

For organizations considering deployment, two primary options are available: **open‑source (self‑hosted)** and **cloud (managed by Collate)**. The open‑source version is free but requires manual deployment and maintenance, while the cloud version is a paid managed service with SLA and support. The choice between Cloud and Open-Source is a key architectural decision. See [[openmetadata-cloud-vs-os]] for a detailed comparison.

## Key Features

### Active Metadata Platform

Metadata in OpenMetadata is not merely cataloged but actively used to drive governance, data quality, and discovery. The platform enriches metadata with context, lineage, and relationships, enabling proactive data management.

### Unified Knowledge Graph

As described in detail in the Architecture section, the core is a Unified Knowledge Graph that structures metadata as interconnected nodes and edges, enabling enhanced discovery, lineage, and governance. The graph treats columns as first-class assets and supports typed relationships for AI reasoning.

### Data Quality

OpenMetadata provides native quality tests that can be created, deployed, scheduled, and run. The platform includes alerting, a health dashboard, and resolution workflows with failure acknowledgment and remediation. See [[openmetadata-data-quality]] for a detailed guide.

### Column‑Level Lineage

Column‑level lineage is extracted by **parsing SQL statements** of underlying assets, providing detailed visibility into data transformations. Lineage visualization shows data flow across assets with manual drag-and-drop editing for accuracy.

### Data Profiling and PII Detection

Data profiling can be configured by row count or percentage, with **automatic PII tagging** to help identify sensitive data.

### Governance and Collaboration

- **Task assignment** and **approval workflows** for metadata changes
- **Request tags/terms** to facilitate controlled additions
- **Activity feed** providing social network‑like interaction around metadata
- **Authorization** via roles and policies, with hierarchical team structures (Organization, Business Unit, Division, Department, Group)
- **Versioning** and compliance enforcement through the interconnected graph

### Model Context Protocol (MCP) Integration

With the release of enterprise-grade MCP support, OpenMetadata embeds an MCP server directly into the platform. This enables AI assistants and LLMs to interact with the Unified Knowledge Graph through natural language, while inheriting the platform's full RBAC, audit, and governance controls. See [[openmetadata-mcp-server]] for detailed architecture and use cases.

### Search and Discovery

Combines advanced filters, profiling, and relationships for contextual asset location. The graph-based architecture enables scalable queries through keyword search, associations, and lineage tracing. See also [[data-discovery-tools]].

### Custom Connectors

In addition to over 100 pre‑built connectors, OpenMetadata supports custom integrations tailored to specific data sources. For example, the [[openmetadata-dremio-connector]] enables metadata ingestion from Dremio. Custom connectors can be built using the OpenMetadata SDK or by extending the ingestion framework.

## Strengths

- **Superior governance features**: task assignment, approval workflows, PII detection
- **Excellent user experience**: intuitive UI‑based ingestion configuration with interactive documentation
- **Simple architecture**: fewer components compared to [[DataHub]]
- **Collaboration features**: activity feed and social interaction around metadata
- **Unique MCP integration**: enterprise-grade MCP server for AI-driven metadata access

## Weaknesses

- **Open‑source future uncertain**: roadmap indicates increasing focus on SaaS (Collate)
- **Authorization limitations**: does not yet support groups from external authentication providers
- **Upgrade process**: requires manual steps and detailed documentation
- **Permission visibility (pre-v1.6)**: unauthorized users can see asset existence in Explore even without access; search-based RBAC was planned for v1.6. See [[openmetadata-permission-limitations]] and the [[#Limitations]] section for details.

## Limitations

### Permission Control (pre-v1.6)

OpenMetadata (pre-v1.6) cannot hide data assets from the Explore tab UI. Policies can restrict *access* to assets but not *visibility*. This means unauthorized users can see the existence of tables, databases, and other assets they cannot access. See [[openmetadata-permission-limitations]] for details.

**Planned Solution:** Search-based RBAC was scheduled for OpenMetadata v1.6.

## Comparison

OpenMetadata competes with [[datahub]] and [[amundsen]] in the open-source data catalog space. Its MCP integration gives it a unique advantage for AI-driven metadata access, while its governance and collaboration features distinguish it from simpler catalog tools. For a critique of how OpenMetadata addresses common catalog limitations, see [[data-catalog-critique]]. See also [[data-catalog-tool-comparison]] for a detailed evaluation.

## Data Mesh Enablement

OpenMetadata is referenced in the [[data-mesh-maturity-assessment]] as a tool for publishing and discovering [[data-product-definition|data products]], a key indicator of data accessibility/discoverability maturity, and a platform for [[federated-computational-governance]] enforcement. It is one of several data catalog tools (alongside [[datahub]] and [[amundsen]]) that serve as maturity indicators in the [[data-mesh-kpis]].

## Related Pages

- [[openmetadata-unified-knowledge-graph]]
- [[openmetadata-integration-patterns]]
- [[data-catalog-critique]]
- [[data-discovery-tools]]
- [[data-catalog-tool-comparison]]
- [[openmetadata-data-quality]]
- [[openmetadata-mcp-server]]
- [[collate]]
- [[openmetadata-dremio-connector]]
- [[active-metadata-platform]]
- [[openmetadata-cloud-vs-os]]
- [[data-mesh]]
- [[data-mesh-maturity-assessment]]
- [[data-mesh-kpis]]
- [[data-product-definition]]
- [[federated-computational-governance]]
- [[openmetadata-permission-limitations]]