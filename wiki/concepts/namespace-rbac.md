---
type: concept
title: "Namespace Rbac"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: Namespace-Scoped RBAC
created: 2026-05-14
updated: 2026-05-14
tags: [kubernetes, rbac, namespaces, security, least-privilege]
related: [kubernetes-namespaces, resource-quotas-limit-ranges, omjob-operator, kubernetes-native-orchestrator]
sources: ["research-production-namespace-best-practices-2026-05-14.md"]
---

# Namespace-Scoped RBAC

Role-Based Access Control (RBAC) in Kubernetes restricts who can interact with resources in a namespace. For production environments, RBAC should follow the principle of least privilege: only the minimum necessary permissions should be granted to users, service accounts, and automation.

## Recommended Patterns

- **Only CI/CD pipelines and a small operations team** should have write access to the `production` namespace.
- **Developers should have read-only or no direct access** to production; they work in `development` or `staging` environments.
- **Service accounts used by operators** (e.g., the [[omjob-operator]]) should receive minimal, scoped permissions in the namespaces they manage.

## OMJob Operator RBAC Requirements

The [[omjob-operator]] needs just enough privileges to manage ingestion pipeline resources in its designated namespace. At minimum, it requires permissions to:
- Create, get, list, watch, update, and delete Jobs and CronJobs
- Create, get, list, and delete Pods (to monitor job execution)
- Create, get, list, and delete ConfigMaps and Secrets (for pipeline configurations)

These permissions should be scoped to a single namespace (e.g., `openmetadata` or `ingestion`) using a Role and RoleBinding, rather than granting cluster-wide access via ClusterRole and ClusterRoleBinding.

## Cross-Namespace Considerations

If OpenMetadata and its external dependencies (MySQL, ElasticSearch) reside in different namespaces, service accounts may need cross-namespace access. This should be explicitly configured and audited, as it weakens namespace isolation. Where possible, co-locate tightly coupled components in the same namespace to simplify RBAC and reduce attack surface.