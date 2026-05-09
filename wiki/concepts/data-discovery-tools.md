---
type: concept
title: Data Discovery Tools
created: 2026-04-04
updated: 2026-04-04
tags: [data-discovery, data-governance, data-catalog]
related: [data-domain-governance, data-contract, data-product-definition]
sources: ["Data Contracts Implementation Guide.md"]
---
# Data Discovery Tools

Data discovery tools are used to identify and catalog data assets within an organization. They are the first step in implementing [[data-contract]]s at scale, as described in [[Jatin Solanki]]'s 8-step process.

## Role in Data Contracts

Deploying data discovery enables an organization to understand its existing data landscape and prepare for structured governance. The output of data discovery feeds into [[data-domain-governance]], where assets are organized into domains with assigned ownership.

## Distinction from Data Catalogs

While data discovery tools are related to [[data-catalog]]s, [[Jatin Solanki]] distinguishes data contracts (preventive measures) from data catalogs (discovery tools). Data discovery is a prerequisite for contracts, but the contract itself is enforced through [[CI-CD-for-data-pipelines]].