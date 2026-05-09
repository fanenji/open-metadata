---
type: concept
title: Data Product Categories
created: 2026-05-08
updated: 2026-05-08
tags: [data-products, taxonomy, data-mesh]
related: [data-product-definition, data-product-vs-data-as-product, operational-vs-analytical-data-products, universal-data-product, enterprise-context-layer, dbt-data-contract-implementation, feature-store-architecture, model-context-protocol]
sources: ["research-data-product-examples-expansion-2026-05-08.md"]
---
# Data Product Categories

A taxonomy of seven distinct categories of data products, reflecting the expansion beyond traditional analytical datasets. This framework helps teams scope their data products consistently and choose appropriate platforms and governance patterns.

## The Seven Categories

### 1. Analytical Datasets
The classic form: curated, cleaned, well-documented tables or views optimized for BI tools and analysts.
- **Example:** A "Sales Snapshot" product with certified quality scores.
- **Platforms:** [[duckdb]], [[dremio]], [[snowflake-zero-copy-clone]], [[data-lakehouse]].

### 2. dbt Data Models as Data Products
In [[dbt-mesh]], a dbt model acts as a data product with YAML [[dbt-data-contract-implementation|data contracts]] defining schema, quality, lineage, and versioning.
- **Example:** A `fct_orders` model exposed as a public product with contract guarantees.
- **Platforms:** [[dbt-cloud]], [[dbt-osmosis]].

### 3. Machine Learning Feature Data Products
Outputs of a [[feature-store-architecture]] designed for low-latency ML model serving.
- **Example:** A "User Fraud Score" feature served via API for real-time payment decisions.
- **Platforms:** Feast, Tecton, Databricks Feature Store.

### 4. Streaming / Real-Time Data Products
Continuous data flows packaged with schema, SLAs, and quality guarantees, consumed via topics or streams.
- **Example:** "Order Status Change Events" consumed by a real-time dashboard and analytics warehouse.
- **Platforms:** Kafka, Apache Flink, [[dremio]].

### 5. GenAI and Vector Data Products
Domain data converted into embeddings for [[model-context-protocol|RAG]] and LLM applications.
- **Example:** "Product Catalog Embeddings" grounding a customer service AI.
- **Platforms:** Pinecone, Weaviate, [[data-lakehouse]] with embedding support.

### 6. API and Service-Based Data Products
Data exposed via REST, GraphQL, or gRPC with formal contracts (e.g., OpenAPI) and SLAs.
- **Example:** A "Customer 360" API merging profile, transaction, and support data.
- **Platforms:** [[fastapi]], Apigee.

### 7. Domain-Specific Operational Products
- **Sales:** Product inventory served to e-commerce frontends.
- **Marketing:** Campaign performance aggregates for ad-spend optimization.
- **Finance:** Risk exposure metrics for compliance monitoring.
- **Healthcare:** Clinical trial results with strict lineage for regulatory submission.

## Usage

Use this taxonomy to:
- Classify existing data products in your organization.
- Identify gaps in your data product portfolio.
- Select appropriate platforms and governance patterns for each category.
- Communicate the breadth of data product possibilities to stakeholders.
