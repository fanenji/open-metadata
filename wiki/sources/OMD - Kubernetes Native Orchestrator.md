---
type: source
title: "OMD - Kubernetes Native Orchestrator"
created: 2026-05-14
updated: 2026-05-14
tags: [kubernetes, ingestion, orchestration, operator, crd]
related: [kubernetes-native-orchestrator, omjob-operator, pipeline-service-client, ingestion-framework, openmetadata]
sources: ["OMD - Kubernetes Native Orchestrator.md"]
authors: []
year: 2025
url: "https://docs.open-metadata.org/v1.12.x/deployment/ingestion/kubernetes"
venue: "OpenMetadata Official Documentation"
---
# OMD - Kubernetes Native Orchestrator

Official OpenMetadata documentation (v1.12.x) describing how to run ingestion pipelines using native Kubernetes Jobs and CronJobs, eliminating the dependency on Apache Airflow. The source covers two orchestration modes: the recommended OMJob Operator (using CRDs `OMJob` and `CronOMJob`) and native Kubernetes Jobs (using standard `Job` and `CronJob` resources). It provides complete Helm values configurations, RBAC permission sets, and guidance on choosing between the two options based on production reliability requirements.

Key differentiators include the exit handler guarantee (ensuring pipeline status is always reported even on pod crashes) and automatic failure diagnostics, both exclusive to the OMJob Operator mode.