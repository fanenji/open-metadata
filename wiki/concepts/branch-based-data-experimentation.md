---
type: concept
title: Branch-Based Data Experimentation
created: 2026-05-07
updated: 2026-05-07
tags: [nessie, versioning, data-development, lakehouse]
related: [nessie-catalog-versioning, dremio-nessie-connector, data-lakehouse-versioning-strategies, git-like-workflows-on-data]
sources: ["Introducing Nessie as a Dremio Source.md"]
---
# Branch-Based Data Experimentation

Branch-based data experimentation is a workflow pattern enabled by catalog-level versioning systems like [[nessie-catalog-versioning|Nessie]]. It allows data engineers, analysts, and data scientists to create temporary branches of the entire lakehouse for safe experimentation without affecting production workloads.

## Workflow

1. **Create a branch**: `CREATE BRANCH "experiment_branch"` — creates a lightweight pointer to the current state of the lakehouse
2. **Experiment**: Insert, update, or delete data on the branch using `AT BRANCH` syntax
3. **Validate**: Run quality checks and analyses on the branch data
4. **Merge or discard**: Merge changes back to main with `MERGE BRANCH` or discard by simply deleting the branch

## Key Benefits

- **Isolation**: Production users are completely unaware of experimental changes
- **Cost efficiency**: Eliminates the need for duplicate environments (dev, test, prod)
- **Speed**: Branch creation and merging are instantaneous (pointer operations, not data copies)
- **Safety**: Mistakes can be rolled back immediately by reassigning the branch commit pointer

## Implementation

In the [[dremio-nessie-connector|Dremio Nessie Connector]], branch-based experimentation is supported through SQL commands:

```sql
-- Create an experiment branch
CREATE BRANCH "experiment_06092023";

-- Query production data
SELECT * FROM "my_table" AT BRANCH "main";

-- Insert experimental data
INSERT INTO "my_table" VALUES (5, 'New Data', 100000) AT BRANCH "experiment_06092023";

-- Merge when ready
MERGE BRANCH "experiment_06092023" INTO "main";

-- Rollback if needed
ALTER BRANCH "main" ASSIGN COMMIT "9b24dc...";
```

## Related

- [[nessie-catalog-versioning]] — The catalog-level versioning system enabling this pattern
- [[data-lakehouse-versioning-strategies]] — Comparative framework for versioning approaches
- [[git-like-workflows-on-data]] — The broader concept of applying Git semantics to data management