---
type: entity
title: Cosmos
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, airflow, orchestration, astronomer]
related: [dbt-dag-generator, blablacar, airflow, dbt-core]
sources: ["Scaling Success The dbt Ecosystem at BlaBlaCar.md"]
---
# Cosmos

Cosmos is an open-source solution developed by Astronomer for integrating dbt with Airflow. It provides a `DbtDag` class that automatically generates Airflow DAGs from dbt projects.

## Comparison with dbtDagGenerator

At [[BlaBlaCar]], Cosmos was considered as an alternative to building the custom [[dbt-dag-generator]] framework. It was ultimately rejected because it lacked the ability to define sensors in dbt source configuration, which was a critical requirement for managing cross-DAG dependencies in BlaBlaCar's data mesh architecture. The custom dbtDagGenerator provides this capability by converting dbt sources with defined metadata into `ExternalTaskSensors` or `PythonVirtualenvOperator` tasks.