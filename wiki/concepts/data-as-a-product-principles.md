---
type: concept
title: "Data as a Product Principles"
created: 2026-05-08
updated: 2026-05-08
tags: [data-products, data-mesh, design-principles]
related: [data-product-vs-data-as-product, data-product-definition, data-mesh, data-product-categories]
sources: ["research-data-product-examples-expansion-2026-05-08.md"]
---
# Data as a Product Principles

The six design principles that define the "data as a product" mindset, derived from Domain-Driven Design and [[data-mesh]]. These principles guide how data should be treated with the same rigor as a software product.

## The Six Principles

### 1. Discoverable
Data products must be findable by potential consumers. This requires:
- Registration in a [[data-discovery-tools|catalog]] or marketplace.
- Rich metadata including description, owner, and tags.
- Search and browsing interfaces.

### 2. Addressable
Each data product must have a unique, stable identifier that consumers can reference:
- A URL, URN, or fully qualified table name.
- Versioned identifiers for tracking changes.
- Stable endpoints that don't break on internal changes.

### 3. Trustworthy
Consumers must be able to trust the data product's quality and freshness:
- Published [[data-quality-dimensions|quality scores]].
- Freshness SLAs with monitoring.
- [[data-contract-observability|Observability]] dashboards.
- Certification badges (bronze, silver, gold).

### 4. Self-describing
The data product must carry its own metadata explaining its meaning and structure:
- Schema definitions with column descriptions.
- Business glossary terms and definitions.
- Lineage showing upstream sources and downstream consumers.
- Usage examples and documentation.

### 5. Interoperable
Data products must work with standard tools and protocols:
- Open formats (Parquet, Avro, Iceberg).
- Standard APIs (REST, GraphQL, SQL).
- Compatibility with common BI tools and data platforms.

### 6. Secure
Access must be governed and auditable:
- Role-based access control (RBAC).
- Data masking for sensitive fields.
- Audit logging of all access.
- Compliance with data governance policies.

## Relationship to Other Concepts

- [[data-product-vs-data-as-product]] — these principles define the mindset; the concrete output is the data product.
- [[data-product-definition]] — the wiki's existing definition is now enriched with these principles.
- [[data-mesh]] — "data as a product" is one of the four pillars of data mesh architecture.
