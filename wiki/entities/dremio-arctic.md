---
type: entity
title: Dremio Arctic
created: 2026-04-29
updated: 2026-04-29
tags: [dremio, managed-service, nessie, versioning]
related: [dremio, dremio-sonar, nessie-catalog-versioning, iceberg-table-versioning, data-lakehouse]
sources: ["Dremio.md"]
---
# Dremio Arctic

Dremio Arctic is a managed service offering from Dremio that integrates the Dremio query engine with Nessie catalog-level versioning. It provides Git-like capabilities (branching, tagging, merging) for data lakehouse environments.

## Key Features

- **Integrated Nessie Versioning** — Native support for Nessie catalog branching and tagging.
- **Managed Infrastructure** — Fully managed deployment, reducing operational overhead.
- **Time-Travel Queries** — Query data as of any point in time using Nessie's versioning.
- **Isolated Development** — Create branches for experimentation without affecting production data.

## Relationship to Other Components

- **Dremio Sonar** — Arctic includes the Sonar query engine as its core execution component.
- **Nessie** — Arctic provides a managed Nessie catalog service.
- **Iceberg** — Arctic works with Apache Iceberg tables for versioned storage.

## Use Cases

- Development and testing with isolated data branches
- Data pipeline experimentation without production impact
- Reproducible analytics through versioned data snapshots
- Collaborative data engineering with merge workflows

## Related Pages

- [[dremio]] — Primary Dremio entity page
- [[dremio-sonar]] — Core query engine component
- [[nessie-catalog-versioning]] — Catalog versioning concept
- [[iceberg-table-versioning]] — Table format versioning