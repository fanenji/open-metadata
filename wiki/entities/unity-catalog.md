---
type: entity
title: Unity Catalog
created: 20
updated: 2026-05-07
tags: [unity-catalog, databricks, governance, data-catalog, abac]
related: [semantic-context-layer, data-governance-system, databricks, data-classification-automation, sensitive-data-handling-strategies]
sources: ["Cataloghi Data Lake - Differenze Nessie, Polaris e Unity.md", "Handling Sensitive Data in Your Data Platform.md"]
---
# Unity Catalog

[[unity-catalog]] is Databricks' unified, proprietary governance solution for data and AI assets. Designed as a centralized "control tower," it combines fine-grained access control, automated data lineage, data discovery, auditing, multi-format support, automated data classification, and attribute-based access control (ABAC) into a single platform.

## Core Capabilities

- **Fine-grained Access Control**: Provides SQL-based permissions for catalogs, schemas, tables, views, and row‑/column‑level security through masking. In addition, **Attribute‑Based Access Control (ABAC)** enables dynamic tag‑based policies that apply masking or restrict access for specific groups.

- **Automated Data Lineage**: Automatically captures data movement and transformations at the column level.

- **Data Discovery and Auditing**: Centralized search for data assets and comprehensive logging of all access and operations.

- **Multi-format Support**: Optimized for [[delta-lake]], but also supports [[apache-iceberg]], Apache Hudi, and unstructured formats such as Parquet, CSV, and JSON.

- **Automated Data Classification**: Scans datasets to detect sensitive fields (e.g., PII) and tags them for appropriate protection.

## Use Case

Ideal for organizations deeply integrated into the Databricks ecosystem that require a unified, high‑security governance model for both tabular and non‑tabular assets. The combination of fine‑grained access control, automated classification, and ABAC makes it particularly well‑suited for handling sensitive data and enforcing dynamic policies across the data platform.