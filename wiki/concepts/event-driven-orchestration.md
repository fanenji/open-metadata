---
type: concept
title: Event-Driven Orchestration
created: 2026-04-04
updated: 2026-04-04
tags: [orchestration, events, triggers, real-time]
related: [kestra, apache-airflow, declarative-yaml-orchestration]
sources: ["Kestra vs Airflow (Video).md"]
---
# Event-Driven Orchestration

Event-driven orchestration is a paradigm where workflow execution is triggered by external events (file changes, messages, API calls, database changes) rather than solely by scheduled cron intervals. [[Kestra]] implements this as a first-class feature, distinguishing it from [[Apache Airflow]]'s schedule-first model.

## Key Characteristics

- **Native Event Triggers**: First-class support for S3 events, Kafka messages, webhooks, and database change data capture (CDC).
- **Real-Time Pipelines**: Enables immediate processing when data arrives, without polling or workarounds.
- **Multiple Triggers per Flow**: A single flow can have multiple independent triggers (cron + events + API).
- **Cross-Flow Dependencies**: First-class expression of inter-flow dependencies (e.g., "flow C runs when flows A and B succeed").

## Advantages over Schedule-First Models

- Enables real-time data processing without polling
- Reduces latency between data arrival and processing
- Supports event-driven architectures and microservices integration
- More natural fit for modern data stacks with streaming components

## Limitations

- Event-driven systems can be harder to debug and monitor
- Requires infrastructure for event ingestion (Kafka, SQS, etc.)
- May introduce complexity in handling event ordering and deduplication

## Related Concepts

- [[declarative-yaml-orchestration]] — Event-driven triggers are defined declaratively in YAML
- [[elt-pattern]] — Event-driven orchestration can trigger both ETL and ELT workflows
- [[stream-processing-ingestion]] — Event-driven orchestration complements streaming ingestion patterns