---
type: entity
title: LakeFS File Versioning
created: 2026-05-07
updated: 2026-05-07
tags: [versioning, data-lakehouse, lakefs, file-versioning]
related: [nessie-catalog-versioning, iceberg-table-versioning, data-lakehouse-versioning-strategies, data-lakehouse]
sources: ["data-lakehouse-versioning-nessie-vs-iceberg-vs-lakefs.md"]
---
# LakeFS File Versioning

LakeFS provides a versioning system for data lakes by implementing a Git-like interface at the **file level**. It operates over object storage (S3, GCS, Azure Blob, MinIO, Ceph) and uses key-value metadata storage (PostgreSQL, DynamoDB, CosmosDB) to track changes.

## Key Features

- **Git-like Interface:** Branching, committing, merging, and reverting at the file level.
- **Multi-Session, Multi-File Transactions:** Supports complex operations across multiple files and sessions.
- **Cloud and Storage Agnostic:** Works across multiple object stores and metadata databases.
- **CLI Interface:** Primarily command-line driven.

## Use Cases

- **File-level experimentation:** Branch entire datasets for isolated modifications.
- **Data pipeline validation:** Commit and merge workflows for data ingestion.
- **Reproducibility:** Tag specific file versions for analysis traceability.

## Pros and Cons

**Pros:** Comprehensive file-level versioning, cloud/storage agnostic, supports multi-session transactions.  
**Cons:** Requires S3-compatible storage, disconnected from table concepts (no table optimization/cleanup), less accessible for non-technical users (no SQL interface).

## Example (Python)

```python
repo = lakefs.Repository("quickstart", client=client)
new_branch = repo.branch("denmark-lakes").create(source_reference_id="main")
new_branch.object(path="lakes.parquet").upload(data=modified_data, pre_sign=True)
commit_ref = new_branch.commit(message="Create dataset of lakes in Denmark")
merge_result = new_branch.merge_into(repo.branch("main"))
```

## Related

- [[nessie-catalog-versioning]] — Catalog-level versioning alternative
- [[iceberg-table-versioning]] — Table-level versioning alternative
- [[data-lakehouse-versioning-strategies]] — Comparative framework
- [[data-lakehouse]] — Core architecture