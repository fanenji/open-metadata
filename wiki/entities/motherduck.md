---
type: entity
title: MotherDuck
created: 2026-04-08
updated: 2026-05-07
tags: [cloud, duckdb, serverless, data-warehouse, database, managed-service, platform, collaborative]
related: [duckdb, hybrid-execution-pattern, kestra, aws-s3, duckdb-labs, jordan-tigani, embedded-olap-database, duckdb-spatial-extension, simon-spati]
sources: ["Beyond Storing Data How to Use DuckDB", "MotherDuck and Kestra for ETL.md", "DuckDB — What’s the Hype About?.md", "Mastering Geospatial Analysis with DuckDB Spatial and MotherDuck.md"]
---

# MotherDuck

[[MotherDuck]] is a commercial serverless cloud service built on top of [[DuckDB]], co-founded by [[Jordan Tigani]] (former BigQuery product lead at Google) and Tino Tereshko (also ex-Google). It provides a managed environment that scales DuckDB workloads to the cloud while retaining the simplicity of the in-process engine. A defining capability is its **hybrid execution** model, which enables seamless querying across datasets residing locally on a user's machine and datasets stored in the cloud. MotherDuck also acts as a collaborative backend platform that extends DuckDB for scaling SQL and geospatial workloads, offering shared databases and cloud-based query execution.

## Funding

- Announced a $47.5 M funding round in November 2022  
- Led by a16z (early investors in Databricks) and Redpoint Ventures (early investors in Snowflake)  
- A strategic partnership with [[DuckDB Labs]] was announced simultaneously  

## Core Features

- **Hybrid Execution** – Seamless querying across local and cloud datasets.  
- **Persistent Storage** – Managed, persistent storage for tables and files, overcoming the ephemeral nature of standard in‑process DuckDB.  
- **Secrets Management** – Centralized management of credentials (e.g., AWS S3 keys) to avoid hard‑coding sensitive information in SQL or orchestration scripts.  
- **Collaborative SQL IDE** – A notebook‑like environment for interactive analysis, data management, and sharing results with teammates.  
- **Shared Databases** – Databases can be shared across users and environments using the `ATTACH 'md:_share/...'` syntax, enabling team-wide data access.  
- **Serverless Architecture** – No database server management is required; DuckDB instances connect directly to MotherDuck’s cloud backend.  
- **Scalable Storage** – Data is stored in MotherDuck’s cloud infrastructure, accessible from any location.  
- **Extension Ecosystem Integration** – Full support for DuckDB extensions, including the [[duckdb-spatial-extension]] for geospatial analysis.  

### Usage Example

```sql
-- Attach a shared Foursquare database on MotherDuck
ATTACH 'md:_share/foursquare/0cbf467d-03b0-449e-863a-ce17975d2c0b';
USE foursquare;
```

## Positioning and Role in the Modern Data Stack

MotherDuck follows the classic open‑source commercialization playbook (similar to Databricks with Spark or Confluent with Kafka): taking an open‑source tool with momentum and building a managed cloud service around it. The service acts as the “cloud warehouse” layer in a lightweight architecture, enabling a “Low‑Ops” approach by reducing the operational burden of managing complex infrastructure while providing the scalability required for production‑grade ETL.

## Relationship with DuckDB and DuckDB Labs

MotherDuck is not a replacement for DuckDB but a complementary platform that delivers:
- Persistent storage and sharing capabilities  
- Multi‑user collaboration  
- Cloud‑based execution for larger‑than‑memory workloads  
- Tight integration with DuckDB’s extension ecosystem, including the Spatial extension  

A strategic partnership with [[DuckDB Labs]] provides core DuckDB expertise, while MotherDuck builds and maintains the managed cloud layer. This relationship enables workflows such as [[cloud-native-geospatial-workflow]], where spatial analysis runs seamlessly on MotherDuck’s infrastructure.