---
type: concept
title: Unified Metadata Model
created: 2026-04-05
updated: 2026-04-05
tags: [openmetadata, metadata, schema, standardization]
related: [openmetadata, openmetadata-architecture, metadata-fields-definition]
sources: ["OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md"]
---
# Unified Metadata Model

The Unified Metadata Model is the core architectural principle of [[OpenMetadata]]. It defines an open, standard schema for all metadata entities — tables, pipelines, dashboards, users, tags, lineage, and more. Every entity in the platform conforms to this model, enabling consistent storage, retrieval, and manipulation of metadata across all connectors and features.

Key characteristics:
- **Open standard** — Not proprietary; the schema is publicly available and extensible.
- **Structured** — Entities have well-defined fields, types, and relationships.
- **Versioned** — Every change creates a new version with full diff and restore capabilities.
- **API-driven** — The full REST API and Python SDK operate on this model.

This model is what distinguishes OpenMetadata from tools that store metadata in ad-hoc or proprietary formats.