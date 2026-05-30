---
type: source
title: "Data Governance Glossary Troubleshooting | OpenMetadata Guide"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, troubleshooting, nginx, websocket]
related: [glossary-terms, how-to-add-glossary-terms, openmetadata-administration, nginx-websocket-proxy-troubleshooting]
sources: ["data-governance-glossary-troubleshooting-openmetad-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/glossary/troubleshooting"
venue: "OpenMetadata Documentation"
---
# Data Governance Glossary Troubleshooting | OpenMetadata Guide

This official OpenMetadata documentation page (v1.12.x) provides a single troubleshooting scenario: glossary bulk import/export operations hanging when OpenMetadata runs behind NGINX with SSL. The root cause is identified as missing WebSocket upgrade headers in the NGINX proxy configuration. The solution involves adding specific `proxy_set_header` directives (`Upgrade`, `Connection`) and setting `proxy_http_version 1.1` to enable WebSocket passthrough.

The page is part of the Data Governance section of the OpenMetadata documentation, specifically under the Glossary sub-section. It follows the "Glossary Approval Workflow" page and precedes the "Glossary Styling" page in the documentation hierarchy.

## Key Content

- **Issue:** Glossary bulk import/export stuck in "Import is in progress" state when using NGINX with SSL.
- **Cause:** WebSocket communication failure due to missing NGINX WebSocket upgrade configuration.
- **Solution:** Add `proxy_set_header Upgrade $http_upgrade;`, `proxy_set_header Connection 'upgrade';`, and `proxy_http_version 1.1;` to the NGINX `location /` block.

## Relevance

This source is narrowly focused on a specific deployment configuration issue. Its primary value is documenting the WebSocket dependency of glossary operations and providing a concrete fix for NGINX-based deployments. It does not cover other reverse proxies or alternative causes for the same symptom.