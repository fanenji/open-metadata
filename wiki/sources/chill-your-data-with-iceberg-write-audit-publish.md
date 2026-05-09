---
type: source
title: "Chill Your Data with Iceberg Write Audit Publish"
created: 2026-04-04
updated: 2026-05-22
tags: [clippings, ci-cd, wap, iceberg]
related: [apache-iceberg, write-audit-publish-pattern, data-quality-dimensions]
sources: ["Chill Your Data with Iceberg Write Audit Publish.md"]
authors: [Vincent Daniel]
year: 2025
url: "https://medium.com/expedia-group-tech/chill-your-data-with-iceberg-write-audit-publish-746c9eb3db48"
venue: "Medium (Expedia Group Tech)"
---
# Chill Your Data with Iceberg Write Audit Publish

An article by Vincent Daniel discussing the implementation of the **Write-Audit-Publish (WAP)** pattern using **Apache Iceberg**'s branching and tagging capabilities.

## Key Takeaways
- **WAP Pattern**: A three-stage workflow (Write $\rightarrow$ Audit $\rightarrow$ Publish) to ensure data quality.
- **Iceberg Implementation**: Uses isolated branches for the "Write" and "Audit" phases, and metadata "fast-forwarding" for the "Publish" phase.
- **Economic Impact**: Case study from **Expedia Group** shows a **30% reduction in storage** and up to **99% reduction in release costs** by eliminating the need to run ETL pipelines twice.
- **Efficiency**: Avoids data duplication by reusing existing data files through branching.

## Technical Details
- **Branching**: Creates isolated, non-production environments.
- **Tagging**: Immutable pointers for long-term auditing and compliance.
- **Fast-Forwarding**: Atomic metadata update to promote a validated branch to the main branch.
- **Risks**: Potential for metadata bloat and complexity in managing branch lifecycles.
