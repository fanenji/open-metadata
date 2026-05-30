---
type: concept
title: Pull-Based Ingestion Model
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, ingestion, architecture, orchestration]
related: [ingestion-framework, openmetadata-connectors, apache-airflow, kubernetes-native-orchestrator]
sources: ["understand-code-layout---openmetadata-documentatio-20260514.md"]
---
# Pull-Based Ingestion Model

OpenMetadata employs a **pull-based ingestion model** to collect metadata from external sources. Rather than waiting for source systems to push metadata changes, OpenMetadata actively reaches out and extracts metadata on a scheduled basis.

## Design Rationale

- **Control**: OpenMetadata dictates the ingestion schedule, independent of source system capabilities.
- **Compatibility**: Works with any source that exposes an API or connection endpoint, regardless of whether the source supports push notifications.
- **Simplicity**: Connectors only need to implement read/extract logic, not listen for events.

## Implementation

The pull-based model is implemented through the [[ingestion-framework]], which orchestrates workflows composed of:
- **Source**: Connects to the external system and extracts metadata.
- **Processor**: Transforms or enriches extracted metadata.
- **Sink**: Sends processed metadata to the OpenMetadata API.

## Orchestration

- **Apache Airflow**: Historically the primary orchestrator; DAG definitions exist under `ingestion/examples/airflow/dags`.
- **Kubernetes-Native Orchestrator**: In v1.12+, the [[kubernetes-native-orchestrator]] provides an alternative using Kubernetes Jobs and CronJobs via the [[omjob-operator]], eliminating the Airflow dependency for new deployments.

The pull-based model is a deliberate architectural choice that shapes how [[openmetadata-connectors]] are designed and how ingestion pipelines are scheduled and monitored.