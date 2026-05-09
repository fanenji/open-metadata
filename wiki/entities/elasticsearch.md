---
type: entity
title: Elasticsearch
created: 2026-04-04
updated: 2026-05-07
tags: [database, search, infrastructure, elasticsearch, openmetadata]
related: [kestra, postgresql, openmetadata, openmetadata-architecture]
sources: ["Kestra vs Airflow (Video).md", "OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md"]
---
# Elasticsearch

Elasticsearch (or its open-source fork OpenSearch) is a distributed search and analytics engine.

## In Kestra

In the context of [[Kestra]], Elasticsearch is a required external dependency for operation, alongside [[PostgreSQL]]. This dependency adds setup complexity and is considered a limitation for very small teams or simple use cases.

## In OpenMetadata

[[OpenMetadata]] uses Elasticsearch as its search backend. It powers all search and discovery features in the platform, including natural language search, filtering by tags/owners/domains, and ranked result retrieval. When a user searches for a table name or filters by tag in OpenMetadata, the query hits Elasticsearch under the hood. Elasticsearch is a required dependency for running OpenMetadata.