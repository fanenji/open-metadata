---
type: entity
title: "Certbot"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: entity
title: Certbot
created: 2026-05-14
updated: 2026-05-14
tags: [ssl, tls, certificate, security, openmetadata]
related: [http-artifact-storage, dbt-artifact-storage, lets-encrypt, nginx, apache]
sources: ["dbt-artifact-storage---http-server-configuration-o-20260514.md"]
---

# Certbot

Certbot is a free, open-source software tool for automatically using [[lets-encrypt]] SSL/TLS certificates to enable HTTPS on web servers. In the context of OpenMetadata's [[dbt-integration]], Certbot is used to secure the [[http-artifact-storage]] server.

## Usage

The official documentation provides commands for installing Certbot and obtaining certificates for Nginx:

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d artifacts.yourcompany.com
sudo certbot renew --dry-run
```

Certbot automatically modifies the web server configuration to use the obtained certificate and configures automatic certificate renewal.