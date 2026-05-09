---
type: entity
title: Nessie
created: 2026-05-22
updated: 2026-05-07
tags: ["nessie", "data-versioning", "iceberg", "data-catalog", "versioning", "git-for-data"]
related: ["apache-iceberg", "nessie-versioning-strategy", "data-storage-layer"]
sources: ["Cataloghi Data Lake - Differenze Nessie", "Polaris e Unity.md", "AMBIENTI.md"]
---
# Nessie

[[nessie]] is not a traditional catalog in the sense of a Hive Metastore, but rather a **versioning service** that provides Git-imitation transactional semantics for the data lake. It allows for managing data state through branches, tags, and commits, enabling much-needed data lineage and reproducibility.

## Core Functionality
- **Branching and Merging**: Allows creating isolated branches for ETL processes or experimentation, which can later be merged into the main branch.
- **Tagging**: Enables labeling specific data versions for reproducibility.
- **Commits**: Tracks changes to the data state.
- **Multi-table ACID Transactions**: Ensures consistency across operations involving multiple tables or compute engines.
- **Time Travel and Rollback**: Provides the ability to access historical states of data and revert to previous versions easily.

## Ecosystem and Integration
Nessie is primarily optimized for [[apache-iceberg]] and is compatible with compute engines such as Apache Spark, Trino, Flink, and Dremio. In the current implementation, it is integrated with:
- **Minio**: Serving as the physical storage layer.
- **Dremio**: Serving as the virtualization engine.

## Implementation Context
The platform is currently evaluating two primary strategies for environment isolation within Nessie:
- **Folder-based isolation**: Using separate root-level paths.
- **Branch-based isolation**: Using Nessie branches to manage project-specific states.