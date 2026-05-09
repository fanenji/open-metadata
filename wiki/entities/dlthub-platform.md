---
type: entity
title: dltHub Platform
created: 2026-04-29
updated: 2026-04-29
tags: [saas, elt, ai-native, governance, platform]
related: [dlt-data-load-tool, dlthub-context, python-native-elt, ai-native-pipeline-generation, self-serve-data-platform]
sources: ["dltHub ELT as Python Code.md"]
---
# dltHub Platform

**dltHub** is the upcoming SaaS platform from the creators of [[dlt-data-load-tool]]. It extends the open-source dlt library from pure extraction and loading (EL) into full ELT, storage, and runtime capabilities. The first release for individual developers is planned for Q1 2026.

## Vision

dltHub aims to transform complex data workflows into something any Python developer can run: deploy pipelines, transformations, and notebooks — all in a platform that feels as natural as writing Python code.

## Key Features (Planned)

- **AI-native pipeline generation**: Leverages [[dlthub-context]] to enable LLM-driven pipeline creation from REST API specifications.
- **Governance and compliance**: Designed for regulated industries (finance, healthcare) with built-in lineage, observability, quality control, and compliance with standards like BCBS 239.
- **Pythonic simplicity**: Preserves the code-first philosophy of dlt while adding platform capabilities.
- **Tiered availability**: Individual developers (Q1 2026), then small teams and enterprises.

## Target Audience

- Individual developers and data engineers
- Small teams needing lightweight data infrastructure
- Enterprises in regulated industries requiring governance

## Connections

- Extends [[dlt-data-load-tool]] from open-source library to full platform
- Competes with/complements [[self-serve-data-platform]] approaches
- Conceptually similar to [[dbt-cloud]] but Python-native rather than SQL/YAML-native