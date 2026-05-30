---
type: source
title: Troubleshooting for Import-Export Issue - OpenMetadata Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [troubleshooting, import-export, websocket, glossary, csv]
related: [import-export-troubleshooting, glossary-terms, websocket-dependency, openmetadata-system-architecture]
sources: ["troubleshooting-for-import-export-issue---openmeta-20260514.md"]
---
# Troubleshooting for Import-Export Issue - OpenMetadata Documentation

This source is the official OpenMetadata v1.12.x troubleshooting guide for the Glossary CSV export issue. It documents a specific failure mode where the export process hangs on "Export initiated successfully" due to WebSocket traffic being blocked by network infrastructure (load balancer or proxy). The guide provides a four-step diagnostic and resolution procedure: checking the load balancer/proxy configuration, verifying WebSocket connectivity via browser Developer Tools, adjusting proxy settings to allow WebSocket traffic, and restarting services to verify the fix.

The source establishes that OpenMetadata relies on WebSockets for real-time communication during async export operations. It does not cover alternative failure modes such as server-side errors, permission denials, or large glossary timeouts.