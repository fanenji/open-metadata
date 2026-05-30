---
type: entity
title: "Apache"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: entity
title: Apache
created: 2026-05-14
updated: 2026-05-14
tags: [web-server, http-server, configuration, openmetadata]
related: [http-artifact-storage, dbt-artifact-storage, dbt-integration]
sources: ["dbt-artifact-storage---http-server-configuration-o-20260514.md"]
---

# Apache

Apache HTTP Server is a widely-used open-source web server. In the context of OpenMetadata's [[dbt-integration]], Apache can be configured as a static file server to serve dbt JSON artifacts (manifest.json, catalog.json, run_results.json) for the [[http-artifact-storage]] pattern.

## Configuration for dbt Artifacts

The official documentation provides a complete Apache VirtualHost configuration for serving dbt artifacts:

- VirtualHost on port 80 with ServerName `artifacts.yourcompany.com`
- DocumentRoot: `/var/www/dbt-artifacts`
- Directory configuration with `Options Indexes FollowSymLinks`
- CORS headers enabled via `Header set Access-Control-Allow-Origin "*"`
- Separate error and access log files

## Security Features

- **HTTPS**: Can be enabled using Let's Encrypt and Certbot
- **Basic Authentication**: Password protection using htpasswd-generated `.htpasswd` file with `AuthType Basic`, `AuthName`, `AuthUserFile`, and `Require valid-user` directives

## Installation

Supported on Ubuntu/Debian (apt) and CentOS/RHEL (yum). Site enabled using `a2ensite` command.