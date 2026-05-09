---
type: source
title: "Introducing Nessie as a Dremio Source"
created: 2026-05-07
updated: 2026-05-07
tags: [nessie, dremio, lakehouse, versioning, git-workflows]
related: [nessie-catalog-versioning, dremio, dremio-nessie-connector, data-lakehouse-versioning-strategies, dbt-nessie-branch-workaround, iceburg-table-versioning, dremio-arctic]
sources: ["Introducing Nessie as a Dremio Source.md"]
authors: [Ben Hudson]
year: 2023
url: "https://www.dremio.com/blog/introducing-nessie-as-a-dremio-source/"
venue: Dremio Blog
---
# Introducing Nessie as a Dremio Source

This blog post by Ben Hudson announces that Dremio Software (v24.1+) can now connect to Nessie (v0.59+) as a data source. Nessie is an open-source lakehouse catalog that enables git-like workflows (branches, commits, merges, rollbacks) and cross-table transactions on the lakehouse.

## Key Capabilities

- **Single lakehouse environment**: Replace multiple expensive dev, test, and production environments with one environment using branches.
- **Branch-based experimentation**: Create temporary branches for safe data experimentation without affecting production.
- **Instantaneous merge/rollback**: Merges and rollbacks happen by moving commit pointers, not copying data.
- **Catalog-level time travel**: Reproduce models and analyses at any point in history.
- **Cross-table transactions**: Nessie supports transactions across multiple tables (mentioned but not demonstrated).

## Setup and Connection

The post provides a step-by-step guide for connecting Dremio to a Nessie server via the Dremio UI, including configuration of the Nessie REST endpoint, credentials, and storage settings.

## SQL Workflow Example

The post demonstrates a complete workflow using SQL commands:

1. Query a table on the `main` branch using `AT BRANCH` syntax
2. Create an ETL branch with `CREATE BRANCH`
3. Insert data into the branch with `AT BRANCH`
4. Verify isolation between branches
5. Merge changes with `MERGE BRANCH ... INTO ...`
6. Rollback with `ALTER BRANCH ... ASSIGN COMMIT ...`

## Status and Caveats

- The feature is in **public preview** (not GA)
- A testimonial from a large European government entity reports "snappy" performance with thousands of tables and hundreds of branches
- No performance benchmarks or production case studies are provided
- Cross-table transactions are mentioned but not demonstrated with examples

## Related Resources

- [[nessie-catalog-versioning]] — Core concept page for Nessie's catalog-level versioning
- [[dremio-nessie-connector]] — Technical details of the Dremio-Nessie connector
- [[data-lakehouse-versioning-strategies]] — Comparative framework for versioning approaches
- [[dbt-nessie-branch-workaround]] — Macro override pattern for Nessie branch support in dbt-dremio
- [[dremio-arctic]] — Fully-managed lakehouse management service built on Nessie