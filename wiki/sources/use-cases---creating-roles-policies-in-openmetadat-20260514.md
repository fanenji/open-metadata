---
type: source
title: "Use Cases - Creating Roles & Policies in OpenMetadata"
authors: []
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/roles-policies/use-cases"
venue: "OpenMetadata Documentation v1.12.x"
tags: [roles, policies, authorization, governance, use-cases]
related: [roles-and-policies, building-blocks-of-authorization---rules-policies--20260514, spel-conditions, hybrid-rbac-abac-model, default-organization-policy, glossary-tags, teams-and-users, data-steward-role, serviceowner-role, tag-based-access-control, policy-use-cases]
created: 2026-05-14
updated: 2026-05-14
sources: ["use-cases---creating-roles-policies-in-openmetadat-20260514.md"]
---
# Use Cases - Creating Roles & Policies in OpenMetadata

Official documentation page providing practical use cases for designing Roles and Policies in OpenMetadata v1.12.x. The guide demonstrates how to operationalize the hybrid RBAC-ABAC authorization framework through four concrete scenarios: delegating service creation to teams, configuring Data Steward governance permissions, restricting data access to owning teams, and implementing tag-based access control for sensitive data.

## Key Recommendations

- **Retain the default Organization Policy** — it enables basic data collaboration by allowing everyone to view assets and claim ownership when no owner is specified.
- **Tailor team policies** to specific organizational needs, adopting stricter policies where required.

## Use Cases Covered

1. **Service Creation Delegation** — Empower teams to create Database Services, Ingestion Pipelines, and Workflows without Admin intervention via a ServiceOwner role.
2. **Data Steward Role** — Configure a two-rule policy granting glossary management and universal edit permissions for governance.
3. **Team-Owned Data Protection** — Deny access to data assets unless the user or their team is the owner.
4. **PII.Sensitive Tag-Based Deny** — Restrict access to tables tagged `PII.Sensitive` to owners only, using complex SpEL conditions.

These use cases demonstrate practical application of [[spel-conditions|SpEL conditions]], [[hybrid-rbac-abac-model|ABAC evaluation]], and [[building-blocks-of-authorization---rules-policies--20260514|authorization building blocks]].