---
type: concept
title: Data Classification Automation
created: 2026-04-29
updated: 2026-04-29
tags: [data-governance, data-catalog, pii-detection, automation]
related: [automated-data-discovery-and-classification, unity-catalog, microsoft-presidio, sensitive-data-handling-strategies, databricks-sensitive-data-handling]
sources: ["Handling Sensitive Data in Your Data Platform.md"]
---
# Data Classification Automation

The practice of using automated tools and frameworks to detect sensitive data fields (PII, PHI, financial data, etc.) and store the classification in a data catalog. This process should involve data owners and governance teams, not just the data engineering team.

## Approaches

- **Built-in platform tools** — e.g., Databricks Data Classification on Unity Catalog.
- **Open-source frameworks** — e.g., Microsoft Presidio.
- **Custom tools** — Built using Generative AI for pattern detection.

## Benefits

- Reduces manual effort in identifying sensitive fields.
- Enables downstream enforcement of masking, access control, and isolation policies.
- Supports compliance with regulations like GDPR.