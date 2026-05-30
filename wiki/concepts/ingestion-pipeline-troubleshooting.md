---
type: concept
title: Ingestion Pipeline Troubleshooting
created: 2026-05-14
updated: 2026-05-14
tags: [troubleshooting, kubernetes, ingestion, operations, diagnostics]
related: [kubernetes-native-orchestrator, omjob-operator, exit-handler-guarantee, airflow-to-kubernetes-migration]
sources: ["OMD - Kubernetes Orchestrator Operations & Troubleshooting.md"]
---
# Ingestion Pipeline Troubleshooting

A consolidated reference for diagnosing and resolving common failure modes in OpenMetadata ingestion pipelines running on the [[kubernetes-native-orchestrator]]. This guide covers both plain K8s-native mode and operator mode with the [[omjob-operator]].

## Common Failure Modes

### Pipeline Stuck in "Queued" State

The pod cannot be scheduled. Diagnose with:

```shell
kubectl get pods -l app.kubernetes.io/pipeline=<pipeline-name>
kubectl describe pod <pod-name>
```

**Common causes:**
- **Image pull errors** — Verify `imagePullSecrets` are correctly configured.
- **Insufficient cluster resources** — Increase CPU/memory limits in Helm values or add cluster nodes.
- **Node selector constraints** — Ensure node affinity rules match available nodes.

### Permission Denied (RBAC) Errors

Verify the OpenMetadata service account has the required Kubernetes permissions:

```shell
kubectl auth can-i create jobs --as=system:serviceaccount:<namespace>:openmetadata
```

The service account must have permissions to create Jobs, CronJobs, and ConfigMaps in the target namespace.

### Ingestion Pod Crashes (OOMKilled)

The pod exceeds its memory limit. Increase limits in Helm values:

```yaml
k8s:
  resources:
    limits:
      memory: "8Gi"
    requests:
      memory: "2Gi"
```

### CronJob Not Triggering

Inspect the CronJob resource:

```shell
kubectl get cronjob <cronjob-name> -o yaml
kubectl describe cronjob <cronjob-name>
```

**Common issues:**
- Invalid cron expression in the schedule.
- `startingDeadlineSeconds` too short for the cluster's scheduling latency.
- Concurrency policy blocking execution (e.g., previous job still running).

## Log Retrieval

Pipeline logs are retrieved directly from Kubernetes pod logs with pagination (~1MB chunks). View them in the OpenMetadata UI under **Settings → Services → Agents → Logs**, or directly via kubectl:

```shell
kubectl logs job/<pipeline-name> -c main
```

## Operator vs. Plain K8s Diagnostics

The [[omjob-operator]] provides enhanced failure diagnostics not available in plain K8s-native mode. When troubleshooting in operator mode, also check the CronOMJob custom resource status for operator-specific error details.