---
type: concept
title: K8s-native Orchestration
created: 2026-05-07
updated: 2026-05-07
tags: [orchestration, kubernetes, argo-workflows, flyte, cloud-native]
related: [argo-workflows-security, flyte-security, kubernetes, orchestration-tool-comparison]
sources: ["Orchestratori Data Platform_ Analisi Comparativa 2.md"]
---
# K8s-native Orchestration

A category of orchestration tools designed specifically for Kubernetes, as opposed to tools adapted for K8s deployment. This distinction affects deployment complexity, scalability, security integration depth, and operational requirements.

## Characteristics

- **Native CRD-based**: Workflows are defined as Kubernetes Custom Resource Definitions (CRDs)
- **Container-native execution**: Each workflow step runs as a container in a pod
- **Deep K8s integration**: Leverages K8s primitives (ServiceAccounts, RBAC, NetworkPolicies, Secrets) directly
- **No external dependencies**: No need for separate metadata databases or schedulers (beyond K8s itself)

## Examples

- **Argo Workflows**: CNCF project, workflow steps as containers, YAML-based workflow definitions
- **Flyte**: Originally by Lyft, strongly typed, Python-defined workflows, ML-focused

## Advantages

- **Scalability**: Inherits K8s horizontal scaling
- **Security**: Leverages K8s RBAC for execution security; OIDC integration for UI/API auth
- **Isolation**: Each step runs in its own container with independent resource limits
- **Ecosystem synergy**: Integrates with other K8s-native tools (Argo CD, K8s monitoring, etc.)

## Disadvantages

- **Requires K8s expertise**: Installation, configuration, and management demand strong K8s skills
- **UI less mature**: Generally simpler UIs compared to Airflow
- **Setup complexity**: Production-grade configuration can be complex
- **Multi-cluster challenges**: Managing across multiple clusters adds operational overhead

## When to Choose

- When the team has strong K8s expertise
- When deep K8s integration is desired for security and resource management
- When scaling to very large workloads (Airflow's scheduler can become a bottleneck)
- When the organization already uses the Argo ecosystem (Argo CD, Argo Events)