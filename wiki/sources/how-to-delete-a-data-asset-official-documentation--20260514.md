---
type: source
title: "Source: how-to-delete-a-data-asset-official-documentation--20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["how-to-delete-a-data-asset-official-documentation--20260514.md"]
tags: []
related: []
---

# Source: how-to-delete-a-data-asset-official-documentation--20260514.md

## Analysis of: how-to-delete-a-data-asset-official-documentation--20260514.md

### Key Entities

- **Data Asset** (central) — Core entity in OpenMetadata representing any metadata object (table, topic, dashboard, pipeline, etc.). Already exists in wiki as a concept implicitly across many pages (e.g., [[data-asset-ownership]], [[classification-tags]]).
- **Soft Delete** (central) — Deletion mode that marks an asset as deleted but retains it with read-only access. Already exists in wiki as [[soft-deletion]] (in the context of ingestion pipelines).
- **Hard Delete** (central) — Permanent removal of a data asset and all associated metadata from OpenMetadata. Not explicitly documented in the wiki index.
- **Explore** (peripheral) — UI navigation section for browsing data assets. Not a dedicated wiki page.
- **Announcements** (peripheral) — Referenced as a tip for notifying team members. Already exists as [[announcements]].

### Key Concepts

- **Soft Delete** — Deletion mode preserving the asset in read-only state; all user-generated and system-generated metadata (descriptions, tags, ownership, tiering, profiling, usage, lineage, test results, graph relationships) is retained but the asset is hidden from normal views. Already documented in wiki under [[soft-deletion]] but only in the context of ingestion pipeline behavior.
- **Hard Delete** — Permanent, irreversible removal of the data asset and all associated metadata from OpenMetadata. Not currently documented in the wiki.
- **Deletion Confirmation** — User must type "DELETE" to confirm the action; a safeguard against accidental deletion. Not documented in wiki.

### Main Arguments & Findings

- **Core claim:** OpenMetadata provides two deletion modes for data assets: soft delete (read-only preservation) and hard delete (permanent removal).
- **Evidence:** Official documentation page from OpenMetadata v1.12.x.
- **Strength:** High — this is official documentation, authoritative for the platform's behavior.

### Connections to Existing Wiki

- **Strengthens:** [[soft-deletion]] — The existing wiki page covers soft deletion only in the context of ingestion pipelines (marking absent tables as deleted). This source extends the concept to manual user-initiated deletion of any data asset via the UI.
- **Extends:** The wiki lacks any page on hard delete or the general data asset deletion workflow. This source fills that gap.
- **Related pages:** [[data-asset-ownership]], [[classification-tags]], [[glossary-terms]], [[data-profiling]], [[data-lineage]], [[data-quality]] — all mention metadata that is lost upon deletion.

### Contradictions & Tensions

- **No contradictions** with existing wiki content. The source is consistent with the soft delete concept already documented.
- **Minor tension:** The existing [[soft-deletion]] page describes it as an "ingestion option that marks absent tables as deleted." This source describes soft delete as a user-initiated action on any data asset. These are complementary
