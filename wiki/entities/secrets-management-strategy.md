---
type: entity
title: Secrets Management Strategy
created: 2026-02-23
updated: 2026-02-23
tags: [security, secrets-management, gitlab, data-platform]
related: [gestione-secrets, openmetadata-dremio-connector-password-issue, custom-connector-openmetadata, openmetadata-dremio-connector, dbt-cloud-security, kubernetes-etl-deployment-strategies]
sources: ["Gestione Secrets.md"]
---
# Secrets Management Strategy

The Data Platform's canonical approach to managing secrets, defined in [[Gestione Secrets.md]]. All infrastructure and application secrets are stored exclusively as GitLab CI/CD variables, organized by application group. This establishes a single, auditable source of truth and avoids scattered `.env` files, configuration files, or manual configuration.

## Principles

- **Single source of truth**: GitLab CI/CD Settings is the only location where secrets are defined.
- **Group-level scoping**: Secrets are assigned to the most specific GitLab group that needs them, enforcing least-privilege access.
- **No plaintext storage**: Secrets must never be stored in plaintext in code, configuration files, or connector implementations.
- **Auditability**: GitLab provides an audit log for CI/CD variable changes.

## GitLab Group Mapping

| Group | Purpose | Secrets |
|---|---|---|
| Data Platform/Infrastructure/Application | Infrastructure-level credentials | Platform-wide secrets |
| Data Platform/Application/dbt | dbt application secrets | Dremio credentials, OpenMetadata token |
| Data Platform/Application/Kestra | Kestra application secrets | Kestra credentials |
| Data Platform/Application/OpenMetadata | OpenMetadata secrets | (Flagged: Dremio password in plaintext issue) |

## Open Questions

1. Should the strategy include a formal rotation policy and audit trail?
2. How does this approach scale to non-GitLab environments (local development, Kubernetes-native deployments)?
3. Is the plaintext password issue in the OpenMetadata connector a blocker for production deployment?

## Related Pages

- [[gestione-secrets]] — The source note defining this strategy
- [[openmetadata-dremio-connector-password-issue]] — Tracking the plaintext password vulnerability
- [[custom-connector-openmetadata]] — Pattern for building custom OpenMetadata connectors
- [[openmetadata-dremio-connector]] — The specific connector with the password issue
- [[dbt-cloud-security]] — Related credential management in dbt Cloud
- [[kubernetes-etl-deployment-strategies]] — Alternative approach using Kubernetes Secrets