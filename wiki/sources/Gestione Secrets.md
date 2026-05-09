---
type: source
title: Gestione Secrets
created: 2026-02-23
updated: 2026-02-23
tags: [security, secrets-management, gitlab, data-platform]
related: [secrets-management-strategy, openmetadata-dremio-connector-password-issue, custom-connector-openmetadata, openmetadata-dremio-connector, dbt-cloud-security]
sources: ["Gestione Secrets.md"]
---
# Gestione Secrets

This internal project note defines the canonical secrets management strategy for the Data Platform. It mandates that all infrastructure and application secrets be stored exclusively as GitLab CI/CD variables, organized by application group. The document provides a concrete mapping of which secrets belong to which GitLab group (Infrastructure, dbt, Kestra, OpenMetadata) and flags a known security vulnerability: the custom OpenMetadata connector stores the Dremio password in plaintext.

## Key Points

- **Single source of truth**: All secrets are defined in GitLab CI/CD Settings, not in `.env` files, configuration files, or Kubernetes Secrets.
- **Group-level organization**: Secrets are scoped to the appropriate GitLab group (Infrastructure, dbt, Kestra, OpenMetadata) to enforce least-privilege access.
- **Flagged issue**: The custom OpenMetadata connector stores the Dremio password in plaintext, violating the platform's security policy. This requires resolution.

## GitLab Group Mapping

| GitLab Group | Secrets Stored |
|---|---|
| Data Platform/Infrastructure/Application | Infrastructure-level credentials |
| Data Platform/Application/dbt | Dremio credentials, OpenMetadata token |
| Data Platform/Application/Kestra | Kestra credentials |
| Data Platform/Application/OpenMetadata | (Flagged: Dremio password in plaintext in custom connector) |

## Related Pages

- [[secrets-management-strategy]] — Formal documentation of the GitLab CI/CD variable approach
- [[openmetadata-dremio-connector-password-issue]] — Tracking the plaintext password vulnerability
- [[custom-connector-openmetadata]] — Pattern for building custom OpenMetadata connectors
- [[openmetadata-dremio-connector]] — The specific connector with the password issue
- [[dbt-cloud-security]] — Related credential management in dbt Cloud