---
type: concept
title: Catalog Mutations
created: 2026-02-26
updated: 2026-02-26
tags: [metadata, governance, automation]
related: [data-governance, openmetadata-ai-sdk]
sources: ["ai-sdk Bring Semintics to your AI Agents via the OpenMetadata & Collate AI SDK.md"]
---
# Catalog Mutations

**Catalog Mutations** refers to the ability of AI agents and automated processes to not only read metadata but also write and modify it within a data catalog.

## Significance in AI Governance
While many AI integrations are read-only, the ability to perform mutations enables **Active Governance**. Examples include:
- Automatically updating table descriptions based on schema changes.
- Adding lineage edges discovered during pipeline analysis.
- Patching entities with PII classifications or glossary terms.

## Risks and Considerations
Allowing AI agents to perform mutations introduces new security and permission requirements to prevent unauthorized or destructive changes to the metadata estate.