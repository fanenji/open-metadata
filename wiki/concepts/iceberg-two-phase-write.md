---
type: concept
title: Iceberg Two-Phase Write
created: 2026-04-29
updated: 2026-04-29
tags: [iceberg, etl, geospatial, data-lakehouse, consistency]
related: [geospatial-etl-pipeline-iceberg, legacy-geospatial-etl-pipeline, gdal-ogr, write-audit-publish-pattern, nessie-catalog-versioning]
sources: ["Ingestione dati cartografici_ analisi alternative.md"]
---
# Iceberg Two-Phase Write

The Iceberg Two-Phase Write is a fundamental architectural challenge that arises when using tools unaware of Iceberg's metadata management (like GDAL/OGR) to produce data for Iceberg tables.

## The Problem

GDAL operates at the file level, writing GeoParquet and COG output to object storage (MinIO) but is completely unaware of Iceberg's table structure and metadata. After GDAL completes file writing, a separate post-processing step is required to:

1. Identify the new files produced by GDAL
2. Calculate column-level statistics (counts, null values, min/max bounds) — crucial for Iceberg's file pruning optimization
3. Update Iceberg manifest files with references to new files and their statistics
4. Create a new Iceberg table snapshot and update the catalog pointer (Nessie)

## Consequences

- **Complexity**: Additional integration step beyond the core ETL process
- **Latency**: Data is not queryable via Iceberg until the second step completes
- **Consistency Risks**: If the Iceberg registration step fails after GDAL writes files, the table remains in an inconsistent state relative to physical data on storage
- **Metadata Coordination**: GeoParquet may contain its own metadata (bounding boxes, CRS) in the Parquet footer, but Iceberg needs its own statistics in manifest files — requiring coordination between the two metadata systems

## Desired Alternative

An approach that writes data and updates Iceberg metadata atomically would be intrinsically more robust and simpler. This is a key advantage of using Iceberg-aware tools like [[apache-spark]] with [[apache-sedona]], which can write directly to Iceberg tables in a single, atomic operation.

## Related

- [[geospatial-etl-pipeline-iceberg]] — Proposed pipeline that could avoid this issue
- [[legacy-geospatial-etl-pipeline]] — Current pipeline affected by this issue
- [[gdal-ogr]] — The tool that creates the two-phase problem
- [[write-audit-publish-pattern]] — Iceberg pattern for safe write validation
- [[nessie-catalog-versioning]] — Catalog-level versioning that can help manage consistency
