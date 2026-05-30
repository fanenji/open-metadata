---
type: concept
title: Exit Handler Guarantee
created: 2026-05-14
updated: 2026-05-14
tags: [reliability, ingestion, kubernetes, operator, callbacks]
related: [omjob-operator, kubernetes-native-orchestrator, ingestion-pipeline-troubleshooting, data-quality, data-lineage]
sources: ["OMD - Kubernetes Orchestrator Operations & Troubleshooting.md"]
---
# Exit Handler Guarantee

The assurance that pipeline completion and failure callbacks execute reliably at the end of every ingestion run. Exit handlers are critical for metadata integrity — they trigger actions such as data quality test result callbacks, lineage finalization, and status updates that downstream systems depend on.

## Reliability by Orchestration Mode

| Mode | Exit Handler Behavior |
|------|----------------------|
| **Apache Airflow** | Guaranteed — Airflow's task lifecycle ensures handlers execute. |
| **Plain K8s-native** | Best-effort — no guarantee; handlers may not execute if the pod terminates abnormally or the node fails. |
| **K8s with OMJob Operator** | Guaranteed — the operator monitors Job lifecycle and ensures handlers run regardless of pod termination conditions. |

## Why It Matters

Without guaranteed exit handlers, ingestion pipelines may complete data extraction but fail to finalize metadata updates. This can lead to:

- Incomplete [[data-lineage]] graphs.
- Missing [[data-quality]] test results.
- Stale or inconsistent metadata in the [[unified-metadata-graph]].
- Silent failures that are difficult to detect without manual inspection.

## Operator Implementation

The [[omjob-operator]] achieves this guarantee by managing the full lifecycle of ingestion Jobs and CronJobs through custom resources (CronOMJob). It intercepts Job completion and failure events at the Kubernetes API level, executing exit handlers before marking the custom resource as complete. This is the primary architectural advantage of the operator over plain K8s-native mode and is a key decision factor for production deployments.