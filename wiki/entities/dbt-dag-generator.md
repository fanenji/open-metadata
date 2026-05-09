---
type: entity
title: dbtDagGenerator
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, airflow, orchestration, internal-tool]
related: [blablacar, airflow, dbt-core, cosmos, ci-cd-for-data-pipelines, dbt-project-scaffolding]
sources: ["Scaling Success The dbt Ecosystem at BlaBlaCar.md"]
---
# dbtDagGenerator

dbtDagGenerator is an internally developed framework at [[BlaBlaCar]] that reads the dbt manifest and programmatically generates Airflow DAGs. It was created because existing solutions like Cosmos (Astronomer) lacked sensor features for cross-DAG dependencies.

## How It Works

1. The CI/CD pipeline builds the dbt project and generates a manifest.
2. The manifest is synchronized with Airflow storage.
3. Airflow DAGs call the dbtDagGenerator (Python class), which reads the manifest and programmatically generates tasks.
4. Each dbt model/test is transformed into an Airflow task based on `PythonVirtualenvOperator`.
5. dbt sources with defined metadata are converted into `ExternalTaskSensors` or `PythonVirtualenvOperator` depending on the source type (database table vs. GSheet-based external table).
6. dbt dependencies (`{{ ref }}`) are converted into Airflow task dependencies.

## Mapping: dbt → Airflow

| dbt Element | Airflow Element |
|---|---|
| dbt model | Airflow task (PythonVirtualenvOperator) |
| dbt test | Airflow task (PythonVirtualenvOperator) |
| dbt source (database table) | ExternalTaskSensor |
| dbt source (GSheet external table) | PythonVirtualenvOperator |
| dbt ref() | Airflow task dependency |

## Key Features

- **Source-to-Sensor Mapping:** Automatically creates sensors from dbt source configurations, enabling cross-DAG dependency management.
- **Manifest-Driven:** Uses the dbt manifest as the single source of truth for DAG structure.
- **CI/CD Integration:** Manifest is generated during CI/CD and synchronized with Airflow storage.

## Comparison with Cosmos

BlaBlaCar considered Cosmos (Astronomer's dbt-Airflow integration) but rejected it because Cosmos lacked the ability to define sensors in dbt source configuration. The custom dbtDagGenerator provides this capability, which is essential for managing cross-DAG dependencies in a data mesh architecture with multiple domain-aligned dbt projects.