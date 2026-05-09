---
type: concept
title: DremioFrame Orchestration
created: 2026-04-29
updated: 2026-04-29
tags: [dremio, orchestration, pipeline, scheduling, python]
related: [dremioframe, kestra, airflow, dremioframe-data-quality-framework, dremioframe-iceberg-management]
sources: ["DremioFrame - Dremio Dataframe Library.md"]
---
# DremioFrame Orchestration

DremioFrame Orchestration provides built-in pipeline scheduling, task management, and distributed execution capabilities within the [[dremioframe|DremioFrame]] library. It allows users to define, schedule, and monitor data pipelines without requiring external orchestration tools.

## Key Features

- **Tasks & Sensors**: Define pipeline tasks and sensors for monitoring conditions
- **Scheduling**: Schedule pipeline execution with cron-like expressions
- **Dremio Jobs**: Manage and monitor Dremio jobs
- **Iceberg Tasks**: Specialized tasks for Iceberg table management (see [[dremioframe-iceberg-management]])
- **Reflection Tasks**: Manage Dremio reflections
- **Data Quality Task**: Run data quality checks as pipeline tasks (see [[dremioframe-data-quality-framework]])
- **Distributed Execution**: Execute pipelines across multiple workers
- **Deployment**: Deploy pipelines to production
- **CLI & UI**: Command-line and web interfaces for pipeline management
- **Backends**: Support for multiple execution backends
- **Extensions**: Extend orchestration with custom components

## Comparison

DremioFrame's orchestration provides a lightweight, embedded alternative to dedicated orchestration tools like [[kestra]] or [[airflow]]. It is tightly integrated with the Dremio ecosystem but may lack the breadth of connectors and community support of standalone orchestration platforms.

## Related

- [[dremioframe]] — The parent library
- [[dremioframe-data-quality-framework]] — DQ tasks for orchestration
- [[dremioframe-iceberg-management]] — Iceberg-specific tasks