---
type: concept
title: Git-Like Workflows on Data
created: 2026-05-07
updated: 2026-05-07
tags: [nessie, versioning, data-development, lakehouse, git]
related: [nessie-catalog-versioning, branch-based-data-experimentation, data-lakehouse-versioning-strategies, dremio-nessie-connector]
sources: ["Introducing Nessie as a Dremio Source.md"]
---
# Git-Like Workflows on Data

Git-like workflows on data apply the familiar Git version control paradigm (branches, commits, merges, rollbacks) to data management in the lakehouse. This concept is the core value proposition of [[nessie-catalog-versioning|Nessie]].

## Core Operations

- **Branching**: Create independent lines of development for experimentation, ETL, or testing
- **Committing**: Save state changes as immutable snapshots
- **Merging**: Combine changes from one branch into another
- **Rollback**: Revert to a prior state by reassigning the branch pointer
- **Time travel**: Query data as it existed at any point in history

## Benefits Over Traditional Approaches

| Aspect | Traditional | Git-Like |
|--------|-------------|----------|
| Environments | Multiple (dev, test, prod) | Single lakehouse with branches |
| Experimentation | Copy data to sandbox | Create lightweight branch |
| Rollback | Restore from backup | Move commit pointer |
| Cost | Duplicate storage and compute | Single storage, pointer operations |
| Isolation | Physical separation | Logical separation via branches |

## Implementation

In the [[dremio-nessie-connector|Dremio Nessie Connector]], git-like workflows are implemented through SQL commands:

- `CREATE BRANCH "name"` — Like `git branch`
- `MERGE BRANCH "src" INTO "tgt"` — Like `git merge`
- `ALTER BRANCH "name" ASSIGN COMMIT "hash"` — Like `git reset`
- `AT BRANCH "name"` — Like checking out a branch

## Related

- [[nessie-catalog-versioning]] — The catalog-level versioning system
- [[branch-based-data-experimentation]] — Practical workflow pattern
- [[data-lakehouse-versioning-strategies]] — Comparison with table-level and file-level versioning