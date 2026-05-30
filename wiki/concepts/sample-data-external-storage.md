---
type: concept
title: Sample Data External Storage
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, sample-data, s3, parquet, auto-classification, data-profiling, storage]
related: [auto-classification, sample-data-storage-toggle, data-profiling, snowflake, order-of-precedence-storage-credentials, openmetadata-storage-config]
sources: ["external-storage-for-sample-data---openmetadata-do-20260514.md"]
---
# Sample Data External Storage

Sample Data External Storage is a capability introduced in OpenMetadata v1.2.1 that allows sample data generated during [[auto-classification|auto-classification]] and [[data-profiling|profiling]] workflows to be uploaded to an AWS S3 bucket in Parquet format. This enables efficient, scalable external analysis of sampled data using columnar storage.

## How It Works

When the **Generate Sample Data** flag is enabled in the profiler configuration, the auto-classification workflow ingests a random sample of rows from each table. By default, this sample contains 50 rows, but the count is now configurable via the **Sample Data Rows Count** parameter. With external storage configured, this sample data is written to S3 as a Parquet file.

### UI Row Limit vs. Storage Row Count

A critical distinction: the OpenMetadata UI always displays **50 or fewer rows** of sample data, regardless of the configured Sample Data Rows Count. Values higher than 50 only affect the Parquet file stored in object storage — they do not increase the rows visible in the UI.

## Configuration Hierarchy

Storage credentials can be configured at three levels, following a strict [[order-of-precedence-storage-credentials|order of precedence]]:

1. **Database Schema** (highest priority)
2. **Database**
3. **Database Service** (lowest priority)

If credentials are configured at the Database Schema level, they override any Database or Database Service settings. If no schema-level config exists, the system falls back to Database, then to Database Service.

### Configuration Parameters

| Parameter | Description |
|-----------|-------------|
| **Profile Sample Value** | Percentage or row count for sampling tables during profiling |
| **Profile Sample Type** | `Percentage` or `Row Count` — determines how Profile Sample Value is interpreted |
| **Sample Data Rows Count** | Number of sample data rows to ingest; values >50 only affect the Parquet file |
| **Sampling Method Type** | `BERNOULLI` or `SYSTEM` — effective for [[snowflake|Snowflake]] only |
| **Bucket Name** | S3 bucket identifier for storing Parquet files |
| **Prefix** | Path prefix within the bucket for generated Parquet files |
| **Overwrite Sample Data** | If enabled, one Parquet file per table; otherwise, daily files are generated |

## AWS S3 Connection Details

The external storage target is AWS S3, configured with standard AWS credentials:

- **AWS Access Key ID** and **AWS Secret Access Key** for authentication
- **AWS Region** (required) — the geographic region of the S3 bucket
- **AWS Session Token** (optional) — for temporary credentials
- **Endpoint URL** (optional) — for alternate service endpoints
- **Profile Name** — named AWS CLI profile
- **Assume Role Arn**, **Assume Role Session Name**, **Assume Role Source Identity** — for cross-account access

## OpenMetadata Storage Config

The [[openmetadata-storage-config]] option provides an opt-out mechanism. When storage credentials are configured at a parent level (e.g., Database), individual schemas or databases can skip sample data upload by enabling this option. This is useful when only specific subsets of data should be exported externally.

## Relationship to Other Features

- **[[sample-data-storage-toggle]]**: The toggle in the Auto Classification Agent controls whether sample data is ingested at all. External storage configuration determines where that ingested data is persisted beyond the UI.
- **[[auto-classification]]**: External storage is an optional output of the auto-classification workflow, activated when both the sample data toggle and S3 credentials are configured.
- **[[data-profiling]]**: The sampling parameters (Profile Sample Value, Profile Sample Type) are profiler configurations that also govern what data is exported to external storage.