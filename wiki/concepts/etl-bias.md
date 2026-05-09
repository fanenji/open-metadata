---
type: concept
title: "The ETL Bias"
created: 2026-04-04
updated: 2026-04-04
tags: [organizational-risk, data-engineering, bottleneck]
related: [unbundled-data-architecture, data-sovereignty-strategy, data-downtime]
sources: ["Building Data Platforms — The ETL bias.md"]
---
# The ETL Bias

**The ETL Bias** refers to the organizational and technical tendency to centralize all data extraction, transformation, and loading (ETL) responsibilities within a single, specialized Data Engineering team.

## The Problem
While this model is effective in simple, monolithic environments where schemas are stable and ownership is clear, it fails in modern, decentralized architectures (e.g., microservices). The bias leads to several critical issues:

- **The Bottleneck Effect**: As the number of data sources and the complexity of the ecosystem grow, the central team becomes a single point of failure and a bottleneck for the entire company.
- **Knowledge Silos**: The central team is forced to understand the ontologies and schemas of every disparate system in the organization, which is unscalable.
- **Data Downtime**: Because product/engineering teams do not "own" the data they produce, upstream schema changes in microservices frequently break downstream ETL pipelines, leading to periods where data is inaccurate or missing.
- **Reduced Velocity**: Product teams become dependent on the Data Engineering team to implement new features that require new metrics, slowing down the overall business.

## Connection to Modern Architectures
The ETL bias is the primary driver for the move toward **[[unbundled-data-</strong>architecture]]** and **[[data-mesh]]** principles, where data ownership is pushed back to the domain experts who create the data.