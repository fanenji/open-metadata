---
type: concept
title: Run dbt Workflow Externally
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, ingestion, cli, yaml-configuration, metadata-ingestion]
related: [dbt, dbt-integration, dbt-artifact-storage, dbt-lineage-ingestion, cli-ingestion-with-basic-auth, ingestion-framework, metadata-ingestion-workflow, filter-patterns, dbt-artifacts]
sources: ["run-dbt-workflow-externally-openmetadata-guide---o-20260514.md"]
---

# Run dbt Workflow Externally

The external dbt workflow is a method for running the dbt metadata ingestion pipeline outside of the OpenMetadata UI, using a YAML configuration file executed via the `metadata ingest -c <path-to-yaml>` CLI command. This approach provides flexibility for automation, CI/CD integration, and environments where the UI-based workflow is not suitable.

## Prerequisites

- Python 3.9-3.11 with `openmetadata-ingestion[dbt]` package installed
- Access to dbt artifacts (at minimum `manifest.json`; `catalog.json` and `run_results.json` are optional but recommended)
- For dbt Cloud: a service token with Account Viewer permission and account/project/job IDs

## YAML Configuration Structure

The YAML configuration has four main sections:

### 1. Source Configuration

```yaml
source:
  type: dbt
  serviceName: service_name
  sourceConfig:
    config:
      type: DBT
      dbtConfigSource:
        # Varies by artifact source (see below)
      # Optional source config flags
      # dbtUpdateDescriptions: true or false
      # dbtUpdateOwners: true or false
      # includeTags: true or false
      # dbtClassificationName: dbtTags
      # databaseFilterPattern:
      #   includes:
      #     - .*db.*
      #   excludes:
      #     - .*demo.*
      # schemaFilterPattern:
      #   includes:
      #     - .*schema.*
      #   excludes:
      #     - .*demo.*
      # tableFilterPattern:
      #   includes:
      #     - .*table.*
      #   excludes:
      #     - .*demo.*
```

### 2. Sink Configuration

```yaml
sink:
  type: metadata-rest
  config: {}
```

### 3. Workflow Configuration

```yaml
workflowConfig:
  loggerLevel: INFO
  openMetadataServerConfig:
    hostPort: "http://localhost:8585/api"
    authProvider: openmetadata
    securityConfig:
      jwtToken: "{bot_jwt_token}"
    storeServiceConnection: true
    # Optional SSL configuration
    # verifySSL: validate
    # sslConfig:
    #   caCertificate: /local/path/to/certificate
```

### 4. Ingestion Pipeline FQN (optional)

```yaml
# ingestionPipelineFQN: <service name>.<ingestion name>
```

## Artifact Source Types

The `dbtConfigSource` block varies by artifact source:

### AWS S3 Buckets

```yaml
dbtConfigSource:
  dbtConfigType: s3
  dbtSecurityConfig:
    awsConfig:
      awsRegion: us-east-2
      awsAccessKeyId: KEY
      awsSecretAccessKey: SECRET
      # awsSessionToken: TOKEN
      # endPointURL: https://...
      # profileName: profile
      # assumeRoleArn: "arn:..."
      # assumeRoleSessionName: session
      # assumeRoleSourceIdentity: identity
  dbtPrefixConfig:
    dbtBucketName: bucket_name
    dbtObjectPrefix: main_dir/dbt_files/
```

### Google Cloud Storage Buckets

```yaml
dbtConfigSource:
  dbtConfigType: gcs
  dbtSecurityConfig:
    gcpConfig:
      gcpCredentialsPath: /path/to/service-account.json
  dbtPrefixConfig:
    dbtBucketName: bucket_name
    dbtObjectPrefix: main_dir/dbt_files/
```

### Azure Storage Buckets

```yaml
dbtConfigSource:
  dbtConfigType: azure
  dbtSecurityConfig:
    clientId: client-id
    clientSecret: client-secret
    tenantId: tenant-id
    accountName: account-name
  dbtPrefixConfig:
    dbtBucketName: bucket_name
    dbtObjectPrefix: main_dir/dbt_files/
```

### Local Storage

```yaml
dbtConfigSource:
  dbtConfigType: local
  dbtCatalogFilePath: /path/to/catalog.json
  dbtManifestFilePath: /path/to/manifest.json
  dbtRunResultsFilePath: /path/to/run_results.json
```

### File Server (HTTP)

```yaml
dbtConfigSource:
  dbtConfigType: http
  dbtCatalogHttpPath: https://example.com/catalog.json
  dbtManifestHttpPath: https://example.com/manifest.json
  dbtRunResultsHttpPath: https://example.com/run_results.json
```

### dbt Cloud API

```yaml
dbtConfigSource:
  dbtConfigType: cloud
  dbtCloudAuthToken: AUTH_TOKEN
  dbtCloudAccountId: ACCOUNT_ID
  dbtCloudProjectId: PROJECT_ID
  dbtCloudJobId: JOB_ID
  dbtCloudUrl: https://cloud.getdbt.com
```

## Execution

After saving the YAML configuration file, run:

```bash
metadata ingest -c <path-to-yaml>
```

## Key Configuration Flags

- **dbtUpdateDescriptions** (boolean): Controls whether dbt descriptions override existing OpenMetadata descriptions. Default: false.
- **dbtUpdateOwners** (boolean): Controls whether dbt owners override existing OpenMetadata owners. Default: false.
- **includeTags** (boolean): Whether to ingest tags from dbt. Default: true.
- **dbtClassificationName** (string): Custom OpenMetadata Classification name for dbt tags. Default: `dbtTags`.
- **storeServiceConnection** (boolean): If true (default), sensitive connection info is stored encrypted in the database. If false, used only at runtime.
- **dbtPrefixConfig**: Optional bucket/prefix specification for cloud storage. If omitted, ingestion scans all buckets.

## Filter Patterns

The workflow supports [[filter-patterns]] at the database, schema, and table levels to scope which dbt models are ingested:

- `databaseFilterPattern`
- `schemaFilterPattern`
- `tableFilterPattern`

Each supports `includes` and `excludes` arrays with regex patterns.

## Relationship to Other Workflows

- The external CLI workflow is an alternative to the UI-driven [[metadata-ingestion-workflow]] process
- It uses the same [[ingestion-framework]] backend as UI-triggered pipelines
- The YAML structure is consistent across all connectors; only the `dbtConfigSource` block varies
- For dbt Cloud, the workflow uses dbt Cloud v2 APIs to retrieve the latest successful run and download artifacts

## Caveats

- If `dbtPrefixConfig` is omitted for cloud storage, ingestion scans all buckets, which may be inefficient in environments with many buckets
- The `ingestionPipelineFQN` parameter affects pipeline tracking and monitoring when running externally
- JWT token authentication is required for CLI-based ingestion; see [[cli-ingestion-with-basic-auth]] for details