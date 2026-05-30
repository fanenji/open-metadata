---
type: concept
title: pbit File Lineage Extraction
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, lineage, pbit, storage]
related: [powerbi-connector, dashboard-lineage, powerbi-admin-vs-non-admin-apis]
sources: ["run-the-powerbi-connector-externally---openmetadat-20260514.md"]
---
# pbit File Lineage Extraction

PowerBI template files (`.pbit`) contain embedded lineage information that can be extracted by the OpenMetadata PowerBI connector. This provides an alternative or complementary lineage source to the API-based methods.

## Storage Backends

The `pbitFilesSource` configuration supports four storage backends:

- **Local:** Files stored on the local filesystem where the ingestion process runs.
- **Azure Blob Storage (`azureConfig`):** Requires Azure storage account credentials (clientId, clientSecret, tenantId, accountName).
- **Google Cloud Storage (`gcsConfig`):** Supports authentication via GCP Credentials Values or GCP Credentials Path (service account or external account).
- **Amazon S3 (`s3Config`):** Supports AWS access keys, session tokens, assume role, and custom endpoint URLs.

## Configuration

Each backend requires:
- `pbitFileConfigType`: The storage type (`azure`, `gcs`, or `s3`).
- `securityConfig`: Authentication credentials for the storage backend.
- `prefixConfig`: `bucketName` (container/bucket) and `objectPrefix` (path prefix).
- `pbitFilesExtractDir`: Local directory where extracted `.pbit` files are stored for processing.

## Usage

The pbit file lineage extraction is configured in the `source.serviceConnection.config` section of the YAML configuration. It is independent of the Admin/Non-Admin API toggle and can be used alongside API-based lineage.

## Related

- [[powerbi-connector]] — The parent connector page.
- [[dashboard-lineage]] — General dashboard lineage concepts.
- [[powerbi-admin-vs-non-admin-apis]] — API-based lineage methods.