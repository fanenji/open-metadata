---
type: concept
title: Ingestion Scheduling
created: 2026-05-14
updated: 2026-05-14
tags: [metadata-ingestion, scheduling, automation, cron]
related: [metadata-agent, metadata-ingestion-workflow, kubernetes-native-orchestrator, omjob-operator]
sources: ["how-to-ingest-metadata-official-documentation---op-20260514.md"]
---

# Ingestion Scheduling

The mechanism by which [[metadata-agent|Metadata Agent]] pipelines are configured to run automatically on a recurring basis, ensuring metadata stays current without manual intervention.

## Schedule Options

### Preset Intervals
- **Hour**: Run every hour
- **Day**: Run once daily
- **Week**: Run once weekly
- **Month**: Run once monthly

### Custom Cron Expressions
For advanced scheduling needs, custom cron expressions provide fine-grained control over execution timing (e.g., specific days of the week, multiple times per day, business-hours-only schedules).

## Retry Configuration

Each scheduled pipeline can be configured with a **Number of Retries** value. This defines how many times the ingestion workflow automatically restarts if it fails. Retries help handle transient errors (network timeouts, temporary source unavailability) without requiring manual intervention.

## Orchestration Backend

The scheduling mechanism is implemented by the underlying orchestration backend:

- **Apache Airflow**: Schedules are managed as Airflow DAG schedules
- **[[kubernetes-native-orchestrator|Kubernetes-native orchestrator]]**: Schedules are managed as Kubernetes CronJobs via the [[omjob-operator|OMJob Operator]]

The UI-based scheduling configuration is orchestrator-agnostic — administrators define schedules in the same way regardless of the backend.

## Agent Run Status

After deployment, the Agents tab displays the current status of each scheduled pipeline:
- **Queued**: Pipeline is waiting to execute
- **Running**: Pipeline is actively ingesting metadata
- **Failed**: Pipeline encountered an error
- **Successful**: Pipeline completed without errors

Hovering over an agent reveals its scheduling frequency and the start/end times of recent runs.