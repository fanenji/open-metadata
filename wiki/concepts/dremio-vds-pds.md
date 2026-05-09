---
type: concept
title: Dremio VDS/PDS
created: 2026-05-07
updated: 2026-05-07
tags: [dremio, data-virtualization, abstraction, semantic-layer]
related: [dremio, dremio-reflections, dremio-row-column-security, data-virtualization-pattern, semantic-layer]
sources: ["Sintesi Architettura (Claude).md"]
---
# Dremio VDS/PDS

Dremio organizes data access through two types of datasets: Physical Datasets (PDS) and Virtual Datasets (VDS). This abstraction layer enables logical data modeling without physical data movement.

## Physical Datasets (PDS)

- **Definition**: Direct representations of underlying data sources (Iceberg tables, Oracle tables, files, etc.)
- **Characteristics**: Read-only, reflect source schema, can be accelerated with [[dremio-reflections]]
- **Use cases**: Raw data access, source-of-truth references

## Virtual Datasets (VDS)

- **Definition**: SQL-based views that transform, join, or aggregate PDS and other VDS
- **Characteristics**: Defined by SQL queries, can include business logic, row/column transformations
- **Use cases**: Semantic layer creation, data masking, business-friendly views, cross-source joins

## Role in Architecture

VDS/PDS form the foundation of Dremio's [[data-virtualization-pattern]] and [[semantic-layer]] capabilities. They enable:
- **Data Abstraction**: Consumers see logical datasets, not physical storage details
- **Security**: [[dremio-row-column-security]] can be applied at the VDS level
- **Reusability**: Common transformations defined once in VDS, reused by multiple consumers
- **Performance**: PDS can be accelerated with Reflections, VDS inherit underlying PDS acceleration