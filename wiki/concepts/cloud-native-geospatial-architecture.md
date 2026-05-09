---
type: concept
title: Cloud-Native Geospatial Architecture
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, architecture, cloud-native, data-lakehouse, best-practices]
related: [data-lakehouse, cloud-native-geospatial-workflow, geospatial-etl-pipeline-iceberg, geoparquet-vs-iceberg-metadata, stac-standard, legacy-geospatial-etl-pipeline]
sources: ["Ingestione dati cartografici_ analisi alternative.md"]
---
# Cloud-Native Geospatial Architecture

Cloud-Native Geospatial Architecture refers to the design principles and patterns for building geospatial data pipelines that leverage cloud infrastructure for scalability, efficiency, and interoperability.

## Key Principles

1. **Object Storage as Primary Persistence**: Use S3-compatible object storage (MinIO, AWS S3, GCS, Azure Blob) for near-unlimited scalability, durability, and lower cost per GB compared to traditional file systems or databases.

2. **Cloud-Optimized Formats**: Adopt file formats designed for efficient access on object storage:
   - **COG (Cloud Optimized GeoTIFF)**: De facto standard for raster data, enabling partial reads via HTTP range requests
   - **GeoParquet**: Columnar format for vector data with standardized geospatial metadata and spatial partitioning support

3. **Scalable Compute**: Use serverless functions (AWS Lambda), container orchestration (Kubernetes), or distributed computing frameworks (Apache Spark) depending on transformation complexity and data volume.

4. **Compute-Storage Separation**: Scale compute and storage independently based on needs.

5. **Catalog Integration**: Use metadata catalogs for data discovery and management:
   - **STAC (SpatioTemporal Asset Catalog)**: Emerging standard for Earth observation data
   - **Data Catalogs**: DataHub, OpenMetadata for internal platform governance

## Architectural Patterns

### Event-Driven Pipeline
An event (e.g., new raw file uploaded to S3) triggers automatic processing (e.g., Lambda function or container) that transforms data to the desired format and saves it to final storage. Suitable for frequent updates or near-real-time processing of individual files.

### Batch Pipeline (Current Approach)
An orchestrator (Airflow, Dagster, Prefect) schedules periodic jobs that extract data from batch sources (databases, APIs, file systems), transform using GDAL, Spark, or Python scripts, and load results (COG, GeoParquet) to object storage.

### Streaming Pipeline
Systems like Apache Kafka ingest continuous geospatial data streams (e.g., GPS positions). Streaming engines (Spark Streaming, Flink, Kafka Streams) process data in real-time, potentially using libraries like GeoMesa, and write results to object storage, databases, or other Kafka topics.

## Lakehouse Integration

Regardless of the ingestion pattern, processed data (GeoParquet, COG) is typically registered in a table format like Apache Iceberg or Delta Lake, adding transactional control, versioning, schema evolution, and multi-engine access.

## Related

- [[data-lakehouse]] — The target architecture for cloud-native geospatial data
- [[cloud-native-geospatial-workflow]] — Practical pattern for querying remote GeoParquet with DuckDB
- [[geospatial-etl-pipeline-iceberg]] — Proposed cloud-native ETL pattern for spatial data
- [[legacy-geospatial-etl-pipeline]] — Current pipeline being modernized
- [[stac-standard]] — Emerging standard for EO data cataloging
