---
type: concept
title: Federated Computational Governance
created: 2026-04-29
updated: 2026-04-29
tags: [data-governance, data-mesh, automation]
related: [data-mesh, data-domain-governance, data-contract-platform]
sources: ["DATA MESH.md"]
---
# Federated Computational Governance

Federated computational governance is a core principle of [[data-mesh]] that addresses how global standards are enforced across autonomous domain teams. Instead of a central governance team manually reviewing and approving data products, governance rules are codified and enforced automatically by the [[self-serve-data-platform]].

## Key Characteristics

- **Global standards** — Organization-wide rules for data privacy, interoperability, access control, and quality
- **Local autonomy** — Domain teams retain control over how they implement their data products
- **Automated enforcement** — The platform validates compliance at build and runtime
- **Computational** — Rules are expressed as code (e.g., policies, contracts, tests) rather than documents

## Relationship to Data Contracts

[[data-contract-platform]] is a concrete implementation mechanism for federated computational governance. Contracts define the global standards (schema, quality, SLAs) and the platform enforces them automatically.

## Relationship to Data Domain Governance

While [[data-domain-governance]] focuses on creating domains and assigning ownership, federated computational governance provides the automated enforcement layer that ensures domains comply with organizational standards.