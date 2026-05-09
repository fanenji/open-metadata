---
type: entity
title: Jupyter Deployment
created: 2026-01-15
updated: 2026-01-15
tags: [infrastructure, notebooks, jupyter, data-science]
related: [test-environment-infrastructure, dremio, duckdb, data-lakehouse]
sources: ["Installazione Test Env.md"]
---
# Jupyter Deployment

Jupyter is deployed as the notebook environment in the Data Platform test environment, enabling interactive data exploration and analysis.

## Access

- **URL**: `http://jupyter.dp.liguriadigitale.it` (HTTP only)
- **Credentials**: Shared `dpadmin`/`dpAdm1n!` credentials

## Security Note

Jupyter is the only service in the test environment that uses HTTP instead of HTTPS. This may indicate intentional internal-only access or a configuration gap that should be addressed.

## Role in the Stack

Jupyter provides a flexible environment for data scientists and engineers to:

- Explore data stored in [[dremio]] and [[minio-deployment]]
- Prototype transformations using [[duckdb]] and Python
- Develop and test geospatial analytics workflows
- Create ad-hoc visualizations and reports

## Related

- [[test-environment-infrastructure]] — Overall test environment topology
- [[dremio]] — Query engine accessible from notebooks