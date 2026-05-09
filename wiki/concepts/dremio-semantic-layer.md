---
type: concept
title: Dremio Semantic Layer
created: 2026-04-29
updated: 2026-05-07
tags: [dremio, semantic-layer, data-abstraction, virtualization]
related: [dremio, dremio-acceleration-engine, data-lakehouse, data-virtualization-pattern, dbt-mesh]
sources: ["Dremio.md"]
---
# Dremio Semantic Layer

## Overview

The Dremio semantic layer provides a business-friendly abstraction over physical data stored in data lakes. It is a key differentiator from pure query engines like Trino or Presto, enabling non-technical users to interact with data through curated, semantically meaningful views. It functions as a virtualized data layer that uses views, spaces, folders, user-defined functions (UDFs), and reflections to deliver a unified, governed, and performant data access layer over data lake storage.

## Architecture

The semantic layer maintains a strict separation between two logical tiers:

- **Object storage sources** (e.g., S3, ADLS) — These contain physical tables (often in Iceberg, Parquet, or CSV format) created by ingestion pipelines or dbt table/incremental materializations.
- **Dremio spaces and folders** — These contain virtual datasets that define the semantic views on top of the physical data.

This separation is enforced by the `twin_strategy` setting in the Dremio dbt connector, ensuring that consumption views remain distinct from raw physical datasets. Physical datasets (PDS) represent direct references to the source tables in object storage, while virtual datasets (VDS) define semantic mappings, transformations, and joins without duplicating data.

## Components

### Physical Datasets (PDS)

Direct references to source tables in object storage (Iceberg, Parquet, CSV, etc.). PDSs form the raw physical layer that the semantic layer abstracts.

### Virtual Datasets (VDS) / Views

The core of the semantic layer. VDSs are SQL-based views that define business logic, calculations, joins, and field remappings on top of physical data. They provide a business-friendly representation without moving or copying the underlying data. In Dremio these are also commonly referred to simply as views.

### Spaces and Folders

Organizational containers for managing VDSs and other objects. Spaces act as top-level namespaces, and folders provide hierarchical grouping. When deploying with dbt, spaces and folders can be auto-created as part of the CI/CD process.

### User-Defined Functions (UDFs)

Custom SQL functions that encapsulate reusable logic and security policies. UDFs are critical for implementing row-level and column-level security directly within the semantic layer.

### Reflections

Hybrid materialisations that accelerate query performance. Reflections can be created on VDSs so that queries automatically benefit from pre‑computed results without changing the user‑facing view. They are part of the [[dremio-acceleration-engine]].

### Role‑Based Access Control (RBAC) and Security

The semantic layer supports fine‑grained RBAC at the space and folder level. Additionally, row and column security policies can be embedded in UDFs, enabling governed access to data through the semantic views.

### Semantic Mappings

The ability to rename, transform, and combine fields to produce business‑friendly representations. This capability is inherent in VDSs and UDFs and forms the essence of the semantic layer’s abstraction power.

## Relationship to Data Reflections

The semantic layer works hand‑in‑hand with [[dremio-acceleration-engine]] and Data Reflections. When a VDS is queried, Dremio automatically routes the query to pre‑materialised Reflections if they are available, providing semantic abstraction without any performance penalty. This allows users to interact with curated views while still obtaining near‑instant query responses.

## CI/CD Integration

The entire semantic layer can be managed as code using dbt. This enables:

- **Version‑controlled SQL definitions** for all VDSs, UDFs, and security policies.
- **Automated deployment** across environments (development, staging, production).
- **Coordinated creation** of dependent objects (e.g., views that rely on other views).
- **Automated data quality testing** after each deployment.

The dbt connector for Dremio automates the creation of spaces, folders, views, and reflections, and enforces the `twin_strategy` separation between physical and virtual layers.

## Comparison with Other Semantic Layers

- **vs. dbt Semantic Models** — dbt’s semantic models are defined in YAML and compiled into SQL at transformation time. Dremio’s semantic layer is runtime‑based, defined and evaluated within the engine itself. When dbt is used with Dremio, it deploys and manages the runtime layer rather than compiling it away.
- **vs. Traditional BI Semantic Layers** — Dremio’s layer operates directly on data lake storage without requiring a separate warehouse or extensive ETL processes. It provides interactive query speeds through reflections and columnar execution.

## Use Cases

- Providing business users with curated views of raw data lake content.
- Enabling self‑service analytics without data duplication.
- Abstracting complex joins and transformations behind simple table names.
- Supporting data governance through controlled access to semantic views (via RBAC and row/column security).

## Limitations

- Sources (external storage connections) cannot be created via dbt; they require the Dremio REST API or manual configuration.
- Wikis and tags have no SQL interface in Dremio and cannot be managed through the semantic layer’s SQL‑based workflows.
- Users and roles are best managed via external identity providers; the semantic layer does not replace a full IAM solution.

## Related Pages

- [[dremio]] — Primary Dremio entity page
- [[dremio-acceleration-engine]] — Performance optimisation for semantic queries
- [[data-virtualization-pattern]] — Broader virtualization pattern
- [[data-lakehouse]] — Architectural context
- [[data-lakehouse]]
- [[dremio-dbt-connector-configuration]] — Configuration details for CI/CD deployments