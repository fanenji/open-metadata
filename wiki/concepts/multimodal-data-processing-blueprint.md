type: concept
title: Multimodal Data Processing Blueprint
created: 2026-04-29
updated: 2026-04-29
tags: [architecture, blueprint, data-processing, streaming, batch]
related: [unified-data-infrastructure-architecture, data-lifecycle-stages, modern-business-intelligence-blueprint, ai-ml-blueprint, data-lakehouse]
sources: ["Data-Report-Martin-Inline-Graphics-R8-1.pdf"]
---
# Multimodal Data Processing Blueprint

Blueprint #2 of the [[unified-data-infrastructure-architecture]], representing an architecture that supports multiple data processing modalities: batch, streaming, and interactive query workloads. This blueprint extends the BI pattern to handle diverse data velocities and processing requirements.

## Architecture

The blueprint follows the [[data-lifecycle-stages]] with expanded capabilities:
- **Sources**: Same as BI blueprint plus logs and event streams
- **Ingestion**: Adds event streaming (Confluent/Kafka, Pulsar, AWS Kinesis) and stream processing (Databricks/Spark, Flink) alongside traditional connectors
- **Storage**: Data lakehouse table formats (Delta Lake, Iceberg, Hudi) on object storage (S3/GCS/ABS/HDFS), with Parquet/ORC/Avro as file formats. Data warehouse remains for structured analytics
- **Historical/Query**: Multiple query engines — ad hoc (Presto, Dremio/Drill, Impala), batch (Hive), real-time analytics (Druid, Clickhouse, Rockset), Spark Platform (Databricks, EMR)
- **Output**: Same as BI blueprint

## Key Characteristics

- Supports batch, streaming, and interactive workloads simultaneously
- Data lakehouse as the central storage layer, combining lake flexibility with warehouse performance
- Multiple query engines optimized for different use cases
- Higher operational complexity than the BI blueprint
- Requires stronger data governance and metadata management

## Relationship to Other Blueprints

This blueprint represents an evolution from [[modern-business-intelligence-blueprint]] for organizations that need real-time data processing alongside traditional batch analytics. It shares the output layer with the BI blueprint but adds significant complexity in ingestion and storage.