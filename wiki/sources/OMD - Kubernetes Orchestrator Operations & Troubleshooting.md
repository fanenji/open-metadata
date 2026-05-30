---
type: source
title: "OMD - Kubernetes Orchestrator Operations & Troubleshooting"
created: 2026-05-14
updated: 2026-05-14
tags: [kubernetes, ingestion, troubleshooting, migration, operations]
related: [kubernetes-native-orchestrator, omjob-operator, pipeline-service-client, helm-charts, airflow-to-kubernetes-migration, ingestion-pipeline-troubleshooting, exit-handler-guarantee]
sources: ["OMD - Kubernetes Orchestrator Operations & Troubleshooting.md"]
authors: []
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/deployment/ingestion/kubernetes/troubleshooting"
venue: "OpenMetadata Official Documentation"
---
# OMD - Kubernetes Orchestrator Operations & Troubleshooting

Official OpenMetadata v1.12.x guide covering validation, monitoring, and troubleshooting of the Kubernetes native orchestrator for ingestion pipelines. Includes procedures for viewing pipeline logs, diagnosing common failure modes (Queued state, OOMKilled, RBAC errors, CronJob scheduling issues), and migrating from Apache Airflow to the K8s-native orchestrator. Provides a comparison table of Airflow, plain K8s-native, and OMJob Operator modes, highlighting the operator's exit handler guarantee and failure diagnostics as key differentiators.

## Key Takeaways

1. **Validation is three-step**: Health check in UI → deploy test pipeline → verify K8s resources via kubectl.
2. **Logs are K8s-native**: Retrieved directly from pod logs with ~1MB chunk pagination; viewable in both OpenMetadata UI and kubectl.
3. **Common failure modes are well-defined**: Queued state (image pull, resources, node selectors), RBAC errors, OOMKilled pods, CronJob scheduling issues.
4. **Migration from Airflow is manual**: Requires stopping Airflow pipelines, switching Helm `type` value, redeploying, and re-deploying each pipeline individually. Schedules are not auto-transferred.
5. **OMJob Operator provides superior reliability**: Guaranteed exit handlers and failure diagnostics vs. best-effort in plain K8s-native mode.