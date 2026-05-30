---
type: source
title: "Reindexing Search — OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [administration, search, elasticsearch, maintenance, reindexing]
related: [reindexing-search, elasticsearch-7x, openmetadata-administration, openmetadata-system-architecture]
sources: ["reindexing-search---openmetadata-documentation-20260514.md"]
authors: ["OpenMetadata"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/reindexing-search"
venue: "OpenMetadata Official Documentation v1.12.x"
---
# Reindexing Search — OpenMetadata Documentation

Official documentation for the Reindexing Search administrative operation in OpenMetadata v1.12.x. Covers the symptom-driven triggers for reindexing, the step-by-step UI procedure (Settings → Applications → Search Indexing → Run Now), the critical Recreate Indexes toggle, all nine configurable parameters with defaults and best practices, a high-performance example configuration, and the re-installation fallback.

## Key Content

- **Symptom checklist:** Count mismatches, missing data, shard exceptions, search failures, empty Explore results, missing lineage
- **UI procedure:** Settings → Applications → Search Indexing, with entity selection and Recreate Indexes toggle
- **Nine parameters:** `recreateIndex`, `batchSize` (default 100), `payLoadSize` (default ~100 MB), `producerThreads` (default 10), `maxConcurrentRequests` (default 100), `maxRetries` (default 3), `initialBackoff` (default 1s), `maxBackoff` (default 10s), `queueSize` (default 100)
- **High-performance starting config:** batchSize 300, queueSize 500, producerThreads 20, maxConcurrentRequests 500
- **Fallback:** Re-install the search application if reindexing does not resolve issues (procedure is ambiguous)