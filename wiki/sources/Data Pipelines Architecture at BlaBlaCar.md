---
type: source
title: Data Pipelines Architecture at BlaBlaCar
created: 2026-04-29
updated: 2026-04-29
tags: [architecture, data-pipelines, elt, data-mesh, dbt, airflow]
related: [elt-pattern, data-mesh, data-product-definition, CI-CD-for-data-pipelines, data-ingestion-architectural-patterns, reverse-etl-pattern, dbt-dag-generator, feature-store-architecture, database-snapshotting-pattern, blablacar, antoine-lefebvre]
sources: ["Data Pipelines Architecture at BlaBlaCar.md"]
authors: [Antoine Lefebvre]
year: 2025
url: "https://medium.com/blablacar/data-pipelines-architecture-at-blablacar-3ca43403cb39"
venue: "BlaBlaCar Engineering Blog"
---
# Data Pipelines Architecture at BlaBlaCar

This article by [[Antoine Lefebvre]] describes the end-to-end data pipeline architecture at [[BlaBlaCar]], the world's leading community-based travel app. The architecture follows a classic [[elt-pattern]] organized as a [[data-mesh]] with functional domains, orchestrated by Airflow (Google Cloud Composer), and using dbt for transformations.

## Key Architecture Components

- **Ingestion**: Google Dataflow for database snapshotting, Rivery for external APIs, custom Python scripts for Google Sheets and GCS files, and Freeway (a Java application) for Kafka event streaming.
- **Transformation**: dbt with over 30 projects, orchestrated via a custom [[dbt-dag-generator]] middleware that creates one Airflow task per dbt model, preserving lineage.
- **Reverse ETL**: Outgoing pipelines using Dataflow, GCS, SFTP, webhooks, and direct BigQuery connections to serve data to CRM, production systems, and partners.
- **Feature Store**: A Java application backed by BigTable for low-latency serving of ML features, ingesting from both streaming events and batch warehouse data.

## Data Mesh Organization

Data is organized in BigQuery datasets per domain with staging, intermediate, model, and mart/reporting layers. This [[data-mesh]] approach promotes domain ownership and data product thinking.

## Development Flow

The team follows a software development lifecycle with version control, code reviews, local testing, PR-based deployment, and CI/CD synchronization with Airflow.

## Future Directions

The article identifies key areas for investment: dbt testing (currently "almost non-existent"), SLOs for data products, and reducing data processing volume for sustainability.