---
type: concept
title: "Data Downtime"
created: 2026-04-04
updated: 2026-04-04
tags: [data-quality, observability, reliability]
related: [etl-bias, data-observability, data-contracts]
sources: ["Building Data Platforms — The ETL bias.md"]
---
# Data Downtime

**Data Downtime** is the period during which data is inaccurate, missing, incomplete, or otherwise unusable for its intended business purpose.

## Causes
In modern distributed architectures, data downtime is frequently caused by the decoupling of data ownership from the teams that manage the source systems. Specifically:
- **Upstream Schema Changes**: When engineering teams modify microservice databases without coordination, downstream ETL pipelines break.

- **The ETL Bias**: Because the responsibility for data stability lies with a central team rather than the producers, there is no incentive for source teams to maintain data contracts.

## Mitigation
Reducing data downtime requires moving toward **[[open-data-contract-standard-odcs]]** and ensuring that data is treated as a "first-class citizen" by the teams producing it.