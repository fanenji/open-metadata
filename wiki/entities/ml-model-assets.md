---
type: entity
title: ML Model Assets
created: 2026-05-15
updated: 2026-05-15
tags: [ml, governance, versioning, lineage]
related: [ml-model-versioning, unified-metadata-graph, data-lineage, service-connection, openmetadata-connectors]
sources: ["research-capture-referenced-design-page-2026-05-15.md"]
---
# ML Model Assets

OpenMetadata models Machine Learning assets as first-class citizens within the [[unified-metadata-graph]], supporting the full ML lifecycle and governance. ML models are treated with the same rigor as database tables, dashboards, and pipelines.

## Entity Hierarchy

- **MlModelService** — Represents the ML platform or service (e.g., MLflow, SageMaker, custom model registry). This is a type of [[service-connection]].
- **MlModel** — Represents an individual ML model within a service. Each model has its own metadata including algorithm, hyperparameters, training data, and governance attributes.

## Versioning

ML models follow a strict major versioning scheme:
- Changes to the algorithm, server configuration, or integrations trigger a **major version bump**.
- Experimental feature tweaks do **not** trigger a version bump, preventing alert fatigue.
- Version history is preserved for lineage and auditability.

## Governance Features

OpenMetadata tracks the following governance attributes for ML models:
- **Fairness Metrics** — Quantitative measures of model bias across protected attributes.
- **Explainability** — SHAP (SHapley Additive exPlanations) values for model interpretability.
- **Compliance** — GDPR and other regulatory compliance tracking.
- **Model Cards** — Standardized documentation cards summarizing model purpose, performance, and limitations.
- **Drift Detection** — Monitoring for data drift and concept drift over time.

## Lineage Integration

ML Models can be connected to their training datasets and downstream predictions via the [[data-lineage]] framework. This enables end-to-end traceability from raw data through model training to production predictions.