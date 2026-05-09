type: concept
title: Modern Business Intelligence Blueprint
created: 2026-04-29
updated: 2026-04-29
tags: [architecture, blueprint, business-intelligence, analytics]
related: [unified-data-infrastructure-architecture, data-lifecycle-stages, multimodal-data-processing-blueprint, ai-ml-blueprint, dbt, data-lakehouse]
sources: ["Data-Report-Martin-Inline-Graphics-R8-1.pdf"]
---
# Modern Business Intelligence Blueprint

Blueprint #1 of the [[unified-data-infrastructure-architecture]], representing the traditional BI pipeline pattern. This blueprint focuses on delivering analytical insights from operational data through a structured pipeline of ingestion, storage, modeling, and visualization.

## Architecture

The blueprint follows the standard [[data-lifecycle-stages]] with emphasis on:
- **Sources**: OLTP databases (via CDC), applications/ERP, third-party APIs, event collectors
- **Ingestion**: Connectors (Fivetran, Stitch, Matillion), event streaming (Kafka, Pulsar, Kinesis)
- **Storage**: Data warehouse (Snowflake, BigQuery, Redshift) as the primary analytical store, with data lake (S3/GCS/ABS/HDFS) for raw data
- **Data Modeling**: dbt and LookML for transforming raw data into analytical models
- **Historical/Query**: Ad hoc query engines (Presto, Dremio/Drill, Impala), batch query (Hive), real-time analytics (Druid, Clickhouse, Rockset)
- **Output**: Dashboards (Looker, Superset, Mode, Tableau), embedded analytics, augmented analytics, app frameworks (Plotly Dash, Streamlit), custom apps

## Key Characteristics

- Primary consumers are business analysts and decision-makers
- Batch-oriented with scheduled refreshes
- Centralized data warehouse as the single source of truth
- SQL-centric data modeling
- Mature tool ecosystem with well-established vendors

## Relationship to Other Blueprints

This is the most common and mature blueprint. Organizations typically start here before evolving to [[multimodal-data-processing-blueprint]] or [[ai-ml-blueprint]] as their data needs grow.