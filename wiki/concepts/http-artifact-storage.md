---
type: concept
title: "Http Artifact Storage"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: HTTP Artifact Storage
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, artifact-storage, http-server, configuration, openmetadata]
related: [dbt-artifact-storage, dbt-artifacts, dbt-integration, dbt-lineage-ingestion, ingestion-framework]
sources: ["dbt-artifact-storage---http-server-configuration-o-20260514.md"]
---

# HTTP Artifact Storage

HTTP Artifact Storage is a configuration pattern for serving dbt JSON artifacts (manifest.json, catalog.json, run_results.json) via an HTTP/HTTPS server, enabling the [[dbt-integration]] for dbt Core without requiring cloud storage backends like S3, GCS, or Azure. This approach is ideal for multi-cloud or on-premises deployments.

## Server Options

Three server options are documented:

1. **S3 + CloudFront (Recommended)**: Combines S3 bucket storage with CloudFront CDN for HTTPS, global access, and managed infrastructure. The recommended production path.
2. **Nginx Static File Server**: A self-managed Nginx server configured to serve artifact files with CORS headers, directory listing, and optional Basic Authentication.
3. **Apache Static File Server**: A self-managed Apache server with equivalent capabilities to the Nginx option.

## Upload Methods

Artifacts can be uploaded to the HTTP server via:
- **Manual upload** using rsync or SCP
- **Automated upload** via an Airflow DAG that runs dbt and then syncs artifacts
- **curl HTTP POST** (requires a custom server endpoint not configured in the provided examples)

## OpenMetadata Configuration

In the OpenMetadata UI, the HTTP storage backend is configured under Settings → Services → Database Services → Ingestion → Add Ingestion → dbt. The configuration requires:
- **dbt Configuration Source**: HTTP
- **dbt Catalog HTTP Path**: Full URL to catalog.json
- **dbt Manifest HTTP Path**: Full URL to manifest.json
- **dbt Run Results HTTP Path**: Full URL to run_results.json (optional)
- **Username/Password**: For Basic Authentication (if enabled)

## Security Considerations

- **HTTPS**: Enable using Let's Encrypt and Certbot for free SSL certificates.
- **Basic Authentication**: Protect artifact URLs with username/password using htpasswd.
- **IP Whitelisting**: Restrict access to internal network ranges and OpenMetadata server IPs.

## Troubleshooting

Common issues include 403 Forbidden (file permissions), 404 Not Found (file paths), Connection Timeout (firewall rules), CORS Error (missing headers), and Stale Data (upload timing).

## Relationship to Other Concepts

HTTP Artifact Storage is one of five storage backends documented in [[dbt-artifact-storage]], alongside S3, GCS, Azure, and Local. It is a prerequisite for the [[dbt-lineage-ingestion]] workflow when using dbt Core without cloud storage.