---
type: source
title: "OpenMetadata System Architecture | Developer Guide"
created: 2026-05-14
updated: 2026-05-14
tags: [architecture, developer-guide, openmetadata]
related: [openmetadata-system-architecture, jsonschemas, dropwizard, mysql-8x, elasticsearch-7x, jetty]
sources: ["openmetadata-system-architecture-developer-guide---20260514-2.md"]
authors: ["OpenMetadata Documentation Team"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/developers/architecture"
venue: "OpenMetadata Official Documentation v1.12.x"
---

# OpenMetadata System Architecture | Developer Guide

This official developer guide page provides a concise, high-level overview of the OpenMetadata system architecture. It identifies the four core external dependencies that form the foundation of the platform:

1. **[[jsonschemas|JSON Schemas]]** — for defining metadata schemas (supporting the [[schema-first-approach]])
2. **[[dropwizard|Dropwizard]]/[[jetty|Jetty]]** — for REST APIs
3. **[[mysql-8x|MySQL 8.x]]** — to store metadata
4. **[[elasticsearch-7x|ElasticSearch 7.x]]** — to index metadata and power search

The page is notably terse and serves as an entry point, directing readers to a more detailed "Design page" and an "ML Model entity page" for deeper understanding of schema design and API mechanics. It reinforces the canonical architecture already documented in the [[openmetadata-system-architecture]] concept page.