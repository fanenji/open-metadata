---
type: concept
title: Tag-Based Access Control
created: 2026-05-14
updated: 2026-05-14
tags: [authorization, abac, tags, governance, security, pii]
related: [hybrid-rbac-abac-model, spel-conditions, glossary-tags, building-blocks-of-authorization---rules-policies--20260514, policy-use-cases, roles-and-policies]
sources: ["use-cases---creating-roles-policies-in-openmetadat-20260514.md"]
---
# Tag-Based Access Control

Tag-Based Access Control is an authorization pattern in OpenMetadata that uses classification tags as attributes in ABAC (Attribute-Based Access Control) policies. By evaluating tags on data assets — such as `PII.Sensitive` — policies can dynamically restrict or grant access based on data sensitivity, regulatory requirements, or organizational classifications.

## How It Works

Tags applied through the [[glossary-tags|Glossary and Tags]] system serve as [[hybrid-rbac-abac-model|resource attributes]] in the authorization framework. When a policy rule includes a SpEL condition that checks for specific tags, the authorization engine evaluates whether the target resource carries those tags and applies the rule accordingly.

## Example: PII.Sensitive Deny Rule

The canonical example from the official documentation denies access to tables tagged `PII.Sensitive` unless the requesting user is the owner or belongs to the owning team:

```
Deny all operations if:
  - the table tag contains PII.Sensitive
  AND
  - the logged-in user is not the owner
  AND
  - the logged-in user's team is not the owner of the table
```

This uses the [[spel-conditions|SpEL condition functions]]:
- `matchAllTags('PII.Sensitive')` — evaluates to true if the resource has the specified tag
- `isOwner()` — evaluates to true if the current user is the resource owner
- `matchTeam()` — evaluates to true if the current user's team matches the resource's owning team

## Design Considerations

- **Tag governance is critical** — The effectiveness of tag-based access control depends on accurate and consistent tagging. [[data-steward-role|Data Stewards]] play a key role in maintaining tag hygiene.
- **Deny precedence** — Tag-based Deny rules follow the standard [[building-blocks-of-authorization---rules-policies--20260514|Deny precedence]] principle: if a Deny rule matches, it overrides any Allow rules, ensuring sensitive data is protected.
- **Layered policies** — Tag-based rules can be combined with team-based and ownership-based rules to create defense-in-depth authorization. For example, a broad Allow for a team can be narrowed by a tag-based Deny for sensitive assets.
- **Performance** — Complex SpEL conditions with multiple tag checks add evaluation overhead. Test policies with representative data volumes before production deployment.

## Common Use Cases

| Scenario | Tag(s) | Rule Type |
|----------|--------|-----------|
| PII protection | `PII.Sensitive` | Deny all except owners |
| Regulatory compliance | `GDPR`, `HIPAA` | Deny access to unauthorized teams |
| Internal-only data | `Internal` | Deny external users |
| Public data | `Public` | Allow all authenticated users |