---
type: concept
title: NGINX WebSocket Proxy Troubleshooting for OpenMetadata
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, nginx, websocket, proxy, troubleshooting, glossary]
related: [glossary-terms, how-to-add-glossary-terms, openmetadata-administration]
sources: ["data-governance-glossary-troubleshooting-openmetad-20260514.md"]
---
# NGINX WebSocket Proxy Troubleshooting for OpenMetadata

When OpenMetadata is deployed behind NGINX with SSL (HTTPS proxy to port 8585), glossary bulk import and export operations may hang indefinitely, displaying a persistent "Import is in progress" state in the UI. This is not a bug in the glossary feature itself, but a proxy configuration issue: the glossary import/export functionality relies on WebSocket communication, and NGINX defaults do not support WebSocket upgrades.

## Root Cause

NGINX's default proxy configuration does not include the necessary headers to initiate a WebSocket upgrade handshake. When the OpenMetadata UI attempts to establish a WebSocket connection for the glossary import/export operation, the handshake fails silently, causing the operation to appear stuck.

## Solution

Update the NGINX `location /` block to include WebSocket support directives:

```nginx
location / {
    proxy_pass http://127.0.0.1:8585;

    # Enable WebSocket support
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_http_version 1.1;
}
```

The three directives are:
- `proxy_set_header Upgrade $http_upgrade;` — Passes the client's WebSocket upgrade request to the backend.
- `proxy_set_header Connection 'upgrade';` — Sets the Connection header to `upgrade`, signaling the protocol switch.
- `proxy_http_version 1.1;` — Required because HTTP/1.0 does not support the Upgrade header; NGINX defaults to HTTP/1.0 for proxied connections.

## Affected Operations

- Glossary bulk import (uploading glossary terms from a file)
- Glossary bulk export (downloading glossary terms to a file)

Both operations use WebSocket communication and will exhibit the same symptom when the proxy is misconfigured.

## Open Questions

- Are other reverse proxies (Apache HTTPD, HAProxy, Cloudflare, AWS ALB) similarly affected? The official documentation only addresses NGINX.
- Do other OpenMetadata features that rely on WebSocket communication (e.g., real-time notifications, activity feed updates) exhibit similar issues under the same misconfiguration?
- Is there a way to detect this misconfiguration proactively (e.g., via a health check or diagnostic endpoint)?

## Related Pages

- [[glossary-terms]] — The glossary feature that is affected by this issue.
- [[how-to-add-glossary-terms]] — Procedure for adding glossary terms, which may involve bulk import.
- [[openmetadata-administration]] — General administration guide covering deployment configuration.