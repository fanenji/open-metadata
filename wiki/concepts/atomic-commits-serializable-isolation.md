---
type: concept
title: Atomic Commits and Serializable Isolation
created: 2026-04-04
updated: 2026-04-04
tags: [apache-iceberg, transactions, concurrency, data-integrity]
related: [apache-iceberg, optimistic-concurrency, iceberg-maintenance-operations]
sources: ["Is Apache Iceberg Melting?.md"]
---
# Atomic Commits and Serializable Isolation

Iceberg's transaction model that provides atomic commits and serializable isolation on object storage. Table state is maintained in metadata files; every change creates a new metadata file and replaces the old metadata with an atomic swap.

## Key Properties

- Reads are isolated from concurrent writes and always use a committed snapshot
- Writes support adding and removing files in a single operation
- Readers don't acquire locks
- No partial visibility of writes

## Reality Check

Iceberg uses optimistic concurrency. Conflicting commits can fail and require retries. Large maintenance operations can conflict with frequent writes. Commit conflicts need to be planned for.
