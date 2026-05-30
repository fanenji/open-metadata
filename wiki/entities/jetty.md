---
type: entity
title: Jetty
created: 2026-05-14
updated: 2026-05-14
tags: [web-server, servlet-container, java, infrastructure]
related: [dropwizard, openmetadata-system-architecture]
sources: ["openmetadata-system-architecture-developer-guide---20260514-2.md"]
---

# Jetty

Jetty is an open-source Java HTTP web server and servlet container. In the context of OpenMetadata, Jetty serves as the embedded HTTP server bundled within the [[dropwizard|Dropwizard]] framework. Dropwizard packages Jetty to handle incoming HTTP requests and serve the REST API endpoints that power the OpenMetadata platform.

The official OpenMetadata system architecture documentation explicitly lists "Dropwizard/Jetty" as one of the four core dependencies, acknowledging Jetty's role as the underlying web server layer. While Dropwizard abstracts much of Jetty's configuration, understanding Jetty's presence is relevant for advanced tuning of thread pools, connection timeouts, and SSL/TLS settings in production deployments.