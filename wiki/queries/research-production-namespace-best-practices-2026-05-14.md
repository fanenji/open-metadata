---
type: query
title: "Research: Production Namespace Best Practices"
created: 2026-05-14
origin: deep-research
tags: [research]
---

# Research: Production Namespace Best Practices

---
type: concept
title: Production Namespace Best Practices
tags: [kubernetes, namespaces, resource-quotas, rbac, openmetadata]
related: [[kubernetes]], [[omjob-operator]], [[kubernetes-native-orchestrator]], [[helm-charts]], [[on-premises-kubernetes-deployment]]
---

# Production Namespace Best Practices

Kubernetes namespaces are foundational to operating safe, scalable, and governable production clusters. This page synthesises community and vendor guidance on creating and managing namespaces for production workloads, and applies those patterns to [[openmetadata]] deployments on Kubernetes.

## What Is a Kubernetes Namespace?

A namespace is a logical partition inside a Kubernetes cluster that scopes resource names and provides a boundary for policies [1][4]. Each namespace acts as a virtual sub‑cluster, allowing multiple teams or environments to share the same physical infrastructure without interference. The default namespace (`default`) is automatically created but is generally unsuitable for production because it lacks isolation and makes accidental modifications more likely [14].

Key properties:
- Resources in different namespaces can have the same name (e.g., a service called `database` can exist in both `dev` and `prod`).
- Namespaces cannot be nested; every Kubernetes object belongs to exactly one namespace [2].
- Policies such as ResourceQuotas, LimitRanges, NetworkPolicies, and RBAC rules can be scoped to a namespace [4][13].

## Core Best Practices

### 1. Separate Environments by Namespace
Use distinct namespaces for development, staging, and production environments within the same cluster [3][11]. This prevents operators from accidentally altering production resources while working in a lower environment.

Recommended naming conventions:
- `development` or `dev`
- `staging` or `uat`
- `production` or `prod`

Avoid placing production workloads in the `default` namespace [14].

### 2. Isolate Teams and Applications
For clusters serving multiple teams, assign a dedicated namespace to each team [2][5]. The optimal granularity depends on team size, project complexity, and organisational structure [5]:

- **Small teams / few microservices** – a single namespace with labels to distinguish versions may suffice [2].
- **Large organisations / many services** – separate namespaces per team or per critical service improve security and resource fairness.

Labels (e.g., `app: myapp`, `version: v2`) should still be used inside a namespace to organise resources without creating unnecessary namespace sprawl [2][3].

### 3. Enforce Resource Quotas and Limit Ranges
Production namespaces must be protected from resource starvation and misconfigured pods.

- **ResourceQuota** – caps the total amount of CPU, memory, storage, and object counts (pods, services, ConfigMaps) that a namespace can consume [13][14]. Example:
  ```yaml
  apiVersion: v1
  kind: ResourceQuota
  metadata:
    name: prod-quota
    namespace: production
  spec:
    hard:
      requests.cpu: "8"
      requests.memory: "16Gi"
      limits.cpu: "16"
      limits.memory: "32Gi"
      pods: "50"
  ```
- **LimitRange** – sets default, minimum, and maximum resource requests/limits for containers within the namespace [11][12]. This ensures every pod receives sensible defaults and prevents a single container from requesting excessive resources.

Best practices for quotas and limits [11][12]:
- Always pair a ResourceQuota with a LimitRange.
- Start with generous limits and tighten them based on observed usage.
- Set `maxLimitRequestRatio` to avoid extreme overcommitment.
- Use object count quotas to prevent overly many ConfigMaps, Secrets, or Services.
- Monitor quota usage with alerts when capacity approaches the hard limit.

### 4. Apply Role‑Based Access Control (RBAC)
Restrict who can interact with a production namespace using RBAC policies [3][4]. Typical patterns:
- Only CI/CD pipelines and a small operations team have write access to the `production` namespace.
- Developers have read‑only or no direct access to production; they work in `development` or `staging` environments.
- Service accounts used by operators (e.g., the [[omjob-operator]]) should receive minimal, scoped permissions in the namespaces they manage.

### 5. Network and Ingress Isolation
Use NetworkPolicies to control traffic flow between namespaces. In production, the OpenMetadata application typically exposes ports `8585` and `8586` through a Kubernetes Service, optionally fronted by an Ingress controller [10]. Namespace‑scoped ingress rules can further limit exposure.

## Relevance to OpenMetadata Deployments

[[openmetadata]]’s official [[helm-charts]] support namespace‑aware deployment. In production, you should:
- Deploy OpenMetadata in its own namespace (e.g., `openmetadata`) rather than in `default` [9][10].
- If using the [[kubernetes-native-orchestrator]], enable the [[omjob-operator]] inside that namespace (or a dedicated `ingestion` namespace) to run ingestion pipelines as native Kubernetes Jobs [8].
- Apply ResourceQuotas to the namespace to prevent ingestion jobs from overwhelming cluster resources.
- Use RBAC to grant the omjob‑operator just enough privileges to create Jobs, Pods, and ConfigMaps in the designated namespace.

When running [[on-premises-kubernetes-deployment]] with shared storage via NFS (e.g., [[nfs-subdir-external-provisioner]]), the provisioner often operates cluster‑wide. However, PersistentVolumeClaims are namespace‑scoped, so you can still enforce storage quotas per namespace.

## Monitoring and Governance

Regularly audit namespace usage against quotas. Tools like OpenMetadata itself can help track data assets and pipelines across namespaces, adding a layer of governance. Integrate Kubernetes metrics with monitoring systems to fire alerts when resource consumption nears defined quotas [11].

## References

[1] “Kubernetes Namespace: Basics, Tutorial & Critical Best Practices,” Tigera, https://www.tigera.io/learn/guides/kubernetes-namespace/  
[2] “Kubernetes namespaces: Best practices?,” Stack Overflow, https://stackoverflow.com/questions/50914136/kubernetes-namespaces-best-practices  
[3] J. Singh, “Kubernetes Production Best Practices — Part I,” Medium, https://medium.com/@jaspreet.singh/kubernetes-production-best-practices-part-i-8a8b5cbee9e6  
[4] “Kubernetes Namespaces: Security Best Practices,” Wiz, https://www.wiz.io/academy/kubernetes-namespaces-security-best-practices  
[5] “Kubernetes Namespace: How To Use It To Organize And Optimize Costs,” Cast AI, https://cast.ai/blog/kubernetes-namespace-how-to-use-it-to-organize-and-optimize-costs/  
[6] “Deployment | OpenMetadata Installation & Setup Guide,” OpenMetadata Docs, https://docs.open-metadata.org/latest/deployment  
[8] “AWS EKS Deployment | OpenMetadata Kubernetes Guide,” OpenMetadata Docs, https://docs.open-metadata.org/latest/deployment/kubernetes/eks  
[9] “Try OpenMetadata in Kubernetes,” OpenMetadata Docs, https://docs.open-metadata.org/latest/deployment/kubernetes/local  
[10] “Kubernetes Deployment | Official Documentation,” OpenMetadata Docs, https://docs.open-metadata.org/latest/deployment/kubernetes  
[11] “How to Set Up Kubernetes Namespace Resource Quotas and LimitRanges,” OneUptime, https://oneuptime.com/blog/kubernetes-namespace-resource-quotas-limitranges-setup  
[12] “Hands-on Guide on Kubernetes Resource Quotas & Limit Ranges,” PerfectScale, https://www.perfectscale.io/blog/kubernetes-resource-quotas-limit-ranges  
[13] “Resource Quotas,” Kubernetes Documentation, https://kubernetes.io/docs/concepts/policy/resource-quotas/  
[14] “Kubernetes Namespaces, Resource Quota, and Limits for QoS in Cluster,” CloudBees, https://www.cloudbees.com/blog/kubernetes-namespaces-resource-quota-and-limits-for-qos-in-cluster

## References

1. [Kubernetes Namespace: Basics, Tutorial & Critical Best Practices](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-namespace/) — tigera.io
2. [Kubernetes namespaces: Best practices? - Stack Overflow](https://stackoverflow.com/questions/68020893/kubernetes-namespaces-best-practices) — stackoverflow.com
3. [Kubernetes Production Best Practices — Part I](https://medium.com/@singhjaspreet291/kubernetes-production-best-practices-part-i-bf75cf41a74e) — medium.com
4. [Kubernetes Namespaces: Security Best Practices | Wiz](https://www.wiz.io/academy/container-security/kubernetes-namespaces) — wiz.io
5. [Kubernetes Namespace: How To Use It To Organize And Optimize Costs - Cast AI](https://cast.ai/blog/kubernetes-namespace-how-to-use-it-to-organize-and-optimize-costs/) — cast.ai
6. [Deployment | OpenMetadata Installation & Setup Guide - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/deployment) — docs.open-metadata.org
7. [Effortlessly Setting Up a Development OpenMetadata Data Catalog with Terraform](https://medium.com/d-one/effortlessly-setting-up-a-development-openmetadata-data-catalog-with-terraform-14cdc44d40c7) — medium.com
8. [AWS EKS Deployment | OpenMetadata Kubernetes Guide - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/deployment/kubernetes/eks) — docs.open-metadata.org
9. [Try OpenMetadata in Kubernetes - OpenMetadata Documentation](https://docs.open-metadata.org/v1.11.x/quick-start/local-kubernetes-deployment) — docs.open-metadata.org
10. [Kubernetes Deployment | Official Documentation - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/deployment/kubernetes) — docs.open-metadata.org
11. [How to Set Up Kubernetes Namespace Resource Quotas and LimitRanges](https://oneuptime.com/blog/post/2026-02-20-kubernetes-namespace-resource-quotas/view) — oneuptime.com
12. [Hands-on Guide on Kubernetes Resource Quotas & Limit Ranges](https://www.perfectscale.io/blog/kubernetes-resource-quotas-limit-ranges) — perfectscale.io
13. [Resource Quotas | Kubernetes](https://kubernetes.io/docs/concepts/policy/resource-quotas/) — kubernetes.io
14. [Kubernetes Namespaces, Resource Quota, and Limits for QoS in Cluster](https://www.cloudbees.com/blog/kubernetes-namespaces-resource-quota-limits-qos-cluster) — cloudbees.com
