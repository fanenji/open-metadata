---
type: entity
title: ServiceOwner Role
created: 2026-05-14
updated: 2026-05-14
tags: [roles, policies, ingestion, services, delegation]
related: [roles-and-policies, building-blocks-of-authorization---rules-policies--20260514, metadata-agent, service-connection, policy-use-cases, teams-and-users]
sources: ["use-cases---creating-roles-policies-in-openmetadat-20260514.md"]
---
# ServiceOwner Role

The ServiceOwner role is a custom role pattern that delegates the ability to create and manage metadata ingestion services to non-Administrator users. This addresses the operational need for teams to independently connect data sources and run ingestion pipelines without requiring Admin intervention.

## Policy Configuration

The recommended policy grants **All** operations on the following resources:

| Resource | Purpose |
|----------|---------|
| `DatabaseService` | Create and configure connections to external data sources |
| `IngestionPipeline` | Define and manage metadata extraction pipelines |
| `Workflow` | Orchestrate ingestion workflows |

All three resources are set to **Allow** with **All** operations, giving ServiceOwners full control over the ingestion lifecycle for the services they manage.

## Role Assignment

Once the policy is created and attached to a ServiceOwner role, the role can be assigned to specific users or teams. This enables those users to:

1. Create new [[service-connection|service connections]] to data sources
2. Configure and schedule [[metadata-agent|metadata ingestion pipelines]]
3. Manage workflows without escalating to an Administrator

## Security Considerations

- **Broad permissions** — The "All" operations grant is intentionally broad. In environments with strict security requirements, consider scoping operations more narrowly (e.g., excluding Delete).
- **Interaction with Deny policies** — If a user holds both the ServiceOwner role (Allow) and a team policy with Deny rules, [[building-blocks-of-authorization---rules-policies--20260514|Deny precedence]] applies: the Deny will override the Allow. Ensure team-level restrictive policies are compatible with the ServiceOwner role.
- **Scope by team** — Assign the ServiceOwner role only to teams that genuinely need autonomous service management.

## Relationship to Other Roles

- **Distinct from Admin** — ServiceOwners cannot manage users, teams, or global platform settings.
- **Complementary to Data Steward** — A [[data-steward-role|Data Steward]] governs metadata quality; a ServiceOwner brings data into the platform.