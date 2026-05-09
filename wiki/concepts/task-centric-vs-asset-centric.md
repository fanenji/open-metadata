---
type: concept
title: Task-centric vs Asset-centric Orchestration
created: 2026-05-07
updated: 2026-05-07
tags: [orchestration, paradigm, dagster, airflow, data-pipeline-design]
related: [dagster-security-oss, airflow-on-premise-k8s, orchestration-tool-comparison]
sources: ["Orchestratori Data Platform_ Analisi Comparativa 2.md"]
---
# Task-centric vs Asset-centric Orchestration

A fundamental paradigm distinction in data pipeline orchestration that affects pipeline design, observability, and team alignment.

## Task-centric (Airflow, Argo, Luigi)

- Focuses on the **tasks** (operations) that make up a workflow
- Pipelines are defined as Directed Acyclic Graphs (DAGs) of tasks
- The primary abstraction is the task and its dependencies
- Observability is centered on task execution status and timing
- Example: "Run extract task, then transform task, then load task"

## Asset-centric (Dagster)

- Focuses on the **data assets** produced and consumed by workflows
- Pipelines are defined as graphs of assets and their dependencies
- The primary abstraction is the data asset (e.g., a table, a file, an ML model)
- Observability is centered on asset materialization status, lineage, and metadata
- Example: "Produce the cleaned_sales table, which depends on the raw_sales table"

## Implications

- **Developer experience**: Asset-centric is often more intuitive for data teams, aligning with how they think about data products
- **Testability**: Asset-centric design facilitates unit and integration testing of individual data assets
- **Observability**: Asset-centric provides clearer lineage and data quality visibility
- **Team alignment**: Asset-centric maps well to data mesh and domain ownership patterns
- **Security**: The paradigm choice does not directly affect security, but Dagster (asset-centric) has weaker native auth than Airflow (task-centric)

## Recommendation

- Choose **asset-centric** (Dagster) when team alignment, data product thinking, and observability are top priorities, and the team can manage reverse-proxy auth
- Choose **task-centric** (Airflow) when mature auth/RBAC is required out-of-the-box and the team is comfortable with a steeper learning curve