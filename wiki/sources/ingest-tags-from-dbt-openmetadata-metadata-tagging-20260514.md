---
type: source
title: "Source: ingest-tags-from-dbt-openmetadata-metadata-tagging-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["ingest-tags-from-dbt-openmetadata-metadata-tagging-20260514.md"]
tags: []
related: []
---

# Source: ingest-tags-from-dbt-openmetadata-metadata-tagging-20260514.md

## Analysis: Ingest Tags from dbt | OpenMetadata Metadata Tagging Guide

### Key Entities

- **dbt (Data Build Tool)** — Central entity; the source system from which tags are ingested. Already exists in the wiki as [[dbt]].
- **OpenMetadata** — The target platform ingesting dbt tags. Already exists in the wiki as [[openmetadata]].
- **manifest.json** — Core artifact; the dbt-generated JSON file containing table-level and column-level tag information. Already exists in the wiki as [[dbt-artifacts]].
- **DBTTags** — Auto-created tag category in OpenMetadata for ingested dbt tags. Not explicitly in the wiki index; related to [[classification-tags]].
- **model.jaffle_shop.customers** — Example dbt model node used for illustration. Peripheral.

### Key Concepts

- **dbt Tag Ingestion** — Process of extracting table-level and column-level tags from the dbt `manifest.json` artifact and importing them into OpenMetadata under the `DBTTags` category. This is a specific sub-feature of the broader [[dbt-integration]].
- **Auto-creation of Tag Category** — If a dbt tag does not already exist in OpenMetadata, it is automatically created under the `DBTTags` category. This is a convenience mechanism that reduces manual setup.
- **Table-Level vs. Column-Level Tags** — Tags can be applied at the table level (under `node_name->tags`) or at the column level (under `node_name->columns->column_name->tags`). OpenMetadata ingests both levels.

### Main Arguments & Findings

- **Core Claim:** OpenMetadata can ingest both table-level and column-level tags from the dbt `manifest.json` file.
- **Evidence:** The source provides two JSON snippets from `manifest.json` showing the exact structure for table-level tags (`"tags": ["model_tag_one", "model_tag_two"]`) and column-level tags (`"tags": ["tags_column_one"]`).
- **Evidence Strength:** Strong. The source is official OpenMetadata documentation (v1.12.x). The JSON examples are clear and directly demonstrate the required artifact structure.

### Connections to Existing Wiki

- **[[dbt-integration]]** — This source is a direct sub-page of the dbt integration documentation. It extends the dbt integration by detailing a specific metadata category (tags) that can be ingested.
- **[[dbt-artifacts]]** — The source confirms that `manifest.json` is the artifact containing tag information, reinforcing the existing documentation.
- **[[classification-tags]]** — The `DBTTags` category is a specific instance of classification tags in OpenMetadata. This source shows how external tags (from dbt) map into the OpenMetadata classification system.
- **[[glossary-terms]]** — Tags are distinct from glossary terms; this source focuses on tags, not glossary terms.
- **[[how-to-add-tags-openmetadata-user-tagging-guide----20260514]]** — This source provides an automated ingestion path for tags, complementing the manual tagging workflow documented elsewhere.

### Contradictions & Tensions

- **No contradictions** with existing wiki content. The sour
