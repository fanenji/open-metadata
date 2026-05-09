---
type: entity
title: dbt Catalog
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, catalog, discovery, documentation, governance]
related: [dbt-cloud, dbt-mesh, data-catalog-critique, embedded-metadata]
sources: ["dbt Certified Architect Path beta - dbt Learn.md"]
---
# dbt Catalog

dbt Catalog is dbt Cloud's built-in data discovery and documentation tool. It provides a searchable, browsable interface for understanding the data assets managed by dbt projects, including model definitions, column descriptions, lineage, and freshness information.

## Key Features

- **Search and discovery**: Find models, sources, and exposures across projects.
- **Lineage visualization**: View upstream and downstream dependencies for any model.
- **Documentation**: Display model and column descriptions defined in YAML schema files.
- **Governance**: Enable teams to understand, refine, and govern their dbt projects.

## Relationship to Data Catalog Critique

The wiki's [[data-catalog-critique]] argues that traditional data catalogs fail because they are disconnected from data creation tools. dbt Catalog is notable because it is *embedded* in the dbt development workflow — documentation is generated from the same YAML files that define models, and lineage is derived from the `ref()` functions used in SQL. This makes dbt Catalog an example of [[embedded-metadata]], potentially addressing the critique's core concern. This tension is worth exploring further.