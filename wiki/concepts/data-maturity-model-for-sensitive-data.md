---
type: concept
title: Data Maturity Model for Sensitive Data
created: 2026-04-04
updated: 2026-04-04
tags: [data-governance, maturity-model, sensitive-data, compliance]
related: [data-masking-techniques, data-pseudonymization, token-vault-architecture, data-discovery-tools, data-domain-governance, data-product-definition]
sources: ["Data Engineering Architectures & Strategies for Handling Sensitive Data.md"]
---
# Data Maturity Model for Sensitive Data

A three-level framework for matching sensitive data handling strategies to an organization's data maturity, as described by [[Hussein Jundi]].

## The Three Levels

### Level 1 — Initial
- **Characteristics:** No established data management practices, undefined data roles, early-stage warehouse, small team.
- **Recommended Technique:** [[data-masking-techniques]] (full anonymization, irreversible).
- **Architecture:** Simple masking or column exclusion during ingestion/transformation. No Data Catalog or token store.
- **Trade-off:** Compliant but limited customer analytics capabilities.

### Level 2 — Intermediate
- **Characteristics:** Some data management practices, manual data discovery and cataloging, partially modeled warehouse, small team (~3 members).
- **Recommended Technique:** [[data-pseudonymization]] (reversible via separate token store).
- **Architecture:** Adds a [[data-discovery-tools|Data Catalog]] (manually populated by data stewards) and a [[token-vault-architecture|Token Vault]] for re-identification tokens.
- **Trade-off:** Enhanced analytics capabilities at the cost of added system complexity and manual effort.

### Level 3 — Advanced
- **Characteristics:** Established data management and governance, automated data discovery and classification, fully modeled data products, multi-national teams.
- **Recommended Technique:** Pseudonymization plus encryption.
- **Architecture:** Adds automated discovery/classification services and an encryption stage during transformation. Data Catalog is populated automatically.
- **Trade-off:** Maximum security and analytics capability, but highest complexity and cost.

## Key Insight

The framework emphasizes that the "best" solution is the one that fits the organization's current maturity. Implementing a Level 3 architecture in a Level 1 organization is likely to fail due to resource and expertise constraints. Even simple masking at Level 1 provides substantial risk mitigation.

## Limitations

- The three-level model is simplified; real-world maturity models are more nuanced.
- The boundary between Level 2 and Level 3 can blur, as automated tools may still require data steward involvement for complex assets.
- The framework does not address Data Catalog adoption challenges (see [[data-catalog-critique]]).

## Connections to Existing Wiki

- Level 3's "fully modelled and tested Data Products" connects to [[data-product-definition]] and [[data-contract-platform]].
- The progression from manual to automated discovery connects to [[data-discovery-tools]].
- The governance practices in Level 3 connect to [[data-domain-governance]].