---
type: concept
title: Metadata-driven API Configuration
created: 2026-05-07
updated: 2026-05-07
tags: [api, metadata, configuration, automation]
related: [api-configurator-system, ogc-api-features, data-download-service, legacy-geospatial-etl-pipeline]
sources: ["SISTEMA API - CONFIGURATORE API.md"]
---
# Metadata-driven API Configuration

Metadata-driven API configuration is the pattern of generating read-only APIs from metadata stored in databases or JSON files. Instead of manually coding API endpoints, the system reads configuration metadata to dynamically expose datasets and their items.

## Key Characteristics

- **Read-only**: APIs serve data without write capabilities
- **Metadata-driven**: Configuration stored in databases or JSON files
- **Dynamic**: New datasets can be exposed by adding metadata entries
- **Standardized**: Follows OGC API - Features endpoint structure

## Architecture

The [[api-configurator-system]] implements this pattern with:
- A landing page with title, description, and links
- SwaggerUI for interactive documentation
- Conformance endpoint listing supported standards
- Dataset listing and detail endpoints
- Item listing and detail endpoints

## Benefits

- Reduces manual API development effort
- Enables self-service dataset exposure
- Consistent API structure across all datasets
- Easy integration with existing metadata management

## Open Questions

- What is the exact metadata schema?
- How does it integrate with the [[data-download-service]]?
- What storage/query engine backs the API?