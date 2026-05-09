---
type: source
title: Experimenting with Data Contracts
created: 2026-04-04
updated: 2026-04-04
tags: [data-contracts, data-governance, data-mesh, tutorial]
related: [bitol-open-data-contract-standard, jean-georges-perrin, ddl-to-data-contract-conversion, data-contract-platform, YAML-data-contract-format, data-contract-versioning-strategy]
sources: ["Experimenting with Data Contracts.md"]
authors: ["Jean-Georges Perrin"]
year: 2025
url: "https://medium.com/data-mesh-learning/experimenting-with-data-contracts-9d36219e139e"
venue: "Data Mesh Learning (Medium)"
---
# Experimenting with Data Contracts

A hands-on tutorial introducing the Bitol REST-based service for building, validating, and storing data contracts. The tutorial demonstrates how to convert SQL DDL into an Open Data Contract Standard (ODCS)-aligned contract using simple `curl` commands, without manual YAML writing.

## Key Points

- Introduces the Bitol service on JGP.ai cloud for free data contract management.
- Demonstrates DDL-to-contract conversion via REST API.
- Uses the Open Data Contract Standard (ODCS) v3.0.2 specification.
- Supports semantic versioning (semver) for contract versions.
- Allows enrichment with descriptions, SLAs, and data quality rules.
- Part of a four-tutorial series with associated GitHub repository and surveys.

## Structure

1. **Contextualize** — Example customer/address DDL schema.
2. **Setting up the playground** — Account creation and API key export.
3. **Creating the first contract** — DDL upload, contract retrieval, and enrichment.
4. **More experimentations** — Extracting real schemas, adding documentation, SLAs, and data quality rules.

## Related Content

- [[ddl-to-data-contract-conversion]] — Pattern for generating contracts from database schemas.
- [[bitol-open-data-contract-standard]] — The ODCS specification used by Bitol.
- [[jean-georges-perrin]] — Author and creator of Bitol.
- [[data-contract-platform]] — Broader context of data contract management systems.
- [[YAML-data-contract-format]] — Standard YAML structure for data contracts.
- [[data-contract-versioning-strategy]] — Semantic versioning for contracts.