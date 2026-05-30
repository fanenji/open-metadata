---
type: source
title: "dbt Artifact Storage - AWS S3 Configuration | OpenMetadata"
tags: [dbt, s3, artifact-storage, aws, ingestion]
related: [dbt-artifact-storage, dbt-artifact-storage-s3, dbt-integration, dbt-artifacts, ingestion-framework, openmetadata]
sources: ["dbt-artifact-storage---aws-s3-configuration-openme-20260514.md"]
created: 2026-05-14
updated: 2026-05-14
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/storage-s3-guide"
venue: OpenMetadata Documentation
---

# dbt Artifact Storage - AWS S3 Configuration | OpenMetadata

This official guide walks through configuring AWS S3 as the artifact storage layer for the dbt Core + OpenMetadata integration. It covers the complete workflow: creating an S3 bucket, setting up two separate IAM policies (write for dbt/Airflow, read for OpenMetadata), uploading artifacts via a production-ready Airflow DAG, and configuring the OpenMetadata ingestion pipeline to read from S3.

## Key Content

- **Prerequisites**: AWS account with S3 and IAM permissions, AWS CLI, existing dbt project, Airflow or similar scheduler, and an already-ingested database service.
- **Step 1: AWS S3 Setup**: Bucket creation, two IAM policies (write for dbt, read for OpenMetadata), and verification steps.
- **Step 2: Upload Artifacts from dbt**: Understanding required artifacts (manifest.json, catalog.json, run_results.json), a complete Airflow DAG example with Python upload function, and verification.
- **Step 3: Configure OpenMetadata**: UI configuration for S3 source, two credential options (Access Keys or IAM Role), dbt options, and test/deploy workflow.
- **Verification**: Checklist for S3 artifacts, ingestion status, lineage, descriptions, and tags.
- **Troubleshooting**: Common issues (Access Denied, manifest not found, no lineage, stale data, missing columns) with causes and solutions.

## Connections

- Provides the concrete S3 implementation details for the [[dbt-artifact-storage]] concept.
- Extends [[dbt-integration]] with the S3-specific configuration workflow.
- References the same artifact files (manifest.json, catalog.json, run_results.json) documented in [[dbt-artifacts]].
- Part of the broader [[ingestion-framework]] pipeline setup.