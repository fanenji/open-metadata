---
type: concept
title: SQL Lakehouse
created: 2026-05-07
updated: 2026-05-07
tags: [sql-lakehouse, data-lakehouse, architecture, dremio]
related: [data-lakehouse, dataops-definition, dremio, elt-pattern, data-federation-for-sensitive-data, iceberg-table-versioning, nessie-catalog-versioning]
sources: ["The SQL Lakehouse Principles and Best Practices.md"]
---
# SQL Lakehouse

The SQL lakehouse is a subset of cloud data platforms that simplifies BI workloads by applying SQL queries directly to object stores, eliminating the ETL copies traditionally required by data warehouses. It merges data warehouse SQL querying capabilities with data lake object storage flexibility, consuming elastic cloud compute and storage resources.

## Key Characteristics

- **Direct SQL on object stores**: Queries, transforms, and updates data objects without intermediate ETL copies
- **Common semantic layer**: Presents transformed data to BI tools through a unified interface
- **Open architecture**: Supports open APIs (ODBC, JDBC, REST), open data formats (Apache Iceberg, Parquet, ORC, CSV, JSON), and multiple programming languages (Python, R, Scala, Java)
- **Federated access**: Queries data across cloud object stores, on-premises databases, IoT sensors, and HDFS
- **Query acceleration**: Uses columnar processing, parallel processing, and query pre-computations

## Relationship to Data Lakehouse

The SQL lakehouse is a specialization of the broader [[data-lakehouse]] concept, emphasizing SQL as the primary interface for BI workloads. While the general data lakehouse encompasses any architecture combining data lake and warehouse features, the SQL lakehouse specifically prioritizes direct SQL access to object storage.

## Best Practices

1. **Start with [[dataops-definition|DataOps]]** — Apply DevOps and agile practices to data pipeline management
2. **Assemble the right team** — Align executive sponsors, technical leads, and functional contributors
3. **Integrate a variety of data** — Use a federated approach to access diverse data sources
4. **Open your architecture** — Maintain data portability across tools, platforms, and formats

## Critical Analysis

The SQL lakehouse concept is primarily promoted by [[Dremio]], which sells a SQL lakehouse product. The evidence for its benefits is largely anecdotal, based on customer testimonials rather than independent benchmarks. Key tensions include:

- The "no ETL copies" claim is overstated — periodic ETL batches or streaming pipelines are still needed for data ingestion
- The federated approach and single semantic layer can conflict when data sources have incompatible schemas
- Governance simplification claims contrast with evidence that centralized approaches often face adoption challenges

## Connections

- Extends [[data-lakehouse]] as a SQL-focused specialization
- Aligns with [[elt-pattern]] philosophy of eliminating unnecessary ETL copies
- Related to [[data-federation-for-sensitive-data]] via federated access patterns
- Supported by open table formats like [[iceberg-table-versioning]] and version control platforms like [[nessie-catalog-versioning]]