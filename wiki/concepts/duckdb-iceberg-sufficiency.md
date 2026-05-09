---
type: concept
title: DuckDB-Iceberg Sufficiency
created: 2025-02-10
updated: 2025-02-10
tags: [duckdb, iceberg, data-architecture, lightweight-stack]
related: [duckdb, iceberg, duckdb-iceberg-limitations, single-user-database-limitation, medium-scale-data-architecture, vendor-lock-in-tradeoff, embedded-query-engine-for-bi, data-lakehouse, elt-pattern]
sources: ["Quando duckdb e iceberg sono sufficienti?.md"]
---
# DuckDB-Iceberg Sufficiency

The proposition that [[duckdb]] (as a lightweight, in-process compute/transformation engine) combined with [[iceberg]] (as an open table format on object storage like S3) is sufficient for medium-scale data workloads, replacing traditional data warehouses.

## Core Idea

For teams processing a few TB of data per year, a full distributed system (Spark, Snowflake, Databricks) may be overkill. DuckDB + Iceberg on S3 offers a simpler, cheaper, and less vendor-locked alternative:

- **DuckDB** handles the "T" in ELT/ETL — in-process SQL transformations running in Python scripts or applications.
- **Iceberg** provides ACID-compliant, queryable storage on object storage, decoupling compute from storage.
- **Object storage (S3/GCS)** serves as the shared data layer, enabling multiple consumers to read the same Iceberg tables.

## When It Works

- **Data volume:** <1-2 TB/year. DuckDB's single-node, in-memory architecture handles this efficiently.
- **Consumer type:** Technical users (data scientists, analysts) who can run DuckDB locally or use programmatic queries.
- **Workload type:** Batch processing, aggregation, joins of moderate datasets.
- **Team size:** Small teams where concurrent write contention is manageable.

## When It Fails

- **Multi-user concurrency:** DuckDB is single-user. Multiple concurrent writers require workarounds.
- **Iceberg integration gaps:** DuckDB lacks native Iceberg catalog read support, write support, and efficient predicate pushdown.
- **Security requirements:** No RBAC or column-level security — access control must be handled at the storage layer (IAM).
- **Scale beyond threshold:** Performance degrades unpredictably beyond a few TB. No built-in query profiling or optimization tools.
- **Non-technical consumers:** BI tools cannot directly query Iceberg without an intermediate engine.

## Future Outlook

The architecture could become mainstream if BI tools embed DuckDB-like engines (e.g., [[Rill]]) to query Iceberg/Delta files directly, eliminating the need for a dedicated warehouse for most organizations. DuckDB's Iceberg integration is also expected to improve over time.

## Related Concepts

- [[duckdb-iceberg-limitations]] — Detailed limitations of DuckDB's Iceberg support.
- [[single-user-database-limitation]] — DuckDB's design constraint.
- [[medium-scale-data-architecture]] — The broader category of lightweight data stacks.
- [[vendor-lock-in-tradeoff]] — The trade-off between avoiding vendor lock-in and losing vendor optimizations.
- [[embedded-query-engine-for-bi]] — BI tools embedding query engines.