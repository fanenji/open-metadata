---
type: source
title: Installazione Test Env
created: 2026-01-15
updated: 2026-01-15
tags: [infrastructure, test-environment, kubernetes, data-platform]
related: [test-environment-infrastructure, dremio, openmetadata, kestra, minio-deployment, superset-deployment, opensearch-deployment, jupyter-deployment, metallb-configuration, nginx-ingress-configuration]
sources: ["Installazione Test Env.md"]
---
# Installazione Test Env

This document is an infrastructure reference note listing the complete configuration of the Data Platform test environment. It includes credentials, server hostnames and IPs, and service URLs for all deployed components.

## Content Summary

The test environment is a Kubernetes-based deployment running on Liguria Digitale infrastructure. It consists of:

- **1 Master Node**: `ld-test-k8s-master-01.dp.liguriadigitale.it` (10.11.9.10)
- **4 Worker Nodes**: `ld-test-k8s-worker-02/05.dp.liguriadigitale.it` (10.11.9.11–14)
- **GitLab Repository**: `https://10.11.9.20/`
- **Load Balancer**: MetalLB at 10.11.9.100
- **Ingress Controller**: NGINX at `nginx.dp.liguriadigitale.it`

### Deployed Services

| Service | URL |
|---------|-----|
| MinIO | `https://minio-console.dp.liguriadigitale.it` |
| Dremio | `https://dremio.dp.liguriadigitale.it` |
| Superset | `https://superset.dp.liguriadigitale.it` |
| OpenSearch Dashboards | `https://opensearch-dashboards.dp.liguriadigitale.it` |
| Jupyter | `http://jupyter.dp.liguriadigitale.it` (HTTP only) |
| OpenMetadata | `https://openmetadata-test.dataliguria.it` (different domain) |
| Kestra | `https://kestra.dp.liguriadigitale.it` |

### Credentials

- Username: `dpadmin`
- Password: `dpAdm1n!`

### Client Tools

- **Freelens**: Installed on macOS for Kubernetes cluster management.

## Notes

- All services except Jupyter use HTTPS. Jupyter is HTTP-only, which may indicate intentional internal-only access or a configuration gap.
- OpenMetadata uses a separate subdomain (`dataliguria.it`) while all other services use `dp.liguriadigitale.it`.
- This document serves as a reference for deployment patterns (MetalLB + NGINX Ingress, service URL naming conventions) and should be kept updated as the environment evolves.