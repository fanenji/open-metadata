---
type: concept
title: Separation of Orchestration and Business Logic
created: 2026-04-04
updated: 2026-04-04
tags: [architecture, pattern, docker]
related: [apache-airflow]
sources: ["Airflow vs K']]
---
# Separation of Orchestration and Business Logic

A design pattern used to decouple the workflow management layer from the actual data processing logic.

## Description
In this pattern, the orchestrator (e.g., [[apache-airflow]]) is responsible only for the scheduling and triggering of tasks. The actual business logic—including specific Python libraries, dependencies, and data processing code—is encapsulated within independent, versioned Docker containers.

## Benefits
- **Avoids Dependency Hell**: Prevates conflicts between different task requirements within the orchestrator's environment.
- **Portability**: Tasks can be run in any environment that supports the container runtime.
- **Simplified Maintenance**: The orchestrator remains lightweight and stable, as updates to business logic do not require changes to the orchestration infrastructure.