---
type: concept
title: WebSocket Dependency
created: 2026-05-14
updated: 2026-05-14
tags: [websocket, real-time, architecture, networking, troubleshooting]
related: [import-export-troubleshooting, openmetadata-system-architecture, change-events-system, activity-feed]
sources: ["troubleshooting-for-import-export-issue---openmeta-20260514.md"]
---
# WebSocket Dependency

OpenMetadata relies on WebSockets for real-time communication between the server and client. This dependency is critical for certain asynchronous operations and is a known prerequisite for network configuration.

## Known WebSocket-Dependent Features

- **Glossary CSV Export** — The export process is initiated asynchronously and uses a WebSocket connection to deliver the completed file. If WebSockets are blocked, the export hangs on "Export initiated successfully."
- **Activity Feed** — Real-time updates to the [[activity-feed]] likely depend on WebSocket connections.
- **Notifications** — Live notifications for announcements, tasks, and data observability alerts may use WebSockets.

## Deployment Implications

When deploying OpenMetadata behind a load balancer or proxy, WebSocket traffic must be explicitly allowed. Common configurations that may block WebSockets include:

- **Nginx** — Requires `proxy_http_version 1.1;` and `proxy_set_header Upgrade $http_upgrade;` directives.
- **AWS ALB** — Supports WebSockets natively but may require target group health check adjustments.
- **HAProxy** — Requires `option http-server-close` and `timeout tunnel` settings.

## Troubleshooting

If WebSocket-dependent features fail, verify connectivity using browser Developer Tools (Network tab, filter by WS). See [[import-export-troubleshooting]] for the specific Glossary export issue.

## Open Questions

- What is the exact WebSocket endpoint or path pattern used by OpenMetadata?
- Are there server-side logs that confirm WebSocket connection failures?
- Which other features beyond exports depend on WebSockets?