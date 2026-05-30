---
type: source
title: "Best Practices for Classification | Official Documentation - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [classification, best-practices, data-governance, openmetadata]
related: [classification-tags, glossary-terms, tiers, tag-based-access-control, classification-best-practices, tag-to-glossary-attachment, tag-rename-vs-delete, tag-display-name-improvement]
sources: ["best-practices-for-classification-official-documen-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/best-practices"
venue: "OpenMetadata Documentation"
---
# Best Practices for Classification | Official Documentation

This official OpenMetadata documentation page (v1.12.x) provides six best practices for using the classification system effectively. It covers attaching classification tags to glossary terms for auto-assignment of PII tags, using Tier classification for prioritization and decluttering, leveraging tags to simplify policy creation, improving display names for better discovery, renaming tags instead of deleting them to preserve tagging effort, and grouping similar concepts semantically.

The source emphasizes that both Glossary and Classification are controlled vocabularies and should be used together strategically. The most impactful recommendation is attaching classification tags to glossary terms, which enables scaling governance by combining semantic meaning with automated PII tagging. The guide also introduces the pattern of using classification tags to group data assets for simplified policy management via the [[hybrid-rbac-abac-model]] and [[spel-conditions]].