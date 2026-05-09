---
type: entity
title: MetalLB Configuration
created: 2026-01-15
updated: 2026-01-15
tags: [infrastructure, kubernetes, networking, load-balancer]
related: [test-environment-infrastructure, nginx-ingress-configuration, kubernetes-etl-deployment-strategies]
sources: ["Installazione Test Env.md"]
---
# MetalLB Configuration

MetalLB is deployed as the bare-metal load balancer for the Kubernetes cluster in the Data Platform test environment.

## Configuration

- **IP Pool**: 10.11.9.100 (single IP for the load balancer service)
- **Role**: Provides external IP addresses for services exposed via [[nginx-ingress-configuration]]

## Role in the Stack

MetalLB enables the Kubernetes cluster to expose services without a cloud provider's load balancer. It assigns the 10.11.9.100 IP to the NGINX Ingress controller, which then routes traffic to individual services based on hostname rules.

## Related

- [[test-environment-infrastructure]] — Overall test environment topology
- [[nginx-ingress-configuration]] — Ingress controller using MetalLB
- [[kubernetes-etl-deployment-strategies]] — Deployment patterns on Kubernetes