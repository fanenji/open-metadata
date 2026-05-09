---
type: entity
title: Nessie Catalog Versioning
created: 2026-05-07
updated: 2026-05-07
tags: [versioning, data-lakehouse, catalog, git-for-data, catalog-versioning, nessie, lakehouse, dataops, git-like, data-lake]
related: [iceberg-table-versioning, lakefs-file-versioning, data-lakehouse-versioning-strategies, write-audit-publish-pattern, data-lakehouse, dremio-mcp-server, data-platform-infrastructure-sizing, dataops-definition, ci-cd-for-data-pipelines, dremio, nessie-branching-strategies, nessie-commit-best-practices, nessie-operational-practices, nessie-multi-table-transactions, nessie-vs-iceberg-branching, dbt-nessie-branch-workaround]
sources: ["data-lakehouse-versioning-nessie-vs-iceberg-vs-lakefs.md", "Dimensionamento.md", "How Project Nessie Improves DataOps for the Lakehouse.md", "nessie-branching-best-practices.md", "Project Nessie Transactional Catalog for Data Lakes with Git-like semantics.md"]
---

# Nessie Catalog Versioning

Project Nessie is an open-source transactional catalog for data lakes that provides Git-like semantics for versioning data at the catalog level. It operates by managing pointers to table metadata files (e.g., Iceberg or Delta Lake metadata), rather than managing data files directly. This enables branching, committing, merging, and tagging of entire data lakehouse states across multiple tables simultaneously, allowing teams to apply software development best practices to data management. Nessie tracks commits across all tables, namespaces, and views, recording changes without duplicating actual data files. This gives a consistently updated, unified view of data across all datasets and enables data engineers and analysts to create virtual copies of datasets for isolated experimentation, transformation, and validation without corrupting the single source of truth.

## How It Works

Nessie leverages and extends modern table formats like Apache Iceberg and Delta Lake by version-controlling their table metadata files. Instead of managing copies of data files, Nessie version-controls the metadata, so it knows which data file versions are currently referenced (and must be retained) and which are no longer needed (and can be safely deleted). This metadata-level versioning forms the basis for all Nessie operations, enabling efficient branching and time travel without data duplication.

## Core Concepts

- **Commit:** A transaction affecting one or more tables, views, or namespaces. Commits capture changes such as inserts, updates, deletes, schema alterations, or view definition changes.
- **Branch:** An ordered list of commits with a linear history and a name (e.g., `main`, `dev`, `etl`). By default, all operations are performed on the `main` branch. Creating a branch acts as an isolated workspace.
- **Tag:** An immutable reference to a specific commit. Tags point to a particular state and cannot be committed to (e.g., `EOY-2020`). Useful for auditing and release management.
- **Merge / Cherry-pick:** The process of moving commits from one branch to another, making changes visible to users of the target branch.

## Key Features

- **Isolation:** Development work on branches does not affect production queries on the `main` branch.
- **Atomic Multi-Table Transactions:** Group changes across multiple tables into a single atomic transaction, ensuring consistency. This is a core differentiator from single-table versioning.
- **Time Travel:** Access any historical state of the data lake via commits or tags.
- **Tags:** Known versions of data can be tagged for easy reference, supporting auditing and compliance.
- **Automatic Garbage Collection:** Nessie tracks which data files are in use and safely deletes unused ones.
- **SQL Interface:** Versioning operations are accessible via SQL, making it the most accessible option for non-technical users.

## Git-like Semantics (Not Git)

Nessie is "Git-like" — it uses similar terminology (commit, branch, merge, tag) but is not built on Git itself, which would be orders of magnitude too slow. It omits complex Git features like stash operations and complex merge conflict resolution.

## DataOps Framing

The article "How Project Nessie Improves DataOps for the Lakehouse" positions Nessie as a CI/CD enabler for data, strengthening the [[dataops-definition|DataOps]] methodology. Nessie's branching workflow directly supports the CI/CD pillar of DataOps by allowing:
- **Branching** – Creating virtual copies of datasets for isolated work
- **Updating** – Transforming and experimenting within the branch
- **Merging** – Integrating trusted changes back into the core dataset

## Benefits

- **Safe, isolated data development:** Branches provide isolated environments without copying data.
- **Atomic multi-table commits:** Ensure consistency across related tables.
- **Undo/rollback:** Branch operations enable easy rollback.
- **CI/CD for data pipelines:** Merge workflows support automated data pipeline CI/CD.
- **No production contamination:** Development does not affect production workloads.
- **Consistent cross-table views:** A unified commit log across all tables.
- **Simplified data management:** Automated metadata tracking reduces manual effort.
- **Immutable data files:** Data integrity is preserved.
- **Time travel and auditing:** Historical states are easily accessible.

## Use Cases

### Isolated Experimentation
Data scientists and analysts can branch datasets without risking production integrity.

### Auditing and Compliance
Tagged commits provide easily accessible historical records.

### Simplified Data Ops
Automates schema changes, data file management, and cleanup.

### Business Intelligence: CSAT Dashboard
A data analyst and data engineer branch the core dashboard dataset to integrate CSAT survey scores and touchtone survey responses. They join, reformat, and create a weighted model within the virtual copy. Once trusted, they merge back to create a new source of truth.

### Data Science: Social Media Sentiment
A data scientist branches the core dataset to incorporate Facebook postings about products. NLP is applied to summarize content and derive a sentiment score, which is fed into the existing CSAT model. The updated model is merged back into the core data.

## Examples

### SQL with Dremio
```sql
CREATE BRANCH dataIntegration_010224;
USE BRANCH dataIntegration_010224;
MERGE INTO DACSalesData AS target USING DACStagingSalesData AS source ON target.id = source.id
WHEN MATCHED THEN UPDATE SET ...
WHEN NOT MATCHED THEN INSERT ...;
-- Perform data quality checks
USE BRANCH main;
MERGE BRANCH dataIntegration_010224 INTO main;
```

### PySpark with PyNessie
```python
# Create a branch
spark.sql("CREATE BRANCH dev IN nba_catalog AS main")
# Switch to dev branch
spark.sql("USE REFERENCE dev IN nba_catalog")
# Create tables and insert data on dev branch
spark.sql("""CREATE TABLE IF NOT EXISTS nba_catalog.nba.salaries (...) USING iceberg""")
spark.sql("""INSERT INTO nba_catalog.nba.salaries SELECT * FROM salaries_table""")
# Merge dev into main (atomic multi-table commit)
spark.sql("MERGE BRANCH dev INTO main IN nba_catalog")
# Clean up
spark.sql("DROP BRANCH dev IN dev_catalog")
```

## Best Practices

For detailed operational guidance on using Nessie effectively, see the dedicated pages:
- [[nessie-branching-strategies]] — Branching patterns (feature branches, main/develop, short-lived)
- [[nessie-commit-best-practices]] — Commit message guidelines and atomic commits
- [[nessie-operational-practices]] — Data validation, review processes, rollbacks, and tagging

## Comparison with Other Versioning Approaches

Nessie operates at the **catalog level**, providing cross-table, cross-schema versioning. This distinguishes it from:
- [[iceberg-table-versioning]] — Table-level branching and tagging within Apache Iceberg
- [[lakefs-file-versioning]] — File-level Git-like versioning over object storage

For a full comparison, see [[data-lakehouse-versioning-strategies]].

## Infrastructure Sizing

For small‑to‑medium workloads Nessie can be deployed with minimal resources. The recommended deployment is a single node with 2 vCPU, 8 GB RAM, and 50 GB storage. The service can be run as a container or as a `.jar` file, and it can be co‑located with other services that require basic sizing.

## Considerations and Limitations

**Pros:**
- Consistent cross‑table views, simplified data management, supports CI/CD for data, immutable data files.

**Cons:**
- Learning curve for version control concepts, integration effort required (mitigated by Dremio).

**Aspects not covered in source material:**
- Scalability constraints, merge conflict resolution strategies, integration challenges with non-Iceberg formats, data retention implications of metadata-level versioning, and performance overhead compared to Hive Metastore are not discussed in the available sources. As Dremio is Nessie’s primary commercial sponsor, claims should also be validated against neutral sources.

## Related

- [[iceberg-table-versioning]]
- [[lakefs-file-versioning]]
- [[data-lakehouse-versioning-strategies]]
- [[write-audit-publish-pattern]]
- [[data-lakehouse]]
- [[data-platform-infrastructure-sizing]]
- [[dremio]]
- [[dremio-mcp-server]]
- [[dataops-definition]]
- [[ci-cd-for-data-pipelines]]
- [[nessie-branching-strategies]]
- [[nessie-commit-best-practices]]
- [[nessie-operational-practices]]
- [[nessie-multi-table-transactions]]
- [[nessie-vs-iceberg-branching]]
- [[dbt-nessie-branch-workaround]]