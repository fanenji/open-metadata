type: concept
title: Data Lifecycle Stages
created: 2026-04-29
updated: 2026-04-29
tags: [architecture, data-lifecycle, framework]
related: [unified-data-infrastructure-architecture, modern-business-intelligence-blueprint, multimodal-data-processing-blueprint, ai-ml-blueprint]
sources: ["Data-Report-Martin-Inline-Graphics-R8-1.pdf"]
---
# Data Lifecycle Stages

A foundational organizational framework from the [[unified-data-infrastructure-architecture]] that decomposes the data lifecycle into six sequential stages. This framework provides a common vocabulary for discussing data infrastructure architecture.

## The Six Stages

1. **Sources** — Operational systems (OLTP databases, applications/ERP), logs, third-party APIs, and event collectors that generate relevant business and operational data.

2. **Ingestion and Transformation** — The ELT process: Extract data from operational systems (E), Load it into storage aligning schemas between source and destination (L), Transform data to a structure ready for analysis (T). Tools include connectors (Fivetran, Stitch, Matillion), event streaming (Kafka, Pulsar, Kinesis), and data modeling (dbt, LookML).

3. **Storage** — Store data in formats accessible to query and processing systems, optimized for low cost, scalability, and analytic workloads (e.g., columnar storage). Includes data warehouses (Snowflake, BigQuery, Redshift), data lake table formats (Delta Lake, Iceberg, Hudi), and file/object storage (S3, GCS, ABS, HDFS).

4. **Historical** — Describe what happened in the past (including the very recent past). Provides an interface for analysts and data scientists to derive insights through query and processing engines (Presto, Dremio, Spark, Hive).

5. **Predictive** — Predict what will happen in the future. Build data-driven and ML applications using data science platforms, ML frameworks, and feature stores.

6. **Output** — Present results of data analysis to internal and external users. Embed data models into operational systems and applications. Includes dashboards (Looker, Superset, Tableau), embedded analytics, augmented analytics, and custom applications.

## Cross-Cutting Concerns

- Workflow orchestration coordinates the flow of data and execution of computations across the full lifecycle
- Data quality, performance, and governance ensure proper operation of all systems and datasets
- Metadata management, entitlements/security, and observability span all stages