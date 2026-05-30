---
type: query
title: "Research: Capture Referenced Design Page"
created: 2026-05-15
origin: deep-research
tags: [research]
---

# Research: Capture Referenced Design Page

---
type: architecture
title: OpenMetadata System Architecture and Design
tags: [architecture, design, schema-first, system]
related: [openmetadata-system-architecture, schema-first-approach, jsonschemas, unified-metadata-graph]
---

# OpenMetadata System Architecture and Design

This page synthesizes the official "Design" and "Architecture" documentation into a single, comprehensive reference. OpenMetadata is purpose-built on a **Schema-First** and **API-First** architecture, centered around a unified metadata model that ensures consistency across the backend, ingestion pipelines, and user interface. [1][8]

## Core Design Principles

- **Unified Metadata Model & Schema-First Approach** — All metadata entities are defined in [[jsonschemas]], serving as the single source of truth for the platform's vocabulary and structure. [1][2]
- **Three Views from One Source:** The same JSON Schema definitions are used to auto-generate:
    - **Java Classes** for the [[dropwizard]] / [[jetty]] backend REST API.
    - **Python Classes** for the [[ingestion-framework]] and its connectors.
    - **TypeScript Types** for the UI. [1][10]
- **API-First Design:** Backed by strongly-typed schemas, the API is fully documented via [[openapi-specification|Swagger/OpenAPI]] and powers all components. [8]
- **Pull-Based Ingestion Model:** The [[ingestion-framework]] actively pulls metadata from external systems on a schedule rather than relying on push events. This ensures decoupling from source-side configurations and maintains consistency across the [[unified-metadata-graph]]. [8]
- **Streamlined Dependencies:** The architecture intentionally minimizes system components to just four core dependencies, simplifying deployment, operation, and scaling. [2][10]

## Core System Components

The platform depends on exactly four components to function: [2]

1. **[[jsonschemas]]** — The foundation of the metadata standard defining every asset entity (e.g., Table, Dashboard, [[snowflake]] service, [[ml-modeling|ML Model]]).
2. **[[dropwizard]] / [[jetty]]** — The Java REST API framework handling all client requests, authentication, and business logic.
3. **[[mysql-8x]]** — The primary transactional metadata store (Entity Store).
4. **[[elasticsearch-7x]]** — Powers full-text search, the search index, and the activity feed.

## Entity Store & Relationship Model

A key architectural innovation is the decoupled storage of entities and their relationships within MySQL: [1]

- **Entity Tables:** Each entity type (e.g., `table_entity`, `dashboard_entity`) holds the JSON definition of the entity's attributes plus system fields (`id`, `updatedAt`, `updatedBy`). Relationships are *not* stored in this JSON.
- **Relationship Table:** A separate `entity_relationship` table stores connections as graph edges (nodes with a labeled edge, e.g., `contains`, `uses`, `owns`).
- **Benefits:** This design decouples concerns. Deleting a Dashboard does not directly cascade into the ownership relationship logic; the relationship is cleaned up independently. It allows the system to process entities and relationships efficiently and validate at runtime what needs updating or retrieving. [1]

## ML Model Assets

OpenMetadata models Machine Learning assets as first-class citizens within the [[unified-metadata-graph]], supporting the full ML lifecycle and governance:

- **Entity Hierarchy:** `MlModelService` (e.g., MLflow, SageMaker) → `MlModel`. [6][9]
- **Versioning:** A strict major versioning scheme is used. Changes to the algorithm, server configuration, or integrations trigger a major version bump, while experimental feature tweaks do not, preventing alert fatigue. [7]
- **Governance:** Tracks fairness metrics, explainability (SHAP values), compliance (GDPR), model cards, and drift detection. [6]
- **Lineage:** ML Models can be connected to their training datasets and downstream predictions via the [[data-lineage]] framework. [7]

## Extensibility & Customization

- **[[custom-properties]]:** Users can extend standard JSON Schema entities with custom fields via the API. [11]
- **[[persona]] & [[pluggable-panels]]:** The UI can be tailored by role, defining custom landing pages with modular widgets (KPIs, Activity Feed, Announcements). [3]
- **Access Control:** A [[hybrid-rbac-abac-model]] governs access down to the row/column level using Roles, Policies, and [[classification-tags]]. [8]

## References

[1] High Level Design | OpenMetadata Architecture Overview [Source 1]
[2] OpenMetadata System Architecture | Developer Guide [Source 2]
[3] OpenMetadata Release 1.2 — Customizable Landing Page [Source 3]
[6] Overview - OpenMetadata Standards (ML Model Specs) [Source 6]
[7] ML Model | OpenMetadata Machine Learning Model SDK [Source 7]
[8] OpenMetadata: Design Principles, Architecture, Applications & More [Source 8]
[9] ML Models — API Endpoints [Source 9]
[10] OpenMetadata #1 Open Source Metadata Platform — Architecture Highlights [Source 10]
[11] OpenMetadata Developers | Developer Resources Overview [Source 11]

## References

1. [High Level Design | OpenMetadata Architecture Overview - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/api-reference/main-concepts/high-level-design) — docs.open-metadata.org
2. [OpenMetadata System Architecture | Developer Guide - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/developers/architecture) — docs.open-metadata.org
3. [OpenMetadata Release 1.2](https://www.getcollate.io/blog/openmetadata-release-12) — getcollate.io
4. [Getting Started - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/api-reference/getting-started) — docs.open-metadata.org
5. [All Releases | OpenMetadata All Releases - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/releases/all-releases) — docs.open-metadata.org
6. [Overview - OpenMetadata Standards](https://openmetadatastandards.org/data-assets/ml/overview/) — openmetadatastandards.org
7. [ML Model | OpenMetadata Machine Learning Model SDK - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/api-reference/sdk/python/entities/ml-model) — docs.open-metadata.org
8. [OpenMetadata: Design Principles, Architecture, Applications & More](https://atlan.com/openmetadata-explained/) — atlan.com
9. [ML Models - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/api-reference/data-assets/mlmodels) — docs.open-metadata.org
10. [OpenMetadata: #1 Open Source Metadata Platform](https://open-metadata.org/) — open-metadata.org
11. [OpenMetadata Developers | Developer Resources Overview - OpenMetadata Documentation](https://docs.open-metadata.org/v1.11.x/developers) — docs.open-metadata.org
