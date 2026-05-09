---
type: source
title: "Dati Geo con Dremio e Nessie: Geospatial Challenges with Iceberg, Nessie, and Dremio"
created: 2026-03-18
updated: 2026-03-18
tags: [geospatial, iceberg, dremio, nessie, gis, data-lakehouse]
related: [iceberg-geospatial-support, dremio-geospatial-limitations, geospatial-etl-pipeline-iceberg, geoparquet-vs-iceberg-metadata, nessie-catalog-versioning, iceberg-table-versioning, dremio-mcp-server, data-lakehouse-versioning-nessie-vs-iceberg-vs-lakefs]
sources: ["Dati Geo con Dremio e Nessie.md"]
---
# Dati Geo con Dremio e Nessie: Geospatial Challenges with Iceberg, Nessie, and Dremio

This source analyzes the challenges and potential problems of using Apache Iceberg, Nessie, and Dremio together for managing and analyzing geospatial data. It highlights issues stemming from the relative novelty of native geospatial support in Iceberg and the specific integration characteristics between the components.

## Key Findings

- **Iceberg GEO V3 Maturity:** Native geometry/geography types are recent (V3), with limited query engine adoption and evolving best practices for encoding (WKB vs GeoArrow), spatial partitioning (XZ2, Hilbert curves), and indexing.
- **Dremio's Limited Native GEO Support:** Dremio likely lacks full native support for Iceberg GEO types, potentially treating them as generic binary (WKB) and requiring User-Defined Functions (UDFs) like `dremio-udf-gis` for spatial analysis. This introduces maintenance, performance, and completeness risks.
- **Spatial Query Optimization Uncertainty:** It is unclear how effectively Dremio can leverage Iceberg's spatial metadata (bounding box statistics) or spatial partitioning/ordering (Z-ordering) for query optimization.
- **Missing Advanced Iceberg Features:** Dremio may not support advanced Iceberg features like time travel via snapshots or access to metadata tables (history, snapshots, files, manifests).
- **ETL Pipeline Complexity:** Common ETL tools (GDAL/OGR) are not Iceberg-aware, requiring a separate Spark step to register data into Iceberg tables, adding complexity and latency.
- **GeoParquet vs Iceberg Metadata Overlap:** Potential inconsistency between GeoParquet's embedded metadata (CRS, bounding box per row group) and Iceberg's manifest-level statistics.
- **Nessie Adds Operational Complexity:** While powerful for governance and isolation (branching/merging), Nessie adds another layer of abstraction and configuration complexity, with dual time travel (table-level vs catalog-level) requiring careful attention.

## Implications

The primary risk factor for production spatial workloads is the UDF dependency in Dremio. The core issue is Dremio's GEO support, not Nessie. The stack is viable but requires careful design, testing, and potentially alternative query engines (e.g., Trino, Spark) for heavy spatial workloads.
