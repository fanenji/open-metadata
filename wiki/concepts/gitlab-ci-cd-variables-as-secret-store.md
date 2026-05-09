---
type: concept
title: GitLab CI/CD Variables as Secret Store
created: 2026-02-23
updated: 2026-02-23
tags: [security, secrets-management, gitlab, ci-cd, data-platform]
related: [gestione-secrets, secrets-management-strategy, openmetadata-dremio-connector-password-issue, kubernetes-etl-deployment-strategies]
sources: ["Gestione Secrets.md"]
---
# GitLab CI/CD Variables as Secret Store

The practice of using GitLab's built-in CI/CD variable mechanism as the single, authoritative store for all infrastructure and application secrets. This approach is the canonical secrets management strategy for the Data Platform, as defined in [[Gestione Secrets.md]].

## Advantages

- **Single source of truth**: Eliminates scattered `.env` files, configuration files, and manual secret management.
- **Auditability**: GitLab provides audit logs for variable changes.
- **Access control**: Variables can be scoped to specific groups, projects, or environments.
- **Integration**: Native to the GitLab CI/CD pipeline, requiring no additional infrastructure.
- **Masking**: GitLab can mask variable values in job logs.

## Limitations

- **GitLab dependency**: Not applicable to non-GitLab environments (local development, other CI/CD systems).
- **No rotation policy**: GitLab CI/CD variables lack built-in rotation or expiration mechanisms.
- **No encryption at rest**: Variables are encrypted at rest by GitLab, but the encryption key is managed by GitLab.

## Comparison with Alternatives

| Approach | Pros | Cons |
|---|---|---|
| GitLab CI/CD Variables | Native, auditable, no extra infra | GitLab-only, no rotation |
| Kubernetes Secrets | Kubernetes-native, RBAC | Requires K8s, base64 encoding |
| HashiCorp Vault | Rotation, dynamic secrets, audit | Operational complexity |
| .env files | Simple, portable | Not auditable, easy to leak |

## Related Pages

- [[gestione-secrets]] — The source note defining this approach
- [[secrets-management-strategy]] — Formal documentation of the strategy
- [[openmetadata-dremio-connector-password-issue]] — A violation of this approach
- [[kubernetes-etl-deployment-strategies]] — Alternative deployment context