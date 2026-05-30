---
type: concept
title: "Tag Usage Query Bottleneck (getTagsInternalByPrefix)"
created: 2026-05-15
updated: 2026-05-15
tags: [database, performance, tag-usage, bottleneck, ingestion]
related: [resource-quota-sizing-ingestion, external-dependencies-configuration, ingestion-pipeline-troubleshooting, openmetadata-system-architecture, mysql-8x]
sources: ["research-resourcequota-sizing-for-openmetadata-ingestion-wo-2026-05-15.md"]
---
# Tag Usage Query Bottleneck (getTagsInternalByPrefix)

The `getTagsInternalByPrefix` query is a documented database performance bottleneck in OpenMetadata, particularly affecting metadata ingestion workflows. This query performs sequential scans and Nested Loop Left Joins on the `tag_usage` table, causing high database CPU and I/O.

## Symptoms

- High database CPU utilization (e.g., a t4g.small RDS instance maxing out at 100% CPU).
- Slow metadata ingestion, especially during re-ingestion of large schemas (hundreds of tables).
- Pod restarts due to ingestion timeouts caused by database backpressure.

## Root Cause

The query performs:
1. A sequential scan of the `tag_usage` table (which can grow to hundreds of thousands of rows).
2. `LIKE` prefix scans on tag identifiers.
3. `LEFT JOINs` to `glossary_term_entity` and `tag` tables.
4. Buffer pool thrashing when the database instance is undersized.

## Impact

- Directly affects the [[pull-based-ingestion-model]] by slowing down metadata extraction.
- Can cascade to cause [[ingestion-pipeline-troubleshooting|ingestion pipeline failures]].
- Undersized database instances (e.g., t4g.small with 2 GB RAM) are particularly vulnerable.

## Mitigation

1. **Scale up the database instance**: Move to a larger instance class with more CPU and memory.
2. **Ensure proper indexing**: Verify that the `tag_usage` table has appropriate indexes for prefix scans.
3. **Tune `sort_buffer_size`**: Set to 10–20 MB (see [[external-dependencies-configuration]]).
4. **Apply query optimization patches**: OpenMetadata v1.12.3+ may have addressed this via query optimization; check the changelog for your version.
5. **Use [[filter-patterns]]**: Limit the scope of ingestion to reduce the number of assets being tagged.

## Open Questions

- Which OpenMetadata versions include `tag_usage` query optimization patches?
- What is the exact resource consumption curve for `tag_usage` queries as a function of table count?
- Are there community benchmarks quantifying the performance improvement from indexing changes?
