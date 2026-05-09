type: concept
title: Geospatial Vendor Lock-in Avoidance
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, iceberg, vendor-lock-in, storage-compute-separation, open-format]
related: [iceberggo-v3-spec, geoparquet-vs-iceberg-metadata, iceberggo-vs-delta-lake-geospatial, wherobots, foursquare]
sources: ["Geospatial Tables in the Open Lakehouse A New Era for Iceberg & Parquet.md"]
---
# Geospatial Vendor Lock-in Avoidance

The strategy of using open table formats like Apache Iceberg with native geospatial types to decouple storage from compute, enabling multi-engine query access and eliminating the need for data migration between proprietary systems.

## Core Principles

- **Storage-Compute Separation**: Data stored in Iceberg format on object storage (S3, GCS, ADLS) can be queried by any engine (Snowflake, BigQuery, DuckDB, Spark) without copying or migrating data.
- **Open Standards**: Iceberg GEO v3 and GeoParquet provide standardized formats that any vendor can implement.
- **Catalog Standardization**: The Iceberg REST Catalog specification enables standardized table discovery and access control across engines.

## Benefits

- **For Data Providers**: Lower barrier to sharing data — just put it on a bucket with request pays. No need to maintain separate copies for each cloud platform.
- **For Data Consumers**: Freedom to choose the best query engine for each job without being locked into a single vendor.
- **For Both**: Reduced migration costs, improved observability, and better control over data access patterns.

## Challenges

- **Vendor Tension**: While customers want no lock-in, vendors have tension between proprietary formats and open standards. Full adoption of Iceberg REST Catalog is still in progress.
- **Implementation Timeline**: The Iceberg GEO v3 spec is approved but implementation across major engines is pending Parquet release.

## Key Quote

> "The core of it really is this separation of compute from storage... the fact that iceberg makes it possible where you can just find the best query engine for your given job." — Chris Holmes