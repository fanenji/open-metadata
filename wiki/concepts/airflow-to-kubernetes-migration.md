---
type: concept
title: Airflow to Kubernetes Migration
created: 2026-05-14
updated: 2026-05-14
tags: [migration, kubernetes, airflow, ingestion, operations]
related: [kubernetes-native-orchestrator, pipeline-service-client, helm-charts, omjob-operator, ingestion-pipeline-troubleshooting]
sources: ["OMD - Kubernetes Orchestrator Operations & Troubleshooting.md"]
---
# Airflow to Kubernetes Migration

The process of switching OpenMetadata ingestion pipelines from Apache Airflow orchestration to the Kubernetes native orchestrator. This migration is a manual, multi-step procedure that requires stopping existing Airflow-managed pipelines, reconfiguring the [[pipeline-service-client]] via [[helm-charts]], redeploying OpenMetadata, and individually re-deploying each pipeline.

## Migration Steps

1. **Stop existing Airflow-managed pipelines** — Disable or delete all pipelines currently managed by Airflow.
2. **Update Helm values** — Change the pipeline service client configuration from `type: "airflow"` to `type: "k8s"` in the Helm values file.
3. **Redeploy OpenMetadata** — Apply the updated Helm configuration to the cluster.
4. **Re-deploy pipelines** — Navigate to each pipeline in the OpenMetadata UI and click "Deploy" to create the corresponding Kubernetes resources (Jobs or CronJobs).

## Critical Caveat

**Pipeline schedules are not automatically transferred.** After switching to the Kubernetes orchestrator, every pipeline's schedule must be manually re-configured. This represents a significant operational burden for deployments with many scheduled ingestion pipelines and should be factored into migration planning.

## Rollback

To revert to Airflow, reverse the Helm `type` value back to `"airflow"`, redeploy, and re-deploy pipelines. The same manual re-deployment and schedule re-configuration applies.

## Related Considerations

- The [[kubernetes-native-orchestrator]] eliminates the Airflow infrastructure dependency entirely.
- Using the [[omjob-operator]] provides guaranteed exit handlers and failure diagnostics that Airflow also provides, making it the recommended target for production migrations.
- The [[airflow-storage-requirements]] (RWX volumes) become irrelevant after a successful migration.