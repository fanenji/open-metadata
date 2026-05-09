---
type: source
title: "Building Data Platforms — The ETL bias"
created: 2026-04-04
updated: 2026-04-04
tags: [architecture, data-engineering, etl]
related: [etl-bias, unbundled-data-architecture, data-soverignty-strategy]
sources: ["Building Data Platforms — The ETL bias.md"]
authors: [João Vazao Vasques]
year: 2021
url: "https://medium.com/codex/building-data-platforms-the-etl-bias-d589733ce4cc"
venue: "CodeX"
---
# Building Data Platforms — The ETL bias

An article by João Vazao Vasques critiquing the "ETL bias"—the organizational tendency to centralize all data extraction, transformation, and loading responsibilities within a single, specialized team.

The author argues that while centralized ETL worked in the era of monolithic architectures, the shift to microservices has made this model a bottleneck. As engineering teams adopt diverse database technologies and fragmented ownership, the centralized Data Engineering team becomes overwhelmed, leading to "data downtime" and slowed product velocity.

The core argument is that the problem is a **mindset** issue rather than a lack of modern tools. To succeed, organizations must move away from treating data as a secondary concern for product teams and instead adopt a model where data ownership is distributed, similar to the DevOps revolution in software engineering.