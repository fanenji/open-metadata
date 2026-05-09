---
type: concept
title: dbt Cloud Security
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, cloud, security, sso, rbac, authentication]
related: [dbt-cloud, dbt-cloud-architect-certification]
sources: ["dbt Certified Architect Path beta - dbt Learn.md"]
---
# dbt Cloud Security

dbt Cloud Security encompasses the authentication, authorization, and access control mechanisms available in dbt Cloud Enterprise. This is a core topic in the [[dbt-cloud-architect-certification]] learning path (Milestone #3: Security and Monitoring).

## Key Components

- **Single Sign-On (SSO)**: Integration with identity providers including Okta, Microsoft Entra ID, and Google Workspace. Allows users to authenticate using their corporate credentials.
- **Role-Based Access Control (RBAC)**: Granular permissions based on user roles (e.g., Account Admin, Developer, Read-Only). Permissions control access to projects, environments, and jobs.
- **SCIM**: System for Cross-domain Identity Management for automated user provisioning and de-provisioning.
- **Multifactor Authentication (MFA)**: Additional security layer for user accounts.
- **Licenses and Permissions**: Management of user licenses (Developer, Read-Only) and group-based permission assignments.

## Relevance

Security configuration is a foundational step for dbt Cloud Enterprise deployments. The learning path includes required courses on authentication fundamentals and licenses/permissions, plus elective videos for specific SSO providers.