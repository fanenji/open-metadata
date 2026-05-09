---
type: entity
title: MySQL
created: 2026-04-05
updated: 2026-04-05
tags: [mysql, database, openmetadata, metadata-store]
related: [openmetadata, openmetadata-architecture]
sources: ["OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md"]
---
# MySQL

MySQL (or compatible databases) serves as the metadata store for [[OpenMetadata]]. It stores all entities — tables, pipelines, dashboards, users, tags, lineage — in a structured, versioned schema. Every change to every asset is tracked and versioned in this database.

MySQL is a required dependency for running OpenMetadata.