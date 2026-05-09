---
type: concept
title: Sensitive Data Handling Strategies
created: 2026-04-29
updated: 2026-04-29
tags: [data-governance, gdpr, data-privacy, pii]
related: [sensitive-data-isolation-pattern, data-classification-automation, data-masking-techniques, data-pseudonymization, databricks-sensitive-data-handling, automated-data-discovery-and-classification, data-maturity-model-for-sensitive-data, data-federation-for-sensitive-data]
sources: ["Handling Sensitive Data in Your Data Platform.md"]
---
# Sensitive Data Handling Strategies

A comprehensive framework of techniques for handling sensitive data in a modern data platform. The core principle is that the first question should always be whether the sensitive data is actually needed — if not, it should not be ingested.

## Hierarchy of Techniques (in order of preference)

1. **Removal** — If there is no justifiable use case for a sensitive field, remove it entirely.
2. **Anonymisation** — Irreversible masking or replacement of sensitive values (e.g., replacing characters with "*" or "x").
3. **Pseudonymisation** — Reversible replacement of personal identifiers with artificial identifiers or pseudonyms, as defined by GDPR.
4. **Generalisation** — Reducing detail (e.g., converting exact ages into age groups like 20–29).
5. **Clear text storage** — When sensitive information must remain in clear text for analytics, apply strict access controls.

## Additional Techniques

- **Tokenization** — Storing the original value in a secure, isolated layer while other layers store only the token.
- **Encryption** — Storing data encrypted with a key in a Key Vault, decrypting only when necessary.
- **Hashing** — Generating an irreversible hash value for consistency without restoration, though re-identification risk exists.

## Key Principles

- Sensitive data should be ingested only when justified.
- Sensitive data should be isolated in separate layers or storage accounts.
- Access to data and changes in permissions should be logged.
- The platform must remain flexible for new regulations.