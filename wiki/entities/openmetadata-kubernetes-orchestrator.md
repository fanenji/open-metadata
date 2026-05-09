---
type: entity
title: OpenMetadata Kubernetes Orchestrator
created: 2026-02-26
updated: 2026-02-26
tags: [kubernetes, orchestration, deployment, cloud-native]
related: [kubernetes, apache-airflow, openmetadata-1.12-release-notes]
sources: ["Announcing OpenMetadata 1.12.md"]
---
# OpenMetadata Kubernetes Orchestrator

The **Kubernetes Orchestrator** is a new native scheduler introduced in OpenMetadata 1.12 designed to simplify cloud-native deployments.

## Purpose
The primary goal is to reduce the operational complexity and infrastructure footprint of OpenMetadata by eliminating the need to manage a separate [[apache-airflow]] instance.

## Architecture Changes
Previously, OpenMetadata relied on Apache Airflow for orchestration. The new architecture leverages the existing [[kubernetes]] cluster as the native scheduler, reducing the required components to:
1. **Application Server**
2. **Database** (e.g., PostgreSQL, MySQL)
3. **Search Index** (e.g., OpenSearch, Elasticsearch)

## Benefits
- **Simplified Deployment**: Fewer moving parts to monitor and maintain.
- **Reduced Infrastructure Cost**: Eliminates the overhead of running a dedicated Airflow cluster.
- **Cloud-Native Alignment**: Uses the orchestration layer (K8s) that most modern data platforms already utilize.