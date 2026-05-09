---
type: entity
title: Argo Workflows Security
created: 2026-05-07
updated: 2026-05-07
tags: [argo-workflows, security, authentication, authorization, kubernetes, oidc, rbac]
related: [kubernetes, reverse-proxy-auth-pattern, oss-vs-cloud-security-gap, orchestration-tool-comparison, k8s-native-orchestration]
sources: ["Orchestratori Data Platform_ Analisi Comparativa 2.md"]
---
# Argo Workflows Security

Argo Workflows is a CNCF-graduated, K8s-native workflow engine. Its security model leverages Kubernetes RBAC for execution authorization and supports OIDC for UI/API authentication.

## Architecture on K8s

- **Workflow Controller**: Observes `Workflow` CRDs and manages their lifecycle
- **Argo Server**: Optional REST API and web UI for managing workflows
- **Workflow CRD**: Custom Resource Definition describing workflow structure, tasks, dependencies
- **Executor**: Component inside each worker pod executing task logic

## Security Model

### Authentication Modes (Argo Server)
- **`server`**: Uses the Argo Server's own ServiceAccount for K8s API authentication
- **`client`** (default from v3.0+): Uses the K8s bearer token of the requesting client (delegates auth to K8s)
- **`sso`**: Enables Single Sign-On via OIDC

### SSO (OIDC)
- Integrates with Identity Providers (IdP) like Dex, Okta, Keycloak
- Configuration in `workflow-controller-configmap.yaml`
- Requires OIDC client creation and K8s secrets for client ID/secret

### RBAC
- **K8s RBAC**: Execution permissions determined by the ServiceAccount assigned to workflow pods
- **SSO RBAC** (v2.12+): Maps OIDC users/groups to K8s ServiceAccounts via annotations (e.g., `workflows.argoproj.io/rbac-rule: "'admin' in groups"`)
- **Namespace-level SSO RBAC** (v3.3+): Allows namespace owners to define their own OIDC-to-ServiceAccount mappings

### LDAP/SAML
- Not natively supported by Argo Server
- Can be achieved via an OIDC bridge like Dex (which supports LDAP and SAML as upstream IdPs)

## Deployment Considerations

- Configure a secure authentication mode (default may be insecure)
- Deep understanding of K8s RBAC (Roles, ClusterRoles, RoleBindings, ServiceAccounts) is essential
- Use NetworkPolicies to restrict access to the Argo Server

## Pros

- Truly K8s-native, deep integration with K8s ecosystem
- Highly scalable (inherits K8s scaling)
- Ideal for CI/CD and parallel batch processing
- Part of the Argo ecosystem (Argo CD, Argo Events, Argo Rollouts)

## Cons

- Requires strong K8s expertise
- UI is simpler than Airflow's
- Setup for production can be complex
- Multi-cluster management adds operational overhead