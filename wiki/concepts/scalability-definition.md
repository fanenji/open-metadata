---
type: concept
title: Scalability Definition
created: 2026-04-29
updated: 2026-04-29
tags: [scalability, architecture, performance]
related: [cloud-native-data-systems, reliability-definition, maintainability-definition]
sources: ["Designing Data-intensive Applications with Martin Kleppmann.md"]
---
# Scalability Definition

Scalability, as defined in DDIA, is the ability of a system to cope with changes in load. This includes both scaling up (handling increased load) and scaling down (handling decreased load efficiently).

## Key Aspects

- **Horizontal Scalability**: Adding more machines to handle increased load. This is the more interesting and challenging form of scalability.
- **Vertical Scalability**: Buying a bigger machine. This is straightforward but has limits.
- **Scaling Down**: The ability to run a service cheaply when load is very low. Serverless systems excel at this.
- **Proportional Cost**: The ideal is for cost and computing capacity to be roughly proportional to load.

## Relevance to Data Platform

Scalability considerations affect decisions about sharding, replication, and deployment architecture. The ability to scale down (via serverless) is increasingly important for cost efficiency.
