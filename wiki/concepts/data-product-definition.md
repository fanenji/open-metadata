---
type: concept
title: Data Product Definition
created: 2026-04-04
updated: 2026-04-04
tags: [data-product, data-governance, data-contracts]
related: [data-contract, data-domain-governance, YAML-data-contract-format]
sources: ["Data Contracts Implementation Guide.md"]
---
# Data Product Definition

A data product is a curated dataset or analytical model designed to meet specific business requirements. In the context of [[data-contract]]s, data products are the units around which contracts are defined and enforced.

## Examples

- Recommender systems
- Profit and Loss Dashboard
- Marketing Campaign Performance Dashboard

## Role in Data Contracts

In the 8-step implementation process described by [[Jatin Solanki]], data products are created after establishing [[data-domain]]s and assigning assets to them. The data product's requirements drive the selection of assets and the application of validation, schema, and metadata rules. The resulting [[YAML-data-contract]] encapsulates the agreement for that specific data product.

## Characteristics

- Includes detailed documentation explaining the process and sometimes a glossary
- May include transformation code
- Owned by data engineers, with expectations defined by business stakeholders