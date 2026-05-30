---
type: concept
title: Classification Tags
created: 2026-05-14
updated: 2026-05-15
tags: [data-governance, classification, tags, metadata, openmetadata, governance, discovery, pii]
related: [glossary-tags, tiers, system-classification, tag-based-access-control, tag-request-workflow, data-steward-role, auto-classification, conversations-around-classification, pii-sample-data-masking, how-to-classify-data-assets-official-documentation-20260514, glossary-terms, asset-association]
sources: ["how-to-classify-data-assets-official-documentation-20260514.md", "how-to-add-tags-openmetadata-user-tagging-guide----20260514.md", "how-to-add-assets-to-glossary-terms---openmetadata-20260514.md"]
---
# Classification Tags

Classification Tags are metadata labels applied to data assets (tables, columns, topics, pipelines, etc.) in OpenMetadata for governance, discovery, and access control purposes. They serve as governance markers — indicating sensitivity, importance, ownership domain, or regulatory requirements — and form the foundation for OpenMetadata's classification system and [[tag-based-access-control|Tag-Based Access Control]] policies.

## Distinction from Glossary Terms

Classification Tags are distinct from [[glossary-tags|Glossary Terms]], which provide business definitions and semantic meaning. While Glossary Terms describe *what data means*, Classification Tags describe *how data should be handled*.

| Aspect | Classification Tags | Glossary Terms |
|--------|---------------------|----------------|
| Purpose | Governance, access control, discovery | Business definitions, semantic meaning |
| Examples | `PII.Sensitive`, `Tier.Tier1`, `Confidential` | `Customer`, `Revenue`, `Churn Rate` |
| Used by | ABAC policies, data discovery filters | Data documentation, business context |
| Managed in | Govern > Classification | Govern > Glossary |

## Tag Propagation from Glossary Terms

A powerful automation pattern in OpenMetadata is the propagation of tags from [[glossary-tags|Glossary Terms]]. When a Glossary Term has associated Classification Tags, applying that term to a data asset automatically applies those tags as well. For example, if a Glossary Term "Account" has the `PII.Sensitive` tag, adding the "Account" term to a column will automatically tag that column with `PII.Sensitive`.

This propagation ensures consistent tagging without manual effort and connects directly to downstream governance features:

- [[pii-sample-data-masking]]: a `PII.Sensitive` tag triggers automatic masking of sample data in the UI.
- [[tag-based-access-control]]: tags serve as ABAC attributes for dynamic access restriction.

For more details on the bidirectional relationship between Glossary Terms and data assets, see [[asset-association]].

## Tagging Workflow

Applying classification tags follows a simple three-step process:

1. **Navigate to the asset:** From the Explore page, select a data asset (table, topic, pipeline, etc.).
2. **Select tags:** Click the edit icon or `+ Add` for Tags. Search by typing or scroll through available options.
3. **Save:** Click the checkmark to apply the changes.

## Tag Usage and Discovery

The Classification page (Govern > Classification) provides a reverse-lookup capability:

- It displays all classification tags with their **Usage count** — the number of data assets bearing each tag.
- Clicking the Usage number drills down to show all tagged assets.
- The right panel displays all tags on the selected asset.

This enables governance oversight and impact analysis before modifying or removing tags, and also helps users discover tagged assets.

## Types of Classification Tags

Classification Tags encompass several categories:

### General Classification Tags

User-defined or system-provided labels for arbitrary governance categories. These can be created through the UI or API and cover any governance need not addressed by the specialized systems below.

### [[tiers|Tiers]]

A specialized classification for ranking data importance and quality (e.g., Tier 1 through Tier 5). Tiers help prioritize data governance efforts and indicate criticality.

### [[system-classification|System Classification]]

Pre-built tags provided by OpenMetadata out of the box, covering common governance categories such as PII (Personal Identifiable Information).

### Custom Tags

In addition to the above, users can define fully custom tags through the UI or API to meet specific organizational requirements. (Custom tags are a type of general classification tag.)

## Auto-Classification

OpenMetadata can automatically tag PII-sensitive data using NLP during profiling. This auto-classification feature scans columns and applies appropriate PII tags, streamlining the classification process. See [[auto-classification]] for details.

## Relationship to Access Control

Classification Tags are the prerequisite for [[tag-based-access-control]]. Attribute-Based Access Control (ABAC) policies reference tags in their [[spel-conditions|SpEL conditions]] (e.g., `matchAllTags('PII.Sensitive')`). Without tags applied to assets, these policies have no effect. The tagging workflow documented here is therefore the essential first step in implementing tag-based access governance.

In addition to manual tagging, tags can also be applied automatically via [[glossary-tags|Glossary Term]] propagation (see [[#tag-propagation-from-glossary-terms|Tag Propagation from Glossary Terms]]), providing an alternative pathway to establish tag-based access governance.

## Collaborative Governance

Users can participate in the classification process through several collaborative features:

### Tag Request Workflow

Users can request tag additions or changes through the [[tag-request-workflow]], enabling collaborative governance where [[data-steward-role|Data Stewards]] review and manage classification requests.

### Conversations Around Classification

Threaded discussions can be initiated from individual tags on data assets, allowing teams to discuss tag suitability, propose changes, or ask questions. See [[conversations-around-classification]].

### PII Sample Data Masking

When a PII tag is applied to a column, OpenMetadata automatically masks sample data to protect sensitive information. See [[pii-sample-data-masking]].

## Additional Resources

- [[how-to-classify-data-assets-official-documentation-20260514]] — The detailed admin guide for classification.
- [[auto-classification]] — Automated PII detection via NLP during profiling.
- [[tiers]] — Importance-based classification system.
- [[system-classification]] — Pre-built tags provided by OpenMetadata.
- [[asset-association]] — The bidirectional relationship between Glossary Terms and data assets.
- [[how-to-add-assets-to-glossary-terms]] — Guide for associating Glossary Terms with data assets (which can trigger automatic tag application via propagation).