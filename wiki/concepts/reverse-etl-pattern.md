---
type: concept
title: Reverse ETL Pattern
created: 2026-04-29
updated: 2026-04-29
tags: [data-pipelines, etl, data-warehouse, operational-systems]
related: [elt-pattern, data-product-definition, blablacar, database-snapshotting-pattern]
sources: ["Data Pipelines Architecture at BlaBlaCar.md"]
---
# Reverse ETL Pattern

Reverse ETL refers to outgoing data pipelines that move processed data from a data warehouse back into operational systems (CRM, production services, partner systems). Unlike traditional ETL/ELT which moves data *into* the warehouse, reverse ETL moves data *out of* the warehouse to where it can drive business actions.

## BlaBlaCar Implementation

At [[BlaBlaCar]], reverse ETL pipelines serve several functions:
- Sending calculated customer attributes to CRM for targeted marketing
- Providing business metrics (e.g., conversion rate) to monitoring systems like Datadog
- Computing driver cancellation rates to optimize search results in production systems

## Technologies Used

BlaBlaCar uses multiple technologies for reverse ETL:
- **Google Dataflow**: Batch (and some streaming) jobs to copy data from BigQuery to PostgreSQL, Redis, and other databases
- **GCS File Sharing**: Dropping files in Google Cloud Storage for partner access
- **Google Sheets**: Sharing reports via spreadsheets
- **SFTP**: Sending files to external partners, orchestrated through Airflow
- **SFTP Server backed by GCS**: Partners connect via SFTP to access files stored in GCS
- **Direct BigQuery Connection**: Production services connect directly to BigQuery using service accounts
- **Webhooks**: Building payloads from BigQuery results and pushing to HTTP APIs

## Relationship to ELT

Reverse ETL completes the data lifecycle: data is ingested (EL), transformed (T), and then served back to operational systems. This pattern is essential for operationalizing analytics and closing the loop between data processing and business action.