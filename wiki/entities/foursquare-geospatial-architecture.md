---
type: entity
title: Foursquare Geospatial Architecture
created: 2026-04-29
updated: 2026-04-29
tags: [foursquare, geospatial, architecture, iceberg, gdpr]
related: [iceberg-v3-geo-types, spatial-predicate-pushdown, iceberg-rest-catalog, geospatial-etl-pipeline-iceberg, data-lakehouse]
sources: ["Geospatial Tables in the Open Lakehouse A New Era for Iceberg & Parquet - Summary.md"]
---
# Foursquare Geospatial Architecture

Foursquare processes billions of GPS pings and billions of place event impressions per day. Their architecture provides a real-world validation of the Iceberg geospatial lakehouse pattern.

## Legacy Architecture

Before Iceberg, Foursquare stored geospatial data in custom folder structures on S3 with:
- Manually written GDPR deletion tools (custom bloom filter implementations)
- Fixed partitioning schemes impossible to evolve without rebuilding pipelines
- Separate replication pipelines for different platforms (S3, Snowflake, Hugging Face)

## Iceberg Adoption

Foursquare adopted Iceberg for most new non-geospatial workloads and is beginning the transition of geospatial workloads as V3 implementations mature. Key use cases:

- **Ad measurement by proximity**: Determining which GPS pings are near a billboard (direction + proximity) — currently requires scanning all data; spatial filter pushdown will prune aggressively
- **GDPR deletion**: Previously required custom bloom filter implementations and heavy custom tooling; Iceberg ACID + row-level delete handles this natively
- **Schema evolution**: Changing partitioning on billion-row tables was previously a full rebuild; Iceberg handles it as a metadata-only operation

## Places Open Dataset

Foursquare's places dataset is now open source in GeoParquet format. With Iceberg, one storage location serves all platforms — previously had to replicate to S3, Snowflake, and Hugging Face separately.

## Engine Choice

Foursquare started with both Iceberg and Delta Lake but switched predominantly to Iceberg because Delta Lake's open-source/proprietary boundary was unclear — difficult to know which features required Databricks compute.
