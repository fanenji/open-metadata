---
type: concept
title: Branching and Tagging
created: 2026-04-04
updated: 2026-04-04
tags: [apache-iceberg, versioning, governance, gdpr]
related: [apache-iceberg, snapshot-based-time-travel, iceberg-table-versioning, data-lakehouse-versioning-strategies]
sources: ["Is Apache Iceberg Melting?.md"]
---
# Branching and Tagging

Iceberg's Git-like versioning features that enable branching and tagging of table snapshots. The official docs call out GDPR handling and audit retention as explicit use cases.

## Use Cases

- GDPR right-to-be-forgotten workflows
- Audit retention and compliance
- Development and testing on isolated branches
- Reproducible ML training datasets
