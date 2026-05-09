---
type: concept
title: Two-Phase Ingestion Problem
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, ingestion, iceberg, consistency]
related: [gdal-ogr-container-pipeline, spark-sedona-geospatial-etl, geospatial-etl-pipeline-iceberg, iceberg-geospatial-support]
sources: ["Ingestione Dati Geospaziali_ Analisi e Opzioni_ .md"]
---
# Two-Phase Ingestion Problem

The two-phase ingestion problem describes the fundamental architectural disconnect when using GDAL/OGR to write files to object storage and then requiring a separate process to register those files in Apache Iceberg tables.

## The Problem

1. **Phase 1 (GDAL writes):** GDAL/OGR writes GeoParquet (vector) or COG (raster) files to MinIO object storage. GDAL is completely unaware of Iceberg's table structure and metadata.

2. **Phase 2 (Iceberg registration):** A separate process (Spark, Flink, or Iceberg library) must:
   - Identify the new files written by GDAL.
   - Compute column-level statistics (counts, nulls, min/max) for Iceberg manifest files.
   - Update Iceberg manifest files with references to new files and their statistics.
   - Create a new Iceberg snapshot and update the catalog pointer (Nessie).

## Consequences

- **Complexity:** Requires coordination between two independent systems.
- **Latency:** Data is not queryable via Iceberg until Phase 2 completes.
- **Consistency Risks:** If Phase 2 fails after GDAL writes files, the Iceberg table becomes inconsistent with physical storage.
- **Operational Overhead:** Monitoring and error handling must span both phases.

## Solutions

1. **Spark+Sedona:** Writes directly to Iceberg tables, avoiding the two-phase problem entirely. This is the most promising alternative.
2. **GDAL with Iceberg-aware output:** Not currently supported; would require GDAL to understand Iceberg's manifest structure.
3. **Transactional file staging:** Use Iceberg's write-audit-publish pattern with staged files, but this still requires a separate registration step.

## Related

- [[geospatial-etl-pipeline-iceberg]] — The existing page describing the multi-step ETL pattern that suffers from this problem.
- [[spark-sedona-geospatial-etl]] — The alternative approach that avoids the two-phase problem.