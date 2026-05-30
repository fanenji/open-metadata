---
type: concept
title: Tag Display Name Improvement
created: 2026-05-14
updated: 2026-05-14
tags: [classification, data-governance, discovery, best-practices]
related: [classification-tags, classification-best-practices]
sources: ["best-practices-for-classification-official-documen-20260514.md"]
---
# Tag Display Name Improvement

Tag Display Name Improvement is a best practice in [[OpenMetadata]] that involves renaming [[classification-tags|classification tags]] with better display names to improve searchability and data discovery. This is particularly important when classification tags are inherited from source systems where names may be cryptic or use abbreviations.

## The Problem

When classification tags are inherited from source systems, the names may not communicate the concept well. For example:
- `dep-prod` instead of `Product Department`
- `c_id` instead of `Customer ID`
- `CAC` instead of `Customer Acquisition Cost`

Users are more likely to search using common terms like `Product` or `Department`, so cryptic names hinder data discovery.

## The Solution

OpenMetadata supports setting display names for classification tags that are separate from the technical name. By improving display names, organizations can:
- Make tags more discoverable through search.
- Communicate the meaning of tags more clearly to users.
- Reduce the learning curve for new team members.

## Examples

| Technical Name | Improved Display Name |
|----------------|----------------------|
| `dep-prod` | Product Department |
| `c_id` | Customer ID |
| `CAC` | Customer Acquisition Cost |
| `emp_sal` | Employee Salary |

## Best Practice

- Always set a meaningful display name when creating or importing classification tags.
- Review inherited tags from source systems and improve their display names.
- Use common, searchable terms that users are likely to type.
- Avoid abbreviations and acronyms unless they are universally understood in the organization.