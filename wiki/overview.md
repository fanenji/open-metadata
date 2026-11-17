---
type: overview
title: "Wiki Overview"
updated: 2026-07-07
---
# Overview

This wiki is a comprehensive knowledge base on **OpenMetadata** — the open-source platform for metadata discovery, lineage, quality, and governance. It covers the platform's architecture, deployment, administration, features, and integrations, including the latest **1.12 release** (February 2026).

## Architecture & Deployment

The wiki documents OpenMetadata's [[schema-first-approach|schema-first architecture]], its core dependencies ([[mysql-8x|MySQL]], [[elasticsearch-7x|Elasticsearch]], [[dropwizard|Dropwizard/Jetty]]), and deployment models including [[on-premises-kubernetes-deployment]] with [[helm-charts]]. The [[kubernetes-native-orchestrator]] and [[omjob-operator]] are covered in depth as the modern ingestion backbone, with the 1.12 release making the Kubernetes Orchestrator GA and removing the Airflow dependency entirely.

## Metadata Ingestion

The [[ingestion-framework]] and its 90+ [[openmetadata-connectors|connectors]] are a major focus area, with detailed pages on specific connectors like [[oracle-connector]], [[postgresql-connector]], [[superset-connector]], [[powerbi-connector]], and the [[rest-api-connector]]. The [[metadata-ingestion-workflow]], [[metadata-agent]], [[filter-patterns]], and [[ingestion-scheduling]] concepts are fully documented. New 1.12 connectors include StarRocks, SFTP, and Redshift Serverless.

### DBT Integration

The [[dbt-integration|dbt-OpenMetadata integration]] is well-covered, including [[dbt-artifacts]], [[dbt-lineage-ingestion]], [[dbt-custom-property-ingestion]] (table-level only), and the verification that [[dbt-column-level-custom-properties|column-level custom properties]] ingestion is **NOT supported** by OpenMetadata.

## Access Control & Governance

The wiki deeply covers the [[hybrid-rbac-abac-model|hybrid RBAC-ABAC authorization model]], including [[roles-and-policies]], [[authorization-rules]], [[authorization-policies]], [[spel-conditions]], and [[tag-based-access-control]]. Team management ([[teams-and-users]], [[team-types]], [[team-hierarchy-rules]]) and role patterns are documented. The 1.12 release adds [[audit-logs|AI Agent Audit Logs]] for tracking automated metadata changes.

## Data Quality & Contracts

The wiki covers **[[data-quality]]** across multiple dimensions: traditional UI-driven tests, the new **[[test-library|Data Quality Test Library]]** (v1.12 — reusable parameterized SQL templates), **[[data-quality-as-code]]** (SDK-driven, pipeline-embedded testing with circuit breaker patterns, v1.11), and **[[data-contracts]]** (formal producer-consumer agreements, v1.9) with [[odcs-open-data-contract-standard|ODCS 3.1]] import/export support (v1.12). [[data-profiling]], [[data-observability-alerts]], and [[great-expectations]] complete the quality landscape along with [[dbt-expectations]] and [[ollama]] for local LLM integration.

## Knowledge Graph & Ontology

The **[[knowledge-graph]]** and **[[ontology-explorer]]** (v1.13) provide complementary visualizations of the [[unified-metadata-graph]]: asset-centric and business-glossary-centric respectively. These are critical foundations for trustworthy [[agentic-ai]] and [[mcp-server]] interactions. The new [[semantic-search-openmetadata|Semantic Search]] capability (v1.12) adds vector embedding-based search.

## AI & Modern Features

The [[mcp-server|MCP Server]] integration and the new [[openmetadata-ai-sdk|AI SDK]] (v1.12) provide programmatic access to metadata intelligence. [[agentic-ai]] concepts, [[persona|Persona]] customization with [[pluggable-panels]], and [[announcements]] are documented alongside operational topics like [[reindexing-search]], [[data-insights-application-troubleshooting]], and the [[permission-debugger]].

## Classification & Governance

[[classification-tags]], [[tiers]], [[glossary-terms]], and [[custom-properties]] form the classification and enrichment layer. The [[auto-classification]] agent, [[pii-sample-data-masking]], and [[tag-request-workflow]] are covered. The new [[column-bulk-operations|Column Bulk Operations]] (v1.12) enables cross-asset governance at scale.

## Open Standards

The 1.12 release embraces open standards with [[openlineage-integration|OpenLineage integration]] for lineage ingestion and [[odcs-open-data-contract-standard|ODCS 3.1]] support for interoperable data contracts, preventing vendor lock-in and enabling best-of-breed tool selection.