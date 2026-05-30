---
type: synthesis
title: Policy Use Cases
created: 2026-05-14
updated: 2026-05-14
tags: [roles, policies, authorization, governance, synthesis, patterns]
related: [roles-and-policies, building-blocks-of-authorization---rules-policies--20260514, spel-conditions, hybrid-rbac-abac-model, default-organization-policy, glossary-tags, teams-and-users, data-steward-role, serviceowner-role, data-consumer-role, tag-based-access-control]
sources: ["use-cases---creating-roles-policies-in-openmetadat-20260514.md"]
---
# Policy Use Cases

This synthesis page collects the four official use cases for creating Roles and Policies in OpenMetadata, serving as a reference for policy design patterns. Each use case demonstrates practical application of the [[building-blocks-of-authorization---rules-policies--20260514|authorization building blocks]] and [[spel-conditions|SpEL conditions]] within the [[hybrid-rbac-abac-model|hybrid RBAC-ABAC framework]].

## Foundational Principle: Retain the Organization Policy

All use cases build on the recommendation to retain the [[default-organization-policy|default Organization Policy]], which enables basic data collaboration — everyone can view assets and claim ownership when no owner is specified. Custom policies layer additional restrictions or grants on top of this baseline.

---

## Use Case 1: Service Creation Delegation

**Goal:** Enable teams to create services and extract metadata without Admin intervention.

**Pattern:** Create a [[serviceowner-role|ServiceOwner role]] with a policy granting **All** operations on:
- `DatabaseService`
- `IngestionPipeline`
- `Workflow`

**Key insight:** This decentralizes ingestion management, allowing teams to connect their own data sources and run pipelines autonomously.

**Caution:** The broad "All" operations grant may conflict with restrictive team-level Deny policies. Ensure compatibility through careful policy design.

---

## Use Case 2: Data Steward Governance

**Goal:** Enable Data Stewards to manage glossaries and govern metadata across all assets.

**Pattern:** Create a [[data-steward-role|Data Steward role]] with a two-rule policy:
1. **Allow Glossary Operations** — All operations on Glossary and Glossary Term resources
2. **Edit Rule** — Edit descriptions and tags on all entities

**Key insight:** This separates governance responsibilities from administrative privileges. Data Stewards manage metadata quality without needing access to platform configuration.

**Flexibility:** The Edit Rule can be fine-tuned to narrower entity scopes for organizations with more constrained governance models.

---

## Use Case 3: Team-Owned Data Protection

**Goal:** Restrict data access to only the team that owns the asset.

**Pattern:** A Deny rule with the condition:
```
!isOwner() && !matchTeam()
```
This denies all operations if the logged-in user is neither the owner nor a member of the owning team.

**Key insight:** This leverages [[teams-and-users|team ownership]] as the basis for access control, ensuring data assets are only accessible to the responsible team.

---

## Use Case 4: Tag-Based PII Protection

**Goal:** Deny access to PII-tagged data except for owners.

**Pattern:** A Deny rule with a complex condition:
```
matchAllTags('PII.Sensitive') && !isOwner() && !matchTeam()
```
This denies operations on tables tagged `PII.Sensitive` unless the user or their team owns the table.

**Key insight:** This demonstrates [[tag-based-access-control|tag-based access control]], integrating the [[glossary-tags|Glossary and Tags]] system with the authorization framework. Tags become actionable security attributes.

---

## Design Principles

1. **Start with the Organization Policy** — It provides the collaboration baseline.
2. **Layer custom policies** — Add Allow rules for specific capabilities, Deny rules for restrictions.
3. **Deny takes precedence** — Restrictive rules always override permissive ones.
4. **Use SpEL conditions for context** — Ownership, team membership, and tags enable dynamic, attribute-based decisions.
5. **Test policies thoroughly** — Use the [[permission-debugger|Permission Debugger]] to verify effective permissions before production deployment.