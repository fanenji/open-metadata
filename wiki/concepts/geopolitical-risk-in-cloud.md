---
type: concept
title: Geopolitical Risk in Cloud
created: 2026-04-29
updated: 2026-04-29
tags: [cloud, risk, architecture, europe]
related: [cloud-native-data-systems, multi-region-multi-cloud-trade-offs]
sources: ["Designing Data-intensive Applications with Martin Kleppmann.md"]
---
# Geopolitical Risk in Cloud

Geopolitical risk in cloud refers to the possibility that geopolitical events (e.g., trade disputes, sanctions, or conflict) could disrupt access to cloud services. This is particularly relevant for European organizations dependent on US-based cloud providers.

## Key Considerations

- **European Dependence**: Many European organizations rely heavily on US cloud services (AWS, GCP, Azure). A geopolitical disruption could lock them out of these services.
- **Multi-Cloud Mitigation**: Running workloads across multiple cloud providers (including European providers) can mitigate this risk, but at significant operational and cost overhead.
- **Trade-off**: Multi-cloud provides resilience against geopolitical risk but increases complexity, cost, and consistency challenges.

## Relevance to Data Platform

This is a strategic architectural consideration for the Data Platform. The decision to use single-cloud vs. multi-cloud should account for geopolitical risk alongside technical and cost factors.
