---
type: entity
title: "Htpasswd"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: entity
title: htpasswd
created: 2026-05-14
updated: 2026-05-14
tags: [authentication, basic-auth, security, openmetadata]
related: [http-artifact-storage, dbt-artifact-storage, nginx, apache]
sources: ["dbt-artifact-storage---http-server-configuration-o-20260514.md"]
---

# htpasswd

htpasswd is a command-line tool for managing user authentication files for Basic Authentication on web servers. In the context of OpenMetadata's [[dbt-integration]], htpasswd is used to create password files for securing the [[http-artifact-storage]] server.

## Usage

The official documentation provides commands for creating password files for both Nginx and Apache:

```bash
# Install apache2-utils (provides htpasswd)
sudo apt install -y apache2-utils

# Create password file
sudo htpasswd -c /etc/nginx/.htpasswd collate
```

The generated password file is then referenced in the web server configuration (Nginx's `auth_basic_user_file` or Apache's `AuthUserFile` directive).