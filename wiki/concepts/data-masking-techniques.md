---
type: concept
title: Data Masking Techniques
created: 2026-04-04
updated: 2026-04-04
tags: [data-governance, sensitive-data, de-identification, compliance]
related: [data-maturity-model-for-sensitive-data, data-pseudonymization, token-vault-architecture]
sources: ["Data Engineering Architectures & Strategies for Handling Sensitive Data.md"]
---
# Data Masking Techniques

Data masking is a de-identification technique that replaces personally identifiable information (PII) with meaningless, irreversible characters. It is the simplest approach to achieving compliance with regulations like [[GDPR]] and [[CCPA]].

## Characteristics

- **Irreversible:** The original data cannot be recovered from the masked output.
- **Low effort:** Can be implemented via ETL tools, simple scripts, or SQL transformations.
- **Full anonymization:** Meets GDPR requirements for anonymized data (not subject to data protection obligations).

## Recommended Use Case

According to [[Hussein Jundi]]'s [[data-maturity-model-for-sensitive-data]], data masking is the recommended technique for **Maturity Level 1** organizations — those with no established data management practices, small teams, and early-stage data warehouses.

## Advantages

- Compliant data architecture with minimal effort
- Low implementation and maintenance cost
- Reduces risk of data leaks significantly

## Disadvantages

- Limits customer analytics and BI capabilities (aggregated analysis only)
- Cannot support use cases requiring individual-level re-identification
- May discard potentially valuable data permanently

## Implementation Patterns

- Column exclusion (dropping PII columns entirely)
- Character substitution (e.g., replacing names with "XXXX")
- Shuffling (randomizing values within a column)
- Nulling (replacing values with NULL)

## Connections to Existing Wiki

- Data masking is a simpler alternative to [[data-pseudonymization]], which enables re-identification.
- The choice between masking and pseudonymization is driven by the [[data-maturity-model-for-sensitive-data]].