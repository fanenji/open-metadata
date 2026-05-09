---
type: concept
title: Iceberg REST Catalog
created: 2026-02-13
updated: 2026-02-13
tags: [iceberg, catalog, api, standard, interoperability]
related: [lakekeeper, apache-polaris, nessie-catalog-versioning, dremio, data-lakehouse-versioning-strategies]
sources: ["Nessie vs LakeKeeper.md"]
---
# Iceberg REST Catalog

The Iceberg REST Catalog is a standard API specification for interacting with Apache Iceberg catalogs. It defines a RESTful interface for catalog operations, enabling broad engine interoperability.

## Key Characteristics

- **Standard API**: Provides a uniform way for query engines (Dremio, Spark, Flink, Trino) to interact with Iceberg catalogs.
- **Engine Agnostic**: Any engine that implements the REST API can work with any catalog that exposes it.
- **Table-level operations**: Supports standard Iceberg operations including snapshot management, time travel, schema evolution, and table-level branching/tagging.
- **Security**: Supports vended credentials for secure storage access.

## Ecosystem Implications

- **Interoperability**: Reduces vendor lock-in — catalogs and engines can be mixed and matched.
- **Standardization**: Encourages a pluggable catalog ecosystem where new catalogs (LakeKeeper, Polaris) can immediately work with existing engines.
- **Governance**: Enables centralized governance models where a single catalog controls access across multiple engines.

## Implementations

- **LakeKeeper**: Rust-based, security-focused implementation
- **Apache Polaris**: Java-based, governance-focused implementation
- **Nessie**: Java-based, catalog-level versioning (also supports REST API)

## Related Pages

- [[lakekeeper]] — Rust-based REST catalog implementation
- [[apache-polaris]] — Governance-focused REST catalog implementation
- [[nessie-catalog-versioning]] — Catalog-level versioning approach
- [[dremio]] — Query engine that consumes REST catalogs
- [[data-lakehouse-versioning-strategies]] — Broader versioning comparison
