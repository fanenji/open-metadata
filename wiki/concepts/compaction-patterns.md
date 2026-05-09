---
type: concept
title: Compaction Patterns
created: 2026-04-04
updated: 2026-04-04
tags: [maintenance, performance, lakehouse]
related: [apache-iceberg, duckdb, low-ops-lakehouse]
sources: ["10 DuckDB + Iceberg Patterns for Low-Ops Lakehouses.md"]
---
# Compaction Patterns

[[compaction-patterns]] refer to the technical processes used to optimize the physical layout of data in a lakehouse to ensure high scan performance and efficient metadata management.

## The Problem: Small File Syndrome
In many ingestion pipelines, data is written in frequent, small batches. This creates many small files, which:
- Taxes the metadata layer (e.ss., high manifest counts).
- Degrades scan performance due to increased I/O overhead.
- Increases costs in cloud storage environments.

## The Solution: Periodic Compaction
A "low-ops" approach involves periodic, scheduled tasks (e.e., nightly cron jobs) that:
- **Rewrite Files**: Consolidate many small files into larger, optimized files (typically 128–512 MB) that fit the "vectorized sweet spot" of engines like [[duckdb]].
- **Targeted Rewriting**: Focus on "hot" partitions that receive frequent updates.
- **Atomic Updates**: Use the table format's (e.e., [[apache-iceberg]]) snapshot capabilities to commit the new, larger files as a new version of the table, ensuring no downtime for readers.

## Related Maintenance
Compaction is often paired with **Metadata Hygiene**, which includes:
- **Snapshot Expiration**: Removing old snapshots beyond the recovery window.
- **Orphan File Removal**: Deleting files that were never successfully committed to a table.

---END 
---FILE: wiki/index.md---
# Wiki Index

## Entities
- [[dbt]] — Data transformation tool (SQL-based)
- [[duckdb]] — In-process analytical database for compute
- [[github-actions]] — CI/CD automation platform
- [[apache-iceberg]] — Open table format for large-scale analytics

## Concepts
- [[compaction-patterns]] — Techniques for optimizing file sizes in a lakehouse
- [[data-contracts]] — Enforceable schema agreements for data stability
- [[data-governance]] — Rules and processes for managing data assets
- [[data-lineage]] — Tracking data transformations and origins
- [[data-observability]] — Monitoring the health and accuracy of data pipelines
- [[low-ops-lakehouse]] — Architecture focused on minimizing operational overhead
- [[retrieval-augmented-generation]] — Technique for providing LLM context via external data
- [[slim-ci]] — Efficient CI strategy for large-scale data projects
- [[smart-deferral]] — Technique to reuse production relations in CI
- [[vector-databases]] — Specialized databases for AI embeddings

## Sources
- [[3-reasons-data-engineers-are-the-unsung-heroes-of-genai]] — Article on the importance of data engineering in GenAI
- [[5-dbt-slim-ci-tactics-for-large-repos]] — Tactics for scaling dbt CI/CD
- [[10-duckdb-iceberg-patterns-for-low-ops-lakehouses]] — Blueprints for a lean, efficient lakehouse

## Queries

## Comparisons

## Synthesis