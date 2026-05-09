---
type: concept
title: Frictionless Data Package
created: 2026-04-29
updated: 2026-04-29
tags: [metadata, data-package, standard, opendata]
related: [data-download-service, metadata-fields-definition]
sources: ["DOWNLOAD.md"]
---
# Frictionless Data Package

The Frictionless Data Package is an open standard for packaging and describing data. It provides a simple, machine-readable format (JSON) for bundling data files with their metadata, including schema, description, and provenance. The standard is maintained by the Frictionless Data project and is widely used in open data and research contexts.

## Relevance to the Data Platform

The Data Platform's [[data-download-service]] proposes using the Frictionless Data Package standard as the metadata packaging format for downloads. This would ensure that every downloaded dataset is self-describing, containing:

- **Description**: Human-readable dataset overview.
- **Schema**: Column definitions, types, and constraints.
- **Lineage**: Provenance and transformation history.

## Advantages

- **Open standard**: No vendor lock-in.
- **Machine-readable**: JSON format is easy to parse and validate.
- **Widely adopted**: Used by governments, research institutions, and open data portals.
- **Extensible**: Custom properties can be added without breaking compatibility.

## Open Questions

- Is Frictionless the right standard for the Data Platform, or should a custom metadata format be used?
- How does Frictionless align with the existing [[metadata-fields-definition]]?
- What tooling is needed to generate and validate Frictionless packages from the Data Platform's metadata store?