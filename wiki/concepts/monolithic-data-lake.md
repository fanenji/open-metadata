---
type: concept
title: Monolithic Data Lake
created: 2026-04-29
updated: 2026-04-29
tags: [data-architecture, data-lake, anti-pattern]
related: [data-mesh, data-lakehouse, data-ingestion-architectural-patterns]
sources: ["DATA MESH.md"]
---
# Monolithic Data Lake

A monolithic data lake is a centralized, single repository that stores all raw data from across an organization in its native format. It is the traditional approach to analytical data management that data mesh aims to replace.

## Problems

- **Bottlenecks** — A single central team becomes the gatekeeper for all data ingestion, transformation, and access
- **Ownership ambiguity** — No single team feels responsible for data quality or freshness
- **Scalability limits** — As data volume and domain count grow, the central team cannot keep up
- **Poor discoverability** — Data from different domains is mixed together without clear ownership or context
- **Governance challenges** — Access control and compliance become increasingly complex

## Relationship to Data Mesh

The monolithic data lake is the problem context that [[data-mesh]] solves. The migration path involves decomposing the monolith into domain-owned data products served through a [[self-serve-data-platform]].

## Related Patterns

The [[data-lakehouse]] is a related evolution that adds ACID transactions and performance optimizations to data lakes, but does not inherently solve the ownership and scalability problems of monolithic architecture.