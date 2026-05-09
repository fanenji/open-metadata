---
type: source
title: "Why Every Data Lake Needs a Control Plane: Lessons from Apache Iceberg"
created: 2026-05-07
updated: 2026-05-07
tags: [iceberg, data-lake, control-plane, maintenance, governance]
related: [iceberg-table-versioning, data-lakehouse, data-lakehouse-versioning-strategies, write-audit-publish-pattern, iceberg-query-engine-comparison, iceberg-table-maintenance, data-lake-control-plane, iceberg-snapshot-tags, iceberg-retention-policies, amit-gilad, lakeops]
sources: ["Why Every Data Lake Needs a Control Plane Lessons from Apache Iceberg.md"]
authors: [Amit Gilad]
year: 2025
url: "https://medium.com/@amitgil87/why-every-data-lake-needs-a-control-plane-lessons-from-apache-iceberg-2c035d4386ef"
venue: Medium
---
# Why Every Data Lake Needs a Control Plane: Lessons from Apache Iceberg

This article argues that Apache Iceberg's performance gains create an operational gap: without a centralized **control plane** to orchestrate table maintenance policies across catalogs, query engines, and teams, storage costs climb, metadata bloats, and compliance guarantees break. The author, CEO of LakeOps, presents snapshot expiration as the first of a series of deep dives into Iceberg maintenance procedures.

## Key Arguments

- **Operational Gap**: Iceberg delivers performance but requires disciplined maintenance (snapshot expiration, compaction, orphan cleanup) that diverges across teams without central governance.
- **Silent Fragmentation**: Without a control plane, teams set different retention defaults, engines (Spark vs. Athena vs. Trino) behave differently, and orphan files pile up unseen.
- **Tags as Liability**: Snapshot tags for DR and compliance can become "immortal" references that block cleanup forever if retention policies are not enforced.
- **GDPR Coordination**: Hard deletes require a coordinated sequence of compaction → expiration → orphan cleanup that a control plane can orchestrate.

## Maintenance Procedures Covered

- **Snapshot Expiration** (primary focus): Deleting old snapshots and their referenced data files to reclaim storage and shrink metadata.
- **Compaction**: Rewriting data files to consolidate small files and apply deletes for MOR tables.
- **Manifest Rewriting**: Optimizing manifest lists and manifest files to reduce planning time.
- **Orphan File Removal**: Deleting stray files left by failed jobs.
- **Puffin File Maintenance**: Refreshing auxiliary statistics/index files that can drift out of sync.

## Recommended Default Policy

- `max-snapshot-age-ms`: 14 days
- `min-snapshots-to-keep`: 10
- `max-ref-age-ms`: 90 days

## Caveats

- The author is CEO of LakeOps, which is presented as the solution — the control plane concept is framed as a necessary product category.
- No quantitative benchmarks or case studies are provided; evidence is anecdotal from "dozens of companies."
- The tension between engine-agnostic Iceberg design and centralized policy enforcement is acknowledged but not resolved.