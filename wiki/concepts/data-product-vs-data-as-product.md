---
type: concept
title: "Data Product vs. Data as a Product"
created: 2026-05-08
updated: 2026-05-08
tags: [data-products, data-mesh, conceptual-clarification]
related: [data-product-definition, data-product-categories, data-mesh, data-as-a-product-principles]
sources: ["research-data-product-examples-expansion-2026-05-08.md"]
---
# Data Product vs. Data as a Product

A critical conceptual distinction that clarifies the relationship between mindset and concrete output in data product thinking.

## Data as a Product (Mindset)

A design principle derived from Domain-Driven Design and [[data-mesh]]. It treats data with the same rigor as a software product, requiring it to be:
- **Discoverable** — consumers can find it.
- **Addressable** — it has a unique, stable identifier.
- **Trustworthy** — quality and freshness are guaranteed.
- **Self-describing** — metadata explains its meaning and structure.
- **Interoperable** — it works with standard tools and protocols.
- **Secure** — access is governed and auditable.

## Data Product (Concrete Output)

The specific, consumable asset that results from applying the "data as a product" mindset. This is what a consumer actually uses:
- A table or view.
- An API endpoint.
- A machine learning feature.
- A streaming topic.
- A vector index.
- A report or dashboard.

## Why This Distinction Matters

1. **Avoids confusion** between the principle and the implementation.
2. **Guides investment** — teams should first adopt the mindset, then build the products.
3. **Enables consistent scoping** — a data product is always a concrete, bounded asset.
4. **Supports governance** — contracts and SLAs apply to the product, not the mindset.

## Relationship to Other Concepts

- [[data-product-definition]] — the wiki's existing definition is now enriched with this distinction.
- [[data-product-categories]] — the seven categories are all concrete data products.
- [[data-mesh]] — the "data as a product" principle is one of the four pillars of data mesh.
