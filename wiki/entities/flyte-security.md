---
type: entity
title: Flyte Security
created: 2026-05-07
updated: 2026-05-07
tags: [flyte, security, authentication, authorization, kubernetes, oidc, machine-learning]
related: [kubernetes, oss-vs-cloud-security-gap, orchestration-tool-comparison, k8s-native-orchestration]
sources: ["Orchestratori Data Platform_ Analisi Comparativa 2.md"]
---
# Flyte Security

Flyte is a K8s-native, strongly typed orchestration platform originally developed by Lyft, particularly suited for machine learning and complex data processing workflows. Its security model relies on OIDC/OAuth2 for authentication and K8s RBAC for authorization.

## Architecture on K8s

- **Flyteconsole**: Web UI for managing workflows and executions
- **Flyteadmin**: Management service for workflow definitions, executions, and metadata
- **Flytepropeller**: K8s controller that executes workflow tasks as pods
- **Datacatalog**: Stores metadata about task inputs and outputs for caching
- **Flyteidl**: Interface Definition Language for service definitions

## Security Model

### Authentication
- **OIDC/OAuth2**: Primary authentication mechanism for UI and API
- Integrates with Identity Providers (IdP) supporting OIDC (e.g., Keycloak, Okta, Azure AD)
- Configuration via Helm chart values

### Authorization
- **K8s RBAC**: Execution permissions managed via K8s ServiceAccounts
- No built-in granular RBAC beyond K8s primitives

### LDAP/SAML
- Not natively supported
- Can be achieved via an OIDC bridge (e.g., Dex) that supports LDAP or SAML as upstream IdPs

## Deployment Considerations

- Requires OIDC provider setup and configuration
- Deep K8s expertise needed for RBAC management
- Helm chart simplifies deployment but security configuration requires careful attention

## Pros

- Strong typing and reproducibility for ML workflows
- K8s-native, inherits K8s scalability
- Good for complex, versioned data pipelines
- Python-defined workflows

## Cons

- Requires strong K8s expertise
- Smaller community than Airflow
- ML-focused; may be overkill for simple data pipelines
- OIDC dependency for authentication adds setup complexity