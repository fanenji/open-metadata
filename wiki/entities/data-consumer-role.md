---
type: entity
title: Data Consumer Role
created: 2026-05-14
updated: 2026-05-14
tags: [roles, policies, collaboration, default-configuration]
related: [roles-and-policies, default-organization-policy, hybrid-rbac-abac-model, viewbasic-viewall-operations]
sources: ["use-cases---creating-roles-policies-in-openmetadat-20260514.md"]
---
# Data Consumer Role

The Data Consumer Role is a default role in OpenMetadata, mentioned alongside the [[default-organization-policy|Organization Policy]] as part of the platform's out-of-the-box configuration designed to foster data collaboration.

## Known Characteristics

Based on the official documentation:

- **Pre-configured** — Ships with OpenMetadata as a default role.
- **Collaboration-oriented** — Intended to enable data collaboration across the organization.
- **Complementary to Organization Policy** — Works alongside the Organization Policy, which enables everyone to view assets and claim ownership when no owner is specified.

## Open Questions

- **Exact permissions** — The specific resources and operations granted by the Data Consumer Role are not detailed in the use cases documentation. It is unclear whether it grants [[viewbasic-viewall-operations|ViewBasic or ViewAll]] access, or includes additional operations like commenting or adding announcements.
- **Relationship to Organization Policy** — Are the Data Consumer Role and Organization Policy overlapping, complementary, or hierarchical? The documentation mentions both as defaults but does not clarify their interaction.
- **Customizability** — Can the Data Consumer Role be modified, or is it a fixed system role?

## Practical Guidance

Until the exact permissions are clarified, consider the Data Consumer Role as a baseline for users who need to discover and consume data assets. For more granular control, design custom roles using the [[building-blocks-of-authorization---rules-policies--20260514|authorization building blocks]] and reference the [[policy-use-cases|policy use cases]] for patterns.