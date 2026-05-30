---
type: concept
title: Import-Export Troubleshooting
created: 2026-05-14
updated: 2026-05-14
tags: [troubleshooting, import-export, websocket, glossary, csv]
related: [glossary-terms, websocket-dependency, openmetadata-system-architecture, async-export-via-websocket]
sources: ["troubleshooting-for-import-export-issue---openmeta-20260514.md"]
---
# Import-Export Troubleshooting

This page documents known issues and resolution procedures for import and export operations in OpenMetadata, with a focus on the Glossary CSV export failure.

## Symptom: Glossary CSV Export Hangs

When attempting to export a Glossary as a CSV file, the process displays "Export initiated successfully" but never completes. The file is not downloaded, and the export button remains disabled.

## Root Cause

The most common cause is WebSocket traffic being blocked by network infrastructure (load balancer or proxy). OpenMetadata relies on [[websocket-dependency|WebSockets]] for real-time communication during async export operations. If WebSocket connections are blocked, the export callback cannot deliver the completed file.

## Troubleshooting Steps

### Step 1: Check Load Balancer or Proxy

Verify whether WebSockets are being blocked by your network setup. Run the following API request to check the export status:

```bash
curl -X GET "https://<your-openmetadata-instance>/api/v1/glossaries/name/<Glossary_Name>/exportAsync"
```

If the response does not return a file and remains in an active state indefinitely, WebSockets may be blocked.

### Step 2: Verify WebSocket Connectivity

1. Open browser Developer Tools (F12 or Ctrl+Shift+I in Chrome).
2. Navigate to the **Network** tab.
3. Filter requests by **WebSockets (WS)**.
4. Check if WebSocket requests to OpenMetadata (`wss://<your-openmetadata-instance>`) are blocked, failing, or not established.

### Step 3: Adjust WebSocket Settings in Proxy

Update your proxy or load balancer configuration to allow WebSocket traffic. Specific settings depend on your proxy software (e.g., Nginx, HAProxy, AWS ALB).

### Step 4: Restart Services and Verify

1. Restart your proxy or load balancer after configuration changes.
2. Clear browser cache and cookies.
3. Retry the CSV export in OpenMetadata.

## Known Limitations

- This troubleshooting guide assumes WebSocket blocking is the primary cause. Other potential failure modes (server-side errors, permission denials, large glossary timeouts) are not covered.
- The exact WebSocket endpoint or path pattern used by OpenMetadata for exports is not documented in this source.
- Server-side logs that could confirm WebSocket connection failures are not mentioned.

## Related Pages

- [[glossary-terms]] — The data entity being exported.
- [[websocket-dependency]] — OpenMetadata's reliance on WebSockets for real-time features.
- [[openmetadata-system-architecture]] — Architectural context for real-time communication.