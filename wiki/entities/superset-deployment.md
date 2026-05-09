---
type: entity
title: Superset Deployment
created: 2026-01-15
updated: 2026-01-15
tags: [infrastructure, visualization, bi, superset]
related: [test-environment-infrastructure, dremio, data-lakehouse]
sources: ["Installazione Test Env.md"]
---
# Superset Deployment

Apache Superset is deployed as the BI and visualization layer in the Data Platform test environment.

## Access

- **URL**: `https://superset.dp.liguriadigitale.it`
- **Credentials**: Shared `dpadmin`/`dpAdm1n!` credentials

## Role in the Stack

Superset connects to [[dremio]] as its query engine, enabling interactive dashboards and ad-hoc analysis on data stored in the [[data-lakehouse]].

## Related

- [[test-environment-infrastructure]] — Overall test environment topology
- [[dremio]] — Query engine serving Superset