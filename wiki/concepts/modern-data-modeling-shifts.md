---
type: concept
title: Modern Data Modeling Shifts
created: 2026-05-07
updated: 2026-05-07
tags: [data-modeling, denormalization, star-schema, slowly-changing-dimensions, data-warehouse]
related: [data-engineering-definition, code-over-drag-and-drop-etl, data-warehouse-as-public-institution, maxime-beauchemin, data-quality-certification-vs-usability-certification]
sources: ["The Rise of the Data Engineer.md"]
---
# Modern Data Modeling Shifts

Five key shifts in data modeling practices observed in modern data environments, as described in Maxime Beauchemin's 2017 manifesto. These shifts reflect the changing economics of storage and compute, where engineering time has become the scarcer resource.

## The Five Shifts

### 1. Further Denormalization
Maintaining surrogate keys in dimensions is tricky and makes fact tables less readable. Natural, human-readable keys and dimension attributes in fact tables are becoming more common, reducing costly joins. Modern serialization formats (Parquet, ORC) and database engines (Vertica) address performance loss through built-in encoding and compression.

### 2. Blobs
Modern databases have growing support for blobs through native types and functions. This allows fact tables to store multiple grains at once when needed, opening new possibilities in data modeling.

### 3. Dynamic Schemas
With map-reduce, document stores, and blob support, it is easier to evolve database schemas without executing DDL. This enables iterative approaches to warehousing and removes the need for full consensus prior to development.

### 4. Systematically Snapshotting Dimensions
Storing a full copy of the dimension for each ETL schedule cycle (usually in distinct table partitions) is a simple, generic approach to handling slowly changing dimensions (SCD). Unlike classical SCD techniques, this is easy to grasp when writing ETL and queries. Complex SCD modeling techniques are not intuitive and reduce accessibility.

### 5. Relaxed Conformance
Conformed dimensions and metrics remain important, but with the need for data warehouses to move fast and with more teams contributing, conformance is less imperative and more of a tradeoff. Consensus and convergence can happen as a background process where divergence becomes problematic.

## Context

These shifts are driven by cheaper storage and compute, distributed databases that scale linearly, and the growing number of data-savvy participants in the data warehouse. The result is less need to precompute and store results, as complex analysis can be computed on-demand.

## Connections

- [[data-engineering-definition]] — Context for the shifts
- [[code-over-drag-and-drop-etl]] — Related methodological change
- [[data-warehouse-as-public-institution]] — Governance implications
- [[maxime-beauchemin]] — Author of the observations
- [[data-quality-certification-vs-usability-certification]] — Related to certified core schemas