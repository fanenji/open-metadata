---
type: entity
title: Databricks
created: 2026-05-06
updated: 2026-05-07
tags:
  - cloud-warehouse
  - data-platform
  - delta-lake
  - organization
  - spark
  - platform
  - data-lakehouse
  - company
  - platform-vendor
  - apache-iceberg
  - data-warehouse
  - lakehouse
  - modern-data-stack
related:
  - dbt-python-models-support
  - szehon-ho
  - iceberggo-vs-delta-lake-geospatial
  - iceberggo-v3-spec
  - unity-catalog
  - databricks-sensitive-data-handling
  - sensitive-data-handling-strategies
  - apache-iceberg
  - tabular
  - iceberg-vendor-standardization
  - data-lakehouse
  - snowflake-zero-copy-clone
  - bigquery
  - platformization
sources:
  - Connettori dbt e Python.md
  - Geospatial Tables in the Open Lakehouse A New Era for Iceberg & Parquet.md
  - Handling Sensitive Data in Your Data Platform.md
  - Is Apache Iceberg Melting?.md
  - The Modern Data Stack in 2025 What Actually Won.md
---
# Databricks

Databricks is a unified analytics platform and data and AI platform company built on Apache Spark, used for data engineering, data science, and machine learning. It is the fastest-growing data warehouse/lakehouse platform, surging from 20% to 32% adoption (+60% YoY) between 2023 and 2024, positioning itself as the primary challenger to [[Snowflake]]'s market leadership. The platform develops Delta Lake, a competing open table format to Apache Iceberg, and has committed to full interoperability with Apache Iceberg, especially after its acquisition of Tabular (June 2024). Databricks supports dbt Python models through its integrated Spark clusters.

## Market Position and Growth

- Adoption surged from 20% to 32% (+60% YoY) between 2023–2024.
- Primary challenger to [[Snowflake]].
- **Growth Drivers**:
  - [[Unity Catalog]] (released 2023) simplified governance.
  - Delta Lake matured significantly.
  - ML integration is stronger than competitors.
  - Successful **"lakehouse"** messaging resonated with the market.
- **Job Market**: Databricks skills appear in 42% of job postings (vs. 31% for Snowflake) and are growing +15% YoY. The source predicts Databricks will overtake Snowflake in growth rate (not total users) by 2026–2027.

## Platformization

Databricks is expanding into a full platform, offering:

- [[Unity Catalog]] (governance)
- Delta Live Tables (ETL)
- Databricks SQL (BI)
- MLflow (ML lifecycle)
- Workflows (orchestration)

This [[platformization]] trend is a key theme of the 2025 modern data stack, with warehouse vendors becoming end-to-end platforms.

## Apache Iceberg and Delta Lake

Databricks develops Delta Lake, a competing open table format to Apache Iceberg. In June 2024, Databricks acquired Tabular, the company founded by Iceberg creators Ryan Blue, Daniel Weeks, and Jason Reid. This acquisition is cited as a serious ecosystem accelerant for Iceberg adoption. Databricks has publicly announced full Apache Iceberg support, including the ability to query and govern Iceberg tables managed by external catalogs like AWS Glue, Hive Metastores, and Snowflake catalogs.

[[Szehon Ho]], an Iceberg PMC member working at Databricks, characterized Iceberg as read-optimized and Delta Lake as write-optimized, noting the tension between open standards and vendor proprietary formats. Databricks' position on Iceberg GEO adoption remains cautious.

## Data Governance and Security

[[Unity Catalog]] provides Data Classification and Attribute-Based Access Control (ABAC). Additionally, Databricks offers built-in functions for masking, encryption, and hashing for sensitive data handling.

## dbt Python Models Support

Databricks supports dbt Python models by utilizing its integrated Spark clusters to execute Python-based transformations.