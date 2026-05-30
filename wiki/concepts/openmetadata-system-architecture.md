---
type: concept
title: OpenMetadata System Architecture
created: 2026-05-14
updated: 2026-05-14
tags: [architecture, openmetadata, dependencies, developer-guide, core-dependencies]
related: [openmetadata, schema-first-approach, dropwizard, external-dependencies-configuration, openmetadata-code-layout, unified-metadata-graph, ingestion-framework, jsonschemas, jetty, mysql-8x, elasticsearch-7x, change-events-system, pull-based-ingestion-model]
sources: ["openmetadata-system-architecture-developer-guide---20260514.md", "openmetadata-system-architecture-developer-guide---20260514-2.md"]
---

# OpenMetadata System Architecture

The official system architecture of OpenMetadata, as defined in the developer guide, identifies four core dependencies that form the foundation of the platform.

These are complemented by the [[change-events-system]] (which captures entity changes and updates the search index) and the [[pull-based-ingestion-model]] (which governs how metadata is collected from external sources).

## Core Dependencies

### JSON Schemas — Metadata Schema Definition

OpenMetadata uses [[schema-first-approach|JSON Schemas]] as the single source of truth for defining all metadata entities. These schemas drive code generation for both Java (POJOs) and Python (types), ensuring consistency across the backend API and ingestion framework. See [[openmetadata-code-layout]] for the directory structure that houses these schemas.

### Dropwizard / Jetty — REST API Framework

[[dropwizard]] is the Java REST API framework used to build OpenMetadata’s backend services. It bundles [[jetty|Jetty]] as its embedded HTTP server and servlet container, handling all incoming API requests. Dropwizard provides integrated support for metrics, health checks, and configuration management that power the OpenMetadata server.

### MySQL 8.x — Metadata Storage

All metadata entities, relationships, tags, and system configuration are persisted in a MySQL 8.x relational database. MySQL serves as the transactional store that backs the [[unified-metadata-graph]], storing the canonical state of all metadata. [[flyway|Flyway]] manages versioned schema migrations to keep the database structure in sync with the application. For deployment configuration details, see [[external-dependencies-configuration]].

### ElasticSearch 7.x — Search Index

Metadata is indexed in ElasticSearch 7.x to power the platform’s full-text search, discovery, and activity feed capabilities. ElasticSearch maintains a search-optimized copy of metadata, enabling fast queries across large data estates. The [[change-events-system]] captures entity changes and publishes them to ElasticSearch for near-real-time indexing.

> **Version Note:** The official architecture documentation specifies ElasticSearch 7.x. The [[external-dependencies-configuration]] page covers both ElasticSearch and OpenSearch, reflecting the broader compatibility supported in practice. This source represents a version-specific snapshot.

## Scope

This architectural overview is intentionally minimal. It does not cover:

- The [[ingestion-framework]] and its [[openmetadata-connectors|connectors]]
- The [[kubernetes-native-orchestrator]] and [[omjob-operator]]
- The [[pull-based-ingestion-model]] (beyond its high‑level relationship to the core dependencies)
- Authentication providers such as [[google-oauth]]

For a complete picture, these concepts must be understood alongside the core dependencies listed here. The official documentation directs readers to the “Design page” for a more comprehensive architectural diagram. For a detailed map of how these components are organized in the codebase, see [[openmetadata-code-layout]].