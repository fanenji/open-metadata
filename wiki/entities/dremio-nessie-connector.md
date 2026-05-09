---
type: entity
title: Dremio Nessie Connector
created: 2026-05-07
updated: 2026-05-07
tags: [dremio, nessie, connector, lakehouse, versioning]
related: [nessie-catalog-versioning, dremio, nessie, data-lakehouse-versioning-strategies, dbt-nessie-branch-workaround, dremio-arctic]
sources: ["Introducing Nessie as a Dremio Source.md"]
---
# Dremio Nessie Connector

The Dremio Nessie Connector allows Dremio Software (v24.1+) to connect to a Nessie server (v0.59+) as a data source, enabling git-like workflows on the lakehouse.

## Setup

1. Deploy a Nessie server (Docker, JAR, or Helm chart) with a supported backend database
2. In the Dremio UI, click "Add Source" → "Nessie (Preview)"
3. Configure the Nessie REST endpoint URL and credentials
4. Configure storage credentials in the "Storage" tab
5. Optionally configure cache options in "Advanced Options"

## SQL Syntax

The connector supports the following SQL commands for branch management:

- `AT BRANCH "branch_name"` — Query a table on a specific branch
- `CREATE BRANCH "branch_name"` — Create a new branch from the current state
- `MERGE BRANCH "source_branch" INTO "target_branch"` — Merge changes between branches
- `ALTER BRANCH "branch_name" ASSIGN COMMIT "commit_hash"` — Rollback to a prior commit

## Status

- **Public preview** as of June 2023
- Requires Dremio Software v24.1+ and Nessie v0.59+
- Performance reported as "snappy" with thousands of tables and hundreds of branches (per user testimonial)

## Limitations

- No performance benchmarks or production case studies published
- Cross-table transactions mentioned but not demonstrated
- Preview status implies potential instability or incomplete functionality
- No documented concurrency model for multiple users

## Related

- [[nessie-catalog-versioning]] — Core concept for Nessie's versioning approach
- [[dremio]] — The data lakehouse query engine
- [[nessie]] — The open-source lakehouse catalog
- [[dbt-nessie-branch-workaround]] — Workaround for using Nessie branches with dbt-dremio
- [[dremio-arctic]] — Managed Nessie service from Dremio