---
type: concept
title: ML Model Versioning
created: 2026-05-15
updated: 2026-05-15
tags: [ml, versioning, governance]
related: [ml-model-assets, unified-metadata-graph, data-lineage]
sources: ["research-capture-referenced-design-page-2026-05-15.md"]
---
# ML Model Versioning

ML Model Versioning is a strict major versioning scheme used by [[OpenMetadata]] for [[ml-model-assets|ML Model Assets]]. It ensures that meaningful changes to a model are tracked while avoiding alert fatigue from minor or experimental tweaks.

## Version Bump Triggers

A **major version bump** is triggered by changes to:
- **Algorithm** — The core machine learning algorithm (e.g., switching from Random Forest to Gradient Boosting).
- **Server Configuration** — Changes to the serving infrastructure (e.g., hardware, framework version).
- **Integrations** — Changes to upstream or downstream data pipelines.

## Non-Triggers

Experimental feature tweaks that do **not** trigger a version bump:
- Hyperparameter tuning experiments.
- Minor data preprocessing changes.
- A/B test variants.

## Benefits

- **Clear Communication:** Stakeholders can immediately understand the significance of a version change.
- **Reduced Alert Fatigue:** Teams are not overwhelmed by notifications for every minor experiment.
- **Auditability:** The version history provides a clear record of meaningful model evolution for compliance and governance.