---
type: concept
title: Vendor Lock-In Tradeoff
created: 2025-02-10
updated: 2025-02-10
tags: [vendor-lock-in, architecture, tradeoff, data-engineering]
related: [duckdb-iceberg-sufficiency, medium-scale-data-architecture, data-lakehouse]
sources: ["Quando duckdb e iceberg sono sufficienti?.md"]
---
# Vendor Lock-In Tradeoff

The trade-off between avoiding vendor lock-in by using open-source, file-based architectures and losing the performance optimizations, tooling, and support that vendors provide.

## The Argument for Avoiding Lock-In

- **Cost control:** No surprise bills from cloud warehouse compute or storage.
- **Portability:** Data in open formats ([[iceberg]], Parquet) can be queried by any engine.
- **Flexibility:** No dependency on a single vendor's roadmap or pricing changes.
- **Simplicity:** Fewer moving parts, less operational overhead.

## The Argument for Accepting Lock-In

- **Performance:** Vendors invest heavily in query optimization, caching, and hardware integration. Open-source alternatives may not match this.
- **Tooling:** Cloud warehouses provide built-in query profiling, monitoring, RBAC, and security features.
- **Support:** Vendor support contracts provide SLAs and expertise.
- **Innovation:** Vendors often ship new features faster than open-source projects.

## The "Common Denominator" Problem

As noted by commenter [[LargeSale8354]] in the DuckDB-Iceberg discussion, avoiding vendor lock-in means "limiting yourself to common denominator technology." You cannot use vendor-specific optimizations (e.g., Snowflake's caching, Redshift's sort keys) because your stack must work across any engine.

## Historical Parallel: Hadoop

The Hadoop ecosystem was promoted as a "data warehouse killer" but failed to deliver on performance and concurrency promises. The lesson: storage is cheap, but storage performance is not. Open formats alone do not guarantee good query performance.

## Decision Framework

| Factor | Favor Open Stack | Favor Vendor Stack |
|--------|------------------|-------------------|
| Data volume | <2 TB/year | >10 TB/year |
| Team size | Small, technical | Large, diverse |
| Performance needs | Moderate | High, predictable |
| Security requirements | Basic (IAM) | RBAC, column-level, audit |
| Budget sensitivity | High | Low |
| Consumer type | Technical | Mixed, including BI tools |

## Related Concepts

- [[duckdb-iceberg-sufficiency]] — An open-stack architecture that accepts this tradeoff.
- [[medium-scale-data-architecture]] — The context where this tradeoff is most relevant.