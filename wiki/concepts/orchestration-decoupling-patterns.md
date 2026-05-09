---
type: concept
title: Orchestration Decoupling Patterns
created: 2026-04-04
updated: 2026-04-04
tags: [architecture, design-pattern, airflow]
related: [apache-airflow, docker]
sources: ["Airflow vs Kestra.md"]
---
# Orchestration Decoupling Patterns

A design pattern used to separate the orchestration logic (the "when" and "how" of execution) from the business logic (the "what" of data processing).

## Implementation

In this pattern, the orchestrator (such as [[apache-airflow]]) does not contain the actual data processing code. Instead:

1. **Business Logic**: Resides in a dedicated, versioned Python repository.
2. **Packaging**: The logic is packaged into a Docker image containing all necessary dependencies (e.g., pandas, scikit-learn, specialized drivers).
3. **Orchestration**: The orchestrator's role is limited to triggering the execution of these containers (e.g., via KubernetesPodOperator).

## Benefits

- **Dependency Isolation**: Prevates "dependency hell" where different tasks require conflicting versions of the same library.
- **Simplified Deployment**: The orchestrator environment remains lightweight and stable.
- **Local Debugging**: Developers can test the business logic locally using the Docker image without needing a full Airflow instance.
- **Scalability**: Allows the orchestration layer to scale independently of the compute-heavy processing tasks.
