---
type: source
title: "Research: Capture Referenced Design Page"
created: 2026-05-15
updated: 2026-05-15
tags: [architecture, design, schema-first, system]
related: [openmetadata-system-architecture, schema-first-approach, jsonschemas, unified-metadata-graph, entity-relationship-storage-model, ml-model-assets, ml-model-versioning, dropwizard, jetty, mysql-8x, elasticsearch-7x, ingestion-framework, custom-properties, persona, pluggable-panels, hybrid-rbac-abac-model, classification-tags]
sources: ["research-capture-referenced-design-page-2026-05-15.md"]
---
# Research: Capture Referenced Design Page

This source synthesizes the official "Design" and "Architecture" documentation of OpenMetadata into a comprehensive reference. It documents the platform's Schema-First and API-First architecture, the unified metadata model, the decoupled entity-relationship storage model, and the first-class support for ML model assets with versioning and governance. The source consolidates information from the official High Level Design, System Architecture Developer Guide, ML Model specifications, and a third-party analysis from Atlan.

Key contributions include:
- Detailed explanation of the decoupled entity-relationship storage model (separate `entity_relationship` table for graph edges).
- ML model asset hierarchy (MlModelService → MlModel), strict major versioning scheme, and governance features (fairness, SHAP, compliance, model cards, drift detection).
- Confirmation of the four core dependencies: JSON Schemas, Dropwizard/Jetty, MySQL 8.x, Elasticsearch 7.x.
- The "Three Views from One Source" principle: Java, Python, and TypeScript code generation from JSON Schema definitions.