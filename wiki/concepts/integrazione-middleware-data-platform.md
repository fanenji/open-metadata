---
type: concept
title: Integrazione Middleware Data Platform
created: 2026-01-15
updated: 2026-01-15
tags: [middleware, integration, data-platform, architecture]
related: [piano-generale-attivita, dremio, duckdb, marimo, kestra, datahub, openmetadata, amundsen, dbt-cloud-security, data-virtualization-pattern, casi-pilota-data-platform]
sources: ["Piano Generale Attività.md"]
---
# Integrazione Middleware Data Platform

The middleware layer that enables interoperability between the core components of the Data Platform. The planning document identifies the following integration pairs:

- **Orchestration ↔ Data Analysis:** Connecting workflow orchestration (e.g., [[kestra]], Airflow) with analysis tools (e.g., [[duckdb]], [[marimo]]).
- **Orchestration ↔ Virtualization:** Connecting orchestration with the data virtualization layer ([[dremio]]).
- **Exploration ↔ Orchestration:** Connecting data exploration tools with orchestration.
- **Data Catalog ↔ Orchestration:** Connecting the regional Data Catalog ([[datahub]], [[openmetadata]], [[amundsen]]) with orchestration.
- **Virtualization ↔ Authentication:** Integrating the virtualization layer with the platform's authentication system (see [[dbt-cloud-security]] for related patterns).
- **Exploration/Analysis ↔ Authentication:** Integrating exploration and analysis tools with authentication.

This middleware is the critical architectural component that transforms a collection of tools into an integrated platform. The specific protocols, APIs, and implementation patterns are not yet defined in the planning document.