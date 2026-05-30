---
type: concept
title: Data Governance
created: 2026-05-14
updated: 2026-05-14
tags: [data-governance, classification, glossary, tiers, domains]
related: [classification-tags, glossary-terms, tiers, auto-classification, tag-request-workflow, pii-sample-data-masking, domains-and-data-products]
sources: ["classification-openmetadata-data-classification-gu-20260514.md"]
---
# Data Governance

Data Governance in OpenMetadata encompasses the policies, processes, and tools for managing data assets across the organization. It provides a framework for ensuring data quality, security, compliance, and discoverability through structured metadata management.

## Core Components

- **[[classification-tags|Classification]]** — A controlled vocabulary for labeling data by type (e.g., PII, sensitive, public). Classification tags are technical/governance labels applied to data assets for discovery, access control, and compliance.
- **[[glossary-terms|Glossary]]** — Business metadata classification objects that define business concepts and relationships. Glossary terms are distinct from classification tags but work together for comprehensive governance.
- **[[tiers|Tiers]]** — A five-tier system (Tier 1-5) for ranking data importance and criticality to the organization.
- **[[auto-classification|Auto-Classification]]** — Automated identification and tagging of sensitive data using NLP during profiling.
- **[[tag-request-workflow|Tag Request Workflow]]** — Collaborative process for requesting and discussing tag changes within the platform.
- **[[pii-sample-data-masking|PII Sample Data Masking]]** — Automatic masking of sample data when PII tags are applied.

## Classification vs. Glossary

A key distinction in OpenMetadata's governance model:

| Aspect | Classification | Glossary |
|--------|---------------|----------|
| Purpose | Label data type (technical/governance) | Define business metadata |
| Scope | Tags for organizing and retrieving information | Business concepts and relationships |
| Example | PII.Sensitive, Public, Internal | Customer, Product, Revenue |
| Automation | Auto-classification agent available | Manual term creation |

## Related Features

- **Domains & Data Products** — Organizational grouping of data assets by business domain.
- **Data Contracts** — Formal agreements between data producers and consumers.
- **Data Quality and Observability** — Monitoring and testing data reliability.

## Best Practices

1. Start with system classification tags before creating custom ones.
2. Use Classification for technical labeling and Glossary for business semantics.
3. Leverage auto-classification for PII detection to reduce manual effort.
4. Apply tiers to prioritize governance efforts on critical data.
5. Use the tag request workflow for collaborative governance.