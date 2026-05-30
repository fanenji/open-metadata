---
type: concept
title: Domains
created: 2026-05-14
updated: 2026-05-15
tags: [domains, data-governance, openmetadata]
related: [domains, data-products, data-asset-ownership, hierarchy-view, classification-tags, glossary-terms, teams-and-users, explore-page, data-assets]
sources: ["how-to-use-domains-openmetadata-governance-guide---20260514.md", "how-to-use-data-products-official-documentation----20260514.md"]
---

# Domains

Domains are a top-level organizational concept in [[OpenMetadata]]'s data governance framework. They serve as a logical container for organizing data assets by business area or purpose, providing a governance structure that sits above individual assets. This enables teams to manage data discovery, ownership, and accountability at a higher level of abstraction.

## Purpose

Domains act as a bridge between the technical metadata layer (tables, columns, schemas) and the business organization. They allow data stewards and administrators to group related assets — such as all tables, dashboards, and pipelines belonging to a "Sales" or "Customer 360" initiative — under a single, well-defined domain.

## Domain Types as an Architectural Pattern

The three domain types (Source-aligned, Aggregate, Consumer-aligned) represent a data flow architecture pattern:

1. **Source-aligned** → Raw, operational data from transactional systems and event streams.
2. **Aggregate** → Curated, integrated data that combines multiple source-aligned domains.
3. **Consumer-aligned** → Final, user-facing data products for business decision-making.

This pattern encourages organizations to model their data architecture as a pipeline from source to consumption, with clear ownership and governance at each stage.

## Relationship to Data Products

Domains serve as the parent container for [[data-products|Data Products]]. The hierarchy is:

- **Domain** → **Data Product** → **Data Asset**

A Domain represents a business area (e.g., "Customer," "Finance," "Sales"), while a Data Product is a logical grouping of assets within that domain (e.g., "Customer 360 Data Product"). While domains define the "where" (the business area), data products define the "what" (the specific, curated datasets or dashboards delivered to consumers). The guide positions Data Products as the next logical step after domain creation.

## Relationship to Other Governance Concepts

Domains are distinct from [[classification-tags|Classification Tags]] and [[glossary-terms|Glossary Terms]]. While tags and glossary terms provide cross-cutting metadata (e.g., PII sensitivity, business definitions), Domains provide a structural, hierarchical organization of assets.

## Governance Implications

- **Ownership**: Domains have assigned owners and experts, providing clear accountability.
- **Discovery**: The Explore page supports filtering by domain, making it easier to find relevant assets.
- **Classification**: Domains complement [[classification-tags]] and [[glossary-terms]] by providing a higher-level organizational layer.

## Open Questions

- How are Domains created and managed? Is there a UI workflow similar to Data Products?
- Can a single data asset belong to multiple Domains?
- How do Domains interact with [[teams-and-users|Teams]]? Are Domains a type of Team?
- What is the JSON Schema for Domains?
- Interaction between Domains and the [[hybrid-rbac-abac-model]] is not documented and remains an open question.