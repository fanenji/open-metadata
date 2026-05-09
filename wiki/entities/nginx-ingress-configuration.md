---
type: entity
title: NGINX Ingress Configuration
created: 2026-01-15
updated: 2026-01-15
tags: [infrastructure, kubernetes, networking, ingress]
related: [test-environment-infrastructure, metallb-configuration, kubernetes-etl-deployment-strategies]
sources: ["Installazione Test Env.md"]
---
# NGINX Ingress Configuration

NGINX Ingress Controller is deployed as the ingress gateway for the Kubernetes cluster in the Data Platform test environment.

## Access

- **URL**: `nginx.dp.liguriadigitale.it`

## Role in the Stack

The NGINX Ingress Controller sits behind [[metallb-configuration]] and routes external traffic to the appropriate internal services based on hostname rules. It enables the subdomain-based URL pattern used by all services (e.g., `dremio.dp.liguriadigitale.it`, `superset.dp.liguriadigitale.it`).

## Related

- [[test-environment-infrastructure]] — Overall test environment topology
- [[metallb-configuration]] — Load balancer providing the external IP
- [[kubernetes-etl-deployment-strategies]] — Deployment patterns on Kubernetes