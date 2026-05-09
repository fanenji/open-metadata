type: source
title: "A Unified Data Infrastructure Architecture"
created: 2026-04-29
updated: 2026-04-29
tags: [architecture, data-infrastructure, reference-architecture, blueprints]
related: [unified-data-infrastructure-architecture, modern-business-intelligence-blueprint, multimodal-data-processing-blueprint, ai-ml-blueprint, data-lifecycle-stages, data-lakehouse, feature-store-architecture, dbt]
sources: ["Data-Report-Martin-Inline-Graphics-R8-1.pdf"]
---
# A Unified Data Infrastructure Architecture

A conceptual reference architecture by Martin that decomposes the modern data infrastructure landscape into a unified lifecycle model and three common blueprints. The document presents a visual taxonomy of tools and platforms organized by lifecycle stage (Sources → Ingestion/Transformation → Storage → Historical → Predictive → Output), with each blueprint highlighting different organizational patterns and tool combinations.

## Key Concepts

- **[[unified-data-infrastructure-architecture]]** — The overarching framework covering the full data lifecycle
- **[[modern-business-intelligence-blueprint]]** — Blueprint #1: Traditional BI pipeline with ingestion, warehouse, modeling, and dashboards
- **[[multimodal-data-processing-blueprint]]** — Blueprint #2: Architecture supporting batch, streaming, and interactive query workloads
- **[[ai-ml-blueprint]]** — Blueprint #3: Architecture for ML lifecycle including feature stores, training, and inference
- **[[data-lifecycle-stages]]** — The Sources → Ingestion/Transformation → Storage → Historical → Predictive → Output framework

## Tool Categories

The document catalogs tools across multiple categories:
- **Ingestion**: Fivetran, Stitch, Matillion, Event Streaming (Kafka, Pulsar, Kinesis)
- **Data Modeling**: dbt, LookML
- **Storage**: Data Warehouses (Snowflake, BigQuery, Redshift), Data Lake table formats (Delta Lake, Iceberg, Hudi), File/Object Storage (S3, GCS, ABS, HDFS)
- **Query & Processing**: Ad Hoc Query Engines (Presto, Dremio/Drill, Impala), Batch Query (Hive), Real-time Analytics (Druid, Clickhouse, Rockset), Spark Platform (Databricks, EMR)
- **Orchestration**: Airflow, Dagster, Prefect
- **Quality & Governance**: Great Expectations, DataHub, Collibra, Alation, Privacera, Immuta
- **Output**: Dashboards (Looker, Superset, Mode, Tableau), Embedded Analytics, Augmented Analytics, App Frameworks, Custom Apps

## Limitations

This is a purely descriptive reference architecture without empirical validation, case studies, or comparative analysis. It serves as a classification framework rather than a prescriptive guide. No discussion of trade-offs, costs, or organizational maturity requirements is provided.