---
type: concept
title: Tag-Based Policy Design
created: 2026-05-14
updated: 2026-05-14
tags: [policies, tags, classification, access-control, governance]
related: [tag-based-access-control, classification-tags, roles-and-policies, glossary-best-practices, hybrid-rbac-abac-model, spel-conditions]
sources: ["best-practices-for-glossary-official-documentation-20260514.md"]
---
# Tag-Based Policy Design

Using [[classification-tags]] to group data assets simplifies policy management. Instead of creating separate policies for each resource (e.g., individual tables with sensitive data), a single policy can be created at the tag level.

## How It Works

1. **Define Classification Tags:** Create tags that represent data categories relevant to governance. Examples:
   - `sensitive`
   - `restrictive`
   - `public`
   - `internal`
   - `external`
   - `raw`
   - `confidential`

2. **Tag Data Assets:** Apply the appropriate classification tags to tables, columns, or other assets.

3. **Create Tag-Level Policies:** Use [[spel-conditions]] like `matchAllTags()` or `matchAnyTag()` in authorization rules to match assets by their tags. For example, a single policy with a rule matching the `sensitive` tag will apply to all assets tagged as sensitive.

## Example

Instead of creating separate policies for `customer_pii_table`, `employee_salary_table`, and `patient_records_table`, attach a `sensitive` tag to all three and create one policy:

- **Rule:** If resource has tag `sensitive`, then restrict access to Data Steward role only.

## Benefits

- **Reduced Administrative Overhead:** One policy replaces many.
- **Consistency:** All sensitive assets are governed by the same rules.
- **Scalability:** New assets tagged with the same classification are automatically covered.
- **Flexibility:** Tags can be combined with ownership and team membership for fine-grained control.

## Relationship to Glossary Terms

When [[classification-tags]] are attached to [[glossary-terms]], applying the glossary term to an asset auto-assigns the tags. This creates a powerful workflow: glossary terms define semantic meaning, and their attached tags drive policy enforcement. See [[glossary-best-practices]] for the full pattern.

## Integration with ABAC

Tag-based policies are a form of [[hybrid-rbac-abac-model|Attribute-Based Access Control (ABAC)]], where the tag is a resource attribute evaluated during authorization. This integrates with the existing [[roles-and-policies]] framework.