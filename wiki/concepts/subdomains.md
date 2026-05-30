---
type: concept
title: Subdomains
created: 2026-05-14
updated: 2026-05-14
tags: [data-mesh, domains, planned-feature]
related: [domains, data-mesh-openmetadata]
sources: ["OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md"]
---
# Subdomains

Subdomains are a planned feature in [[OpenMetadata]]'s [[data-mesh-openmetadata|data mesh]] implementation that will enable hierarchical nesting within [[domains]]. They allow specialized sub-groupings within a domain for finer-grained organizational structure.

## Status

- **Backend support**: Subdomains are already supported in the OpenMetadata backend as of the 1.2.0 release.
- **UI hidden**: The feature is intentionally hidden from the user interface to avoid overwhelming users during the initial adoption of domains and data products.
- **Gradual introduction**: The team plans to introduce subdomains in a future release, allowing the community to first become comfortable with the core domain and data product concepts.

## Rationale for Delayed Introduction

The OpenMetadata team acknowledged that data mesh is a complex organizational principle and wanted to introduce features incrementally. By starting with flat domains and data products, users can adopt the core concepts before dealing with nested hierarchies.