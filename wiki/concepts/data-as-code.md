type: concept
title: Data-as-Code
created: 2026-04-22
updated: 2026-04-22
tags: [data-management, versioning, governance, ci-cd]
related: [nessie-catalog-versioning, dbt, data-lakehouse, write-audit-publish-pattern, git]
sources: ["dremio-lakehouse-in-action-with-iceberg-dbt.md"]
---
# Data-as-Code

Data-as-Code is a paradigm that applies software engineering practices — version control, CI/CD, testing, and code review — to data management. It treats data transformations, schemas, and catalog metadata as code artifacts that can be versioned, reviewed, tested, and deployed through automated pipelines.

## Two Layers of Observability

The Dremio Lakehouse Lifecycle demonstrates Data-as-Code through two complementary layers:

1. **Catalog-Level Versioning (Nessie)** — Nessie provides Git-like branching, merging, and time travel for the entire Iceberg catalog. Changes to tables (data ingestion, schema evolution) create commits, enabling time travel and audit trails at the catalog level.
2. **SQL Code Versioning (dbt + Git)** — dbt models (SQL transformations) are checked into Git, providing version control for the semantic layer. Git tracks changes to the raw SQL code, giving visibility into historical modeling decisions.

Together, these two layers provide comprehensive observability: Nessie tracks *what* changed in the data, while Git tracks *why* it changed (via commit messages and code review).

## Key Practices

- **Branch-Based Ingestion** — Creating Nessie branches for isolated data ingestion, running validation on the branch, and merging only after validation passes.
- **Version-Controlled Transformations** — All dbt models are managed in Git, enabling code review, rollback, and collaboration.
- **Automated CI/CD** — Orchestration tools can automate the branch-create → ingest → validate → merge pipeline.
- **Schema Evolution as Code** — Schema changes are managed through version-controlled dbt models and Nessie commits.

## Relationship to Other Concepts

- Enables the [[write-audit-publish-pattern]] through Nessie branching.
- Supports [[data-contract-versioning-strategy]] by providing versioning infrastructure.
- Aligns with [[CI-CD-for-data-pipelines]] by treating data pipelines as code artifacts.
- Complements [[data-lakehouse-versioning-strategies]] by adding the code versioning dimension.