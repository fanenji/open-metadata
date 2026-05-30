---
type: concept
title: Tag Mapping
created: 2026-05-14
updated: 2026-05-14
tags: [data-governance, classification, tags, backend]
related: [auto-classification, classification-tags, tag-based-access-control, roles-and-policies]
sources: ["auto-classification-in-openmetadata---openmetadata-20260514.md"]
---
# Tag Mapping

Tag mapping is a backend-only feature in OpenMetadata that creates an association between two related [[classification-tags]]. When one tag is applied to a data asset, the mapped tag is automatically applied as well, enabling cascading governance policies without additional user intervention.

## How It Works

Tag mapping operates as a directed association: applying Tag A automatically triggers the application of Tag B. The documented example shows:

- Applying `Personal Data.Personal` → automatically applies `Data Classification.Confidential`

This means a single classification action can trigger multiple tag assignments, ensuring that related governance policies are consistently enforced.

## Backend-Only Limitation

Tag mapping is explicitly described as "supported in the backend and not in the OpenMetadata UI." This has significant implications:

- **No UI for creation**: Mappings cannot be created, viewed, or managed through the OpenMetadata user interface.
- **No UI for discovery**: Users cannot see which tags have mappings or what the cascading effects of applying a tag will be.
- **Configuration path unclear**: The documentation does not specify whether mappings are configured via API, YAML configuration files, system-level settings, or database-level operations.

## Use Cases

- **Compliance cascading**: Applying a personal data tag automatically applies a confidentiality classification, ensuring regulatory requirements are met.
- **Multi-framework alignment**: A single tag can trigger classifications aligned with multiple governance frameworks (e.g., GDPR + internal data classification policy).
- **Reducing manual effort**: Governance teams do not need to remember to apply all related tags — the mapping handles it automatically.

## Relationship to ABAC Policies

Tag mapping has direct implications for [[tag-based-access-control]] and [[roles-and-policies|authorization policies]]. Since ABAC policies can evaluate tags as [[resource-attributes]], a cascaded tag application through mapping can trigger access control rules that the user did not explicitly invoke. This makes tag mapping a powerful but potentially surprising mechanism — administrators must understand the full chain of mappings to predict policy behavior.

## Open Questions

- How are tag mappings created, managed, and removed if there is no UI?
- Is there an API endpoint for tag mapping management?
- Are mappings visible in audit logs when triggered?
- Can mappings be scoped (e.g., only apply within certain domains or teams)?
- What happens if a mapping creates a circular reference?