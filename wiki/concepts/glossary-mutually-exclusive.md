---
type: concept
title: Mutually Exclusive Glossary Terms
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, governance, mutually-exclusive]
related: [glossary-setup, glossary-terms, classification-tags]
sources: ["how-to-setup-a-glossary-official-documentation---o-20260514.md"]
---
# Mutually Exclusive Glossary Terms

Mutually Exclusive is a configuration flag on a glossary that ensures only one term from that glossary can be assigned to a single data asset. This is a critical governance feature that prevents conflicting classifications.

## Use Case

There are scenarios where a data asset should only have one classification from a particular glossary. For example:

- An asset can be either **PII-Sensitive** or **PII-NonSensitive**, but not both.
- An asset can be either **Confidential** or **Public**, but not both.

By enabling the Mutually Exclusive flag on the glossary, OpenMetadata enforces this constraint automatically.

## Behavior

- **Enabled:** Users cannot assign multiple terms from the same glossary to the same data asset.
- **Disabled (default):** Multiple terms from the same glossary can be assigned to a single data asset.

## Open Questions

- Can the Mutually Exclusive setting be changed after glossary creation?
- What is the exact behavior when terms are added via API vs. UI?

## Related Concepts

- [[glossary-setup]] — How to create a glossary and enable the Mutually Exclusive flag.
- [[glossary-terms]] — Individual terms within a glossary.
- [[classification-tags]] — Tags that can be added to a glossary.