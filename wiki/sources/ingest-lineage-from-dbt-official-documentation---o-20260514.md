---
type: source
title: Ingest Lineage from dbt | Official Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, lineage, manifest, openmetadata]
related: [dbt-lineage-ingestion, dbt-artifacts, dbt-integration, dbt]
sources: ["ingest-lineage-from-dbt-official-documentation---o-20260514.md"]
---

# Ingest Lineage from dbt | Official Documentation

This source is the official OpenMetadata documentation page for ingesting lineage from dbt (v1.12.x). It explains how OpenMetadata extracts lineage information from the `manifest.json` artifact using two distinct mechanisms: the `depends_on` key for direct node dependencies, and the `compiled_code`/`compiled_sql` key for SQL query parsing by the Lineage parser. The page includes concrete JSON examples and emphasizes the prerequisite of running `dbt compile` and `dbt docs generate` to populate the `compiled_code` field.
