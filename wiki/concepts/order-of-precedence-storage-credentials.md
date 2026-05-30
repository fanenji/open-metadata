---
type: concept
title: "Order of Precedence: Storage Credentials"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, storage, configuration, hierarchy, sample-data]
related: [sample-data-external-storage, openmetadata-storage-config]
sources: ["external-storage-for-sample-data---openmetadata-do-20260514.md"]
---
# Order of Precedence: Storage Credentials

The order of precedence for sample data storage credentials determines which S3 configuration is used when multiple levels have been configured. This hierarchical resolution pattern is consistent with other configuration inheritance models in OpenMetadata.

## Resolution Order

When resolving which storage credentials to use for uploading sample data, OpenMetadata evaluates configurations in this order:

1. **Database Schema** — highest priority
2. **Database** — fallback if no schema-level config
3. **Database Service** — fallback if no database-level config

This means a Database Schema-level storage configuration overrides any Database or Database Service settings. If no schema-level configuration exists, the Database-level configuration is used. If neither exists, the Database Service-level configuration applies.

## Practical Implications

- **Granular control**: Different schemas within the same database can target different S3 buckets or prefixes.
- **Inheritance with override**: Configure a default at the Database Service level, then override specific databases or schemas as needed.
- **Opt-out via [[openmetadata-storage-config]]**: Even when credentials are inherited from a parent level, individual schemas or databases can skip upload entirely using the OpenMetadata Storage Config option.