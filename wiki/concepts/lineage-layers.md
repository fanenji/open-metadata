---
type: concept
title: Lineage Layers
created: 2026-05-14
updated: 2026-05-14
tags: [data-lineage, lineage-view, exploration, openmetadata]
related: [data-lineage, column-level-lineage, observability-layer, service-layer, domain-layer, data-product-layer, data-quality]
sources: ["explore-the-lineage-view-official-documentation----20260514.md"]
---
# Lineage Layers

Lineage Layers are a multi-dimensional exploration framework in the OpenMetadata lineage view that enriches the basic lineage graph with contextual information. Instead of a single flat graph, users can toggle between five layers, each providing a different perspective on data flow and dependencies.

The five layers are:

- **[[column-level-lineage|Column Layer]]** — Traces field-level lineage for specific columns (e.g., `customer_id`, `first_name`) across tables and pipelines.
- **[[observability-layer|Observability Layer]]** — Integrates data quality test outcomes (passes, failures, pending) directly into the lineage graph.
- **[[service-layer|Service Layer]]** — Visualizes data flow across different platforms and services (e.g., Hive, Redshift, Power BI, Tableau).
- **[[domain-layer|Domain Layer]]** — Organizes assets into business-relevant categories (e.g., "Ecommerce", "Customer Data").
- **[[data-product-layer|Data Product Layer]]** — Highlights curated, consumption-ready data products (e.g., Customer Registry, Superstore).

This framework transforms lineage from a simple dependency graph into a rich, contextual discovery and governance tool. It is a key differentiator for OpenMetadata's lineage capabilities.