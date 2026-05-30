---
type: concept
title: ResourceQuota Sizing for Ingestion
created: 2026-05-15
updated: 2026-05-15
tags: [kubernetes, resource-quotas, sizing, ingestion, performance]
related: [kubernetes-native-orchestrator, omjob-operator, ingestion-framework, tag-usage-query-bottleneck, external-dependencies-configuration, reindexing-search, filter-patterns, ingestion-pipeline-troubleshooting, kubernetes-namespaces, resource-quotas-limit-ranges]
sources: ["research-resourcequota-sizing-for-openmetadata-ingestion-wo-2026-05-15.md"]
---
# ResourceQuota Sizing for Ingestion

Proper resource quota sizing for OpenMetadata ingestion workloads is critical for stable operations, preventing OOM errors, and avoiding excessive database load. This page synthesizes official documentation, Helm chart defaults, community performance reports, and best practices to provide a comprehensive sizing guide for administrators using [[kubernetes]] namespaces with `ResourceQuota` and `LimitRange` policies.

## Baseline Resource Recommendations

Official documentation provides separate minimum and production-ready specifications for the core OpenMetadata stack. These represent the *steady-state* resource footprint of the server and its dependencies, excluding ingestion worker spikes.

| Component   | vCPU (Minimum) | vCPU (Production) | Memory (Minimum) | Memory (Production) | Storage (Min / Prod) |
|-------------|----------------|-------------------|------------------|----------------------|----------------------|
| Server      | 4              | 4                 | 16 GiB           | 16 GiB               | 100 GiB (prod)       |
| Database    | 4              | 4                 | 16 GiB           | 16 GiB               | 30–100 GiB / 100–200 GiB |
| Search      | 2              | 2                 | 8 GiB            | 8 GiB                | 100 GiB (per node)   |

**Key database tuning parameters:**
- MySQL `sort_buffer_size`: **20 MB** is recommended for production; the [[helm-charts]] set a default of `--sort_buffer_size=10M`. An undersized sort buffer directly impacts expensive queries such as tag prefix scans.
- The database is frequently the first bottleneck—a t4g.small RDS instance (2 GB RAM) was observed suffering high CPU load from the `getTagsInternalByPrefix` query on `tag_usage`, which performs sequential scans and Nested Loop Left Joins.

## Kubernetes Infrastructure Sizing

When using the [[kubernetes-native-orchestrator]], resource quotas must account for three distinct workloads: the operator itself, the ingestion worker pods, and the backend services managed by the Helm release.

### OMJob Operator

The [[omjob-operator]] is a lightweight Kubernetes controller that watches `OMJob` / `CronOMJob` CRDs. Its default resource profile is well-defined in the Helm chart:

| Resource | Request | Limit   |
|----------|---------|---------|
| CPU      | 100m    | 500m    |
| Memory   | 128 MiB | 256 MiB |

These defaults are generally sufficient.

### Ingestion Worker Pods (Pipeline Service Client)

The actual metadata extraction, profiling, and quality tests run inside Kubernetes Jobs created by the operator. These pods run the `metadata ingest` or `metadata profile` commands.

**Default Resource Template:**
```yaml
requests:
  memory: "1Gi"    # No explicit CPU request default in all versions, often implicitly ~250m
```

**Critical Observation:** The default `1Gi` memory request is a one-size-fits-all baseline. Real-world requirements depend heavily on the workload type and the number of assets being processed. [[ingestion-pipeline-troubleshooting]] often traces pod restarts to OOMKilled when this is exceeded without corresponding limits.

Admins should set `limits` explicitly in their Helm values, e.g.:
```yaml
# Example override for heavy profiling
requests:
  cpu: 500m
  memory: 2Gi
limits:
  cpu: 2
  memory: 4Gi
```

### Job Lifecycle Parameters

The Helm chart exposes several Kubernetes-native job lifecycle settings that directly impact resource quota accounting:

| Parameter                          | Default   | Recommendation                                               |
|------------------------------------|-----------|--------------------------------------------------------------|
| `activeDeadlineSeconds`            | `7200`    | 2 hr max execution. Increase for large dbt or profiling runs.|
| `backoffLimit`                     | `3`       | Retries on pod failure. Re-run under quota limits.            |
| `ttlSecondsAfterFinished`          | `86400`   | 1 day. Shorter values help reclaim quota faster.             |
| `successfulJobsHistoryLimit`       | `3`       | Controls retained pods consuming namespace storage.           |
| `failedJobsHistoryLimit`           | `3`       | Required for [[exit-handler-guarantee]] diagnostics.          |

When configuring `ResourceQuotas` at the namespace level, ensure the `LimitRange` does not prevent the operator from creating Jobs with the required `requests`.

### Airflow Alternative

If using Airflow as the ingestion orchestrator, official minimums are:
- 4 vCPU
- 16 GiB Memory
- 100 GiB Storage (for DAGs, logs, and [[airflow-storage-requirements]])

This represents a persistent baseline that does not scale to zero, unlike the K8s-native model where infrastructure is provisioned ephemerally per-ingestion run.

## Sizing by Workload Type

The resource profile of an ingestion Job varies dramatically between different workflows. Applying a single "1 GiB" default to all pipelines is inefficient and causes either resource waste or instability.

### Metadata Ingestion

- **DB CPU/Memory Intensive**: The [[tag-usage-query-bottleneck|`getTagsInternalByPrefix` query]] in `tag_usage` can cause high database CPU and I/O, particularly during re-ingestion of large schemas (hundreds of tables).
- **Pod Sizing**: Typically lighter. Default `1Gi` request suffices. Large numbers of assets (10k+ tables) or heavy lineage extraction (e.g., [[dbt-lineage-ingestion]]) may require `requests.memory: 2Gi`.
- **Mitigation**: Use [[filter-patterns]] to limit ingestion scope. Stagger ingestion schedules for different services.

### Profiling & Data Quality

- **Workload Profile**: By far the most resource-intensive workload on both the source database (sampling, computing metrics) and the ingestion pod (processing result sets). OpenMetadata documentation explicitly warns of the performance impact and recommends multi-threading and sampling.
- **Pod Sizing**: Default `1Gi` memory request is insufficient for most profiling pipelines beyond small tables. **Recommend starting with `requests.memory: 2Gi` and `limits.memory: 4Gi`**, scaling up based on profiled table row counts and column count.
- **Best Practices:**
  1. Deploy *multiple* profiler ingestion pipelines for the same service, each attacking a specific set of assets based on input filters.
  2. Apply appropriate sampling rates—critical tables can hold higher sampling, while the rest of assets might be good enough with smaller percentages.
  3. Schedule profiling pipelines to run sequentially rather than concurrently.

### dbt Integration

- **Workload Profile**: CPU and memory spikes when parsing large `manifest.json` and `run_results.json` files. The ingestion pod must process compiled SQL for lineage.
- **Pod Sizing**: `requests.memory: 2Gi` is recommended for projects with 500+ models.
- **Concurrency**: Multiple dbt projects ingested in a single workflow ([[multi-project-dbt-ingestion]]) amplify resource needs linearly.

### Reindexing Search

- **Workload Profile**: This is a server-side operation ([[reindexing-search]]) that reads from the database and writes to Elasticsearch. It places significant load on the OpenMetadata server pod(s) and the search index.
- **Server Sizing**: Ensure the `openmetadata-server` pod has adequate CPU/memory (not just the ingestion pod). The server pod must handle high throughput during reindexing.

## Database-Side Tuning for Ingestion Workloads

Database resource allocation is frequently a hidden requirement. The ingestion workloads interact most heavily with the `tag_usage` and `entity_relationship` tables.

| Parameter / Setting          | Recommended Value | Source            |
|------------------------------|-------------------|-------------------|
| MySQL sort_buffer_size       | 10–20 MB          | Official docs     |
| Database Storage (Production)| 100–200 GiB       | Official docs     |
| Connection Pool              | Tune for concurrency of ingestion runs | General DB ops |

The [[tag-usage-query-bottleneck|`getTagsInternalByPrefix` query]] is the canonical example of a database bottleneck:
- **Symptom**: High RDS CPU (t4g.small maxed out), slow metadata ingestion.
- **Root Cause**: The query performs a sequential scan + Nested Loop Left Join. On large `tag_usage` tables (hundreds of thousands of rows), this consumes all available buffer pool.
- **Solution**: Scale up the database instance and ensure proper indexing. OpenMetadata v1.12.3+ may have addressed this via query optimization, but the underlying resource logic remains.

## Gaps and Contradictions in Official Guidance

1. **Minimum vs. Production-Ready Specs**: The "Minimum Requirements" page recommends 4 vCPU / 16 GiB for server and database. The "Production-Ready" page recommends the identical specs for server and database but lowers the minimum database storage to 30 GiB. There is no tiered scaling guidance (e.g., "Small / Medium / Large" environments based on asset count).
2. **Ingestion Pod Default Resources**: The default `requests.memory: 1Gi` for the pipeline service client is a single baseline value. Official documentation does **not** provide a sizing matrix mapping workload type (metadata vs. profiling vs. dbt) to appropriate pod resources.
3. **Database Sizing for Tag Workloads**: The critical impact of `tag_usage` prefix scans on database CPU is documented in a community bug report but absent from the official sizing guides. There is no formula relating the number of tagged assets to the required database compute.
4. **K8s Quota Interaction**: The default `backoffLimit: 3` and `activeDeadlineSeconds: 7200` affect quota exhaustion. A namespace with a hard pod quota can be saturated by failed ingestion runs. The interaction between these job lifecycle defaults and `ResourceQuota` is not addressed in official documentation.

## Summary Matrix

| Workload Type | Pod CPU Request (Recommended) | Pod Memory Request (Recommended) | Pod Memory Limit (Recommended) | Key Infrastructure Bottleneck |
|---------------|-------------------------------|----------------------------------|--------------------------------|-------------------------------|
| Metadata (small) | 250m | 1 GiB | 2 GiB | Database (tag_usage queries) |
| Metadata (large / dbt) | 500m | 2 GiB | 4 GiB | Database + Pod CPU (SQL parsing) |
| Profiling (light) | 500m | 2 GiB | 4 GiB | Source DB (sampling) |
| Profiling (heavy) | 1–2 CPU | 4 GiB | 8 GiB | Source DB + Pod Memory |
| Reindexing | N/A (Server-side) | N/A | N/A | Server Pod + Search Engine |

The single most critical sizing variable is the database instance. Ingestion pods are ephemeral and can be right-sized per workflow using [[filter-patterns]] and scheduling, but an undersized database becomes a hard bottleneck that cannot be solved by throwing pod resources at it. For production deployments running multiple concurrent ingestion pipelines, **start with the Production-Ready specs** and monitor database performance (specifically query execution times for `tag_usage` lookups) as the scaling metric.
