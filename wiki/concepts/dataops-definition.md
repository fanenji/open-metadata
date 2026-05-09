---
type: concept
title: DataOps Definition
created: 2026-05-07
updated: 2026-05-07
tags: [dataops, methodology, ci-cd, testing, orchestration, monitoring, devops, data-pipelines, best-practices]
related: [ci-cd-for-data-pipelines, nessie-catalog-versioning, data-lakehouse-versioning-strategies, data-observability-definition, dbt-cloud, sql-lakehouse, data-lakehouse]
sources: ["How Project Nessie Improves DataOps for the Lakehouse.md", "The SQL Lakehouse Principles and Best Practices.md"]
---
# DataOps Definition

DataOps (Data Operations) is a methodology for developing, deploying, and maintaining data solutions using practices derived from DevOps and agile software development. It encompasses the tools and processes to build, implement, and manage data pipelines, applying these practices to ingest, transform, and deliver data to various users. As defined by Wayne Eckerson, Joe Hilleary, and Dave Wells, DataOps is built on four pillars: CI/CD, testing, orchestration, and monitoring. This page serves as a unified reference for the DataOps methodology, consolidating related concepts previously scattered across the wiki.

## Key Principles / Four Pillars

The following core principles, adapted from DevOps, form the foundation of DataOps:

### CI/CD and Continuous Deployment
Continuously improve both data pipeline code and data itself by branching, updating, and then merging pipeline versions back into the "single source of truth." This includes regularly deploying new data sources, data processors, transformation scripts, and BI queries. Project Nessie's [[nessie-catalog-versioning]] directly enables this pillar for data lakehouses.

### Testing
Check pipeline functionality and data quality to reduce errors while developing, deploying, and operating pipelines. Testing validates data quality and pipeline correctness. This connects to [[dbt-testing-patterns]] and [[data-quality-dimensions]].

### Orchestration
Automate the tasks within a pipeline, and the interactions of multiple pipelines and tools, to reduce the effort of data delivery. Related tools include [[kestra]] and [[airflow]].

### Monitoring
Observe the performance of pipelines and their supporting infrastructure to spot, predict, and prevent issues. Provides vigilant oversight and steady improvements to ensure pipelines meet business requirements. This connects to [[data-observability-definition]] and [[full-data-stack-observability]].

## Relationship to DevOps

DataOps adapts DevOps practices — version control, CI/CD, automated testing, monitoring — to the specific challenges of data engineering. While DevOps focuses on software delivery, DataOps focuses on data delivery: ensuring that data is accurate, timely, and accessible to consumers.

## Role in the SQL Lakehouse

In the [[sql-lakehouse]] context, DataOps is presented as a foundational best practice. Key components that require DataOps oversight include:

- New data sources
- Data processors
- Transformation scripts
- BI queries

Each of these contributes to data pipelines within the SQL lakehouse and needs vigilant oversight and steady improvements. Project Nessie's [[nessie-catalog-versioning]] is a direct enabler of CI/CD practices in the lakehouse environment.

## Related Wiki Concepts

- [[CI-CD-for-data-pipelines]] — DataOps provides the broader discipline; CI/CD is a specific practice within it.
- [[dbt-cloud]] — dbt Cloud provides tooling for DataOps practices like testing, documentation, and CI/CD.
- [[dbt-testing-patterns]], [[data-quality-dimensions]] — Testing frameworks and patterns used in DataOps.
- [[data-observability-definition]], [[full-data-stack-observability]] — Key concepts for the monitoring pillar.
- [[kestra]], [[airflow]] — Orchestration tools commonly used in DataOps.
- [[nessie-catalog-versioning]], [[data-lakehouse-versioning-strategies]] — Versioning and branching for data pipelines.
- [[data-lakehouse]] — The broader architecture DataOps supports, especially in the SQL lakehouse setting.