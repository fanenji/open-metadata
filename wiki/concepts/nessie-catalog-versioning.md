---
type: concept
title: Nessie Catalog Versioning
created: 2026-05-07
updated: 2026-05-07
tags: [nessie, catalog-versioning, data-lakehouse, git-for-data, branching]
related: [iceberg-table-versioning, lakefs-file-versioning, data-lakehouse-versioning-strategies, nessie-cli-commands, nessie-spark-integration]
sources: ["Dremio Open Source Explore Nessie.md"]
---
# Nessie Catalog Versioning

Project Nessie provides Git-like versioning at the **catalog level** for data lakehouses. Unlike table-level versioning (native Iceberg branching) or file-level versioning (LakeFS), Nessie branches the entire catalog — the list of tables and their metadata locations — enabling multi-table atomic transactions and isolated development environments.

## Key Capabilities

- **Catalog-level branching**: Create branches of the entire catalog, isolating changes across multiple tables.
- **Multi-table transactions**: Merge changes across several tables as one atomic operation using `MERGE BRANCH`.
- **Time-travel**: Query or revert to any previous commit state.
- **Isolated development**: Data engineers can perform ETL on a branch without impacting production queries on the main branch.

## SQL Syntax

```sql
-- Create a branch
CREATE BRANCH IF NOT EXISTS my_branch IN nessie;

-- List all branches
LIST REFERENCES IN nessie;

-- Query a specific branch
SELECT * FROM nessie.db.`table@my_branch`;

-- Insert data on a branch
INSERT INTO nessie.db.`table@my_branch` VALUES ('Adam'), ('James');

-- Merge a branch into main as a multi-table transaction
MERGE BRANCH my_branch INTO main IN nessie;
```

## Comparison with Other Versioning Strategies

| Strategy | Scope | Atomicity | Use Case |
|----------|-------|-----------|----------|
| Nessie (catalog-level) | All tables in catalog | Multi-table transactions | ETL isolation, QA, multi-table updates |
| Iceberg (table-level) | Single table | Single-table branching | Table-specific experiments, schema evolution |
| LakeFS (file-level) | Files in object store | File-level operations | Raw data versioning, data recovery |

## Caveats

- Nessie manages versions of the catalog (list of tables + metadata locations), not individual table data.
- Production deployments require proper authentication configuration (the demo uses `authentication.type=NONE`).
- Performance characteristics at scale (1000+ tables) are not well-documented in this source.
- Nessie is a transactional catalog, not a full replacement for Hive/Glue in all environments.

## References

- [[Dremio Open Source Explore Nessie.md]] — Source article with Docker-based tutorial.
- [[nessie-cli-commands]] — CLI commands for managing branches and content.
- [[nessie-spark-integration]] — Configuration for connecting Spark to Nessie.