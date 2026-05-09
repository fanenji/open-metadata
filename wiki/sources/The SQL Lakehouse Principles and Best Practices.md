---
type: source
title: "The SQL Lakehouse: Principles and Best Practices"
created: 2026-05-07
updated: 2026-05-07
tags: [sql-lakehouse, data-lakehouse, dremio, dataops, best-practices]
related: [sql-lakehouse, data-lakehouse, dataops-definition, dremio, iceberg-table-versioning, nessie-catalog-versioning, data-federation-for-sensitive-data, elt-pattern]
sources: ["The SQL Lakehouse Principles and Best Practices.md"]
authors: [Dremio]
year: 2021
url: "https://www.dremio.com/blog/the-sql-lakehouse-principles-and-best-practices/"
venue: "Dremio Blog"
---
# The SQL Lakehouse: Principles and Best Practices

A vendor-published thought leadership article by [[Dremio]] (October 2021) defining the SQL lakehouse concept and presenting best practices for enterprise adoption. The article argues that the SQL lakehouse simplifies BI workloads by eliminating ETL copies and applying SQL directly to object stores, combining data warehouse querying with data lake flexibility.

## Key Claims

- The SQL lakehouse "sweeps aside" ETL copies by applying SQL queries directly to object stores
- It offers an open architecture via open APIs and data formats (Apache Iceberg, Parquet, ORC, CSV, JSON)
- It assists governance by consolidating data views into a single semantic layer
- It accelerates queries with columnar processing, parallel processing, and query pre-computations

## Best Practices Presented

1. **Start with DataOps** — Apply DevOps and agile practices to data pipeline management
2. **Assemble the right team** — Align executive sponsors, technical leads, and functional contributors
3. **Integrate a variety of data** — Use a federated approach to access data across cloud object stores, on-premises databases, IoT sensors, and HDFS
4. **Open your architecture** — Maintain data portability across tools, platforms, formats, APIs, and languages

## Evidence and Limitations

The article relies on customer testimonials from Knauf Insulation, HyreCar, and Raiffeisenbank, presented at Dremio's Subsurface industry event. No quantitative benchmarks, cost comparisons, or independent validation are provided. The evidence strength is weak — the article is primarily a vendor positioning piece.

## Internal Tensions

- Claims "no ETL copies" but acknowledges "periodic ETL batches or streaming pipelines" for data ingestion
- Promotes both a "federated approach" (accessing data in place) and a "single semantic layer" — these can conflict when data sources have incompatible schemas
- Governance simplification claim contrasts with [[data-catalog-critique]] suggesting centralized approaches often fail

## Connections to Existing Wiki

- Directly extends [[data-lakehouse]] — defines a specific SQL-focused subset
- Supports [[iceberg-table-versioning]] and [[nessie-catalog-versioning]] as open components
- Related to [[data-federation-for-sensitive-data]] via the federated approach concept
- Aligns with [[elt-pattern]] philosophy of eliminating unnecessary ETL copies
- Connects to [[dataops-definition]] as a foundational best practice