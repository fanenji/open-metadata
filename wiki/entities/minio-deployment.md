---
type: entity
title: MinIO Deployment
created: 2026-01-15
updated: 2026-01-15
tags: [infrastructure, storage, minio, data-lakehouse]
related: [test-environment-infrastructure, dremio, iceberg-table-versioning, geoparquet-vs-iceberg-metadata, data-lakehouse]
sources: ["Installazione Test Env.md"]
---
# MinIO Deployment

MinIO is deployed as the S3-compatible object storage layer in the Data Platform test environment. It serves as the foundation for the data lakehouse, storing Iceberg tables, GeoParquet files, and other data artifacts.

## Access

- **Console URL**: `https://minio-console.dp.liguriadigitale.it`
- **Credentials**: Shared `dpadmin`/`dpAdm1n!` credentials

## Role in the Stack

MinIO provides the storage layer that supports:

- [[dremio]] queries against Iceberg tables
- [[iceberg-table-versioning]] for data lakehouse versioning
- [[geoparquet-vs-iceberg-metadata]] coordination for geospatial data
- General object storage for pipeline artifacts and backups

## Related

- [[test-environment-infrastructure]] — Overall test environment topology
- [[data-lakehouse]] — Architectural pattern MinIO enables