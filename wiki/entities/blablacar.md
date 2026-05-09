---
type: entity
title: BlaBlaCar
created: 2026-04-29
updated: 2026-05-07
tags: [organization, travel, data-architecture, data-mesh, dbt]
related: [antoine-lefebvre, elt-pattern, data-mesh, dbt-dag-generator, reverse-etl-pattern, feature-store-architecture, database-snapshotting-pattern, dbt-osmosis, dev-containers-for-dbt, read-from-prod-write-to-dev-pattern, dbt-dev-environment-isolation, dbt-power-user, upstream-prod, dbt-dry-run, bigquery, airflow, dbt-project-scaffolding, ci-cd-for-data-pipelines]
sources: ["Data Pipelines Architecture at BlaBlaCar.md", "Scaling Success The dbt Ecosystem at BlaBlaCar.md"]
---

# BlaBlaCar

BlaBlaCar is the world's leading community-based travel app, enabling 29 million members a year to carpool or travel by bus in 21 countries. The company operates multiple marketplaces including Carpool, Operated Buses, and Train Marketplace.

## Data Organization

BlaBlaCar employs over 50 data professionals across 5 job families and 7 teams. The data infrastructure follows a [[data-mesh]] architecture, and the data landscape includes over 4,000 tables and 300 reports.

## Data Architecture

### Stack Components

- **Orchestration**: Airflow (Google Cloud Composer)
- **Warehouse**: BigQuery
- **Ingestion**: Google Dataflow (databases), Rivery (APIs), Freeway (Kafka events)
- **Transformation**: dbt with over 30 projects
- **Feature Store**: Java application backed by BigTable
- **Visualization**: Tableau, Looker Studio

The architecture follows an [[elt-pattern]] organized by functional domains with staging, intermediate, model, and mart/reporting layers in BigQuery.

### dbt Ecosystem

BlaBlaCar has built a comprehensive internal dbt ecosystem to manage its large-scale data transformation needs.

#### Orchestration and Code Generation

- **dbt Core** is used for data transformations across multiple domain-aligned dbt projects in a Git mono-repo.
- **dbtDagGenerator** ([[dbt-dag-generator]]) is an internally developed framework that reads the dbt manifest and programmatically generates Airflow DAGs, mapping dbt models and tests to Airflow tasks, and sources to sensors. This was chosen over Cosmos (Astronomer's solution) due to the need for sensor features to handle cross-DAG dependencies.
- The team chose **dbt Core + Airflow over dbt Cloud** for orchestration flexibility.

#### Development Environment

- **Dev Containers**: Pre-configured VS Code Dev Containers with Docker images provide consistent environments (Python 3.11, dbt-core 1.9, [[dbt-power-user]], SQLFluff, [[dbt-osmosis]]).
- **Dev Environment Isolation**: Per-user BigQuery datasets are provisioned via Terraform, with dataset IDs passed via environment variables to dbt profiles.
- **Read from Prod / Write to Dev**: The [[upstream-prod]] dbt package is used to reference production tables while writing to isolated dev datasets. This pattern avoids costly full pipeline runs in dev environments by leveraging BigQuery on-demand pricing.

#### CI/CD and Testing

- The CI/CD pipeline includes **dbt-dry-run** for production readiness, linting, tag checks, and DAG load validation.

#### Documentation

- A documentation generator uses [[dbt-osmosis]] to create YAML documentation from BigQuery schema and propagate column descriptions to downstream models.

## Key Practices

- **Software development lifecycle** for data pipelines: version control, code reviews, automated testing.
- **[[reverse-etl-pattern]]**: Serving processed data to CRM, production systems, and partners.
- **[[database-snapshotting-pattern]]**: Using Dataflow for production database replication.
- **[[feature-store-architecture]]**: Supporting ML feature serving with low latency.