---
type: concept
title: "Kubernetes Namespaces"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: Kubernetes Namespaces
created: 2026-05-14
updated: 2026-05-14
tags: [kubernetes, namespaces, production, isolation, governance]
related: [kubernetes, resource-quotas-limit-ranges, namespace-rbac, omjob-operator, kubernetes-native-orchestrator, helm-charts, on-premises-kubernetes-deployment]
sources: ["research-production-namespace-best-practices-2026-05-14.md"]
---

# Kubernetes Namespaces

A Kubernetes namespace is a logical partition inside a cluster that scopes resource names and provides a boundary for policies. Each namespace acts as a virtual sub-cluster, allowing multiple teams or environments to share the same physical infrastructure without interference. The default namespace (`default`) is automatically created but is generally unsuitable for production because it lacks isolation and makes accidental modifications more likely.

## Key Properties

- Resources in different namespaces can have the same name (e.g., a service called `database` can exist in both `dev` and `prod`).
- Namespaces cannot be nested; every Kubernetes object belongs to exactly one namespace.
- Policies such as [[resource-quotas-limit-ranges|ResourceQuotas]], LimitRanges, NetworkPolicies, and [[namespace-rbac|RBAC]] rules can be scoped to a namespace.

## Core Best Practices

### 1. Separate Environments by Namespace

Use distinct namespaces for development, staging, and production environments within the same cluster. This prevents operators from accidentally altering production resources while working in a lower environment.

Recommended naming conventions:
- `development` or `dev`
- `staging` or `uat`
- `production` or `prod`

Avoid placing production workloads in the `default` namespace.

### 2. Isolate Teams and Applications

For clusters serving multiple teams, assign a dedicated namespace to each team. The optimal granularity depends on team size, project complexity, and organizational structure:

- **Small teams / few microservices** — a single namespace with labels to distinguish versions may suffice.
- **Large organizations / many services** — separate namespaces per team or per critical service improve security and resource fairness.

Labels (e.g., `app: myapp`, `version: v2`) should still be used inside a namespace to organize resources without creating unnecessary namespace sprawl.

### 3. Enforce Resource Quotas and Limit Ranges

Production namespaces must be protected from resource starvation and misconfigured pods. See [[resource-quotas-limit-ranges]] for detailed configuration guidance.

### 4. Apply Role-Based Access Control (RBAC)

Restrict who can interact with a production namespace using RBAC policies. See [[namespace-rbac]] for patterns and OpenMetadata-specific recommendations.

### 5. Network and Ingress Isolation

Use NetworkPolicies to control traffic flow between namespaces. In production, the OpenMetadata application typically exposes ports `8585` and `8586` through a Kubernetes Service, optionally fronted by an Ingress controller. Namespace-scoped ingress rules can further limit exposure.

## Relevance to OpenMetadata Deployments

[[openmetadata]]'s official [[helm-charts]] support namespace-aware deployment. In production, you should:

- Deploy OpenMetadata in its own namespace (e.g., `openmetadata`) rather than in `default`.
- If using the [[kubernetes-native-orchestrator]], enable the [[omjob-operator]] inside that namespace (or a dedicated `ingestion` namespace) to run ingestion pipelines as native Kubernetes Jobs.
- Apply [[resource-quotas-limit-ranges|ResourceQuotas]] to the namespace to prevent ingestion jobs from overwhelming cluster resources.
- Use [[namespace-rbac|RBAC]] to grant the omjob-operator just enough privileges to create Jobs, Pods, and ConfigMaps in the designated namespace.

When running [[on-premises-kubernetes-deployment]] with shared storage via NFS (e.g., [[nfs-subdir-external-provisioner]]), the provisioner often operates cluster-wide. However, PersistentVolumeClaims are namespace-scoped, so you can still enforce storage quotas per namespace.

## Monitoring and Governance

Regularly audit namespace usage against quotas. Integrate Kubernetes metrics with monitoring systems to fire alerts when resource consumption nears defined quotas. Tools like OpenMetadata itself can help track data assets and pipelines across namespaces, adding a layer of governance.