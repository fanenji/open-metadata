---
type: entity
title: Dremio Geospatial Limitations
created: 2026-05-07
updated: 2026-05-07
tags: [dremio, geospatial, gis, limitations, udf, query-engine, sql, data-lakehouse]
related: ["iceberg-geospatial-support", "geospatial-etl-pipeline-iceberg", "dremio-mcp-server", "data-lakehouse", "data-platform-infrastructure-sizing", "minio", "dremio-geospatial-limitations"]
sources: ["Dati Geo con Dremio e Nessie.md", "Dimensionamento.md"]
---
# Dremio

Dremio is a SQL query engine for data lakehouses, providing fast interactive queries on data lakes. It uses a distributed architecture with a Coordinator and multiple Executors.

## Infrastructure Sizing

### Coordinator
- 1 node: 16 vCPU, 32 GB RAM, 200 GB storage

### Executors
- 3 nodes: 16 vCPU, 128 GB RAM, 300 GB storage each

### Distributed Storage
The executors require 300-500 GB of distributed storage, sourced from the MinIO cluster. This consumption must be factored into MinIO's usable capacity calculation (32 TiB) to avoid overcommitment.

## Geospatial Limitations

Dremio's support for geospatial data, particularly with Iceberg GEO V3 types, has several limitations that affect production spatial workloads.

### Key Limitations

- **Limited Native GEO Type Support:** Dremio likely lacks full native support for Iceberg's geometry and geography types. It may treat these columns as generic binary (WKB), requiring User-Defined Functions (UDFs) for spatial analysis.
- **UDF Dependency:** The `dremio-udf-gis` extension provides spatial SQL functions (ST_Intersects, ST_Distance, etc.), but introduces:
  - **Maintenance burden:** UDFs must be installed, maintained, and upgraded compatibly with Dremio versions.
  - **Performance risk:** UDFs may not be as optimized as native engine functions, especially compared to mature spatial databases like PostGIS.
  - **Completeness gaps:** The range of spatial functions may be less comprehensive than PostGIS or other dedicated spatial engines.
- **Spatial Query Optimization Uncertainty:** It is unclear how effectively Dremio leverages Iceberg's spatial metadata (bounding box statistics) or spatial partitioning/ordering (Z-ordering) for query optimization. Performance may rely primarily on generic Iceberg optimizations.
- **Missing Advanced Iceberg Features:** Dremio may not support Iceberg time travel via snapshots or access to metadata tables (history, snapshots, files, manifests), limiting historical analysis and debugging capabilities.

### Implications

The UDF dependency is the primary risk factor for production spatial workloads. For heavy spatial analytics, alternative query engines (e.g., Trino, Spark + Sedona) may be more suitable. See [[dremio-mcp-server]] for Dremio's general capabilities and configuration.