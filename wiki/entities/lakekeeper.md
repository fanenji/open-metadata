---
type: entity
title: LakeKeeper
created: 2026-02-13
updated: 2026-02-13
tags: [iceberg, catalog, rust, security, open-source]
related: [iceberg-rest-catalog, apache-polaris, nessie-catalog-versioning, dremio, minio, openfga, open-policy-agent]
sources: ["Nessie vs LakeKeeper.md"]
---
# LakeKeeper

LakeKeeper is an open-source Apache Iceberg REST Catalog built in Rust. It is designed as a lightweight, high-performance, and security-focused alternative to JVM-based Iceberg catalogs like Nessie and Polaris.

## Key Characteristics

- **Architecture**: Single binary executable written in Rust, no JVM dependency. Uses a normalized relational database (e.g., PostgreSQL) for metadata storage.
- **Versioning**: Table-level versioning via the Iceberg REST API. Supports standard Iceberg time travel, snapshot management, and table-level branching/tagging.
- **Multi-table transactions**: Enabled through its relational database backend.
- **Security**: Strong focus on fine-grained access control with integrations for OpenFGA and Open Policy Agent (OPA). Supports vended credentials for secure storage access.
- **Deployment**: Simple to deploy as a single binary.
- **Compatibility**: Standard Iceberg REST Catalog, compatible with any engine that supports the REST API (Dremio, Spark, Flink, Trino). Works with S3-compatible storage like MinIO.

## Pros

- High performance and low overhead (Rust)
- Strong modern security integrations (OPA, OpenFGA)
- Simple deployment (single binary)
- Broad Iceberg ecosystem compatibility

## Cons

- Lacks catalog-level branching and merging (table-level only)
- Newer project with a smaller but growing community

## Strategic Fit

Best suited for teams prioritizing performance, security, and deployment simplicity over catalog-level Git-like workflows.

## Related Pages

- [[iceberg-rest-catalog]] — The standard API LakeKeeper implements
- [[nessie-catalog-versioning]] — Catalog-level versioning alternative
- [[apache-polaris]] — Centralized governance alternative
- [[dremio]] — Target query engine
- [[data-lakehouse-versioning-strategies]] — Broader versioning comparison
