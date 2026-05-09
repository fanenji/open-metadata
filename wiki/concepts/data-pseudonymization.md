---
type: concept
title: Data Pseudonymization
created: 2026-04-04
updated: 2026-04-04
tags: [data-governance, sensitive-data, de-identification, gdpr, compliance]
related: [data-masking-techniques, token-vault-architecture, data-maturity-model-for-sensitive-data, data-discovery-tools]
sources: ["Data Engineering Architectures & Strategies for Handling Sensitive Data.md"]
---
# Data Pseudonymization

Data pseudonymization is a de-identification technique defined in Article 3 of the [[GDPR]] as:

> "The processing of personal data in such a manner that the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately and is subject to technical and organizational measures to ensure that the personal data are not attributed to an identified or identifiable natural person."

## Key Characteristics

- **Reversible:** The original data can be recovered using a separate token store ([[token-vault-architecture]]).
- **GDPR-compliant:** Pseudonymized data is still considered personal data under GDPR, but the regulation encourages its use as a privacy-enhancing technique.
- **Medium effort:** Requires a Data Catalog for classification and a Token Vault for re-identification tokens.

## Recommended Use Case

According to [[Hussein Jundi]]'s [[data-maturity-model-for-sensitive-data]], pseudonymization is the recommended technique for **Maturity Level 2** and **Level 3** organizations.

- **Level 2:** Manual data discovery and cataloging, with a Token Vault for re-identification.
- **Level 3:** Automated discovery and classification, with encryption as an additional security layer.

## Advantages

- Enables customer analytics and BI at the individual level (via re-identification)
- Compliant with GDPR and similar regulations
- Balances privacy with analytical utility

## Disadvantages

- Adds system complexity (Token Vault, Data Catalog)
- Requires manual effort for data discovery at Level 2
- Pseudonymized data remains subject to data protection obligations

## Implementation Patterns

- Tokenization (replacing PII with a token that maps to the original value in a secure vault)
- Hashing with salt (one-way hashing for irreversible pseudonymization, though not truly reversible)
- Format-preserving encryption (encrypting data while maintaining its original format)

## Connections to Existing Wiki

- Pseudonymization is a more sophisticated alternative to [[data-masking-techniques]], enabling re-identification.
- The [[token-vault-architecture]] is the key infrastructure component for pseudonymization.
- The progression from masking to pseudonymization is driven by the [[data-maturity-model-for-sensitive-data]].