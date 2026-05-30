---
type: source
title: "External Storage for Sample Data - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, sample-data, s3, parquet, auto-classification, data-profiling]
related: [sample-data-external-storage, auto-classification, sample-data-storage-toggle, data-profiling, snowflake]
sources: ["external-storage-for-sample-data---openmetadata-do-20260514.md"]
authors: ["OpenMetadata"]
year: 2025
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/auto-classification/external-sample-data"
venue: "OpenMetadata Official Documentation"
---
# External Storage for Sample Data - OpenMetadata Documentation

Official documentation for the external sample data storage capability introduced in OpenMetadata v1.2.1. This feature allows sample data generated during auto-classification and profiling workflows to be uploaded to an AWS S3 bucket in Parquet format, enabling efficient external analysis.

The documentation covers the three-tier credential configuration hierarchy (Database Service, Database, Database Schema), the order of precedence (Schema > Database > Service), detailed AWS S3 connection parameters, the OpenMetadata Storage Config opt-out mechanism, and configurable sampling parameters including Profile Sample Value, Profile Sample Type, Sample Data Rows Count, and Sampling Method Type (Snowflake-specific).

Key distinction: the OpenMetadata UI always displays 50 or fewer rows of sample data; higher Sample Data Rows Count values only affect the Parquet file stored in object storage.