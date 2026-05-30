---
type: source
title: "Dbt Artifact Storage   Http Server Configuration O 20260514"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
authors: []
year: 2026
url: ""
venue: ""
---

type: source
title: "dbt Artifact Storage - HTTP Server Configuration | OpenMetadata"
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, artifact-storage, http-server, configuration, openmetadata]
related: [dbt-artifact-storage, http-artifact-storage, dbt-integration, dbt-artifacts, dbt-lineage-ingestion, ingestion-framework]
sources: ["dbt-artifact-storage---http-server-configuration-o-20260514.md"]
---

# dbt Artifact Storage - HTTP Server Configuration | OpenMetadata

Official documentation for configuring an HTTP/HTTPS server as the artifact storage layer for dbt Core + OpenMetadata integration. Covers three server options (S3 + CloudFront, Nginx, Apache), artifact upload methods, OpenMetadata UI configuration, security considerations (HTTPS, Basic Auth, IP whitelisting), and troubleshooting.

## Key Content

- **Prerequisites**: Web server (Nginx, Apache, or cloud CDN), existing dbt project, server access, database service already ingested.
- **Option 1: S3 + CloudFront (Recommended)**: Combines S3 storage with CloudFront CDN for HTTPS and global access. Provides AWS CLI command for CloudFront distribution creation.
- **Option 2: Nginx Static File Server**: Complete Nginx configuration with CORS headers, directory listing, and optional Basic Auth. Installation commands for Ubuntu/Debian, CentOS/RHEL, and macOS.
- **Option 3: Apache Static File Server**: Complete Apache VirtualHost configuration with CORS headers. Installation and site enablement commands.
- **Upload Methods**: Manual upload with rsync/SCP, automated upload via Airflow DAG, and curl HTTP POST (requires custom server endpoint).
- **OpenMetadata Configuration**: Step-by-step UI configuration for dbt Source (HTTP) with field mapping for catalog.json, manifest.json, and run_results.json URLs. Basic Auth credential fields.
- **Verification**: curl commands to verify artifact accessibility from OpenMetadata's network.
- **Security**: HTTPS via Let's Encrypt/Certbot, Basic Authentication with htpasswd, IP whitelisting for Nginx.
- **Troubleshooting**: Table covering 403 Forbidden, 404 Not Found, Connection Timeout, CORS Error, and Stale Data issues with symptoms and solutions.

## Relevance

This source directly extends the [[dbt-artifact-storage]] concept by providing the detailed configuration for the HTTP storage backend. It is essential for multi-cloud or on-premises deployments where cloud storage (S3, GCS, Azure) is not available or desired.