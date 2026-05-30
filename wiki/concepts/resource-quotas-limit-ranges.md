---
type: concept
title: "Resource Quotas Limit Ranges"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: Resource Quotas and Limit Ranges
created: 2026-05-14
updated: 2026-05-14
tags: [kubernetes, resource-quotas, limit-ranges, production, governance]
related: [kubernetes-namespaces, namespace-rbac, omjob-operator, kubernetes-native-orchestrator]
sources: ["research-production-namespace-best-practices-2026-05-14.md"]
---

# Resource Quotas and Limit Ranges

ResourceQuota and LimitRange are paired Kubernetes policy objects that protect production namespaces from resource starvation and misconfigured pods. They are considered non-negotiable for any production namespace.

## ResourceQuota

A ResourceQuota caps the total amount of CPU, memory, storage, and object counts (pods, services, ConfigMaps) that a namespace can consume.

Example for a production namespace:
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

## LimitRange

A LimitRange sets default, minimum, and maximum resource requests/limits for containers within the namespace. This ensures every pod receives sensible defaults and prevents a single container from requesting excessive resources.

## Best Practices

- **Always pair a ResourceQuota with a LimitRange.** Quotas alone do not enforce per-container defaults; LimitRanges fill that gap.
- **Start with generous limits and tighten them** based on observed usage over time.
- **Set `maxLimitRequestRatio`** to avoid extreme overcommitment (e.g., a container requesting 100m CPU but setting a limit of 8 CPUs).
- **Use object count quotas** to prevent overly many ConfigMaps, Secrets, or Services from accumulating.
- **Monitor quota usage** with alerts when capacity approaches the hard limit.

## OpenMetadata-Specific Considerations

When running the [[kubernetes-native-orchestrator]] with the [[omjob-operator]], ingestion jobs are created as Kubernetes Jobs in the designated namespace. Apply ResourceQuotas to prevent a surge of ingestion jobs from starving the OpenMetadata application pods of resources. Start with quotas that reflect your expected ingestion concurrency and adjust based on profiling data from actual pipeline runs.