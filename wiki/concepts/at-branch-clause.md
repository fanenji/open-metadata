type: concept
title: AT BRANCH Clause
created: 2026-05-07
updated: 2026-05-07
tags: [dremio, nessie, sql-syntax, catalog-versioning]
related: [nessie-catalog-versioning, dremio, dbt-git-branching-strategies]
sources: ["The Importance of Versioning in Modern Data Platforms Catalog Versioning with Nessie vs. Code Versioning with dbt.md"]
---
# AT BRANCH Clause

The `AT BRANCH` clause is a Dremio SQL syntax extension that allows users to query data from a specific Nessie catalog branch. This enables environment isolation by allowing dbt projects to target different catalog branches for development, testing, and production without duplicating data.

## Usage

In Dremio SQL, you can reference a specific branch of the Nessie catalog:

```sql
SELECT * FROM my_table AT BRANCH 'dev_branch'
```

## Benefits

- **Zero-copy environments**: Development and testing environments can be created as catalog branches without duplicating underlying data.
- **Safe experimentation**: Changes to data can be tested in isolation before merging to the main branch.
- **Integration with dbt**: dbt profiles can be configured to use different catalog branches for different environments, providing complete control over both code and data in development workflows.

## Related Concepts

- [[nessie-catalog-versioning]] — The catalog versioning system that enables branching.
- [[dbt-git-branching-strategies]] — Code-level branching strategies that complement catalog branching.
- [[data-lakehouse-versioning-strategies]] — Broader framework for comparing versioning approaches.