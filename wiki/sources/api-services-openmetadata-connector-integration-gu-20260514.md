---
type: source
title: "Source: api-services-openmetadata-connector-integration-gu-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["api-services-openmetadata-connector-integration-gu-20260514.md"]
tags: []
related: []
---

# Source: api-services-openmetadata-connector-integration-gu-20260514.md

## Analysis of: API Services | OpenMetadata Connector Integration Guide

### Key Entities

- **OpenMetadata API Service** (Concept/Feature) — Central entity; a connector category for ingesting metadata from RESTful APIs via OpenAPI/Swagger specs. Already exists in wiki as [[rest-api-connector]].
- **REST API Connector** (Product/Feature) — The specific turnkey connector listed under API Services (marked "PROD"). Already exists in wiki.
- **OpenAPI (Swagger) Specification** (Standard) — Required schema format for API metadata ingestion. Already exists in wiki as [[openapi-specification]].
- **Slack / GitHub** (Platforms) — Peripheral; mentioned for connector requests.

### Key Concepts

- **API Service Metadata Ingestion** — Process of extracting metadata from RESTful APIs exposing OpenAPI JSON schemas. Core concept of this source.
- **Custom Integration** — Ability to ingest metadata from proprietary/bespoke systems not natively supported by OpenMetadata's 90+ connectors. Extends the connector ecosystem concept.
- **Flexible Deployment** — Support for both UI-based and CLI-based ingestion workflows for API services. Aligns with existing [[metadata-ingestion-workflow]] and [[cli-ingestion-with-basic-auth]].

### Main Arguments & Findings

- **Core Claim**: The API Services connector enables metadata ingestion from any RESTful API with a valid OpenAPI specification, filling gaps where native connectors don't exist.
- **Evidence**: None provided beyond feature listing; this is a high-level overview page, not a technical deep-dive.
- **Strength**: Low — purely descriptive, no technical details, configuration steps, or troubleshooting.

### Connections to Existing Wiki

- **Strengthens**: [[rest-api-connector]] — confirms it's a production-grade connector (marked "PROD"), not just beta.
- **Extends**: [[openmetadata-connectors]] — adds API Services as a distinct connector category alongside Database, Dashboard, Messaging, etc.
- **Related**: [[openapi-specification]] — the schema format required; [[metadata-ingestion-workflow]] — the UI/CLI workflows referenced.

### Contradictions & Tensions

- **Minor tension with [[rest-api-connector]]**: The existing wiki page describes the REST API Connector as "Beta," but this source marks it as "PROD." This may reflect a version upgrade (v1.12.x vs. earlier) or a documentation inconsistency. Worth flagging.
- **No internal tensions** within the source itself.

### Recommendations

**Create:**
- [[api-services-connector]] — New page for the API Services connector category, consolidating this overview with technical details from the REST API Connector page. Should cover: supported features, use cases, best practices (schema validation, auth management, regular updates), and the PROD status.

**Update:**
- [[rest-api-connector]] — Update status from "Beta" to "PROD" if confirmed for v1.12.x. Add reference to this overview page.
- [[openmetadata-connectors]] — Add "API Services" as a connector category in the list.
