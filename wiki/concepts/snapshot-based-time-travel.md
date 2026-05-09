---
type: concept
title: Snapshot-Based Time Travel
created: 2026-04-04
updated: 2026-04-04
tags: [apache-iceberg, time-travel, reproducibility, governance]
related: [apache-iceberg, iceberg-table-versioning, branching-and-tagging]
sources: ["Is Apache Iceberg Melting?.md"]
---
# Snapshot-Based Time Travel

Iceberg's support for reproducible queries by referencing a specific table snapshot, and rollback to a known-good state when something goes wrong.

## Operational Use Cases

- Proving what data an ML model was trained on
- Reproducing a regulatory report exactly as of a cutoff time
- Rolling back a bad load without rewriting the world

## Related Features

Iceberg also supports branching and tagging, with GDPR handling and audit retention as explicit use cases, not just developer convenience.
