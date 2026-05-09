---
type: concept
title: dbt DAG Generator
created: 2026-04-29
updated: 2026-05-07
tags:
  - dbt
  - airflow
  - orchestration
  - lineage
  - dag
  - automation
related:
  - elt-pattern
  - CI-CD-for-data-pipelines
  - blablacar
  - data-product-definition
  - dbt-scaling-patterns
  - dbt-project-governance
  - dbt-cloud
sources:
  - "Data Pipelines Architecture at BlaBlaCar.md"
  - "One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months - Summary.md"
---
# dbt DAG Generator

The dbt DAG Generator is a middleware pattern that automatically creates Airflow DAGs from dbt projects. It leverages dbt's `manifest.json` file to infer dependencies between models and translate them into Airflow task dependencies, preserving the same lineage in both systems. This pattern was the single most important enabler for [[blablacar]]'s migration of approximately 1,200 dbt models with Airflow orchestration.

## How It Works

The generator reads the compiled dbt project and produces Airflow DAG files that mirror the dbt dependency graph.

```
dbt compile → manifest.json → DAG generator → Airflow DAG Python files
```

- **`manifest.json`** contains the full DAG structure: every node, its dependencies, tests, and metadata.
- Each dbt model becomes a separate Airflow task that performs a `dbt run` for that specific model.
- Dependencies from the dbt manifest are used to set task dependencies in Airflow, ensuring the lineage in Airflow matches dbt.
- The generator can produce tasks that use dbt's `--select` syntax for per‑model scheduling and partial runs (node selector support).

Engineers never write Airflow DAG files for dbt models — they only write SQL and `schema.yml`.

## Benefits

- **Eliminates manual DAG definition** for dbt transformations, removing the biggest operational overhead when scaling dbt with Airflow.
- **Ensures consistency** between dbt and Airflow dependency graphs; Airflow DAGs automatically reflect the current dbt project structure.
- **Enables visualization** of model lineage in the Airflow UI.
- **Provides access to Airflow’s operational features**: retry mechanisms, backfill support, and Python‑based customization.
- **Supports [[CI-CD-for-data-pipelines]] workflows** by keeping DAG generation part of the development pipeline.
- **Always in sync**: any change to the dbt project is reflected in the next DAG file generation.

## BlaBlaCar Implementation

At [[BlaBlaCar]], the dbt DAG Generator bridged dbt and Airflow during their migration of ~1,200 models. Key implementation details:

### Task Mapping and Lineage
- **One task per model**: each dbt model is mapped to a distinct Airflow task.
- **Lineage preservation**: the generator uses the dbt manifest to set Airflow task dependencies, giving teams the same dependency view in both tools.

### Isolation and Dependencies
- **PythonVirtualenvOperator**: each dbt project runs in an isolated virtual environment to avoid dependency conflicts.
- **Source freshness sensors**: Airflow sensors on `dbt source freshness` checks enable cross‑DAG dependency management.

### Development and Deployment Flow
1. Data engineers/analysts modify dbt models locally.
2. For new dbt projects, they create an Airflow DAG using the generator library.
3. Code is pushed via Pull Request.
4. CI/CD synchronizes the code with the Airflow instance, automatically updating the generated DAGs.
5. Updated pipelines execute at the next scheduled time.

## Related Concepts

- [[dbt-scaling-patterns]] — Collection of practices for scaling dbt adoption.
- [[dbt-project-governance]] — Criteria for managing dbt project boundaries.
- [[dbt-cloud]] — Alternative orchestration approach that doesn’t require a DAG generator.