---
type: concept
title: Airflow DAG Pattern for dbt S3 Upload
tags: [airflow, dbt, s3, orchestration, dag]
related: [dbt-artifact-storage-s3, dbt-artifact-storage, dbt-integration, dbt-artifacts]
sources: ["dbt-artifact-storage---aws-s3-configuration-openme-20260514.md"]
created: 2026-05-14
updated: 2026-05-14
---

# Airflow DAG Pattern for dbt S3 Upload

This concept describes the production-ready Airflow DAG pattern used to run dbt and upload its artifacts to S3 for consumption by OpenMetadata. The DAG is designed to be self-contained — no OpenMetadata packages are installed in the Airflow environment.

## DAG Structure

The DAG (`dbt_with_collate`) follows this execution flow:

1. **dbt Execution Task Group** (sequential):
   - `dbt_run`: Runs `dbt run` to generate manifest.json
   - `dbt_test`: Runs `dbt test` (triggered even if dbt_run fails via `trigger_rule="all_done"`)
   - `dbt_docs_generate`: Runs `dbt docs generate` to produce catalog.json

2. **Upload Task** (after dbt execution):
   - `upload_artifacts_to_s3`: PythonOperator using boto3 to upload artifacts to S3

## Artifact Handling

The upload function handles four artifact files:
- `manifest.json` (required — raises error if missing)
- `catalog.json` (optional but recommended)
- `run_results.json` (optional)
- `sources.json` (optional)

## Configuration

The DAG uses environment variables for all configuration:
- `DBT_PROJECT_DIR`: Path to dbt project
- `DBT_PROFILES_DIR`: Path to dbt profiles
- `S3_BUCKET`: S3 bucket name
- `S3_PREFIX`: S3 key prefix (default: `dbt-artifacts`)
- `AWS_DEFAULT_REGION`: AWS region

## Production Features

- Retry configuration (2 retries, 5-minute delay)
- Email notifications on failure
- Execution timeout (2 hours)
- Max active runs (1) to prevent concurrent executions
- Detailed logging with upload summary