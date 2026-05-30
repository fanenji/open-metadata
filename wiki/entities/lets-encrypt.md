---
type: entity
title: "Lets Encrypt"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: entity
title: Let's Encrypt
created: 2026-05-14
updated: 2026-05-14
tags: [ssl, tls, certificate, security, openmetadata]
related: [http-artifact-storage, dbt-artifact-storage, nginx, apache]
sources: ["dbt-artifact-storage---http-server-configuration-o-20260514.md"]
---

# Let's Encrypt

Let's Encrypt is a free, automated, and open certificate authority that provides SSL/TLS certificates. In the context of OpenMetadata's [[dbt-integration]], Let's Encrypt (via Certbot) is used to enable HTTPS for the [[http-artifact-storage]] server.

## Usage

The official documentation recommends using Certbot to obtain and install free SSL certificates:

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d artifacts.yourcompany.com
sudo certbot renew --dry-run
```

Certbot automatically configures the web server (Nginx or Apache) to use the obtained certificate and sets up auto-renewal.