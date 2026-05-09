---
type: entity
title: OpenSearch Deployment
created: 2026-01-15
updated: 2026-01-15
tags: [infrastructure, search, analytics, opensearch]
related: [test-environment-infrastructure, openmetadata, data-lakehouse]
sources: ["Installazione Test Env.md"]
---
# OpenSearch Deployment

OpenSearch is deployed as the search and analytics engine in the Data Platform test environment. It provides log analytics, full-text search, and observability capabilities.

## Access

- **URL**: `https://opensearch-dashboards.dp.liguriadigitale.it`
- **Credentials**: Shared `dpadmin`/`dpAdm1n!` credentials

## Role in the Stack

OpenSearch complements [[openmetadata]] by providing search capabilities across platform logs and metadata. It may also serve as a backend for observability and monitoring use cases.

## Related

- [[test-environment-infrastructure]] — Overall test environment topology
- [[openmetadata]] — Data catalog and governance platform