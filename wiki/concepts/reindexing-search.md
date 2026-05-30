---
type: concept
title: Reindexing Search
created: 2026-05-14
updated: 2026-05-14
tags: ["administration", "maintenance", "search", "elasticsearch", "opensearch", "reindexing"]
related: ["openmetadata-administration", "elasticsearch-7x", "openmetadata-system-architecture", "mysql-8x"]
sources: ["admin-guide-openmetadata-administration-documentat-20260514.md", "reindexing-search---openmetadata-documentation-20260514.md"]
---
# Reindexing Search

Reindexing Search is a targeted administrative maintenance operation that rebuilds the [[elasticsearch-7x|Elasticsearch/OpenSearch]] search indexes from the authoritative transactional data stored in [[mysql-8x|MySQL]]. It is not a routine task but a remediation measure triggered by specific symptoms indicating index corruption or inconsistency.

## When to Reindex

Perform reindexing when you encounter any of the following:

- **Mismatch in counts** of Data Assets between the UI and the actual data
- **Data not appearing** in search results or entity listings
- **Shard exceptions** or errors in Elasticsearch/OpenSearch logs
- **Problems with the search mechanism** (slow, incomplete, or failing queries)
- **Empty results** in the Explore section despite known data
- **Missing lineage** information that should be present

## UI Procedure

1. Navigate to **Settings → Applications → Search Indexing**
2. In the configuration section, select the entities you want to reindex
3. Decide whether to enable the **Recreate Indexes** toggle (see below)
4. Click **Run Now** to initiate the process

## Recreate Indexes Toggle

The `recreateIndex` parameter controls whether the existing index is dropped and recreated from scratch (`true`) or updated in-place (`false`).

**Use with caution.** Set to `true` only when you need a clean slate — for example, after significant data model changes or during data migration. For routine updates, keep it `false` to preserve the existing index and avoid unnecessary downtime.

## Configuration Parameters

Nine parameters govern the performance and reliability of the reindexing process. All defaults are starting points; tune based on your system's capabilities and observed behavior.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `recreateIndex` | `false` | Drop and recreate the index from scratch |
| `batchSize` | `100` | Maximum events per batch; larger values improve throughput but increase memory usage |
| `payLoadSize` | `104,857,600` (100 MB) | Maximum payload size in bytes per batch; reduce if memory issues or timeouts occur |
| `producerThreads` | `10` | Number of threads producing reindexing events; balance against CPU and I/O capacity |
| `maxConcurrentRequests` | `100` | Maximum simultaneous requests to the search index; prevent overwhelming the search backend |
| `maxRetries` | `3` | Retry attempts for failed requests; keep reasonable to avoid excessive load |
| `initialBackoff` | `1000` (1 second) | Initial backoff in milliseconds before first retry; increase if failures are frequent |
| `maxBackoff` | `10000` (10 seconds) | Maximum backoff in milliseconds; longer backoff reduces load but slows recovery |
| `queueSize` | `100` | Internal queue capacity; larger queues handle spikes but consume more memory |

## High-Performance Starting Configuration

For systems with ample resources, the documentation suggests this starting point:

```json
{
  "batchSize": 300,
  "queueSize": 500,
  "producerThreads": 20,
  "maxConcurrentRequests": 500
}
```

Monitor system performance and adjust iteratively.

## Fallback: Re-install the Search Application

If reindexing does not resolve the issues, the documentation suggests re-installing the search application as a last resort. **Note:** The exact meaning of "re-installing the search application" is ambiguous — it is unclear whether this refers to restarting the OpenMetadata search service, deleting and recreating Elasticsearch indexes via API, or fully redeploying Elasticsearch/OpenSearch. Administrators should seek clarification from OpenMetadata support before pursuing this path.

## Architectural Context

Reindexing reinforces the [[openmetadata-system-architecture|system architecture]] principle: [[mysql-8x|MySQL]] is the source of truth for all metadata, and the [[elasticsearch-7x|Elasticsearch]] indexes are a derived layer optimized for search. Reindexing rebuilds the derived layer from the authoritative source, resolving any drift or corruption.

## Open Questions

- **Performance impact on live systems:** Does reindexing cause search downtime or degraded performance during the operation? The documentation does not address this.
- **Consistency guarantees:** If metadata ingestion runs concurrently with reindexing, does the process capture a consistent snapshot? Locking or isolation behavior is not documented.
- **Search application re-installation:** What specific procedure does "re-installing the search application" entail?