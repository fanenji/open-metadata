---
type: query
title: "Research: ResourceQuota Sizing for OpenMetadata Ingestion Workloads"
created: 2026-05-15
origin: deep-research
tags: [research]
---

# Research: ResourceQuota Sizing for OpenMetadata Ingestion Workloads

---
type: synthesis
title: ResourceQuota Sizing for OpenMetadata Ingestion Workloads
tags: [kubernetes, resource-quotas, sizing, ingestion, performance]
related: [kubernetes-native-orchestrator, omjob-operator, ingestion-framework, openmetadata-system-architecture]
---

# ResourceQuota Sizing for OpenMetadata Ingestion Workloads

## Overview

Proper resource quota sizing for OpenMetadata ingestion workloads is critical for ensuring stable operations, preventing out-of-memory (OOM) errors, and avoiding excessive database load. OpenMetadata’s [[pull-based-ingestion-model]] relies on schedulable agents that extract metadata from 90+ source systems. Depending on the chosen architecture—[[kubernetes-native-orchestrator]] via the [[omjob-operator]], or Apache Airflow—the resource demands on both the orchestration plane and the backend services (database, search, server) vary significantly.

This page synthesizes official documentation, Helm chart defaults, community performance reports, and best practices to provide a comprehensive sizing guide for administrators using [[kubernetes]] namespaces with `ResourceQuota` and `LimitRange` policies.

## Baseline Resource Recommendations

Official documentation provides separate minimum and production-ready specifications for the core OpenMetadata stack [2, 3]. These represent the *steady-state* resource footprint of the server and its dependencies, excluding ingestion worker spikes.

### OpenMetadata Server & Dependencies

| Component   | vCPU (Minimum) | vCPU (Production) | Memory (Minimum) | Memory (Production) | Storage (Min / Prod)         |
|-------------|----------------|-------------------|------------------|----------------------|------------------------------|
| Server      | 4              | 4                 | 16 GiB           | 16 GiB               | 100 GiB (prod)               |
| Database    | 4              | 4                 | 16 GiB           | 16 GiB               | 30–100 GiB / 100–200 GiB [3] |
| Search      | 2              | 2                 | 8 GiB            | 8 GiB                | 100 GiB (per node)           |

**Key database tuning parameters:**
- MySQL `sort_buffer_size`: **20 MB** is recommended for production [3]; the [[helm-charts]] set a default of `--sort_buffer_size=10M` [4]. An undersized sort buffer directly impacts expensive queries such as tag prefix scans.
- The database is frequently the first bottleneck—a t4g.small RDS instance (2 GB RAM) was observed suffering high CPU load from the `getTagsInternalByPrefix` query on `tag_usage`, which performs sequential scans and Nested Loop Left Joins [1].

These specifications apply equally to managed services (AWS RDS, GCP Cloud SQL, Azure Flexible Server) [2, 3].

## Kubernetes Infrastructure Sizing

When using the [[kubernetes-native-orchestrator]], resource quotas must account for three distinct workloads: the operator itself, the ingestion worker pods, and the backend services managed by the Helm release.

### OMJob Operator

The [[omjob-operator]] is a lightweight Kubernetes controller that watches `OMJob` / `CronOMJob` CRDs. Its default resource profile is well-defined in the Helm chart [6, 8]:

| Resource | Request | Limit   |
|----------|---------|---------|
| CPU      | 100m    | 500m    |
| Memory   | 128 MiB | 256 MiB |

This operator is responsible for creating and monitoring ingestion pod lifecycles but does *not* perform the data extraction itself. These defaults are generally sufficient.

### Ingestion Worker Pods (Pipeline Service Client)

The actual metadata extraction, profiling, and quality tests run inside Kubernetes Jobs created by the operator. These pods run the `metadata ingest` or `metadata profile` commands and are defined under `openmetadata.config.pipelineServiceClientConfig.k8s.resources` [8].

**Default Resource Template:**
```yaml
requests:
  memory: "1Gi"    # No explicit CPU request default in all versions, often implicitly ~250m
```
**Critical Observation:** The default `1Gi` memory request is a one-size-fits-all baseline. Real-world requirements depend heavily on the workload type (see § below) and the number of assets being processed. [[ingestion-pipeline-troubleshooting]] often traces pod restarts to OOMKilled when this is exceeded without corresponding limits.

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

The Helm chart exposes several Kubernetes-native job lifecycle settings that directly impact resource quota accounting [8]:

| Parameter                          | Default   | Recommendation                                               |
|------------------------------------|-----------|--------------------------------------------------------------|
| `activeDeadlineSeconds`            | `7200`    | 2 hr max execution. Increase for large dbt or profiling runs.|
| `backoffLimit`                     | `3`       | Retries on pod failure. Re-run under quota limits.            |
| `ttlSecondsAfterFinished`          | `86400`   | 1 day. Shorter values help reclaim quota faster.             |
| `successfulJobsHistoryLimit`       | `3`       | Controls retained pods consuming namespace storage.           |
| `failedJobsHistoryLimit`           | `3`       | Required for [[exit-handler-guarantee]] diagnostics.          |

When configuring `ResourceQuotas` at the namespace level (`hard limits for pods, CPU, memory, and count`), ensure the `LimitRange` does not prevent the operator from creating Jobs with the required `requests` [6].

### Airflow Alternative

If using Airflow as the ingestion orchestrator, official minimums are [2, 3]:
- 4 vCPU
- 16 GiB Memory
- 100 GiB Storage (for DAGs, logs, and [[airflow-storage-requirements]])

This represents a persistent baseline that does not scale to zero, unlike the K8s-native model where infrastructure is provisioned ephemerally per-ingestion run.

## Sizing by Workload Type

The resource profile of an ingestion Job varies dramatically between different workflows. Applying a single "1 GiB" default to all pipelines is inefficient and causes either resource waste or instability.

### Metadata Ingestion

- **DB CPU/Memory Intensive**: The `getTagsInternalByPrefix` query in `tag_usage` can cause high database CPU and I/O, particularly during re-ingestion of large schemas (hundreds of tables). The query performs `LIKE` prefix scans with `LEFT JOINs` to `glossary_term_entity` and `tag`, causing sequential scans and buffer pool thrashing when the database is undersized [1].
- **Pod Sizing**: Typically lighter. Default `1Gi` request suffices. Large numbers of assets (10k+ tables) or heavy lineage extraction (e.g., [[dbt-lineage-ingestion]]) may require `requests.memory: 2Gi`.
- **Mitigation**: Use [[filter-patterns]] to limit ingestion scope. Stagger ingestion schedules for different service.

### Profiling & Data Quality

- **Workload Profile**: By far the most resource-intensive workload on both the source database (sampling, computing metrics) and the ingestion pod (processing result sets). OpenMetadata documentation explicitly warns of the performance impact and recommends multi-threading and sampling [11].
- **Pod Sizing**: Default `1Gi` memory request is insufficient for most profiling pipelines beyond small tables. **Recommend starting with `requests.memory: 2Gi` and `limits.memory: 4Gi`**, scaling up based on profiled table row counts and column count.
- **Best Practices [11]:**
  1. Deploy *multiple* profiler ingestion pipelines for the same service, each attacking a specific set of assets based on input filters.
  2. Apply appropriate sampling rates—critical tables can hold higher sampling, while the rest of assets might be good enough with smaller percentages.
  3. Schedule profiling pipelines to run sequentially rather than concurrently.

### dbt Integration

- **Workload Profile**: CPU and memory spikes when parsing large `manifest.json` and `run_results.json` files. The ingestion pod must process compiled SQL for lineage [14].
- **Pod Sizing**: `requests.memory: 2Gi` is recommended for projects with 500+ models.
- **Concurrency**: Multiple dbt projects ingested in a single workflow ([[multi-project-dbt-ingestion]]) amplify resource needs linearly.

### Reindexing Search

- **Workload Profile**: This is a server-side operation ([[reindexing-search]]) that reads from the database and writes to Elasticsearch. It places significant load on the OpenMetadata server pod(s) and the search index.
- **Server Sizing**: Ensure the `openmetadata-server` pod has adequate CPU/memory (not just the ingestion pod). The server pod must handle high throughput during reindexing.

## Database-Side Tuning for Ingestion Workloads

Database resource allocation is frequently a hidden requirement. The ingestion workloads interact most heavily with the `tag_usage` and `entity_relationship` tables [1].

| Parameter / Setting          | Recommended Value | Source            |
|------------------------------|-------------------|-------------------|
| MySQL sort_buffer_size       | 10–20 MB          | [3, 4]            |
| Database Storage (Production)| 100–200 GiB       | [2]               |
| Connection Pool              | Tune for concurrency of ingestion runs | (General DB ops) |

The `getTagsInternalByPrefix` query [1] is the canonical example of a database bottleneck:

- **Symptom**: High RDS CPU (t4g.small maxed out), slow metadata ingestion.
- **Root Cause**: The query performs a sequential scan + Nested Loop Left Join. On large `tag_usage` tables (hundreds of thousands of rows), this consumes all available buffer pool.
- **Solution**: Scale up the database instance and ensure proper indexing. OpenMetadata v1.12.3+ may have addressed this via query optimization, but the underlying resource logic remains.

## Gaps and Contradictions in Official Guidance

1. **Minimum vs. Production-Ready Specs [2, 3]**: The "Minimum Requirements" page [2] recommends 4 vCPU / 16 GiB for server and database. The "Production-Ready" page [3] recommends the identical specs for server and database but lowers the minimum database storage to 30 GiB. There is no tiered scaling guidance (e.g., "Small / Medium / Large" environments based on asset count).

2. **Ingestion Pod Default Resources**: The default `requests.memory: 1Gi` for the pipeline service client [8] is a single baseline value. Official documentation does **not** provide a sizing matrix mapping workload type (metadata vs. profiling vs. dbt) to appropriate pod resources.

3. **Database Sizing for Tag Workloads**: The critical impact of `tag_usage` prefix scans on database CPU is documented in a community bug report [1] but absent from the official sizing guides [2, 3]. There is no formula relating the number of tagged assets to the required database compute.

4. **K8s Quota Interaction**: The default `backoffLimit: 3` and `activeDeadlineSeconds: 7200` [8] affect quota exhaustion. A namespace with a hard pod quota can be saturated by failed ingestion runs. The interaction between these job lifecycle defaults and `ResourceQuota` is not addressed in official documentation.

## Sources Worth Finding

- **Community benchmarks**: Large-scale performance tests from the OpenMetadata community showing resource consumption curves for metadata ingestion and profiling as functions of table count.
- **Query optimization patches**: Detailed changelog for `tag_usage` / `getTagsInternalByPrefix` query optimizations across versions.
- **Storage performance testing**: I/O benchmarks for MySQL/PostgreSQL when running back-to-back ingestion pipelines to quantify disk throughput requirements.
- **Enterprise case studies**: Deployments by companies operating OpenMetadata at scale (e.g., Thndr's implementation of profiling [10]) to validate pod sizing assumptions.
- **Resource consumption per connector**: A detailed breakdown showing how different connectors (e.g., Hive [1] vs. Snowflake vs. PowerBI) place different loads on ingestion pods.

## Summary

| Workload Type | Pod CPU Request (Recommended) | Pod Memory Request (Recommended) | Pod Memory Limit (Recommended) | Key Infrastructure Bottleneck |
|---------------|-------------------------------|----------------------------------|--------------------------------|-------------------------------|
| Metadata (small) | 250m | 1 GiB | 2 GiB | Database (tag_usage queries) |
| Metadata (large / dbt) | 500m | 2 GiB | 4 GiB | Database + Pod CPU (SQL parsing) |
| Profiling (light) | 500m | 2 GiB | 4 GiB | Source DB (sampling) |
| Profiling (heavy) | 1–2 CPU | 4 GiB | 8 GiB | Source DB + Pod Memory |
| Reindexing | N/A (Server-side) | N/A | N/A | Server Pod + Search Engine |

The single most critical sizing variable is the database instance. Ingestion pods are ephemeral and can be right-sized per workflow using [[filter-patterns]] and scheduling, but an undersized database becomes a hard bottleneck that cannot be solved by throwing pod resources at it. For production deployments running multiple concurrent ingestion pipelines, **start with the Production-Ready specs**[3] and monitor database performance (specifically query execution times for `tag_usage` lookups) as the scaling metric [1].

## References

1. [Hive ingestion slowdown after upgrade to 1.12.3 · Issue #27158 · open-metadata/OpenMetadata · GitHub](https://github.com/open-metadata/OpenMetadata/issues/27158) — github.com
2. [Minimum Requirements | Official Documentation - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/deployment/minimum-requirements) — docs.open-metadata.org
3. [Production-Ready Requirements for OpenMetadata Deployment - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/deployment/production-ready-requirements) — docs.open-metadata.org
4. [openmetadata-helm-charts/README.md at main · open-metadata/openmetadata-helm-charts · GitHub](https://github.com/open-metadata/openmetadata-helm-charts/blob/main/README.md) — github.com
5. [OpenMetadata Ingestion Framework & Workflows](https://atlan.com/openmetadata-ingestion/) — atlan.com
6. [AKS Deployment: Prerequisites & Kubernetes Orchestrator - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/deployment/kubernetes/aks) — docs.open-metadata.org
7. [Profiler Workflow | OpenMetadata Profiling Workflow - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/profiler/profiler-workflow) — docs.open-metadata.org
8. [Kubernetes Helm Values | Official Documentation - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/deployment/kubernetes/values) — docs.open-metadata.org
9. [Streamlining data discovery for AI/ML with OpenMetadata on AKS and Azure NetApp Files | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/azurearchitectureblog/streamlining-data-discovery-for-aiml-with-openmetadata-on-aks-and-azure-netapp-f/4404467) — techcommunity.microsoft.com
10. [Data Cataloging and Governance using OpenMetadata at Thndr](https://medium.com/thndr-engineering/data-cataloging-and-governance-at-thndr-a1929d341db5) — medium.com
11. [Metadata Ingestion Best Practices - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/connectors/ingestion/best-practices) — docs.open-metadata.org
12. [Run the ingestion from the Collate UI - Collate Documentation](https://docs.getcollate.io/deployment/ingestion/openmetadata) — docs.getcollate.io
13. [How to Integrate OpenMetadata Test Suites with Your Data Pipelines](https://www.getcollate.io/blog/how-to-integrate-openmetadata-test-suites-with-your-data-pipelines) — getcollate.io
14. [Overview - OpenMetadata Standards](https://openmetadatastandards.org/data-products/overview/) — openmetadatastandards.org
15. [OpenMetadata Data Quality: A Complete Guide for 2025](https://atlan.com/know/openmetadata/data-quality/) — atlan.com
