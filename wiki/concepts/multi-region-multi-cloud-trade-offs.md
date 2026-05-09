---
type: concept
title: Multi-Region/Multi-Cloud Trade-offs
created: 2026-04-29
updated: 2026-04-29
tags: [cloud, architecture, trade-offs, availability]
related: [geopolitical-risk-in-cloud, cloud-native-data-systems, reliability-definition]
sources: ["Designing Data-intensive Applications with Martin Kleppmann.md"]
---
# Multi-Region/Multi-Cloud Trade-offs

Multi-region and multi-cloud architectures involve running workloads across multiple geographic regions or cloud providers to improve availability and resilience. These architectures come with significant trade-offs.

## Trade-offs

- **Availability vs. Consistency**: Multi-region setups can tolerate region outages but introduce consistency challenges (e.g., cross-region replication lag).
- **Cost vs. Resilience**: Multi-cloud provides resilience against provider outages but dramatically increases operational overhead and cost.
- **Complexity vs. Risk Reduction**: The operational complexity of managing multiple regions or clouds must be weighed against the risk being mitigated.

## Relevance to Data Platform

This concept directly informs architectural decisions about where to deploy the Data Platform and how to design for disaster recovery and business continuity.
