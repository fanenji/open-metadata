---
type: concept
title: Classification APIs
created: 2026-05-14
updated: 2026-05-14
tags: [api, classification, tags, automation, openmetadata]
related: [classification-tags, mutually-exclusive-tags, classification-vs-categorization-tags, openmetadata]
sources: ["overview-of-classification-official-documentation--20260514.md"]
---
# Classification APIs

OpenMetadata provides extensive REST APIs for automating the Classification and Tagging workflow. These APIs support two entity types: **Classification** and **Tag**.

## Entity Identification

- Each Classification and Tag entity is identified by a **Unique ID**.
- Tags have a **Fully Qualified Name (FQN)** in the form `classification.tagTerm` (e.g., `PII.Sensitive`, `PersonalData.Personal`).

## API Capabilities

The Classification APIs enable programmatic:

- Creation, reading, updating, and deletion of Classifications.
- Creation, reading, updating, and deletion of Tags within a Classification.
- Assignment and removal of Tags from data assets.
- Configuration of the [[mutually-exclusive-tags]] option on a Classification.

## Automation Use Cases

- **Bulk tagging** of data assets based on external metadata or scanning results.
- **Policy-driven tagging** where tags are applied automatically based on data content or source.
- **Integration with CI/CD pipelines** to enforce governance standards during data pipeline deployments.

## API Documentation

Refer to the official OpenMetadata API documentation for detailed endpoint specifications, request/response formats, and authentication requirements.