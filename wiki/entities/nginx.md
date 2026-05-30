---
type: entity
title: "Nginx"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: entity
title: Nginx
created: 2026-05-14
updated: 2026-05-14
tags: [web-server, http-server, configuration, openmetadata]
related: [http-artifact-storage, dbt-artifact-storage, dbt-integration]
sources: ["dbt-artifact-storage---http-server-configuration-o-20260514.md"]
---

# Nginx

Nginx is a high-performance web server and reverse proxy server. In the context of OpenMetadata's [[dbt-integration]], Nginx can be configured as a static file server to serve dbt JSON artifacts (manifest.json, catalog.json, run_results.json) for the [[http-artifact-storage]] pattern.

## Configuration for dbt Artifacts

The official documentation provides a complete Nginx configuration for serving dbt artifacts:

- Listens on port 80 with server name `artifacts.yourcompany.com`
- Root directory: `/var/www/dbt-artifacts`
- Optional directory listing enabled via `autoindex on`
- CORS headers configured for OpenMetadata access: `Access-Control-Allow-Origin: *`
- Location block `/dbt/` aliased to the artifacts directory
- Optional Basic Authentication via `auth_basic` and `auth_basic_user_file`

## Security Features

- **HTTPS**: Can be enabled using Let's Encrypt and Certbot
- **Basic Authentication**: Password protection using htpasswd-generated `.htpasswd` file
- **IP Whitelisting**: Restrict access to specific IP ranges using `allow`/`deny` directives

## Installation

Supported on Ubuntu/Debian (apt), CentOS/RHEL (yum), and macOS (Homebrew).