---
type: concept
title: Federated Semantic Governance
created: 2026-05-06
updated: 2026-05-06
tags: [semantic-layer, governance, federation, architecture]
related: [semantic-layer-architecture, metrics-repo, data-mesh, federated-computational-governance]
sources: ["Semantic Layer in Big Tech.md"]
---
# Federated Semantic Governance

An architectural pattern for semantic layers where multiple domain-specific metric repositories and analytical layers coexist rather than a single universal system. This pattern is observed at Netflix, which has separate metric frameworks for experimentation, efficiency analytics, creative analytics, and other use cases.

## Key Characteristics

- Domain-specific metric repositories rather than one universal system
- Each domain manages its own metric definitions and computation
- Shared infrastructure for cross-domain concerns (catalog, lineage, quality)
- Challenges the "one semantic layer to rule them all" approach

## Relationship to Data Mesh

Federated semantic governance aligns with [[data-mesh]] principles: domain ownership of data products, self-serve platform infrastructure, and federated computational governance. The semantic layer becomes a platform capability that domains use to define and manage their metrics, rather than a centrally imposed system.

## Tension with Centralized Approaches

The article does not resolve whether centralized (Airbnb Minerva, LinkedIn UMP) or federated (Netflix) patterns are superior. The choice likely depends on organizational scale, domain heterogeneity, and governance maturity.