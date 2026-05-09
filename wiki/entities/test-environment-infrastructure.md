---
type: entity
title: Test Environment Infrastructure
created: 2026-01-15
updated: 2026-01-15
tags: [infrastructure, kubernetes, test-environment, data-platform]
related: [dremio, openmetadata, kestra, minio-deployment, superset-deployment, opensearch-deployment, jupyter-deployment, metallb-configuration, nginx-ingress-configuration, kubernetes-etl-deployment-strategies, container-image-strategy-for-data-pipelines]
sources: ["Installazione Test Env.md"]
---
# Test Environment Infrastructure

The test environment for the Data Platform is a Kubernetes-based deployment running on Liguria Digitale infrastructure. It serves as a staging ground for validating all platform components before production deployment.

## Topology

- **Master Node**: `ld-test-k8s-master-01.dp.liguriadigitale.it` (10.11.9.10)
- **Worker Nodes**: `ld-test-k8s-worker-02/05.dp.liguriadigitale.it` (10.11.9.11–14)
- **GitLab**: `https://10.11.9.20/` (source code repository)

## Networking

- **Load Balancer**: MetalLB at 10.11.9.100
- **Ingress Controller**: NGINX at `nginx.dp.liguriadigitale.it`

## Deployed Services

The test environment hosts the full Data Platform stack:

- [[minio-deployment]] — Object storage (S3-compatible)
- [[dremio]] — Query engine
- [[superset-deployment]] — BI/visualization
- [[opensearch-deployment]] — Search/analytics engine
- [[jupyter-deployment]] — Notebook environment
- [[openmetadata]] — Data catalog/governance
- [[kestra]] — Workflow orchestration

## Domain Convention

Most services use the `dp.liguriadigitale.it` domain with subdomain naming (e.g., `dremio.dp.liguriadigitale.it`). [[openmetadata]] is an exception, using `openmetadata-test.dataliguria.it`.

## Client Tools

- **Freelens**: Installed on macOS for Kubernetes cluster management.

## Security Notes

- Credentials (`dpadmin`/`dpAdm1n!`) are shared across the environment.
- [[jupyter-deployment]] is HTTP-only, while all other services use HTTPS.