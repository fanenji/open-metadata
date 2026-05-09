---
type: source
title: "Beyond Storing Data: How to Use DuckDB, MotherDuck and Kestra for ETL"
created: 2026-04-08
updated: 2026-04-08
tags: [duckdb, kestra, motherduck, etl, data-engineering]
related: [duckdb, motherduck, kestra, hybrid-execution-pattern, event-driven-etl, data-masking]
sources: ["Beyond Storing Data How to Use DuckDB, MotherDuck and Kestra for ETL.md"]
authors: [Anna Geller]
year: 2023
url: "https://motherduck.com/blog/motherduck-kestra-etl-pipelines/"
venue: "MotherDuck Blog"
---
# Beyond Storing Data: How to Use DuckDB, MotherDuck and Kestra for ETL

This article explores the use of [[duckdb]] and [[motherduck]] as powerful data transformation engines within orchestrated workflows using [[kestra]]. It covers several practical use cases:

- **Simplified Reporting**: Using DuckDB to query S3 directly, bypassing the need for a traditional warehouse schema definition for simple aggregate reports.
- **Data Masking**: Utilizing DuckDB's `hash()` and `md5()` functions to obfuscate PII (Personally Identifiable Information) during the ETL process between extraction and loading.
- **Lightweight Transformation**: Using the `dbt-duckdb` adapter to run modular SQL transformations, leveraging MotherDuck for persistent storage and hybrid execution.
- **Event-Driven Anomaly Detection**: Combining Kestra's S3 event triggers with DuckDB queries to automatically detect and alert on data outliers as soon as new files arrive in object storage.

The "Modern Trio" of **DuckDB** (compute), **MotherDuck** (cloud/persistence), and **Kestra** (orchestration) is presented as a highly efficient, low-overhead alternative to traditional, heavy-duty data stacks.
