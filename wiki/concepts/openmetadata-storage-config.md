---
type: concept
title: OpenMetadata Storage Config
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, storage, sample-data, configuration, opt-out]
related: [sample-data-external-storage, order-of-precedence-storage-credentials]
sources: ["external-storage-for-sample-data---openmetadata-do-20260514.md"]
---
# OpenMetadata Storage Config

The OpenMetadata Storage Config is an opt-out mechanism that prevents sample data from being uploaded to external object storage, even when storage credentials are configured at a parent level.

## Purpose

When S3 storage credentials are configured at the Database Service or Database level, sample data from all tables in the scope is uploaded by default. The OpenMetadata Storage Config option allows specific schemas or databases to be excluded from this upload.

## Example Scenario

Consider a database with three schemas: A, B, and C. S3 storage credentials are configured at the Database level. By default, sample data from all three schemas would be uploaded to S3. If schema A should not have its sample data exported, enabling the OpenMetadata Storage Config option at the schema level for A will skip the upload for that schema only. Schemas B and C continue to upload normally.

## Relationship to Credential Hierarchy

The OpenMetadata Storage Config works within the [[order-of-precedence-storage-credentials|order of precedence]] framework. It is set at the same level (Database Schema or Database) and takes effect regardless of whether credentials are inherited from a parent or configured directly at that level.