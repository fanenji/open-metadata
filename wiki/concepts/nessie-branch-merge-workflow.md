---
type: concept
title: Nessie Branch and Merge Workflow
created: 2026-04-04
updated: 2026-04-04
tags: [nessie, versioning, data-lakehouse, git-for-data]
related: [project-nessie, nessie-catalog-versioning, nessie-multi-table-transactions, data-lakehouse]
sources: ["Open Source and the Data Lakehouse Iceberg and Project Nessie.md"]
---
# Nessie Branch and Merge Workflow

[[Project Nessie]] provides a Git-like branching and merging workflow for data lakehouse catalogs. This enables several powerful patterns:

- **Ingestion Isolation:** Create a branch of the catalog, ingest new data, run data quality checks and transformations, then merge the branch into the default branch when ready. This prevents incomplete or low-quality data from affecting production consumers.
- **Zero Copy Environment Generation:** Each branch references the same underlying data files but has its own metadata snapshot. Changes in one branch are isolated without duplicating data, enabling safe experimentation and development environments at minimal storage cost.
- **Disaster Recovery:** The full history of catalog commits allows rolling back to any previous state.
- **Reproducibility:** Tagging catalog commits enables running queries on the catalog as it existed at a specific point in time.

This workflow complements [[Apache Iceberg]]'s table-level versioning by providing catalog-level versioning, forming a unified stack for data lakehouse management.